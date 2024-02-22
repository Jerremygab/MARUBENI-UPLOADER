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
from modules.utilities import http as http
from modules.utilities import host as host
from modules.utilities import port as port
from modules.utilities import database as database
from modules.utilities import sapusername as sapusername
from modules.utilities import sappassword as sappassword


date_format = "%Y%m%d"

import modules.utilities as Utilities


class ARCreditMemo():
    def processDataFrame(self, file_name):

        bpCodeListArr = Utilities.Utilities.bpQueryValidator()
        bpcode_list = bpCodeListArr[0]
        bpname_list = bpCodeListArr[1]


        itemCodeListArr = Utilities.Utilities.itemQueryValidator()
        itemcode_list = itemCodeListArr[0]
        itemcode_uomcode_list = itemCodeListArr[1]

        arcmCodeListArr = Utilities.Utilities.arcmQueryValidator()
        arcmcode_list = arcmCodeListArr[0]
        arcmcode_linenum_list = arcmCodeListArr[1]

        

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')
        df = df.loc[df['DT'].isin(['RV','H1','H9'])]
        df = df.loc[df['A/C Code'].isin(['30112','30211','30212','30214','30215','11310'])]
        df = df.loc[df['2nd Sub-Account'].str.contains('DM', na=False)]
        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48, 50, 51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )

        df3 = df2[[
            'Status',
            'DT', 
            'Ent.DT', 
            'Trn DT', 
            'Due Date',
            'Ref.No.',
            'S-AC',
            'S-AC Name',
            'A/C Code',
            'Unit',
            'Unit Name',
            'Doc.No.',
            'REMARKS',
            'Instruction No.',
            'Cont.No.',
            'Clrng doc.',
            'Clrng DT',
            '2nd Sub-Account',
            'Items',
            'Curr',
            'Trans. Amt.',
            'Dom. Amt.',
            'Material Code',
            'Tx',
            'Quantity',
            'Quantity Unit',

            ]]
        
        # print(len(df2.axes[1]))
        # df3.to_csv('file_name1.csv', index=False)

        totalBPNotExist = 0
        totalItemNotExist = 0
        totalGrpoExist = 0

        # df3.groupby('Cont.No.')
        # df3.sort_values(['Items'],ascending=False).groupby('Cont.No.')
        df3 = df3.sort_values(['Doc.No.','Cont.No.','Items'], ascending=True)

        array2 = []
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            ctrlacctrow = 0
            # ARCM VALIDATION
            # ARCM CODE
            try:
                if(df3['A/C Code'][ind] != "11310"):
                    if(df3['Cont.No.'][ind] in arcmcode_list):
                        
                        array1 = []
                        array1.append(df3['Cont.No.'][ind])
                        array1.append(df3['Items'][ind])
                        
                        # array2.append(array1)
                        # arcmcode_linenum_list.index(array1)
                        
                        df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - AlreadyPosted'
                        failedrow += 1
                        totalGrpoExist += 1
                    
                    else:
                        df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind])

                else:
                    df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - ControlAccount'
                    ctrlacctrow += 1
                          
            except ValueError:
                    df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - InvalidContNo'
                    failedrow += 1
                    totalGrpoExist += 1


            ###########################################################################################
            # CLIENT/VENDOR VALIDATION
            # BP CODE
            # print(df3['S-AC'][ind])
            try:
                if(df3['S-AC'][ind] + "-C" not in bpcode_list):
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-C") + ' - InvalidBP'
                    failedrow += 1
                    totalBPNotExist += 1        

                else:
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-C")

            except ValueError:
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-C") + ' - InvalidBP'
                    failedrow += 1
                    totalBPNotExist += 1



            ###########################################################################################

            # ITEM VALIDATION
            # ITEM CODE
            try:

                if(df3['Material Code'][ind] != ''):
                    if(df3['Material Code'][ind] not in itemcode_list):
                        df3.at[ind,'Material Code']=str(df3['Material Code'][ind]) + ' - InvalidItem'
                        failedrow += 1
                        totalItemNotExist += 1

                    else:
                        df3.at[ind,'Material Code']=str(df3['Material Code'][ind])
                        item_index = itemcode_list.index(df3['Material Code'][ind])
                        item_uom = itemcode_uomcode_list[item_index][1]
                        df3.at[ind,'Quantity Unit']=str(item_uom)
                
                else:
                    df3.at[ind,'Material Code']=str(df3['Material Code'][ind])

            except ValueError:
                    df3.at[ind,'Material Code']=str(df3['Material Code'][ind]) + ' - InvalidItem'
                    failedrow += 1
                    totalItemNotExist += 1


            ###########################################################################################


            # QUANTITY VALIDATION
            # QUANTITY
            try:
                if(df3['Quantity'][ind] == 0 ):
                    df3.at[ind,'Quantity']= int(1)
                    # failedrow += 1
                    # totalItemNotExist += 1

                else:
                    df3.at[ind,'Quantity']=float(df3['Quantity'][ind])
                          
            except ValueError:
                    df3.at[ind,'Quantity']=str(df3['Quantity'][ind]) + ' - InvalidQuantity'
                    failedrow += 1
                    totalItemNotExist += 1

            ###########################################################################################

            # DATE VALIDATION
            # POSTING DATE
            try:
                    # dateObject = datetime.datetime.strptime(str(math.floor(df3['Ent.DT'][ind])), date_format)
                    # current_date_time = dateObject.strftime("%Y-%m-%d")
                    # df3.at[ind,'Ent.DT']='2023-01-13'\
                    # 20160429
                    date = str(df3['Ent.DT'][ind])
                    year = date[0:4]
                    month = date[4:6]
                    day = date[6:8]
                    
                    df3.at[ind,'Ent.DT'] = str(year) + '-' + str(month) + '-' + str(day)
                    # print(date)
                    # print(year)
                    # print(month)
                    # print(day)
                    # print('------')


            except ValueError:
                    df3.at[ind,'Ent.DT']=str(math.floor(df3['Ent.DT'][ind])) + ' - InvalidDate'
                    failedrow += 1


            # DOCUMENT DATE
            try:
                    if(df3['Trn DT'][ind] != ''):
                        date = str(df3['Trn DT'][ind])
                        year = date[0:4]
                        month = date[4:6]
                        day = date[6:8]
                        df3.at[ind,'Trn DT'] = str(year) + '-' + str(month) + '-' + str(day)
                    else:
                        date = str(df3['Trn DT'][ind])
                        year = date[0:4]
                        month = date[4:6]
                        day = date[6:8]
                        df3.at[ind,'Trn DT'] = str(year) + '-' + str(month) + '-' + str(day)
            except ValueError:
                    df3.at[ind,'Trn DT']=str(math.floor(df3['Trn DT'][ind])) + ' - InvalidDate'
                    failedrow += 1


            # DUE DATE
            try:
                    if(df3['Trn DT'][ind] != ''):
                        date = str(df3['Trn DT'][ind])
                        year = date[0:4]
                        month = date[4:6]
                        day = date[6:8]
                        df3.at[ind,'Due Date'] = str(df3['Trn DT'][ind])
                    else:
                        date = str(df3['Due Date'][ind])
                        year = date[0:4]
                        month = date[4:6]
                        day = date[6:8]
                        df3.at[ind,'Due Date'] = str(year) + '-' + str(month) + '-' + str(day)
            except ValueError:
                    df3.at[ind,'Due Date']=str(math.floor(df3['Due Date'][ind])) + ' - InvalidDate'
                    failedrow += 1




            ###########################################################################################

            # VAT GROUP
            try:
                if(df3.at[ind,'Tx'] == '5'):
                    df3.at[ind,'Tx']='IVAT-E'

                if(df3.at[ind,'Tx'] == 'I2'):
                    df3.at[ind,'Tx']='IVAT-N'

                if(df3.at[ind,'Tx'] == 'IZ'):
                    df3.at[ind,'Tx']='IVAT-Z'

            except ValueError:
                    df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                    failedrow += 1


            ###########################################################################################

            # UOM
            try:
                df3.at[ind,'Tx'] = 'OVAT-N'

            except ValueError:
                    df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                    failedrow += 1


            if(failedrow > 0):
                df3.at[ind,'Status'] = "FAILED"

            else:
                df3.at[ind,'Status'] = "SUCCESS"
                 


            if(ctrlacctrow > 0):
                df3.at[ind,'Status'] = "CTRL ACCT" 
            # print(failedrow)


            self.label_arcm_total_bp_not_exist.setText("BP Does Not Exist: " + str(totalBPNotExist))
            self.label_arcm_total_item_not_exist.setText("Item Does Not Exist: " + str(totalItemNotExist))
            self.label_arcm_total_exist.setText("Doc. Already Exist: " + str(totalGrpoExist))
        
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        
        return df3
    

    def loadCsv(self,file_name):
        totalready = 0


        df3 = ARCreditMemo.processDataFrame(self, file_name)
        print(df3)
        rowcount = len(df3)
        self.tableWidget_arcm.setColumnCount(25)
        self.tableWidget_arcm.setRowCount(rowcount)
        for i in range(rowcount):
            print(str(df3._get_value(i, 18, takeable=True)))
            if(str(df3._get_value(i, 18, takeable=True)) == '2' and str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1



            for j in range(25):
                self.tableWidget_arcm.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))


                if(str(df3._get_value(i, 18, takeable=True)) == '2'):
                    self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                else:
                    self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(240, 255, 255))



                if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                    self.tableWidget_arcm.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_arcm.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    # print(str(df3._get_value(i, j, takeable=True)))
                    try:
                        if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(255, 165, 0))


                        if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(255,255,0))

                    
                        if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(150,75,0))

                    except:
                        self.tableWidget_arcm.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
            


                elif(str(df3._get_value(i, 0, takeable=True))== "CTRL ACCT"):
                    self.tableWidget_arcm.item(i,0).setBackground(QtGui.QColor(13,152,186))
                    if("ControlAccount" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arcm.item(i,j).setBackground(QtGui.QColor(13,152,186))


                else:
                    self.tableWidget_arcm.item(i,0).setBackground(QtGui.QColor(144, 238, 144))


        self.label_arcm_total_ready.setText("AP CREDIT MEMO READY TO POST: " + str(totalready))
   


    def postARCreditMemo(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()

        df3 = ARCreditMemo.processDataFrame(self,file_name)
        # print(df3)
        # print(type(df3))
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        headers = df4.loc[df4['Items'] == 2]
        

        df4.to_csv('arcm.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")

        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPOST /b1s/v1/CreditNotes\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header

        for ind in headers.index:
            # print(headers.at[ind,'Cont.No.'])
            dflines = df4.loc[df4['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            documentlines = []
            for ind2 in dflines.index:
                if(str(dflines['A/C Code'][ind2]) != "11310"):
                    if(str(dflines['Material Code'][ind2]) != ''):
                        linesdict =	{
                            "ItemCode": str(dflines['Material Code'][ind2]),
                            "Quantity": float(str(dflines['Quantity'][ind2]).replace(",", "").replace(".00", "").replace("-", "")),
                            "VatGroup": str(dflines['Tx'][ind2]),
                            "UomCode": str(dflines['Quantity Unit'][ind2]),
                            # "Currency": str(dflines['Curr'][ind2]),
                            
                            "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                            

                        }
                        documentlines.append(linesdict)

                    else:
                        
                            linesdict =	{
                                "AccountCode": str(dflines['A/C Code'][ind2]),
                                "VatGroup": str(dflines['Tx'][ind2]),
                                # "Currency": str(dflines['Curr'][ind2]),
                                
                                "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                                

                            }
                            documentlines.append(linesdict)
                




            documentArray = []

            if(str(headers['DT'][ind]) == 'RV'):
                headerdict =	{
                    "CardCode": str(headers['S-AC'][ind]),
                    "DocDate": str(headers['Ent.DT'][ind]),
                    "TaxDate": str(headers['Trn DT'][ind]),
                    "DocDueDate": str(headers['Due Date'][ind]),
                    "NumAtCard": str(headers['Ref.No.'][ind]),
                    "Comments": str(headers['REMARKS'][ind]),
                    "U_Unit": str(headers['Unit'][ind]),
                    "U_UnitName": str(headers['Unit Name'][ind]),
                    "U_DocNo": str(headers['Doc.No.'][ind]),
                    "U_InsNo": str(headers['Instruction No.'][ind]),
                    "U_ContNo": str(headers['Cont.No.'][ind]),
                    "U_ClrngDoc": str(headers['Clrng doc.'][ind]),
                    "U_ClrngDT": str(headers['Clrng DT'][ind]),
                    "U_SubAccount": str(headers['2nd Sub-Account'][ind]),
                    "DocType": "dDocument_Items",
                    "ControlAccount": "11310",
                    "DocumentLines": documentlines
                }
            else:
                 headerdict =	{
                    "CardCode": str(headers['S-AC'][ind]),
                    "DocDate": str(headers['Ent.DT'][ind]),
                    "TaxDate": str(headers['Trn DT'][ind]),
                    "DocDueDate": str(headers['Due Date'][ind]),
                    "NumAtCard": str(headers['Ref.No.'][ind]),
                    "Comments": str(headers['REMARKS'][ind]),
                    "U_Unit": str(headers['Unit'][ind]),
                    "U_UnitName": str(headers['Unit Name'][ind]),
                    "U_DocNo": str(headers['Doc.No.'][ind]),
                    "U_InsNo": str(headers['Instruction No.'][ind]),
                    "U_ContNo": str(headers['Cont.No.'][ind]),
                    "U_ClrngDoc": str(headers['Clrng doc.'][ind]),
                    "U_ClrngDT": str(headers['Clrng DT'][ind]),
                    "U_SubAccount": str(headers['2nd Sub-Account'][ind]),
                    "DocType": "dDocument_Service",
                    "ControlAccount": "11310",
                    "DocumentLines": documentlines
                }
            # print(documentlines)

            documentArray.append(headerdict)


            if(index == 0):
                data += content_header
                data += '\n'
                data += json.dumps(documentArray[0])
                data += '\n'
            else:
                data += '\n'
                data += changeset_header
                data += '\n'
                data += content_header
                data += '\n'
                data += json.dumps(documentArray[0])
                data += '\n'
                data += changeset_footer
                data += '\n'

            

            index += 1
        
        


        data += batch_footer
        with open('readme.txt', 'w') as f:
            f.write(data)
        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        print(requestUrl.text)  
        ARCreditMemo.loadCsv(self,file_name)

