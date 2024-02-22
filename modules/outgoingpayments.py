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

import modules.utilities as Utilities


class OutgoingPayments():
    def processDataFrame(self, file_name):

        bpCodeListArr = Utilities.Utilities.bpQueryValidator()
        bpcode_list = bpCodeListArr[0]
        bpname_list = bpCodeListArr[1]


        itemCodeListArr = Utilities.Utilities.itemQueryValidator()
        itemcode_list = itemCodeListArr[0]
        itemcode_uomcode_list = itemCodeListArr[1]

        ovpmCodeListArr = Utilities.Utilities.ovpmQueryValidator()
        ovpmcode_list = ovpmCodeListArr[0]
        ovpmcode_linenum_list = ovpmCodeListArr[1]


        apapcmCodeListArr = Utilities.Utilities.apinvoiceForOVPMQueryValidator()
        apv_or_apcm_list = apapcmCodeListArr[0]
        apv_or_apcm_docentry_list = apapcmCodeListArr[1]
        apv_or_apcm_clearingdoc_list = apapcmCodeListArr[2]
        apv_or_apcm_objtype_list = apapcmCodeListArr[3]

        

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')
        df = df.loc[df['DT'].isin(['QU','QS'])]
        # df = df.loc[df['Clrng doc.'].notnull()]
        df = df.loc[df['A/C Code'] != '44111']
        

        # df = df.loc[df['Doc.No.'] == '100014603']

        # df = df.loc[df['A/C Code'] == 33333]
        
        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48, 50, 51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )
        df2.insert(21,'SAP Doc Entry', '' )
        df2.insert(22,'SAP Obj Type', '' )

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
            'SAP Doc Entry',
            'SAP Obj Type'

            ]]
        
        # print(len(df2.axes[1]))
        # df3.to_csv('file_name1.csv', index=False)

        totalBPNotExist = 0
        totalItemNotExist = 0
        totalGrpoExist = 0
        totalDocsExist = 0


        # df3.groupby('Cont.No.')
        # df3.sort_values(['Items'],ascending=False).groupby('Cont.No.')

        # df3 = df3.sort_values(['DT','Doc.No.','A/C Code'], ascending=False)
       
        df3['Dom. Amt.'] = df['Dom. Amt.'].str.replace(",", "").astype(float)


        def sum_(x):
            try:
                return np.sum(x)
            except:
                return np.nan

        def max_(x):
            try:
                return np.max(x)
            except:
                return np.nan


        df3 = df3.groupby(['DT','Doc.No.','A/C Code']).agg({'Status': max_, 
                                                            'DT': max_, 
                                                            'Ent.DT': max_, 
                                                            'Trn DT': max_,  
                                                            'Due Date': max_, 
                                                            'Ref.No.': max_, 
                                                            'S-AC': max_, 
                                                            'S-AC Name': max_, 
                                                            'A/C Code': max_, 
                                                            'Unit': max_, 
                                                            'Unit Name': max_, 
                                                            'Doc.No.': max_, 
                                                            'REMARKS': max_, 
                                                            'Instruction No.': max_, 
                                                            'Cont.No.': max_, 
                                                            'Clrng doc.': max_, 
                                                            'Clrng DT': max_, 
                                                            '2nd Sub-Account': max_, 
                                                            'Items': max_, 
                                                            'Curr': max_, 
                                                            'Trans. Amt.': max_, 
                                                            'Dom. Amt.': sum_, 
                                                            'SAP Doc Entry': max_, 
                                                            'SAP Obj Type' : max_, 
                                                            })
        
       
        
        print(df3)
        # df3 = df3.loc[df3['Doc.No.']=='100001176']
        
        # df3 = df3.loc[df3.groupby('Doc.No.')['Items'].idxmin()]

        # df3 = df3['SERIES3'] = df3.groupby(['Doc.No.'])['Items'].transform('min')

        # print(df3['Items'])

        
        array2 = []
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            bankrow = 0
            bankrowcharge = 0
            # OUTGOING PAYMENTS VALIDATION
            # OUTGOING PAYMENTS CODE
            # print(ovpmcode_list)
            try:
                
                if(str(df3['Doc.No.'][ind]) in ovpmcode_list):
                    
                    
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - AlreadyPosted'
                    failedrow += 1
                    
                    if(str(df3['A/C Code'][ind]) == '41210'):
                        totalDocsExist += 1   
                    
                
                elif(df3['Doc.No.'][ind] == ''):
                        
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - RequiredField'
                    
                    
                        
                else:
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                
                          
            except ValueError:
                    # df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - InvalidContNo'
                    # failedrow += 1
                    totalDocsExist += 1


            ###########################################################################################
            # CLIENT/VENDOR VALIDATION
            # BP CODE
            # print(df3['S-AC'][ind])
            try:
                if(df3['S-AC'][ind] + "-V" not in bpcode_list):
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-V") + ' - InvalidBP'
                    failedrow += 1
                    totalBPNotExist += 1        

                else:
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-V")

            except ValueError:
                    df3.at[ind,'S-AC']=str(df3['S-AC'][ind] + "-V") + ' - InvalidBP'
                    failedrow += 1
                    totalBPNotExist += 1


            ###########################################################################################
            # AP/CM VALIDATION
            try:

                df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "")
                if(str(df3['Clrng doc.'][ind]).replace(".0", "") in apv_or_apcm_clearingdoc_list and str(df3['A/C Code'][ind]).replace(".0", "") == '41210'):
                    docIndex = apv_or_apcm_clearingdoc_list.index(str(df3['Clrng doc.'][ind]).replace(".0", ""))
                    docentry = apv_or_apcm_docentry_list[docIndex]
                    objtype = apv_or_apcm_objtype_list[docIndex]
                    df3.at[ind,'SAP Doc Entry']=str(docentry)
                    df3.at[ind,'SAP Obj Type']=str(objtype)


                elif(str(df3['A/C Code'][ind]).replace(".0", "") in ['10131','10120']):
                    bankrow += 1


                elif(str(df3['A/C Code'][ind]).replace(".0", "") == '33333'):
                    bankrowcharge += 1


                else:
                    df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "")
                    failedrow += 1

            except ValueError:
                    df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "") + ' - InvalidClearNo'
                    failedrow += 1
                    totalBPNotExist += 1

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

            # SAC_next = df3['S-AC'][ind]
            # DocNo_prev = df3['Doc.No.'][ind]
            # Clrng_doc_prev = df3['Clrng doc.'][ind]
            # Items = df3['Items'][ind]

            # next_row = df3.iloc[ind + 1]
            # SAC_next = next_row['S-AC']
            # print(SAC_next)

            
            # if(df3['S-AC'][ind] == SAC_next and df3['Doc.No.'][ind] == DocNo_prev and Clrng_doc_prev == df3['Clrng doc.'][ind] and Items != df3['Items'][ind] and df3['A/C Code'][ind] == "44111"):
            #     print("GOT MISC" + str(df3['A/C Code'][ind]))
                     



            if(failedrow > 0):
                df3.at[ind,'Status'] = "FAILED"

            elif(bankrow > 0):
                df3.at[ind,'Status'] = "BANK"

            elif(bankrowcharge > 0):
                df3.at[ind,'Status'] = "BANK CHARGE"    
            
            else:
                df3.at[ind,'Status'] = "SUCCESS"
                 
            # print(failedrow)


            self.label_ovpm_total_bp_not_exist.setText("BP Does Not Exist: " + str(totalBPNotExist))
            self.label_ovpm_total_item_not_exist.setText("Item Does Not Exist: " + str(totalItemNotExist))
            self.label_ovpm_total_exist.setText("Doc. Already Exist: " + str(totalDocsExist))
        


        
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        return df3
    

    def loadCsv(self, file_name):
        df3 = OutgoingPayments.processDataFrame(self, file_name)
        totalready = 0
        # df3 = df3.loc[df3['Status'] == "SUCCESS"] 
        rowcount = len(df3)
        self.tableWidget_ovpm.setColumnCount(24)
        self.tableWidget_ovpm.setRowCount(rowcount)
        for i in range(rowcount):

            if(str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1


            for j in range(24):
                # print(df3._get_value(i, j, takeable=True) )
                self.tableWidget_ovpm.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                self.tableWidget_ovpm.setCurrentCell(32,1)    

                if(str(df3._get_value(i, 17, takeable=True)) != ''):
                    self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                else:
                    self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(240, 255, 255))

                if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                    self.tableWidget_ovpm.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_ovpm.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    # print(str(df3._get_value(i, j, takeable=True)))
                    try:
                        if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(255, 165, 0))


                        if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(255,255,0))
                            

                        if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(150,75,0))

                    except:
                        self.tableWidget_ovpm.item(i,0).setBackground(QtGui.QColor(255, 128, 128))

                elif(str(df3._get_value(i, 0, takeable=True)) in ["BANK","BANK CHARGE"]):
                    self.tableWidget_ovpm.item(i,j).setBackground(QtGui.QColor(211,211,211))
                else:
                    # self.tableWidget_ovpm.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_ovpm.item(i,0).setBackground(QtGui.QColor(144, 238, 144))



        self.label_ovpm_total_ready.setText("AP INVOICE READY TO POST: " + str(totalready))


    def postOutgoingPayments(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()

        df3 = OutgoingPayments.processDataFrame(self,file_name)
        # print(df3)
        # print(type(df3))
        df4 = df3.loc[df3['Status'] == "SUCCESS"]
        df5 = df3.loc[df3['Status'] == "BANK"]
        df6 = df3.loc[df3['Status'] == "BANK CHARGE"]
        headers = df4.loc[df4['SAP Doc Entry'] != '']

        

        df4.to_csv('ovpm.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")

        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPOST /b1s/v1/VendorPayments\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header

        for ind in df4.index:
            # print(headers.at[ind,'Cont.No.'])
            dfbanklines = df5.loc[df5['Doc.No.'] == df4.at[ind,'Doc.No.']] 
            dfinvoicelines = df4.loc[df4['Doc.No.'] == str((dfbanklines.get("Doc.No.")))]
            dfbankchargeline = df6.loc[df6['Doc.No.'] == df4.at[ind,'Doc.No.']] 
            print(dfbankchargeline)
            print('*****************************8')
            print("Bank Acct:"+ str(dfbanklines.get("A/C Code")[0]))
            print('----------------Bank---------------------------------')
            if(str(dfbanklines.get("Doc.No.")[0]) == str(df4['Doc.No.'][ind])):
                print("Invoice Acct:"+  df4['S-AC'][ind])
                print("Invoice Entry:"+  df4['SAP Doc Entry'][ind])
                print('----------------Invoice---------------------------------')
            # print(dfbanklines)
            # print("Bank Acct:"+ str(dflines['S-AC'][ind]))
            # print("CheckNumber:"+ str(dflines.loc[dflines['Cont.No.']]))
            # print("CheckSum:"+ float(str(dflines.loc[dflines['Dom. Amt.']]).replace(",", "").replace(".00", "").replace("-", "")))
           
            print('----------------haha---------------------------------')


            paymentlines = []
            invoiceslines = []


            if(str(dfbanklines.get('Cont.No.')[0]) != ''):
                linesdict =	{
                    "DueDate": str(dfbanklines.get('Ent.DT')[0]),
                    "CheckNumber": str(dfbanklines.get('Cont.No.')[0]),
                    "BankCode": dfbanklines.get('S-AC')[0],
                    "CheckAccount": dfbanklines.get('A/C Code')[0],
                    "CheckSum": float(str(dfbanklines.get('Dom. Amt.')[0]).replace(",", "").replace(".00", "").replace("-", "")),
                    # "CheckAccount": "161020",
                    "ManualCheck": "tYES"
                }     
                paymentlines.append(linesdict)
            else:
                paymentlines.append(str(dfbanklines.get('A/C Code')[0]))
                paymentlines.append(float(str(dfbanklines.get('Dom. Amt.')[0]).replace(",", "").replace(".00", "").replace("-", "")))
                paymentlines.append(str(dfbanklines.get('Ent.DT')[0]))
                paymentlines.append(str(dfbanklines.get('Ref.No.')[0]))
                paymentlines.append(float(str(dfbankchargeline.get('Dom. Amt.')[0]).replace(",", "").replace(".00", "").replace("-", "")))



            print(paymentlines)
            if(str(dfbanklines.get("Doc.No.")[0]) == str(df4['Doc.No.'][ind])):
                if(str(dfbanklines.get('DT')[0]) == 'QU' and df4['Status'][ind] == 'SUCCESS'):
                    linesdict2 = {         
                        "DocEntry": df4['SAP Doc Entry'][ind],
                        "InvoiceType": "it_PurchaseInvoice"
                    }
                    invoiceslines.append(linesdict2)
                else:
                    linesdict2 = {         
                        "DocEntry": df4['SAP Doc Entry'][ind],
                        "InvoiceType": "it_PurchaseInvoice"
                    }  
                    invoiceslines.append(linesdict2)


                print(invoiceslines)
                print(str(dfbanklines.get('Cont.No.')[0]))
        #             if(str(headers['Ent.DT'][ind])== 'QU'):
        #                 linesdict2 = {         
        #                     "DocEntry": str(headers['SAP Doc Entry'][ind]),
        #                     "InvoiceType": "it_PurchaseInvoice"
        #                 }
        #                 invoiceslines.append(linesdict2)
        #             else:
        #                 linesdict2 = {         
        #                     "DocEntry": str(headers['SAP Doc Entry'][ind]),
        #                     "InvoiceType": "it_PurchaseInvoice"
        #                 }  
        #                 invoiceslines.append(linesdict2)
                


            documentArray = []
            print(paymentlines)
            if(str(dfbanklines.get("Doc.No.")[0]) == str(df4['Doc.No.'][ind])):
                if(str(dfbanklines.get('Cont.No.')[0]) == ''):
                    headerdict =	{
                        "CardCode": str(df4['S-AC'][ind]),
                        "DocDate": str(df4['Ent.DT'][ind]),
                        "TaxDate": str(df4['Trn DT'][ind]),
                        "DueDate": str(df4['Due Date'][ind]),
                        "CounterReference": str(df4['Ref.No.'][ind]),
                        "Remarks": str(df4['REMARKS'][ind]),
                        "U_Unit": str(df4['Unit'][ind]),
                        "U_UnitName": str(df4['Unit Name'][ind]),
                        "U_DocNo": str(df4['Doc.No.'][ind]),
                        "U_InsNo": str(df4['Instruction No.'][ind]),
                        "U_ContNo": str(df4['Cont.No.'][ind]),
                        "U_ClrngDoc": str(df4['Clrng doc.'][ind]),
                        "U_ClrngDT": str(df4['Clrng DT'][ind]),
                        "U_SubAccount": str(df4['2nd Sub-Account'][ind]),
                        "TransferAccount": paymentlines[0],
                        "TransferSum": paymentlines[1],
                        "TransferDate": paymentlines[2],
                        "TransferReference": paymentlines[3],
                        "BankChargeAmount": paymentlines[4],
                        "PaymentInvoices": invoiceslines
                    }
                            
                else:
                    headerdict =	{
                        "CardCode": str(df4['S-AC'][ind]),
                        "DocDate": str(df4['Ent.DT'][ind]),
                        "TaxDate": str(df4['Trn DT'][ind]),
                        "DueDate": str(df4['Due Date'][ind]),
                        "CounterReference": str(df4['Ref.No.'][ind]),
                        "Remarks": str(df4['REMARKS'][ind]),
                        "U_Unit": str(df4['Unit'][ind]),
                        "U_UnitName": str(df4['Unit Name'][ind]),
                        "U_DocNo": str(df4['Doc.No.'][ind]),
                        "U_InsNo": str(df4['Instruction No.'][ind]),
                        "U_ContNo": str(df4['Cont.No.'][ind]),
                        "U_ClrngDoc": str(df4['Clrng doc.'][ind]),
                        "U_ClrngDT": str(df4['Clrng DT'][ind]),
                        "U_SubAccount": str(df4['2nd Sub-Account'][ind]),
                        "PaymentChecks": paymentlines,
                        "PaymentInvoices":invoiceslines
                    }

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
        print(data)
        with open('ovpm.txt', 'w') as f:
            f.write(data)
        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        print(requestUrl.text)  
        print(sessionKey)


        OutgoingPayments.loadCsv(self,file_name)

