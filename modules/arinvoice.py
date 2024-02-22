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
import modules.arinvoice as ARInvoice


class ARInvoice():
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
        arinvoiceSAPDocEntry_list = arinvoiceCodeListArr[2]
        

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')
        df = df.loc[df['DT'].isin(['RV'])]
        # df = df.loc[df['DT'].isin(['RV','H1','H9'])]
        # df = df.loc[df['A/C Code'].isin(['30112','30211','30212','30214','30215'])]
        # df = df.loc[df['A/C Code'].isin(['11310']) == False]
        df = df.loc[df['2nd Sub-Account'].isin(['CM','DM']) == False]
        
        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48, 50, 51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )
        df2.insert(26,'SAP DocEntry', '' )

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
            'SAP DocEntry'

            ]]
        
        # print(len(df2.axes[1]))
        # df3.to_csv('file_name1.csv', index=False)

        totalRequiredFields = 0
        totalBPNotExist = 0
        totalItemNotExist = 0
        totalDocsExist = 0

        # df3.groupby('Cont.No.')
        # df3 = df3.sort_values(['Items'],ascending=False)
        # # .groupby('Cont.No.')
        # df3 = df3.groupby('Cont.No.').first()
        # df3 = df3.groupby(['Cont.No.', 'Items']).reset_index()
        # df3 = df3.first()


        # df3 = df3.sort_values(['Cont.No.', 'Items'])
        # df3=df3.sort_values(['Cont.No.', 'Items'],ascending=True).groupby('Cont.No.').head(3)
        df3 = df3.sort_values(['Doc.No.','Cont.No.','Items'], ascending=True)
        
        print(df3['Cont.No.'])
        array2 = []
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            ctrlacctrow = 0
            postedrow = 0
            # AR INVOICE VALIDATION
            # AR INVOICE CODE
            try:
                if(str(df3['A/C Code'][ind]) != "11310"):
                    if(str(df3['Doc.No.'][ind]) in arinvoicecode_list):
                        indexsapdocentry = arinvoicecode_list.index(str(df3['Doc.No.'][ind]))
                        indexsapdocentry2 = arinvoiceSAPDocEntry_list[indexsapdocentry]
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                        df3.at[ind,'SAP DocEntry']=str(indexsapdocentry2)
                        postedrow += 1
                        totalDocsExist += 1
                    

                    else:
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                else:
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
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
                    # df3.at[ind,'Quantity']=""
                    df3.at[ind,'Quantity']=float(df3['Quantity'][ind])
                    # df3.at[ind,'Quantity']= int(1)
                          
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
                    df3.at[ind,'Tx']='OVAT-E'

                if(df3.at[ind,'Tx'] == 'I2'):
                    df3.at[ind,'Tx']='OVAT-N'

                if(df3.at[ind,'Tx'] == 'IZ'):
                    df3.at[ind,'Tx']='OVAT-Z'

            except ValueError:
                    df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                    failedrow += 1


            ###########################################################################################

            # UOM
            try:
               df3.at[ind,'Tx']='OVAT-N'


            except ValueError:
                    df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                    failedrow += 1

            
            if(df3['Clrng doc.'][ind] != ''):
                    df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "")


            if(failedrow > 0):
                df3.at[ind,'Status'] = "FAILED"

            elif(postedrow > 0):
                    df3.at[ind,'Status'] = "POSTED"

            else:
                df3.at[ind,'Status'] = "SUCCESS"




            print(ctrlacctrow)
            print('HEYHEYHEY')
            if(ctrlacctrow > 0):
                df3.at[ind,'Status'] = "CTRL ACCT" 
                 
            # print(failedrow)

            self.label_arinvoice_total_required_fields.setText("Required Fields: " + str(totalRequiredFields))
            self.label_arinvoice_total_bp_not_exist.setText("BP Does Not Exist: " + str(totalBPNotExist))
            self.label_arinvoice_total_item_not_exist.setText("Item Does Not Exist: " + str(totalItemNotExist))
            self.label_arinvoice_total_exist.setText("Doc. Already Exist: " + str(totalDocsExist))
        
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        
        return df3
    


    def loadCsv(self, file_name):
        totalready = 0
        
        df3 = ARInvoice.processDataFrame(self, file_name)
        rowcount = len(df3)
        self.tableWidget_arinvoice.setColumnCount(27)
        self.tableWidget_arinvoice.setRowCount(rowcount)
        for i in range(rowcount):
            if(str(df3._get_value(i, 18, takeable=True)) == '2' and str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1


            for j in range(27):
                
                self.tableWidget_arinvoice.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))

                if(str(df3._get_value(i, 18, takeable=True)) == '2'):
                    self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                else:
                    self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(240, 255, 255))



                if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                    self.tableWidget_arinvoice.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_arinvoice.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    # print(str(df3._get_value(i, j, takeable=True)))
                    try:

                        if("RequiredField" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(255, 153, 153))


                        if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(255, 165, 0))


                        if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(255,255,0))

                        
                        if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(150,75,0))

                    except:
                        self.tableWidget_arinvoice.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                


                elif(str(df3._get_value(i, 0, takeable=True))== "CTRL ACCT"):
                    self.tableWidget_arinvoice.item(i,0).setBackground(QtGui.QColor(13,152,186))
                    if("ControlAccount" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_arinvoice.item(i,j).setBackground(QtGui.QColor(13,152,186))

                elif(str(df3._get_value(i, 0, takeable=True))== "POSTED"):
                        self.tableWidget_arinvoice.item(i,0).setBackground(QtGui.QColor(176,224,230))

                else:
                    self.tableWidget_arinvoice.item(i,0).setBackground(QtGui.QColor(144, 238, 144))



        
        
        
        self.label_arinvoice_total_ready.setText("AR INVOICES READY TO POST: " + str(totalready))


    def postARInvoice(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()

        df3 = ARInvoice.processDataFrame(self,file_name)
        # df3 = df3.head(500)
        # print(df3)
        # print(type(df3))
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 

        ctrlheaders = df3.loc[df3['Items'].isin([1,"1"])]
        headers = df4.loc[df4['Items'].isin([2,"2"])]
        tax = df4.loc[df4['A/C Code'] == '']
        
        print(type(headers))
        print('WHO CAN IT BE NOW')

        print('---------------------------------')
        print(headers)
        print(ctrlheaders)
        df4.to_csv('arinvoice.csv', index=False)
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

        for ind in headers.index:
            # print(headers.at[ind,'Cont.No.'])
            dflines = df4.loc[df4['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            ctrllines = ctrlheaders.loc[ctrlheaders['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            # print(ctrllines['Clrng doc.'])
            # print(type(ctrllines['Clrng doc.']))
            print(ctrllines)
            ctrlaccount = ctrllines['A/C Code'].values[0]
            clrndoc = ctrllines['Clrng doc.'].values[0]
            documentlines = []
            control_account = ''
            if(str(dflines['A/C Code'][ind]) != "11310"):
                control_account = '11310'




            for ind2 in dflines.index:
                
                if(str(dflines['A/C Code'][ind2]) != "11310"):
                    if(str(dflines['Material Code'][ind2]) != ""):
                        linesdict =	{
                            "ItemCode": str(dflines['Material Code'][ind2]),
                            "Quantity": float(str(dflines['Quantity'][ind2]).replace(",", "").replace(".00", "").replace("-", "")),
                            "VatGroup": str(dflines['Tx'][ind2]),
                            "UomCode": str(dflines['Quantity Unit'][ind2]),
                            "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                                            

                        }
                        documentlines.append(linesdict)

                    else:
                        linesdict =	{
                            "AccountCode": str(dflines['A/C Code'][ind2]),
                            "VatGroup": str(dflines['Tx'][ind2]),
                            "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),

                        }   
                        documentlines.append(linesdict)



            documentArray = []
            if(str(headers['DT'][ind]) == 'RV'):
                headerdict =	{
                    "CardCode": str(headers['S-AC'][ind]),
                    "Series": 4,
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
                    "ControlAccount": "11310",
                    # "DocCurrency": "USD",
                    "DocumentLines": documentlines
                }
            else:
                 headerdict =	{
                    "CardCode": str(headers['S-AC'][ind]),
                    "Series": 4,
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
                    "U_ClrngDT": str(clrndoc),
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
        # print(data)
        with open('arinv.txt', 'w') as f:
            f.write(data)
        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        print(requestUrl.text)  


        df4 = df3.loc[df3['Status'] == "POSTED"] 
        ctrlheaders = df3.loc[df3['Items'].isin([1,"1"])]
        headers = df4.loc[df4['Items'] == 2]
        

        df4.to_csv('arinvoice.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")

        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPATCH /b1s/v1/Invoices\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header

        for ind in headers.index:
            # print(headers.at[ind,'Cont.No.'])
            dflines = df4.loc[df4['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            print('POSTED DF HEADERS')
            print(dflines)
            print(ctrlheaders['Doc.No.'] + '/' + headers.at[ind,'Doc.No.'])
            ctrllines = ctrlheaders.loc[ctrlheaders['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            print('POSTED CTR HEADERS')
            print(ctrllines)
            # print(ctrllines['Clrng doc.'])
            # print(type(ctrllines['Clrng doc.']))
            ctrlaccount = ctrllines['A/C Code'].values[0]
            clrndoc = ctrllines['Clrng doc.'].values[0]
            documentlines = []
            control_account = ''
            if(str(dflines['A/C Code'][ind]) != "11310"):
                control_account = '11310'


            documentArray = []
            if(str(headers['DT'][ind]) == 'RV'):
                headerdict =	{
                    "U_ClrngDoc": str(clrndoc)
                    
                }
            else:
                headerdict =	{
                   
                    "U_ClrngDoc": str(clrndoc)
                    
                }

            # print(documentlines)

            documentArray.append(headerdict)

            content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPATCH /b1s/v1/Invoices(""" + headers['SAP DocEntry'][ind] + """)""" + """\nContent-Type: application/json\n"""
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
        with open('arinv.txt', 'w') as f:
            f.write(data)
        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        print(requestUrl.text)
        # APInvoice.APInvoice.postAPInvoice(self,file_name,sessionKey)
        # APCreditMemo.APCreditMemo.postAPCreditMemo(self,file_name,sessionKey)
        ARInvoice.loadCsv(self,file_name)

