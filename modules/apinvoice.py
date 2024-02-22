import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem, QComboBox
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
import modules.apcreditmemo as APCreditMemo
import modules.grpo as Grpo

mock_wtcode = ['wtcode1', 'wtcode2', 'wtcode3', 'wtcode4',]
mock_wtcode_cardcode = ['PG089-V', 'PM212-V', 'PF107-V','PG089-V']
mock_wtcode_rate = [12.00,2.00,5.00,16.00]
class APInvoice():
    

    def addcombWtLiable(self,row,col,cardcode,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader):
        # combo = QComboBox(self)
        self.tableWidget_apinvoice.setItem(row,self,QTableWidgetItem(str('Yes')))
        # if(cardcode in wtcode_cardcode_list):
        #     combo.addItem("Yes")
        #     combo.addItem("No")
        #     APInvoice.wtliable_change_default(self, row, col, cardcode, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader, 'Yes')
        # else:
        #     combo.addItem("No")
        #     combo.addItem("Yes")
        #     APInvoice.wtliable_change_default(self, row, col, cardcode, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader, 'No')


        # combo.currentIndexChanged.connect(lambda: APInvoice.wtliable_change(self,row,col,cardcode,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader))
        # self.tableWidget_apinvoice.setCellWidget(row, col, combo)

    
    def addcombWtCode(self,row,col,cardcode,value,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader):
        combo = QComboBox(self)
        all_indexes = [a for a in range(len(wtcode_cardcode_list)) if wtcode_cardcode_list[a] == cardcode]
        if(isheader == '2'):
            if(value == "Yes"):
                combo.clear()
                for x in all_indexes:
                    combo.addItem(wtcode_list[x])
            else:
                combo.clear()
                combo.addItem("-")

        self.tableWidget_apinvoice.setCellWidget(row, 27, combo)


    def addcombWtCode2(self,row,col,cardcode,value,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader):
        combo = QComboBox(self)
        all_indexes = [a for a in range(len(wtcode_cardcode_list)) if wtcode_cardcode_list[a] == cardcode]
        if(isheader == '2'):
            if(value == "Yes"):
                combo.clear()
                for x in all_indexes:
                    combo.addItem(wtcode_list[x])
            else:
                combo.clear()
                combo.addItem("-")

        self.tableWidget_apinvoice.setCellWidget(row, 28, combo)




    def wtliable_change(self, row, col, cardcode, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader):
        value = self.tableWidget_apinvoice.cellWidget(row,col).currentText()
        
        APInvoice.addcombWtCode(self, row, col, cardcode, value, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader)
        APInvoice.addcombWtCode2(self, row, col, cardcode, value ,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader)


    def wtliable_change_default(self, row, col, cardcode, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader, value):
        
        APInvoice.addcombWtCode(self, row, col, cardcode, value, wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader)
        APInvoice.addcombWtCode2(self, row, col, cardcode, value ,wtcode_list,wtcode_cardcode_list,wtcode_rate_list,wtcode_liable_list,isheader)

    def processDataFrame(self, file_name):

        bpCodeListArr = Utilities.Utilities.bpQueryValidator()
        bpcode_list = bpCodeListArr[0]
        bpname_list = bpCodeListArr[1]


        itemCodeListArr = Utilities.Utilities.itemQueryValidator()
        itemcode_list = itemCodeListArr[0]
        itemcode_uomcode_list = itemCodeListArr[1]


        grpoCodeListArr = Utilities.Utilities.grpoQueryValidator()
        grpocode_list = grpoCodeListArr[0]
        grpocode_linenum_list = grpoCodeListArr[1]
        grpocode_linenum_docentry_list = grpoCodeListArr[2]
        grpo_list_quantity = grpoCodeListArr[3]
        grpo_list_contno = grpoCodeListArr[4]


        apinvoiceCodeListArr = Utilities.Utilities.apinvoiceQueryValidator()
        apinvoicecode_list = apinvoiceCodeListArr[0]
        apinvoicecode_linenum_list = apinvoiceCodeListArr[1]


       

        # print(apinvoicecode_list)

        print("File selected: " + self.lineEdit_filename.text())
        df = pd.read_csv(self.lineEdit_filename.text(), encoding = 'iso-8859-1')
        df = df.loc[df['DT'] == 'RE']
        df['Trans. Amt.'] = df['Trans. Amt.'].str.replace('-', '')
        df['Dom. Amt.'] = df['Dom. Amt.'].str.replace('-', '')
        # df = df.loc[df['A/C Code'].isin(['41210']) == False]
        df = df.fillna('')
        rowcount = len(df)
        df2 = df.drop(columns=df.columns[[0, 1, 2, 3, 4, 7, 9, 10, 11, 14, 23, 24, 27, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 47, 48, 50, 51, 52]],  axis=1)
        
        df2.insert(0,'Status', '' )
        df2.insert(25,'WT Liable', 'No' )


        # print(len(df2. columns)) 
        df2.insert(26,'WT Code 1', '' )
        df2.insert(27,'WT Code 2', '' )
        df2.insert(28,'WT Amount', '0.00' )
        df2.insert(29,'GRPO Doc. Entry', '' )

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
            'WT Liable',
            'Quantity',
            'Quantity Unit',
            'WT Code 1',
            'WT Code 2',
            'WT Amount',
            'GRPO Doc. Entry'

            ]]
        
        print(type(df3))
        # print(len(df2.axes[1]))
        # df3.to_csv('file_name1.csv', index=False)

        totalBPNotExist = 0
        totalItemNotExist = 0
        totalGrpoExist = 0
        totalAmountNotValid = 0

        # df3.groupby('Cont.No.')
        # df3 = df3.sort_values(['Items'],ascending=True).groupby('Cont.No.')

        
        # df3[['Clrng doc.']]=df3[['Clrng doc.']].replace('',float('NaN'))
        # df3[['Clrng doc.']]=df3.groupby('Doc.No.')[['Clrng doc.']].apply(lambda x:x.ffill().bfill()).fillna('')

        print(df3)
        df3 = df3.sort_values(['Doc.No.','Cont.No.','Items'], ascending=True)
        # df3.groupby('Cont.No.')
        print(df3['Items'])
        d4 = df3['S-AC'].unique()


        d5 = d4.tolist()


        wtCodeListArr = Utilities.Utilities.wtQueryValidator(d5)
        
        wtcode_list = wtCodeListArr[0]
        wtcode_cardcode_list = wtCodeListArr[1]
        wtcode_rate_list = wtCodeListArr[2]
        wtcode_liable_list = wtCodeListArr[3]
        
        df3['A/C Code'] = df3['A/C Code'].astype(str)

        df4 = df3.loc[df3['A/C Code']  == "41210"]
            
        print(df4)
        print('HAHA')
        row_ = None
        array2 = []
        for ind in df3.index:
            ###########################################################################################
            failedrow = 0
            ctrlacctrow = 0


            dfclearing = df4.loc[df4['Doc.No.'] == df3.at[ind,'Doc.No.']] 


            print(type(dfclearing['Clrng doc.']))
            print(dfclearing['Clrng doc.'].values[0])
            # CLEAR DOC BY DOC NO
            if(df3['Clrng doc.'][ind] == ''):
                if(ind != 0):
                    print(df3['Clrng doc.'][ind])
                    df3.at[ind,'Clrng doc.']=str(dfclearing['Clrng doc.'].values[0]).replace(".0", "")
                    print('Prev is here')
                    print('-------------------------------')
            else:
                print(df3['Clrng doc.'][ind])
                df3.at[ind,'Clrng doc.']=str(df3['Clrng doc.'][ind]).replace(".0", "")
                print('Curr is here')
                print('-------------------------------')
                


            ###########################################################################################


            # AP Invoice VALIDATION
            # AP Invoice CODE
            try:
                if(str(df3['A/C Code'][ind]) != "41210"):
                    if(str(df3['Doc.No.'][ind]) in apinvoicecode_list):
                        
                        array1 = []
                        array1.append(df3['Doc.No.'][ind])
                        array1.append(df3['Items'][ind])
                        
                        array2.append(array1)
                        # apinvoicecode_linenum_list.index(array1)
                        
                        # if(apinvoicecode_linenum_list is not None):
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - AlreadyPosted'
                        failedrow += 1
                        totalGrpoExist += 1
                        # else:
                        #     df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                        #     failedrow += 1
                        #     totalGrpoExist += 1

                    else:
                        df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind])
                else:
                    df3.at[ind,'Doc.No.']=str(df3['Doc.No.'][ind]) + ' - ControlAccount'
                    ctrlacctrow += 1

                          
            except Exception as e:
                    print(e)
                    df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + str(e)
                    # failedrow += 1
                    # totalGrpoExist += 1


            ###########################################################################################


            # AP Invoice with GRPO
            # AP Invoice
            try:
                # print(grpo_list_contno)
                if(str(df3['Cont.No.'][ind]) in grpo_list_contno):
                    
                    array1 = []
                    array1.append(str(df3['Cont.No.'][ind]))
                    array1.append(df3['Items'][ind])
                    
                    array2.append(array1)
                    grpocode_linenum_list.index(array1)
                    grpodocentry = grpo_list_contno.index(str(df3['Cont.No.'][ind]))


                    print('Cont.No.: ' + str(df3['Cont.No.'][ind]) + ' GRPO No: ' + str(grpocode_linenum_docentry_list[grpodocentry]) + ' Line No: ' +  str(df3['Items'][ind]) + ' Quantity: ' + str(grpo_list_quantity[grpodocentry]))
                    
                    # print('base entry is: ' + str(grpocode_linenum_docentry_list[grpodocentry]) + " cont.no of: " + str(df3['Cont.No.'][ind]) + " linenum of: " + str(df3['Items'][ind]))
                    if(grpocode_linenum_list is not None):
                        df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind])
                        df3.at[ind,'GRPO Doc. Entry']=str(grpocode_linenum_docentry_list[grpodocentry])
                        # df3.at[ind,'Quantity']=str(grpo_list_quantity[grpodocentry])
                        # failedrow += 1
                        # totalGrpoExist += 1
                    else:
                        df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind])
                       

                else:
                    df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind])
                    if(df3['Quantity'][ind] == 0 ):
                        df3.at[ind,'Quantity']=int(1)
                        # failedrow += 1
                        # totalItemNotExist += 1

                    else:
                        df3.at[ind,'Quantity']=str(df3['Quantity'][ind])
                          
            except Exception as e:
                    print(e)
                    df3.at[ind,'Cont.No.']=str(df3['Cont.No.'][ind]) + str(e)
                    # failedrow += 1
                    # totalGrpoExist += 1


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


            

            # ITEM VALIDATION
            # ITEM CODE
            # print(df3['Material Code'][ind])
            try:
                if(df3['Material Code'][ind] not in itemcode_list):
                    df3.at[ind,'Material Code']=str(df3['Material Code'][ind]) + ' - InvalidItem'
                    failedrow += 1
                    totalItemNotExist += 1

                else:
                    df3.at[ind,'Material Code']=str(df3['Material Code'][ind])
                    item_index = itemcode_list.index(df3['Material Code'][ind])
                    item_uom = itemcode_uomcode_list[item_index][1]
                    df3.at[ind,'Quantity Unit']=str(item_uom)
                          
            except ValueError:
                    df3.at[ind,'Material Code']=str(df3['Material Code'][ind]) + ' - InvalidItem'
                    failedrow += 1
                    totalItemNotExist += 1

            ###########################################################################################


            # AMOUNT VALIDATION
            # AMOUNT
            try:
                if(str(df3['Trans. Amt.'][ind]).replace(",", "").replace(".","").isnumeric() == False):
                    df3.at[ind,'Trans. Amt.']=str(df3['Trans. Amt.'][ind]) + ' - InvalidAmount'
                    failedrow += 1
                    totalAmountNotValid += 1

                else:
                    df3.at[ind,'Trans. Amt.']=str(df3['Trans. Amt.'][ind])
                          
            except ValueError:
                    df3.at[ind,'Trans. Amt.']=str(df3['Trans. Amt.'][ind]) + ' - InvalidAmount'
                    failedrow += 1
                    totalAmountNotValid += 1

            
            try:
                if(str(df3['Dom. Amt.'][ind]).replace(",", "").replace(".","").isnumeric() == False):
                    df3.at[ind,'Dom. Amt.']=str(df3['Dom. Amt.'][ind]) + ' - InvalidAmount'
                    failedrow += 1
                    totalAmountNotValid += 1

                else:
                    df3.at[ind,'Dom. Amt.']=str(df3['Dom. Amt.'][ind])
                          
            except ValueError:
                    df3.at[ind,'Dom. Amt.']=str(df3['Dom. Amt.'][ind]) + ' - InvalidAmount'
                    failedrow += 1
                    totalAmountNotValid += 1


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
                if(str(df3.at[ind,'Tx']) == "5"):
                    df3.at[ind,'Tx']='IVAT-E'

                if(df3.at[ind,'Tx'] == 'I2'):
                    df3.at[ind,'Tx']='IVAT-N'

                if(df3.at[ind,'Tx'] == 'IZ'):
                    df3.at[ind,'Tx']='IVAT-Z'

            except ValueError:
                    df3.at[ind,'Tx']=str(math.floor(df3['Tx'][ind])) + ' - InvalidVatGroup'
                    failedrow += 1


            ##########################################################################################


            # WTTAX VALIDATION
            # WTAX CODE
            # try:
            #      all_indexes = [a for a in range(len(wtcode_cardcode_list)) if wtcode_cardcode_list[a] == df3['S-AC'][ind] + "-V"]
            #         if(isheader == '2'):
            #             if(value == "Yes"):
            #                 combo.clear()
            #                 for x in all_indexes:
            #                     combo.addItem(wtcode_list[x])
            #             else:
            #                 combo.clear()
            #                 combo.addItem("-")

                
            # except ValueError:
            #         df3.at[ind,'WT Liable']=str("Yes") + ' - InvalidBPForWTAX'
            #         failedrow += 1
            #         totalBPNotExist += 1



            ##########################################################################################

            if(failedrow > 0):
                df3.at[ind,'Status'] = "FAILED"

            else:
                df3.at[ind,'Status'] = "SUCCESS"


            if(ctrlacctrow > 0):
                df3.at[ind,'Status'] = "CTRL ACCT"   
            # print(failedrow)


            self.label_apinvoice_total_bp_not_exist.setText("BP Does Not Exist: " + str(totalBPNotExist))
            self.label_apinvoice_total_item_not_exist.setText("Item Does Not Exist: " + str(totalItemNotExist))
            self.label_apinvoice_total_exist.setText("Doc. Already Exist: " + str(totalGrpoExist))
        
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        
        return df3
    

    def loadCsv(self, file_name):

        totalready = 0

        self.tabWidget.setCurrentIndex(1) 
        df3 = APInvoice.processDataFrame(self, file_name)
        
        d4 = df3['S-AC'].unique()
        d5 = d4.tolist()
        wtCodeListArr = Utilities.Utilities.wtQueryValidator(d5)
        
        wtcode_list = wtCodeListArr[0]
        wtcode_cardcode_list = wtCodeListArr[1]
        wtcode_rate_list = wtCodeListArr[2]
        wtcode_liable_list = wtCodeListArr[3]


        rowcount = len(df3)
        self.tableWidget_apinvoice.setColumnCount(31)
        self.tableWidget_apinvoice.setRowCount(rowcount)



        for i in range(rowcount):
            if(str(df3._get_value(i, 18, takeable=True)) == '2' and str(df3._get_value(i, 0, takeable=True))== "SUCCESS"):
                totalready += 1



            for j in range(31):
                # print(df3._get_value(i, j, takeable=True) )
                self.tableWidget_apinvoice.setItem(i,j,QTableWidgetItem(str(df3._get_value(i, j, takeable=True))))
                
                if(str(df3._get_value(i, 18, takeable=True)) == '2'):
                    self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(173, 216, 230))
                else:
                    self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(240, 255, 255))


                if(str(df3._get_value(i, 0, takeable=True))== "FAILED"):
                    self.tableWidget_apinvoice.item(i,0).setBackground(QtGui.QColor(255, 128, 128))
                    # print(str(df3._get_value(i, j, takeable=True)))
                    try:
                        if("InvalidBP" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(255, 165, 0))
                            

                        if("InvalidItem" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(255,255,0))
                            

                        if("AlreadyPosted" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(150,75,0))
                            
                    except:
                        self.tableWidget_apinvoice.item(i,0).setBackground(QtGui.QColor(255, 128, 128))


                elif(str(df3._get_value(i, 0, takeable=True))== "CTRL ACCT"):
                    self.tableWidget_apinvoice.item(i,0).setBackground(QtGui.QColor(13,152,186))
                    if("ControlAccount" in str(df3._get_value(i, j, takeable=True))):
                            self.tableWidget_apinvoice.item(i,j).setBackground(QtGui.QColor(13,152,186))
                    
                    



                else:
                    self.tableWidget_apinvoice.item(i,0).setBackground(QtGui.QColor(144, 238, 144))

        

        

                # print(str(df3._get_value(i, 18, takeable=True)))
                # if(str(df3._get_value(i, 18, takeable=True)) == '2'):
                isheader = str(df3._get_value(i, 18, takeable=True))
                cardcode = df3._get_value(i, 6, takeable=True)

                if(str(df3._get_value(i, 0, takeable=True))!= "CTRL ACCT"):
                    if(cardcode in wtcode_cardcode_list):
                        self.tableWidget_apinvoice.setItem(i,24,QTableWidgetItem(str("Yes")))


                        if(self.tableWidget_apinvoice.setItem(i,24,QTableWidgetItem(str("Yes"))) == "Yes"):

                            self.tableWidget_apinvoice.setItem(i,27,QTableWidgetItem(str("")))
                            self.tableWidget_apinvoice.setItem(i,28,QTableWidgetItem(str("")))
                        else:
                            self.tableWidget_apinvoice.setItem(i,27,QTableWidgetItem(str("")))
                            self.tableWidget_apinvoice.setItem(i,28,QTableWidgetItem(str("")))

                else:
                    self.tableWidget_apinvoice.setItem(i,24,QTableWidgetItem(str("CTRL ACCT")))
                    self.tableWidget_apinvoice.setItem(i,27,QTableWidgetItem(str("")))
                    self.tableWidget_apinvoice.setItem(i,28,QTableWidgetItem(str("")))
                    self.tableWidget_apinvoice.setItem(i,28,QTableWidgetItem(str("")))
                    self.tableWidget_apinvoice.item(i,24).setBackground(QtGui.QColor(13,152,186))
                  
        
        
        
        
        self.label_apinvoice_total_ready.setText("AP INVOICE READY TO POST: " + str(totalready))
            
                # else:
                #     self.tableWidget_apinvoice.setItem(i,24,QTableWidgetItem('-'))





    def postAPInvoice(self,file_name):
        print(file_name)
        sessionKey = Utilities.Utilities.login()
        
        wtCodeListArr = Utilities.Utilities.wtQueryValidator2()
        
        wtcode_list = wtCodeListArr[0]
        # print(type(wtcode_list))
        
        df3 = APInvoice.processDataFrame(self,file_name)

        
        print(df3)
        print(type(df3))
        df4 = df3.loc[df3['Status'] == "SUCCESS"] 
        headers = df4.loc[df4['Items'] == 2]
        ctrlaccts = df4.loc[df4['Items'] == 1]
        
        df3 = df3.sort_values(['Cont.No.','Items'], ascending=True)
        df4.to_csv('grpo.csv', index=False)
        # for ind in header.index:
        # print(df4)
        # print("!!")
        df4.to_csv('apinvoice.csv', index=False)
        batch_header = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        batch_footer = """--batch_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        changeset_header= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c\n"""
        changeset_footer= """--changeset_36522ad7-fc75-4b56-8c71-56071383e77c--\n"""
        content_header = """Content-Type: application/http\nContent-Transfer-Encoding:binary\n\nPOST /b1s/v1/PurchaseInvoices\nContent-Type: application/json\n"""
        index = 0
        data = ''
        data += batch_header

        for ind in headers.index:
            # print(headers.at[ind,'Cont.No.'])
            dflines = df4.loc[df4['Doc.No.'] == headers.at[ind,'Doc.No.']] 
            
            documentlines = []
            wtaxlines = []
            wtaxllinesobject = []
            value = self.tableWidget_apinvoice.item(index,24).text()
            wtaxcode1 =  self.tableWidget_apinvoice.item(index,27).text()
            wtaxcode2 =  self.tableWidget_apinvoice.item(index,28).text()
            header = self.tableWidget_apinvoice.item(index,18).text()

            # print(wtaxcode1,wtaxcode2)
            if(wtaxcode1 == wtaxcode2):
                if(wtaxcode1 in wtcode_list):
                    if(value == 'Yes'):
                        if(str(self.tableWidget_apinvoice.item(index,27).text()) != ''):
                            wtaxllinesobject = {
                                "WTCode": str(self.tableWidget_apinvoice.item(index,27).text())
                            }

                            wtaxlines.append(wtaxllinesobject)
            
            else:
                if(wtaxcode1 in wtcode_list and wtaxcode2 in wtcode_list):
                    if(value == 'Yes'):
                        if(str(self.tableWidget_apinvoice.item(index,27).text()) != ''):
                            wtaxllinesobject = {
                                "WTCode":str(self.tableWidget_apinvoice.item(index,27).text())
                            }
                            wtaxllinesobject2 = {
                                "WTCode":str(self.tableWidget_apinvoice.item(index,28).text())
                            }
                            wtaxlines.append(wtaxllinesobject)
                            wtaxlines.append(wtaxllinesobject2)

                            

            # print(self.tableWidget_apinvoice.cellWidget(index,24).currentText())   
            
            for ind2 in dflines.index:
                WTLiable = ''
                if(value == 'Yes'):
                    WTLiable = 'tYes'
                else:
                    WTLiable = 'tNo'

                print("GRPO DOC ENTRY ------------------------------------------")
                print(dflines['GRPO Doc. Entry'][ind2])
                if(dflines['GRPO Doc. Entry'][ind2] != ''):
                    if(str(dflines['A/C Code'][ind2]) != "41210"):
                        linesdict =	{
                            "ItemCode": str(dflines['Material Code'][ind2]),
                            "Quantity": float(str(dflines['Quantity'][ind2]).replace(",", "").replace(".000000", "").replace("-", "")),
                            "VatGroup": str(dflines['Tx'][ind2]),
                            "UomCode": str(dflines['Quantity Unit'][ind2]),
                            "Currency": str(dflines['Curr'][ind2]),
                            "WTLiable": str(dflines['WT Liable'][ind2]),
                            "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "BaseEntry": int(dflines['GRPO Doc. Entry'][ind2]),
                            "BaseType": int(20),
                            "BaseLine": int(dflines['Items'][ind2]) - 2,
                            "WTLiable": WTLiable
                        }
                else:
                    if(str(dflines['A/C Code'][ind2]) != "41210"):
                        linesdict =	{
                            "ItemCode": str(dflines['Material Code'][ind2]),
                            "Quantity": float(str(dflines['Quantity'][ind2]).replace(",", "").replace(".000000", "").replace("-", "")),
                            "VatGroup": str(dflines['Tx'][ind2]),
                            "UomCode": str(dflines['Quantity Unit'][ind2]),
                            "Currency": str(dflines['Curr'][ind2]),
                            "WTLiable": str(dflines['WT Liable'][ind2]),
                            "U_TransAmt": float(str(dflines['Trans. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "LineTotal": float(str(dflines['Dom. Amt.'][ind2]).replace(",", "").replace("-", "")),
                            "WTLiable": WTLiable
                        }


                documentlines.append(linesdict)




            documentArray = []
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
                "U_ContNo": str(headers['Cont.No.'][ind]).replace(" - AlreadyGRPO", ""),
                "U_ClrngDoc": str(headers['Clrng doc.'][ind]),
                "U_ClrngDT": str(headers['Clrng DT'][ind]),
                "U_SubAccount": str(headers['2nd Sub-Account'][ind]),
                "DocumentLines": documentlines,
                "WithholdingTaxDataCollection": wtaxlines
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
        print("AP INVOICE DATA ENTRY:")
        # print(data)
        with open('apinv.txt', 'w') as f:
            f.write(data)

        
        print('**********************')
        headers = {
                    "Content-Type":"multipart/mixed;boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77c",
                    "Cookie": "B1SESSION=" + sessionKey + "; ROUTEID",
        }

        
        url = http + host + ":" + port + "/b1s/v1/$batch"
        requestUrl = requests.post(url, headers=headers, data=data, verify=False)
        print(requestUrl.text)  
        # self.tabWidget.setCurrentIndex(2) 

        APInvoice.loadCsv(self,file_name)
        # APCreditMemo.APCreditMemo.postAPCreditMemo(self,file_name,sessionKey)