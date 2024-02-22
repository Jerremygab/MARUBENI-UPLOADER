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
import modules.billingstatement as BillingStatement

groupcount = 0


class BillingStatement():

    def properIndex(df):
        df = df[[
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
            'rate'
        ]]


        return df



    def processDataFrame(self, file_name):

        bpCodeListArr = Utilities.Utilities.bpQueryValidator()
        bpcode_list = bpCodeListArr[0]
        bpname_list = bpCodeListArr[1]


        itemCodeListArr = Utilities.Utilities.itemQueryValidator()
        itemcode_list = itemCodeListArr[0]
        itemcode_uomcode_list = itemCodeListArr[1]

        arinvoiceCodeListArr = Utilities.Utilities.arinvoiceQueryValidator()
        arinvoicecode_list = arinvoiceCodeListArr[0]
        arinvoicecode_linenum_list = arinvoiceCodeListArr[1]


        billingStatementListArr = Utilities.Utilities.billingStatementValidAcctCode()
        billingStatement_list = billingStatementListArr[0]


        controlAccountListArr = Utilities.Utilities.controlAccount()
        controlAccount_list = controlAccountListArr[0]

        revenueAccountListArr = Utilities.Utilities.revenueAccount()
        revenueAccount_list = revenueAccountListArr[0]

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')
        
      
        
        df[['A/C Code']] = df[['A/C Code']].astype(str)
        
        print('------------------------UNA-------------------------')
        print(billingStatementListArr)
        df = df.loc[df['DT'].isin(['H1','H9'])]
        df = df.loc[df['A/C Code'].isin(billingStatementListArr)]
        # df = df.loc[df['A/C Code'].isin(['11310']) == False]
        # df = df.loc[df['2nd Sub-Account'].isin(['CM','DM']) == False]

        df = df.loc[df['2nd Sub-Account'].isin(['CM','DM']) == False]


        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48,  51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )

        df3 = BillingStatement.properIndex(df2)
        

        # df3['A/C Code'] = df3['A/C Code'].astype(np.float32)
        # df3['Doc.No.'] = df3['Doc.No.'].astype(np.float32)
        print(df3)
        print("-------------------------------------HAHA--------------------------------")

        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CTRL ACCOUNT LIST
        df4 = df3.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in controlAccountListArr))

        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CTRL REVENE LIST
        df5 = df4.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in revenueAccountListArr))



        # RETURNS TRUE IN GROUP IF TAX CODE IS DETECTED
        # try:
        df5['Tx'] = df['Doc.No.'].map(df.groupby('Doc.No.').apply(lambda x: x['A/C Code'].eq('44420').any()))
        # except:
        #     df5['Tx'] = 'OVAT-Z'     
        
        df6 = df5.groupby(['Doc.No.']).apply(lambda x: x.sort_values(['Items'], ascending=True).head(20))
       
        df6.to_csv('billstatement.csv', index=False)
        
        controlAccountListArr2 = Utilities.Utilities.controlAccount()
        ctrlaccnt = df3.loc[df3['A/C Code'].isin(controlAccountListArr2)]
        ctrlacct_list = ctrlaccnt['Doc.No.'].tolist()
        df3 = df3.loc[df3['Doc.No.'].isin(ctrlacct_list)]

        totalRequiredFields = 0
        totalBPNotExist = 0
        totalItemNotExist = 0
        totalDocsExist = 0

   
        df3 = df6
        array2 = []
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            ctrlacctrow = 0
            # AR INVOICE VALIDATION
            # AR INVOICE CODE
            if(df3['Doc.No.'][ind] in ctrlacct_list):
            
           
                try:
                    if(df3['A/C Code'][ind] not in controlAccountListArr and df3['A/C Code'][ind] not in ["41210"] ):
                        if(str(df3['Doc.No.'][ind]) in arinvoicecode_list and df3['Doc.No.'][ind] != ''):
                            
                            
                            df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - AlreadyPosted'
                            failedrow += 1
                            totalDocsExist += 1
                        
                        elif(df3['Doc.No.'][ind] == ''):
                            
                            df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - RequiredField'
                            failedrow += 1
                            
                            
                        else:
                            df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                    else:
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) 
                        # + ' - ControlAccount'
                        ctrlacctrow += 1
                            
                except ValueError:
                        # df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - InvalidContNo'
                        # failedrow += 1
                        totalDocsExist += 1

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


                if(df3['Clrng doc.'][ind] != ''):
                    df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "")
                




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
                    if(df3.at[ind,'Tx'] == True):
                        df3.at[ind,'Tx']='OVAT-S'

                    else:
                        df3.at[ind,'Tx']='OVAT-Z'
                         

                except ValueError:
                        df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                        failedrow += 1


                ###########################################################################################

               


                # RATE VALIDATION
                # RATE
                if(df3['rate'][ind] == '' ):
                    df3.at[ind,'rate']= int(1)
                    # failedrow += 1
                    # totalItemNotExist += 1

                else:
                    df3.at[ind,'rate']=float(df3['rate'][ind])
                            

                if(failedrow > 0):
                    df3.at[ind,'Status'] = "FAILED"

                else:
                    df3.at[ind,'Status'] = "SUCCESS"



                if(ctrlacctrow > 0):
                    df3.at[ind,'Status'] = "CTRL ACCT" 
                    


                


                if(df3['Status'][ind] == 'SUCCESS' and df3['Items'][ind] == 1):
                    df3.at[ind,'Items'] = 2 
                # print(failedrow)

                self.label_arinvoice_total_required_fields_2.setText("Required Fields: " + str(totalRequiredFields))
                self.label_arinvoice_total_bp_not_exist_2.setText("BP Does Not Exist: " + str(totalBPNotExist))
                self.label_arinvoice_total_item_not_exist_2.setText("Item Does Not Exist: " + str(totalItemNotExist))
                self.label_arinvoice_total_exist_2.setText("Doc. Already Exist: " + str(totalDocsExist))
                
                df4 = df3.loc[df3['Status'] == "SUCCESS"] 
            
        
        
        return [df3, groupcount]
    


    def loadCsv(self, file_name):
        totalready = 0
        
        dataframelist = BillingStatement.processDataFrame(self, file_name)

        df3 = dataframelist[0]
        rowcount = len(df3)
        self.tableWidget_arinvoice_2.setColumnCount(27)
        self.tableWidget_arinvoice_2.setRowCount(rowcount)
        for i in range(rowcount):

            if(str(df3._get_value(i, 18, takeable=True)) == '2' and str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1


            for j in range(27):
                    
                         
                    

                    if(str(df3._get_value(i, 0, takeable=True)) != "CTRL ACCT"):
                        self.tableWidget_arinvoice_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                        self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                    elif( str(df3._get_value(i, 0, takeable=True)) == "CTRL ACCT"):
                        self.tableWidget_arinvoice_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                        self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(240, 255, 255))


                    if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                        
                        self.tableWidget_arinvoice_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                        self.tableWidget_arinvoice_2.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                        # print(str(df3._get_value(i, j, takeable=True)))
                        try:

                            if("RequiredField" in str(df3._get_value(i, j, takeable=True))):
                                self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(255, 153, 153))


                            if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                                self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(255, 165, 0))


                            if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                                self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(255,255,0))

                            
                            if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                                self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(150,75,0))

                        except:
                            self.tableWidget_arinvoice_2.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    

                    elif(str(df3._get_value(i, 0, takeable=True))== "CTRL ACCT"):
                        self.tableWidget_arinvoice_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                        self.tableWidget_arinvoice_2.item(i,0).setBackground(QtGui.QColor(13,152,186))
                        if("ControlAccount" in str(df3._get_value(i, j, takeable=True))):
                                self.tableWidget_arinvoice_2.item(i,j).setBackground(QtGui.QColor(13,152,186))



                    # elif(str(df3._get_value(i, 0, takeable=True))== "CTRL ACCT" and df3._get_value(i, 18, takeable=True) > 1):
                    #     self.tableWidget_arinvoice_2.removeRow(i)



                    elif(str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                        self.tableWidget_arinvoice_2.item(i,0).setBackground(QtGui.QColor(144, 238, 144))






        

        
        
        
        self.label_arinvoice_total_ready_2.setText("AR INVOICES READY TO POST: " + str(totalready))



        # # rowCount() This property holds the number of rows in the table
        # for row in range(self.tableWidget_arinvoice_2.rowCount()): 
            
        #     if(self.tableWidget_arinvoice_2.item(row,0) == None):   
        #         print(self.tableWidget_arinvoice_2.item(row,0))
        #         print(row)
        #         self.tableWidget_arinvoice_2.removeRow(row)


    def postBillingStatement(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()
        
        dataframelist = BillingStatement.processDataFrame(self, file_name)

        df3 = dataframelist[0]
        groupcount = dataframelist[1]
        
        print(groupcount) 
        print(type(df3))
        print("ZOOMBIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe")

        controlAccountListArr = Utilities.Utilities.controlAccount()
        revenueAccountListArr = Utilities.Utilities.revenueAccount()


        print(df3)
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
       
        # df3.loc[df3['A/C Code'].isin(['sale','fullprice'])]
    

        ctrlheaders = df3.loc[df3['A/C Code'].isin(controlAccountListArr)]
        # headers = df4.loc[df4['A/C Code'].isin(revenueAccountListArr)]
        headers = df4.loc[df4['Items'] == 2]
        tax = df4.loc[df4['A/C Code'] == '']
        
        print(type(headers))
        print('WHO CAN IT BE NOW')

        print(controlAccountListArr)
        print(type(controlAccountListArr))
        print('---------------------------------')
        print(headers)
        
        df4.to_csv('billstatement.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")

        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPOST /b1s/v1/Invoices\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header
        print(groupcount)
        print('TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST')
        for ind in headers.index:
            # print(headers.at[ind,'Cont.No.'])
          
            # crlndoclines = df4.loc[df4['Doc.No.'] == ctrlheaders.at[ind,'Doc.No.']]
            dflines = df4.loc[df4['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            ctrllines = ctrlheaders.loc[ctrlheaders['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            # print(ctrllines['Clrng doc.'])
            # print(type(ctrllines['Clrng doc.']))
            ctrlaccount = ctrllines['A/C Code'].values[0]
            clrndoc = ctrllines['Clrng doc.'].values[0]
            # print(ctrllines['Clrng doc.'].values)
            # print(ctrlaccount)
            # print(clrndoc)
            # print('MMATCH----')
            # print('--------************************--------------')
            dflinestax = dflines


            documentlines = []
            tax = ''



            
            # if(str(dflinestax['A/C Code'][ind]) in ["44420"] ):
            #     taxgroup = 'OVAT-S'
            # else:
            #     taxgroup = 'OVAT-Z'

            taxgroup = 'OVAT-Z'
            controlaccount = ''
            for ind2 in dflines.index:
                # if(str(dflines['A/C Code'][ind2]) == '44420'):
                #     taxgroup = 'OVAT-S'

                print(str(dflines['A/C Code'][ind]) )
                
                if(str(ctrlaccount) in controlAccountListArr):
                    # controlaccount = str(dflines['A/C Code'][ind])
                    # clrndoc = str(dflines['Clrng doc.'][ind])
                    print('MMATCH')



                if(str(dflines['A/C Code'][ind2]) != "44420"):
                    if(str(dflines['A/C Code'][ind2]) not in controlAccountListArr):
                        if(str(dflines['Material Code'][ind2]) != ""):
                            
                            linesdict =	{
                                "ItemCode": str(dflines['Material Code'][ind2]),
                                "Quantity": float(str(dflines['Quantity'][ind2]).replace(",", "").replace(".00", "").replace("-", "")),
                                "VatGroup": str(dflines['Tx'][ind2]),
                                "UomCode": str(dflines['Quantity Unit'][ind2]),
                                "U_TransAmt": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                "LineTotal": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                "Currency": str(dflines['Curr'][ind2]),
                                "DocRate" : str(dflines['rate'][ind2]),
                                                

                            }
                            documentlines.append(linesdict)

                        else:
                            linesdict =	{
                                "AccountCode": str(dflines['A/C Code'][ind2]),
                                "VatGroup": str(dflines['Tx'][ind2]),
                                "U_TransAmt": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                "LineTotal": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                "Currency": str(dflines['Curr'][ind2]),
                                "DocRate" : str(dflines['rate'][ind2]),

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
                    "U_ClrngDoc": str(clrndoc),
                    "U_ClrngDT": str(headers['Clrng DT'][ind]),
                    "U_SubAccount": str(headers['2nd Sub-Account'][ind]),
                    "DocType": "dDocument_Items",
                    "ControlAccount": str(ctrlaccount),
                    "DocCurrency": str(headers['Curr'][ind]),
                    "DocRate" : str(dflines['rate'][ind]),
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
                    "U_ClrngDoc": str(clrndoc),
                    "U_ClrngDT": str(headers['Clrng DT'][ind]),
                    "U_SubAccount": str(headers['2nd Sub-Account'][ind]),
                    "DocType": "dDocument_Service",
                    "ControlAccount": str(ctrlaccount),
                    "DocCurrency": str(headers['Curr'][ind]),
                    "DocRate" : str(dflines['rate'][ind]),
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
        # print(data)
        with open('billstatement.txt', 'w') as f:
            f.write(data)
        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        # print(requestUrl.text)  
        
        BillingStatement.loadCsv(self,file_name)
        

