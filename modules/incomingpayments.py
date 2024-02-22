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


class IncomingPayments():
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
            'SAP Doc Entry',
            'SAP Obj Type',
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

        ovpmCodeListArr = Utilities.Utilities.orctQueryValidator()
        ovpmcode_list = ovpmCodeListArr[0]
        ovpmcode_linenum_list = ovpmCodeListArr[1]


        apapcmCodeListArr = Utilities.Utilities.arinvoiceForORCTQueryValidator()
        apv_or_apcm_list = apapcmCodeListArr[0]
        apv_or_apcm_docentry_list = apapcmCodeListArr[1]
        apv_or_apcm_clearingdoc_list = apapcmCodeListArr[2]
        apv_or_apcm_objtype_list = apapcmCodeListArr[3]

        
        controlAccountListArr = Utilities.Utilities.controlAccount()
        controlAccount_list = controlAccountListArr[0]

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')

        df[['A/C Code']] = df[['A/C Code']].astype(str).replace('.0', '')
        df['A/C Code'] = df['A/C Code'].str.replace('.0', '')
        
        df[['Doc.No.']] = df[['Doc.No.']].astype(str).replace('.0', '')
        df['Doc.No.'] = df['Doc.No.'].str.replace('.0', '')

        df[['Clrng doc.']] = df[['Clrng doc.']].astype(str).replace('.0', '')
        df['Clrng doc.'] = df['Clrng doc.'].str.replace('.0', '')


        print(df)
        print('------------------------UNA-------------------------')
        print(controlAccountListArr)
        df = df.loc[df['DT'].isin(['QO','QE'])]
        df = df.loc[df['A/C Code'] != '44111']
        df['DT'] = 'QO'
        # df = df.loc[df['Clrng doc.'].notnull()]
        print(df)
        print(df[['A/C Code']])
        print('------------------------PANGALAWA-------------------------')
        
        
        print(apv_or_apcm_clearingdoc_list)
        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48, 51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )
        df2.insert(21,'SAP Doc Entry', '' )
        df2.insert(22,'SAP Obj Type', '' )

        df3 = IncomingPayments.properIndex(df2)

        
        print(df3)
        print(type(df3))
        print("-------------------------------------HAHA--------------------------------")
        print(df['Clrng doc.'])
        paymenmeansAccount = ['10131','10120']
        cashAccount = ['33333','33331']


        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CTRL ACCOUNT LIST
        dfvalidctrl = df3.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in controlAccountListArr))

        print(dfvalidctrl)
        print(type(dfvalidctrl))
        print(controlAccountListArr)
        print('--------DF VALID CTRL------------')

        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN TRANSER/CHECK LIST
        dfvalidwithPaymentMeans = dfvalidctrl.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in paymenmeansAccount))


        print(dfvalidwithPaymentMeans)
        print(type(dfvalidwithPaymentMeans))
        print(paymenmeansAccount)
        print('--------DF VALID TRFR PAYMENTS------------')

        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CASH W/ BANK TRANSFER
        # RETURNS TRUE IF ALL ACCTCODE IN CASHACCOUNT IS PRESENT IN DOCNUM GROUP
        s = frozenset(cashAccount)
        dfvalidwithCashWithBankTransfrer = dfvalidctrl.groupby(['Doc.No.'])['A/C Code'].apply(s.issubset).reset_index()
        print(dfvalidwithCashWithBankTransfrer)
        print(type(dfvalidwithCashWithBankTransfrer))
        print('--------SERIES VALID CASH WITH TRANSFER------------')

        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CASH
        dfvalidCashOnly = dfvalidwithCashWithBankTransfrer[(dfvalidwithCashWithBankTransfrer['A/C Code'] == False)]
        print(dfvalidCashOnly)
        print(type(dfvalidCashOnly))
        dfvalidwithCash = dfvalidctrl[dfvalidctrl['Doc.No.'].isin(dfvalidCashOnly['Doc.No.'])]
        # dfvalidwithCash = dfvalidctrl.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in cashAccount))
        
        print(dfvalidwithCash)
        print(type(dfvalidwithCash))
        print(cashAccount)
        print('--------DOCNUMS VALID CASH ONLY (CASH WITH TRANSFER ISSUE) ------------')


        # FILTERS ALL GROUP THAT CONTAINS A ACCTCODE IN CASH
        dfvalidTransferOnly = dfvalidwithCashWithBankTransfrer[(dfvalidwithCashWithBankTransfrer['A/C Code'] == True)]
        print(dfvalidTransferOnly)
        print(type(dfvalidTransferOnly))
        dfvalidwithCashWithTransfer = dfvalidctrl[dfvalidctrl['Doc.No.'].isin(dfvalidTransferOnly['Doc.No.'])]
        # dfvalidwithCash = dfvalidctrl.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in cashAccount))
        
        print(dfvalidwithCashWithTransfer)
        print(type(dfvalidwithCashWithTransfer))
        print(cashAccount)
        print(dfvalidTransferOnly['A/C Code'])
        print('--------DOCNUMS VALID TRANSFER WITH CASH ONLY (CASH WITH TRANSFER ISSUE) ------------')
        

        

        # print(dfvalidwithCashWithBankTransfrer)
        # print(type(dfvalidwithCashWithBankTransfrer))
        # print(cashAccount)
        # print('--------DF VALID CASH WITH TRANSFER------------')

        print(dfvalidwithPaymentMeans['Clrng doc.'])
        print(dfvalidwithPaymentMeans['Doc.No.'])
        # FILTERS ALL GROUP THAT CONTAINS A INVOICE LINK IN INCOMING PAYMENT VIA CLRN DOC FIELD
        dfvalidforPyament = dfvalidwithPaymentMeans.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["Doc.No."])) for p in apv_or_apcm_clearingdoc_list))
        

        dfValid = dfvalidforPyament
        print(dfValid)
        print(type(dfValid))
        print('--------DF VALID------------')

        
        df4 = dfValid.loc[dfValid['Cont.No.'] != '']  
        df4 = df4.loc[df4['Ent.DT'] != '']
        df4 = df4.loc[df4['A/C Code'].isin(paymenmeansAccount)]
        df4['Trans. Amt.'] = df4['Trans. Amt.'].astype(str)
        df4['Dom. Amt.'] = df4['Dom. Amt.'].astype(str)

        print(df4['Trans. Amt.'])
        print(type(df4['Trans. Amt.']))

        df4['Trans. Amt.'] = df4['Trans. Amt.'].str.replace(',', '').astype(float)
        df4['Dom. Amt.'] = df4['Dom. Amt.'].str.replace(',', '').astype(float)
        df4.loc[:,'Status'] = '1_CHECK'

        df5 = dfValid.loc[dfValid['Cont.No.'] == '']
        df5 = df5.loc[df5['Ent.DT'] != '']
        df5 = df5.loc[df5['A/C Code'].isin(paymenmeansAccount)]
        df5['Trans. Amt.'] = df5['Trans. Amt.'].astype(str)
        df5['Dom. Amt.'] = df5['Dom. Amt.'].astype(str)
        df5['Trans. Amt.'] = df5['Trans. Amt.'].str.replace(',', '').astype(float)
        df5['Dom. Amt.'] = df5['Dom. Amt.'].str.replace(',', '').astype(float)
        df5.loc[:,'Status'] = '2_TRANSFER'

        # dfvalidctrl[dfvalidctrl['Doc.No.'].isin(dfvalidTransferOnly['Doc.No.'])]
        df6WithTransfer = dfValid.loc[dfValid['Doc.No.'].isin(dfvalidTransferOnly['Doc.No.'])]
        df6WithTransfer = df6WithTransfer.loc[df6WithTransfer['A/C Code'].isin(cashAccount)]
        df6WithTransfer['Trans. Amt.'] = df6WithTransfer['Trans. Amt.'].astype(str)
        df6WithTransfer['Dom. Amt.'] = df6WithTransfer['Dom. Amt.'].astype(str)
        df6WithTransfer['Trans. Amt.'] = df6WithTransfer['Trans. Amt.'].str.replace(',', '').astype(float)
        df6WithTransfer['Dom. Amt.'] = df6WithTransfer['Dom. Amt.'].str.replace(',', '').astype(float)
        df6WithTransfer.loc[:,'A/C Code'] = '33331'
        df6WithTransfer.loc[:,'Status'] = '2_TRANSFER'

        df6 = dfValid.loc[dfValid['A/C Code'].isin(cashAccount)]
        # df6 = dfValid.loc[dfValid['Doc.No.'].isin(dfvalidCashOnly['Doc.No.'])]
        # df6 = df6.loc[df6['A/C Code'].isin(cashAccount)]
        df6['Trans. Amt.'] = df6['Trans. Amt.'].astype(str)
        df6['Dom. Amt.'] = df6['Dom. Amt.'].astype(str)
        df6['Trans. Amt.'] = df6['Trans. Amt.'].str.replace(',', '').astype(float)
        df6['Dom. Amt.'] = df6['Dom. Amt.'].str.replace(',', '').astype(float)
        df6.loc[:,'Status'] = '3_CASH'


        df6WithTransfer.to_csv('df6WithTransfer.csv', index=False)
        df6.to_csv('df6.csv', index=False)

        print(dfValid)
        print('INVOICE CHECKER')
        df7 = dfValid.loc[dfValid['Cont.No.'] != '']  
        print(df7.head(500))
        print(df7['Doc.No.'])
        print(df7['A/C Code'])
        print('INVOICE CHECKER2')
        print(controlAccountListArr)
        df7 = df7.loc[df7['Ent.DT'] != '']

        controlAccountListArr.append('14118')
        df7 = df7.loc[df7['A/C Code'].isin(controlAccountListArr)]
        print(df7)
        df7.to_csv('df7.csv', index=False)
        df7['Trans. Amt.'] = df7['Trans. Amt.'].astype(str)
        df7['Dom. Amt.'] = df7['Dom. Amt.'].astype(str)
        df7['Trans. Amt.'] = df7['Trans. Amt.'].str.replace(',', '').astype(float)
        df7['Dom. Amt.'] = df7['Dom. Amt.'].str.replace(',', '').astype(float)
        df7.loc[:,'Status'] = '4_INVOICE'
        df7 = df7[df7['Clrng doc.'] != 'nan']
        print(df4)
        print(df5)
        
        groupcount = df5.groupby('Doc.No.')
        groupcount = len(groupcount)

        # groupInvoice = df7.groupby('Doc.No.')
        # groupInvoice = df7.groupby(['Doc.No.']).filter(lambda x: any(p in list(set(x["A/C Code"])) for p in ['']))
        

        groupInvoice = df7.groupby(['Doc.No.','Status']).agg(
             {
                'DT'  : 'first', 
                'Ent.DT'  : 'first', 
                'Trn DT'  : 'first', 
                'Due Date'  : 'first',
                'Ref.No.'  : 'first',
                'S-AC'  : 'first',
                'S-AC Name'  : 'first',
                'A/C Code'  : 'first',
                'Unit'  : 'first',
                'Unit Name'  : 'first',
                'REMARKS'  : 'first',
                'Instruction No.'  : 'first',
                'Cont.No.'  : 'first',
                'Clrng doc.'  : 'first',
                'Clrng DT'  : 'first',
                '2nd Sub-Account'  : 'first',
                'Items'  : 'first',
                'Curr'  : 'first',
                'Trans. Amt.'  : 'sum',
                'Dom. Amt.'  : 'sum',
                'SAP Doc Entry'  : 'first',
                'SAP Obj Type' : 'first',
                'rate': 'first'

                }).reset_index()
        
        print(groupInvoice.head(500))
        print(controlAccountListArr)
        print('GROUPED INVOICE')
        df7 = groupInvoice
        print('----------------------')
        # groupedCtrlAcct = df4.groupby(['Doc.No.'], sort=True)['Trans. Amt.'].sum().reset_index()
        bankGroup = df4.groupby(['Doc.No.','Status']).agg(
             {
                'DT'  : 'first', 
                'Ent.DT'  : 'first', 
                'Trn DT'  : 'first', 
                'Due Date'  : 'first',
                'Ref.No.'  : 'first',
                'S-AC'  : 'first',
                'S-AC Name'  : 'first',
                'A/C Code'  : 'first',
                'Unit'  : 'first',
                'Unit Name'  : 'first',
                'REMARKS'  : 'first',
                'Instruction No.'  : 'first',
                'Cont.No.'  : 'first',
                'Clrng doc.'  : 'first',
                'Clrng DT'  : 'first',
                '2nd Sub-Account'  : 'first',
                'Items'  : 'first',
                'Curr'  : 'first',
                'Trans. Amt.'  : 'sum',
                'Dom. Amt.'  : 'sum',
                'SAP Doc Entry'  : 'first',
                'SAP Obj Type' : 'first',
                'rate': 'first'

                }).reset_index()
        

        print(bankGroup)
        print('BANK GROUP UP')
        bankGroup = IncomingPayments.properIndex(bankGroup)

        transferGroup = df5.groupby(['Doc.No.','Status']).agg(
             {
                'DT'  : 'first', 
                'Ent.DT'  : 'first', 
                'Trn DT'  : 'first', 
                'Due Date'  : 'first',
                'Ref.No.'  : 'first',
                'S-AC'  : 'first',
                'S-AC Name'  : 'first',
                'A/C Code'  : 'first',
                'Unit'  : 'first',
                'Unit Name'  : 'first',
                'REMARKS'  : 'first',
                'Instruction No.'  : 'first',
                'Cont.No.'  : 'first',
                'Clrng doc.'  : 'first',
                'Clrng DT'  : 'first',
                '2nd Sub-Account'  : 'first',
                'Items'  : 'first',
                'Curr'  : 'first',
                'Trans. Amt.'  : 'sum',
                'Dom. Amt.'  : 'sum',
                'SAP Doc Entry'  : 'first',
                'SAP Obj Type' : 'first',
                'rate': 'first'

                }).reset_index()
        

        print(transferGroup)
        print('TRANSFER GROUP UP')
        transferGroup = IncomingPayments.properIndex(transferGroup)

        transferGroupFromWithCash = df6WithTransfer.groupby(['Doc.No.','Status']).agg(
             {
                'DT'  : 'first', 
                'Ent.DT'  : 'first', 
                'Trn DT'  : 'first', 
                'Due Date'  : 'first',
                'Ref.No.'  : 'first',
                'S-AC'  : 'first',
                'S-AC Name'  : 'first',
                'A/C Code'  : 'first',
                'Unit'  : 'first',
                'Unit Name'  : 'first',
                'REMARKS'  : 'first',
                'Instruction No.'  : 'first',
                'Cont.No.'  : 'first',
                'Clrng doc.'  : 'first',
                'Clrng DT'  : 'first',
                '2nd Sub-Account'  : 'first',
                'Items'  : 'first',
                'Curr'  : 'first',
                'Trans. Amt.'  : 'sum',
                'Dom. Amt.'  : 'sum',
                'SAP Doc Entry'  : 'first',
                'SAP Obj Type' : 'first',
                'rate': 'first'

                }).reset_index()
        

        print(transferGroupFromWithCash)
        print('TRANSFER GROUP UP FROM CASH WITH TRANSFER ISSUE')
        transferGroupFromWithCash = IncomingPayments.properIndex(transferGroupFromWithCash)


        cashGroup = df6.groupby(['Doc.No.','Status']).agg(
             {
                'DT'  : 'first', 
                'Ent.DT'  : 'first', 
                'Trn DT'  : 'first', 
                'Due Date'  : 'first',
                'Ref.No.'  : 'first',
                'S-AC'  : 'first',
                'S-AC Name'  : 'first',
                'A/C Code'  : 'first',
                'Unit'  : 'first',
                'Unit Name'  : 'first',
                'REMARKS'  : 'first',
                'Instruction No.'  : 'first',
                'Cont.No.'  : 'first',
                'Clrng doc.'  : 'first',
                'Clrng DT'  : 'first',
                '2nd Sub-Account'  : 'first',
                'Items'  : 'first',
                'Curr'  : 'first',
                'Trans. Amt.'  : 'sum',
                'Dom. Amt.'  : 'sum',
                'SAP Doc Entry'  : 'first',
                'SAP Obj Type' : 'first',
                'rate': 'first'

                }).reset_index()
        

        print(cashGroup)
        print('CASH GROUP UP')
        cashGroup = IncomingPayments.properIndex(cashGroup)


        print(df7)
        print('INVOICE UP')

        finalDataFrame = pd.concat([bankGroup, transferGroup, transferGroupFromWithCash, cashGroup, df7], axis=0) 

        finalDataFrame = finalDataFrame.drop('Items', axis=1)

        finalDataFrame = finalDataFrame.sort_values(by=['Doc.No.','Status'])


        finalDataFrame['Items'] = finalDataFrame.groupby(['Doc.No.']).cumcount()+1; finalDataFrame


        finalDataFrame = IncomingPayments.properIndex(finalDataFrame)

        finalDataFrame.to_csv('finalDataFrame.csv', index=False)

        print(finalDataFrame)
        print('FINAL DATAFRAME UP')

        # print(df3['Items'])
        totalBPNotExist = 0
        totalItemNotExist = 0
        totalGrpoExist = 0
        totalDocsExist = 0

        df3 = finalDataFrame.reset_index()
        df3.drop(columns=df3.columns[0], axis=1,  inplace=True)
        array2 = []
        print(ovpmcode_list)
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            bankrow = 0
            bankrowcharge = 0

            # OUTGOING PAYMENTS VALIDATION
            # OUTGOING PAYMENTS CODE
            # print(ovpmcode_list)
            try:
                
                if(str(df3['Doc.No.'][ind]).replace(".0", "") in ovpmcode_list):
             
                    if(df3['A/C Code'][ind] in controlAccountListArr):
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - AlreadyPosted'
                        failedrow += 1
                        totalDocsExist += 1   


                    # if(str(df3['A/C Code'][ind]) == '41210'):
                        
                    
                
                elif(df3['Doc.No.'][ind] == ''):
                        
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - RequiredField'
                    
                    
                        
                else:
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                
                          
            except ValueError:
                    # df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + ' - InvalidContNo'
                    # failedrow += 1
                    # totalDocsExist += 1
                    print('failed')


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
            # AP/CM VALIDATION
            try:

                df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]).replace(".0", "")
                if(str(df3['Doc.No.'][ind]).replace(".0", "") in apv_or_apcm_clearingdoc_list):
                    docIndex = apv_or_apcm_clearingdoc_list.index(str(df3['Doc.No.'][ind]).replace(".0", ""))
                    # print(apv_or_apcm_docentry_list)
                    # print(apv_or_apcm_clearingdoc_list)
                    # print(docIndex)
                    print('DOCENTRY HIT')

                    python_indices  = [index for (index, item) in enumerate(apv_or_apcm_clearingdoc_list) if item == str(df3['Doc.No.'][ind]).replace(".0", "")]

                    # print(python_indices)

                    a = pd.Series(apv_or_apcm_docentry_list)
                    b = python_indices
                    c = a[b].astype(str)

                    print(c.tolist())
                    print(type(c.tolist()))
                    #[1, 3, 5]
                    string_list = [str(element) for element in c.tolist()]
                    delimiter = ", "
                    result_string = delimiter.join(string_list)
                    print(result_string)

                    docentry = apv_or_apcm_docentry_list[docIndex]
                    objtype = apv_or_apcm_objtype_list[docIndex]
                    df3.at[ind,'SAP Doc Entry']=result_string
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
                     

            # AP/CM VALIDATION

            # 1_CHECK
            # 2_TRANSFER
            # 3_CASH
            # 4_INVOICE
            # RATE VALIDATION
                # RATE
            if(df3['rate'][ind] == '' ):
                df3.at[ind,'rate']= int(1)
                # failedrow += 1
                # totalItemNotExist += 1

            else:
                df3.at[ind,'rate']=float(df3['rate'][ind])


            if(str(df3['Status'][ind]) == '1_CHECK'):
                df3.at[ind,'Status'] = "CHECK"

            elif(str(df3['Status'][ind]) == '2_TRANSFER'):
                df3.at[ind,'Status'] = "TRANSFER"

            elif(str(df3['Status'][ind]) == '3_CASH'):
                df3.at[ind,'Status'] = "CASH"

            elif(str(df3['Status'][ind]) == '4_INVOICE' and str(df3['Clrng doc.'][ind]) != 'nan'):
                df3.at[ind,'Status'] = "SUCCESS"

            elif(str(df3['Status'][ind]) == '4_INVOICE' and str(df3['Clrng doc.'][ind]) == 'nan'):
                df3.at[ind,'Status'] = "OTHER DETAILS"


            
            if(failedrow > 0):
                df3.at[ind,'Status'] = "FAILED"




            self.label_ovpm_total_bp_not_exist_2.setText("BP Does Not Exist: " + str(totalBPNotExist))
            self.label_ovpm_total_item_not_exist_2.setText("Item Does Not Exist: " + str(totalItemNotExist))
            self.label_ovpm_total_exist_2.setText("Doc. Already Exist: " + str(totalDocsExist))
        


        
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 

        # df3 = df3.loc[df3['Status'] != "FAILED"] 
        return df3
    

    def loadCsv(self, file_name):
        df3 = IncomingPayments.processDataFrame(self, file_name)
        totalready = 0
        # df3 = df3.loc[df3['Status'] == "SUCCESS"] 
        rowcount = len(df3)
        self.tableWidget_ovpm_2.setColumnCount(25)
        self.tableWidget_ovpm_2.setRowCount(rowcount)
        for i in range(rowcount):

            if(str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1


            for j in range(25):
                # print(df3._get_value(i, j, takeable=True) )
                self.tableWidget_ovpm_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                self.tableWidget_ovpm_2.setCurrentCell(32,1)    

                if(str(df3._get_value(i, 17, takeable=True)) != ''):
                    self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                else:
                    self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(240, 255, 255))

                if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                    self.tableWidget_ovpm_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_ovpm_2.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    # print(str(df3._get_value(i, j, takeable=True)))
                    try:
                        if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(255, 165, 0))


                        if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(255,255,0))
                            

                        if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(150,75,0))

                    except:
                        self.tableWidget_ovpm_2.item(i,0).setBackground(QtGui.QColor(255, 128, 128))

                elif(str(df3._get_value(i, 0, takeable=True)) in ["CHECK","TRANSFER","CASH"]):
                    self.tableWidget_ovpm_2.item(i,j).setBackground(QtGui.QColor(211,211,211))
                else:
                    # self.tableWidget_ovpm_2.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                    self.tableWidget_ovpm_2.item(i,0).setBackground(QtGui.QColor(144, 238, 144))



        self.label_ovpm_total_ready_2.setText("INCOMING PAYMENTS READY TO POST: " + str(totalready))


    def postIncomingPayments(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()

        df3 = IncomingPayments.processDataFrame(self,file_name)
        # print(df3)
        # print(type(df3))
        print(df3)
        print('********************************DF FOR POSTING HERE*******************************************************************')
        df4 = df3.loc[df3['Status'] == "SUCCESS"]
        df5 = df3.loc[df3['Status'] == "TRANSFER"]
        df6 = df3.loc[df3['Status'] == "CHECK"]
        df7 = df3.loc[df3['Status'] == "CASH"]
        headers = df4.loc[df4['SAP Doc Entry'] != '']

       

        df3.to_csv('orct.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")

        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPOST /b1s/v1/IncomingPayments\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header

        for ind in df4.index:

            # print(headers.at[ind,'Cont.No.'])
            dfbanklines = df5.loc[df5['Doc.No.'] == df4.at[ind,'Doc.No.']] 
            dfchecklines = df6.loc[df6['Doc.No.'] == df4.at[ind,'Doc.No.']] 
            dfcashlines = df7.loc[df7['Doc.No.'] == df4.at[ind,'Doc.No.']] 
            print(dfbanklines)

            print("Bank Acct:"+ str(dfbanklines.get("A/C Code")))
            print("Cash Acct:"+ str(dfcashlines.get("A/C Code")))
            print("Check Acct:"+ str(dfchecklines.get("A/C Code")))
            print(type(dfchecklines["A/C Code"]))
            # dfchecklines["A/C Code"].values[0] if dfchecklines["A/C Code"].values[0] is None else dfchecklines["A/C Code"].values[1]
            print('-------------------------------------------------')
            try:
                print("Bank Acct:"+ str(dfbanklines["A/C Code"].values[0]))
            except:
                print('Bank Transfer not available')


            print('-------------------------------------------------')
            try:
                print("Cash Acct:"+ str(dfcashlines["A/C Code"].values[0]))
            except:
                print('Cash not available')

            print('-------------------------------------------------')


            try:
                print("Check Acct:"+ str(dfchecklines["A/C Code"].values[0]))
            except:
                    print('Check not available')

            print('-------------------------------------------------')
            
            print('----------------Bank---------------------------------')
            try:
                if(str(dfbanklines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                    print("Invoice Acct:"+  df4['S-AC'][ind])
                    print("Invoice Entry:"+  df4['SAP Doc Entry'][ind])
                    print('----------------Bank WITH INVOICE---------------------------------')
            
            except:
                    print('Bank Transfer not available')

            try:
                if(str(dfcashlines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                    print("Invoice Acct:"+  df4['S-AC'][ind])
                    print("Invoice Entry:"+  df4['SAP Doc Entry'][ind])
                    print('----------------Cash WITH INVOICE---------------------------------')
            
            except:
                    print('Cash not available')

            
            try:
                if(str(dfchecklines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                    print("Invoice Acct:"+  df4['S-AC'][ind])
                    print("Invoice Entry:"+  df4['SAP Doc Entry'][ind])
                    print('----------------Check WITH INVOICE---------------------------------')
            
            except:
                    print('Check not available')
            # print(dfbanklines)
            # print("Bank Acct:"+ str(dflines['S-AC'][ind]))
            # print("CheckNumber:"+ str(dflines.loc[dflines['Cont.No.']]))
            # print("CheckSum:"+ float(str(dflines.loc[dflines['Dom. Amt.']]).replace(",", "").replace(".00", "").replace("-", "")))
           
            print('----------------haha---------------------------------')

            paymentCheckLines = []
            banktransferLines = []
            paymentlines = []
            invoiceslines = []


            chk = 0
            bnktrnfr = 0
            cash = 0

            # print(dfchecklines["A/C Code"].values[0])
            # print(dfchecklines["Cont.No."].values[0])
            # print(dfchecklines["Trans. Amt."].values[0])
            # print(str(dfchecklines["Ent.DT"].values[0]))
            # print(str(dfchecklines["Curr"].values[0]))
            try:
                if(str(dfchecklines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                    if(str(dfchecklines["Cont.No."].values[0]) != ''):
                        chk += 1
                        linesdict =	{
                            "DueDate": str(dfchecklines["Ent.DT"].values[0]),
                            # "CheckNumber": str(dfchecklines.get('Cont.No.')[0]),
                            # "BankCode": str(dfchecklines.get('S-AC')[0]).replace("-C",""),
                            "BankCode": "BNZ",

                            "CheckAccount": dfchecklines["A/C Code"].values[0],
                            "CheckSum": float(str(dfchecklines["Trans. Amt."].values[0]).replace(",", "").replace(".00", "").replace("-", "")),
                            # "CheckAccount": "161020",
                            "ManualCheck": "tNO",
                            "Currency": str(dfchecklines["Curr"].values[0])
                        }     
                        paymentCheckLines.append(linesdict)
                        
                    
            except:
                    print('Check not available')    

            try:
                if(str(dfbanklines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                    if(str(dfbanklines["Cont.No."].values[0]) != ''):
                        banktransferLines.append(str(dfbanklines['A/C Code'].values[0]))
                        banktransferLines.append(float(str(dfbanklines['Trans. Amt.'].values[0]).replace(",", "").replace(".00", "").replace("-", "")))
                        banktransferLines.append(str(dfbanklines['Ent.DT'].values[0]))
                        banktransferLines.append(str(dfbanklines['Ref.No.'].values[0]))
                        banktransferLines.append(float(str(dfbanklines['Trans. Amt.'].values[0]).replace(",", "").replace(".00", "").replace("-", "")))
                        bnktrnfr += 1

            except:
                    print('Bank not available')


            print('-----------------------------------------')
            print(str(dfcashlines["Doc.No."]))
            # print(str(dfcashlines["Doc.No."].values[0]))
            print(str(df4['Doc.No.'][ind]))
            try:
                
                if(str(dfcashlines["Doc.No."].values[0]) == str(df4['Doc.No.'][ind])):
                        paymentlines.append(str(dfcashlines['A/C Code'].values[0]))
                        paymentlines.append(float(str(dfcashlines['Trans. Amt.'].values[0]).replace(",", "").replace(".00", "").replace("-", "")))
                        paymentlines.append(str(dfcashlines['Ent.DT'].values[0]))
                        paymentlines.append(str(dfcashlines['Ref.No.'].values[0]))
                        paymentlines.append(float(str(dfcashlines['Trans. Amt.'].values[0]).replace(",", "").replace(".00", "").replace("-", "")))
                        cash += 1

            except:
                    print('Cash not available')


            print(paymentCheckLines)
            print(banktransferLines)
            print(paymentlines)

            

            if(df4['DT'][ind] == 'QE' and df4['Status'][ind] == 'SUCCESS'):
                linesdict2 = {         
                    "DocEntry": df4['SAP Doc Entry'][ind],
                    "InvoiceType": "it_Invoice",
                    "DocRate" : str(df4['rate'][ind])
                }
                invoiceslines.append(linesdict2)
            elif(df4['DT'][ind] == 'QO' and df4['Status'][ind] == 'SUCCESS'):
                print(type(df4['SAP Doc Entry'][ind]))
                print(df4['SAP Doc Entry'][ind])

                print('ORIG VALUE UP')


                linesdict2 = []
                myString = df4['SAP Doc Entry'][ind]
                myList = myString.split(', ')


                print(myList)
                print('ARRAYED UP')
                nparray = np.array(myList)
                unique = np.unique(nparray)

                print(unique)
                print('UNIQUE UP')
                for x in unique:
                    print(x)

                    linesdict2Inner = {         
                        "DocEntry": x,
                        "InvoiceType": "it_Invoice",
                        "DocRate" : str(df4['rate'][ind])
                    }  
                    linesdict2.append(linesdict2Inner)
                
                
                
                invoiceslines.append(linesdict2)


            documentArray = []
            print(paymentlines)

            TransferAccount = None
            TransferSum = 0.0
            TransferDate = None
            TransferReference = None
            BankChargeAmount = 0.0
            


            CashAccount = None  
            CashSum = 0.0
            
            CheckAccount = None
            paymentCheckLinesVar = []
            print(paymentCheckLines)

            print(bnktrnfr)
            print('Payment Lines Error ------------------------')
            print(paymentlines)
            if(bnktrnfr > 0):
                TransferAccount = paymentlines[0]
                TransferSum = paymentlines[1]
                TransferDate = paymentlines[2]
                TransferReference = paymentlines[3]
                BankChargeAmount = paymentlines[4]
            
            
            if(cash > 0):
                CashAccount = paymentlines[0]
                CashSum = paymentlines[1]


            if(chk > 0):
                CheckAccount = dfchecklines["A/C Code"].values[0]
                paymentCheckLinesVar = paymentCheckLines




            headerdict =	{
                "CardCode": str(df4['S-AC'][ind]),
                "DocDate": str(df4['Ent.DT'][ind]),
                "TaxDate": str(df4['Trn DT'][ind]),
                "DueDate": str(df4['Due Date'][ind]),
                "DocType": "rCustomer",
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
                "DocRate" : str(df4['rate'][ind]),
                "DocCurrency": str(df4['Curr'][ind]),
                
            
                
                "TransferAccount": TransferAccount,
                "TransferSum": TransferSum,
                "TransferDate": TransferDate,
                "TransferReference": TransferReference,
                
                "CashAccount": CashAccount,
                "CashSum": CashSum,

                "Reference1": None,
                "Reference2": None,
                "CounterReference": None,
                "Remarks": None,
                "JournalRemarks": "Incoming Payments - PW049-C",

                "CheckAccount": str(CheckAccount),
                "PaymentChecks": paymentCheckLinesVar,
                "PaymentInvoices":invoiceslines[0]
            }


            # except:
            #      print('new trick didnt go')
   
            documentArray.append(headerdict)

            # try:
            #     if(str(dfbanklines.get("Doc.No.")[0]) == str(df4['Doc.No.'][ind])):
            #         if(dfbanklines.get("Status")[0] == 'CHECK'):
            #             if(str(dfbanklines.get('Cont.No.')[0]) == ''):
            #                 headerdict =	{
            #                     "CardCode": str(df4['S-AC'][ind]),
            #                     "DocDate": str(df4['Ent.DT'][ind]),
            #                     "TaxDate": str(df4['Trn DT'][ind]),
            #                     "DueDate": str(df4['Due Date'][ind]),
            #                     "DocType": "rCustomer",
            #                     "CounterReference": str(df4['Ref.No.'][ind]),
            #                     "Remarks": str(df4['REMARKS'][ind]),
            #                     "U_Unit": str(df4['Unit'][ind]),
            #                     "U_UnitName": str(df4['Unit Name'][ind]),
            #                     "U_DocNo": str(df4['Doc.No.'][ind]),
            #                     "U_InsNo": str(df4['Instruction No.'][ind]),
            #                     "U_ContNo": str(df4['Cont.No.'][ind]),
            #                     "U_ClrngDoc": str(df4['Clrng doc.'][ind]),
            #                     "U_ClrngDT": str(df4['Clrng DT'][ind]),
            #                     "U_SubAccount": str(df4['2nd Sub-Account'][ind]),

            #                     "CashAccount": None,
            #                     "DocCurrency": "PHP",
            #                     "CashSum": 0.0,
            #                     "CheckAccount": "10120",
                                
            #                     "Reference1": None,
            #                     "Reference2": None,
            #                     "CounterReference": None,
            #                     "Remarks": None,
            #                     "JournalRemarks": "Incoming Payments - PW049-C",
                                
            #                     "TransferAccount": paymentlines[0],
            #                     "TransferSum": paymentlines[1],
            #                     "TransferDate": paymentlines[2],
            #                     "TransferReference": paymentlines[3],
            #                     "BankChargeAmount": paymentlines[4],
            #                     "PaymentInvoices": invoiceslines
            #                 }

            #             print('Bank Transfer available with Invoice')
                
            # except:
            #     print('Bank Transfer not available with Invoice')  


            # try:
            #     if(str(dfcashlines.get("Doc.No.")[1]) == str(df4['Doc.No.'][ind])):
            #         if(dfcashlines.get("Status")[1] == 'CASH'):
            #             headerdict =	{
            #                 "CardCode": str(df4['S-AC'][ind]),
            #                 "DocDate": str(df4['Ent.DT'][ind]),
            #                 "TaxDate": str(df4['Trn DT'][ind]),
            #                 "DueDate": str(df4['Due Date'][ind]),
            #                 "DocType": "rCustomer",
            #                 "CounterReference": str(df4['Ref.No.'][ind]),
            #                 "Remarks": str(df4['REMARKS'][ind]),
            #                 "U_Unit": str(df4['Unit'][ind]),
            #                 "U_UnitName": str(df4['Unit Name'][ind]),
            #                 "U_DocNo": str(df4['Doc.No.'][ind]),
            #                 "U_InsNo": str(df4['Instruction No.'][ind]),
            #                 "U_ContNo": str(df4['Cont.No.'][ind]),
            #                 "U_ClrngDoc": str(df4['Clrng doc.'][ind]),
            #                 "U_ClrngDT": str(df4['Clrng DT'][ind]),
            #                 "U_SubAccount": str(df4['2nd Sub-Account'][ind]),


            #                 "CashAccount": None,
            #                 "DocCurrency": "PHP",
            #                 "CashSum": 0.0,
            #                 "CheckAccount": "10120",
            #                 "TransferAccount": None,
            #                 "TransferSum": 0.0,
            #                 "TransferDate": None,
            #                 "TransferReference": None,
            #                 "Reference1": None,
            #                 "Reference2": None,
            #                 "CounterReference": None,
            #                 "Remarks": None,
            #                 "JournalRemarks": "Incoming Payments - PW049-C",


            #                 "CashAccount": paymentlines[0],
            #                 "CashSum": paymentlines[1],
            #                 "PaymentInvoices": invoiceslines
            #             }


            #         print('Cash available with Invoice')
                
            # except:
            #     print('Cash not available with Invoice')  
            

            # try:
            #     if(str(dfchecklines.get("Doc.No.")[0]) == str(df4['Doc.No.'][ind])):
            #         if(dfchecklines.get("Status")[0] == 'CHECK'):
            #             if(str(dfchecklines.get('Cont.No.')[0]) != ''):  
            #                 headerdict =	{
            #                    "CardCode": str(df4['S-AC'][ind]),
            #                     "DocDate": str(df4['Ent.DT'][ind]),
            #                     "TaxDate": str(df4['Trn DT'][ind]),
            #                     "DueDate": str(df4['Due Date'][ind]),
            #                     "DocType": "rCustomer",
            #                     "CounterReference": str(df4['Ref.No.'][ind]),
            #                     "Remarks": str(df4['REMARKS'][ind]),
            #                     "U_Unit": str(df4['Unit'][ind]),
            #                     "U_UnitName": str(df4['Unit Name'][ind]),
            #                     "U_DocNo": str(df4['Doc.No.'][ind]),
            #                     "U_InsNo": str(df4['Instruction No.'][ind]),
            #                     "U_ContNo": str(df4['Cont.No.'][ind]),
            #                     "U_ClrngDoc": str(df4['Clrng doc.'][ind]),
            #                     "U_ClrngDT": str(df4['Clrng DT'][ind]),
            #                     "U_SubAccount": str(df4['2nd Sub-Account'][ind]),

                            
            #                     "DocCurrency": "PHP",
                            
            #                     "CheckAccount": "10120",
            #                     "TransferAccount": None,
            #                     "TransferSum": 0.0,
            #                     "TransferDate": None,
            #                     "TransferReference": None,
            #                     "Reference1": None,
            #                     "Reference2": None,
            #                     "CounterReference": None,
            #                     "Remarks": None,
            #                     "JournalRemarks": "Incoming Payments - PW049-C",
            #                     "PaymentChecks": paymentCheckLines,
            #                     "PaymentInvoices":invoiceslines
            #                 }

            #         print('Check available with Invoice')
                
            # except:
            #     print('Check not available with Invoice')

                

            print(bnktrnfr)
            print(chk)
            print(cash)     
                        
                        
            documentArray.append(headerdict)
            print('--------------FOR POSTING----------------')
            print(documentArray)

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
        with open('orct.txt', 'w') as f:
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


        IncomingPayments.loadCsv(self,file_name)

