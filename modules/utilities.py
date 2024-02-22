import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5 import uic,QtGui
from PyQt5.QtCore import Qt
import pandas as pd
import csv
import datetime
import math
import pyodbc
import numpy as np
import json 
import requests

#http prefix
http = 'https://'
#Host name
host = 'JUSWA'
#Port
port = '50000'
#Database
database='MPC_TEST_3'
#Username
sapusername='manager'
#Password
sappassword='sapb1'


date_format = "%Y%m%d"
bpcode_list = []
bpname_list = []
itemcode_list = []
itemcode_uomcode_list = []
grpo_list = []
grpo_list_linenum = []
grpo_list_docentry = []
grpo_list_quantity = []
grpo_list_contno = []
apinvoice_list = []
apinvoice_list_linenum = []
apcm_list = []
apcm_list_linenum = []
ovpm_list = []
ovpm_list_linenum = []
orct_list = []
orct_list_linenum = []
arinvoice_list = []
arinvoice_list2 = []
arinvoice_list_linenum = []
arcm_list = []
arcm_list_linenum = []
wtcode_list = []
wtcode_cardcode = []
wtcode_rate = []
wtcode_liable = []
apv_or_apcm_list = []
apv_or_apcm_docentry_list = []
apv_or_apcm_clearingdoc_list = []
apv_or_apcm_objtype_list = []
arv_or_arcm_list = []
arv_or_arcm_docentry_list = []
arv_or_arcm_clearingdoc_list = []
arv_or_arcm_objtype_list = []
journalentry_list = []
journalentry_list_linenum = []
controlaccount_list = []

billStatementValidAcctCode = []
araccounts_list = []
revenueaccounts_list = []


cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=JUSWA;"
            "Database=" + database + ";"
            "UID=SA;"
            "PWD=SAPB1Admin;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

class Utilities():
    def login():
        print('**********************')
        #Login credentials
        payload = {

            "CompanyDB" : database,
            "UserName" : sapusername,
            "Password" : sappassword

        }
        #payload = '{ "UserName" : "manager", "Password" : "sapb1","CompanyDB" : "Inteluck_Train" }'
        jsonPayload = json.dumps(payload)
        url = http + host + ":" + port + "/b1s/v1/Login"
        requestUrl = requests.post(url, data=jsonPayload, verify=False)
        print(requestUrl.text)
        dictcreds = json.loads(requestUrl.text)
        sessionkey = dictcreds['SessionId']

        return sessionkey
    

    def bpQueryValidator():
        # GET BP MASTER DATA
        

        query = "SELECT CardCode, CardName FROM [OCRD]"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                bpcode_list.append(row[0])
                bpname_list.append(row[1])
        print('--------------------------------------------------')


        return bpcode_list, bpname_list


    def itemQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT ItemCode, InvntryUom FROM [OITM]"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                itemcode_list.append(row[0])
                array1 = np.array([row[0],row[1]])
                itemcode_uomcode_list.append(array1)

        # for i in range(12):
        #     for i2 in range(2):
        #         print(itemcode_uomcode_list[i][i2] + " " + str(i) +","+ str(i2))
        print('--------------------------------------------------')


        return itemcode_list, itemcode_uomcode_list
    


    def wtQueryValidator(unique_df):
        # GET WT CODES
        
        carcodeArrStr = ''
        for i in unique_df:
           
            value = "'" + i + "'" + ","
           
            carcodeArrStr += value
           
              

        
        carcodeArrStr += "''"
     
        query = "SELECT OWHT.WTCode, OCRD.CardCode, Rate, OCRD.WTLiable FROM [CRD4] INNER JOIN OCRD ON OCRD.CardCode = CRD4.CardCode INNER JOIN OWHT ON CRD4.WTCode = OWHT.WTCode WHERE OCRD.CardCode IN (" + carcodeArrStr + ")"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                wtcode_list.append(row[0])
                wtcode_cardcode.append(row[1])
                wtcode_rate.append(row[2])
                wtcode_liable.append(row[3])

        print('--------------------------------------------------')

        return wtcode_list, wtcode_cardcode, wtcode_rate, wtcode_liable
    



    def wtQueryValidator2():
        # GET WT CODES
        query = "SELECT OWHT.WTCode, OCRD.CardCode, Rate, OCRD.WTLiable FROM [CRD4] INNER JOIN OCRD ON OCRD.CardCode = CRD4.CardCode INNER JOIN OWHT ON CRD4.WTCode = OWHT.WTCode WHERE OCRD.CardType='S'"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                wtcode_list.append(row[0])
                wtcode_cardcode.append(row[1])
                wtcode_rate.append(row[2])
                wtcode_liable.append(row[3])

        print('--------------------------------------------------')

         
        return wtcode_list, wtcode_cardcode, wtcode_rate, wtcode_liable


    def grpoQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT OPDN.U_DocNo, PDN1.LineNum + 2 AS LineNum, OPDN.DocEntry AS DocEntry,  PDN1.Quantity, OPDN.U_ContNo FROM [OPDN] INNER JOIN [PDN1] ON OPDN.DocEntry = PDN1.DocEntry"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[4])
                array1.append(row[1])

                array2 = []
                array2.append(row[4])
                array2.append(row[1])
                array2.append(row[2])

                array3 = []
                array3.append(row[4])
                array3.append(row[1])
                array3.append(row[2])
                array3.append(row[3])

                grpo_list.append(row[0])
                grpo_list_linenum.append(array1)
                grpo_list_docentry.append(row[2])
                grpo_list_quantity.append(row[3])
                grpo_list_contno.append(row[4])
        print('--------------------------------------------------')


        return grpo_list, grpo_list_linenum, grpo_list_docentry, grpo_list_quantity, grpo_list_contno
    


    
    def apinvoiceQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, LineNum + 1 AS LineNum FROM [OPCH] INNER JOIN [PCH1] ON OPCH.DocEntry = PCH1.DocEntry"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                apinvoice_list.append(row[0])
                apinvoice_list_linenum.append(array1)
        print('--------------------------------------------------')


        return apinvoice_list, apinvoice_list_linenum
    


    def apcmQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, LineNum + 1 AS LineNum FROM [ORPC] INNER JOIN [PCH1] ON ORPC.DocEntry = PCH1.DocEntry"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                apcm_list.append(row[0])
                apcm_list_linenum.append(array1)
        print('--------------------------------------------------')


        return apcm_list, apcm_list_linenum
    



    def apinvoiceForOVPMQueryValidator():
        # GET ITEM MASTER DATA
        query = """
            SELECT CardCode, U_DocNo, DocEntry, ObjType, U_ClrngDoc FROM [OPCH] 
            UNION ALL
            SELECT CardCode, U_DocNo, DocEntry, ObjType, U_ClrngDoc FROM [OPDN]
        """
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])

                array2 = []
                array2.append(row[0])
                array2.append(row[1])
                array2.append(row[2])
                array2.append(row[3])

                array3 = []
                array3.append(row[2])


                array4 = []
                array4.append(row[4])


                apv_or_apcm_list.append(array1)
                apv_or_apcm_docentry_list.append(row[2])
                apv_or_apcm_objtype_list.append(row[3])
                apv_or_apcm_clearingdoc_list.append(row[4])

        print('--------------------------------------------------')


        return apv_or_apcm_list, apv_or_apcm_docentry_list, apv_or_apcm_clearingdoc_list, apv_or_apcm_objtype_list

    def ovpmQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, [VPM2].DocLine + 1 AS LineNum FROM [OVPM] INNER JOIN [VPM2] ON [OVPM].DocEntry = [VPM2].DocNum"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                ovpm_list.append(row[0])
                ovpm_list_linenum.append(array1)
        print('--------------------------------------------------')


        return ovpm_list, ovpm_list_linenum
    






    def arinvoiceForORCTQueryValidator():
        # GET ITEM MASTER DATA
        query = """
            SELECT CardCode, U_DocNo, DocEntry, ObjType, U_ClrngDoc FROM [OINV] 
            WHERE U_ClrngDoc <> ''
            UNION ALL
            SELECT CardCode, U_DocNo, DocEntry, ObjType, U_ClrngDoc FROM [ORIN]
            WHERE U_ClrngDoc <> ''

        """
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])

                array2 = []
                array2.append(row[0])
                array2.append(row[1])
                array2.append(row[2])
                array2.append(row[3])

                array3 = []
                array3.append(row[2])


                array4 = []
                array4.append(row[4])


                arv_or_arcm_list.append(array1)
                arv_or_arcm_docentry_list.append(row[2])
                arv_or_arcm_objtype_list.append(row[3])
                arv_or_arcm_clearingdoc_list.append(row[4])

        print('--------------------------------------------------')


        return arv_or_arcm_list, arv_or_arcm_docentry_list, arv_or_arcm_clearingdoc_list, arv_or_arcm_objtype_list

    def orctQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, [RCT2].DocLine + 1 AS LineNum FROM [ORCT] INNER JOIN [RCT2] ON [ORCT].DocEntry = [RCT2].DocNum WHERE U_DocNo <> '' "
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                orct_list.append(row[0])
                orct_list_linenum.append(array1)
        print('--------------------------------------------------')


        return orct_list, orct_list_linenum



    

    def arinvoiceQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, LineNum + 1 AS LineNum, [OINV].DocEntry FROM [OINV] INNER JOIN [INV1] ON OINV.DocEntry = INV1.DocEntry WHERE CANCELED = 'N'"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array2 = []
                array1.append(row[0])
                array1.append(row[1])
                array2.append(row[2])
                arinvoice_list.append(row[0])
                arinvoice_list2.append(row[2])
                arinvoice_list_linenum.append(array1)
        print('--------------------------------------------------')


        return arinvoice_list, arinvoice_list_linenum, arinvoice_list2
    



    def arcmQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, LineNum + 1 AS LineNum FROM [ORIN] INNER JOIN [RIN1] ON ORIN.DocEntry = RIN1.DocEntry"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                arcm_list.append(row[0])
                arcm_list_linenum.append(array1)
        print('--------------------------------------------------')


        return arcm_list, arcm_list_linenum
    



    def journalentryQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT U_DocNo, Line_Id + 1 AS LineNum FROM [OJDT] INNER JOIN [JDT1] ON OJDT.TransId = JDT1.TransId"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                array1 = []
                array1.append(row[0])
                array1.append(row[1])
                journalentry_list.append(row[0])
                journalentry_list_linenum.append(array1)
        print('--------------------------------------------------')


        return journalentry_list, journalentry_list_linenum
    



    def controlAccountsQueryValidator():
        # GET ITEM MASTER DATA
        query = "SELECT AcctCode FROM OACT Where OACT.LocManTran = 'Y'"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                controlaccount_list.append(row[0])
        print('--------------------------------------------------')


        return controlaccount_list
    


    def billingStatementValidAcctCode():
        # GET ITEM MASTER DATA
        query = "SELECT Code, Name, U_Category FROM [@BS_ACCOUNTS]"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                billStatementValidAcctCode.append(row[0])
        print('--------------------------------------------------')


        return billStatementValidAcctCode
    


    def controlAccount():
        # GET ITEM MASTER DATA
        query = "SELECT Code, Name, U_Category FROM [@BS_ACCOUNTS] WHERE U_Category = 'AR Account'"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                araccounts_list.append(row[0])
        print('--------------------------------------------------')


        return araccounts_list
    



    def revenueAccount():
        # GET ITEM MASTER DATA
        query = "SELECT Code, Name, U_Category FROM [@BS_ACCOUNTS] WHERE U_Category = 'Revenue Account'"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
                
                revenueaccounts_list.append(row[0])
        print('--------------------------------------------------')


        return revenueaccounts_list