import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QTableWidget
from PyQt5 import uic,QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import pandas as pd
import csv
import datetime
import math
import pyodbc
import numpy as np
import json 
import requests
import time
from modules.grpo import Grpo
from modules.apinvoice import APInvoice
from modules.apcreditmemo import APCreditMemo
from modules.outgoingpayments import OutgoingPayments
from modules.arinvoice import ARInvoice
from modules.billingstatement import BillingStatement
from modules.ardebitmemo import ARCreditMemo
from modules.incomingpayments import IncomingPayments
from modules.journalentry import JournalEntry
import os
import patoolib

date_format = "%Y%m%d"

itemcode_list = []
itemcode_uomcode_list = []

from modules.utilities import http as http
from modules.utilities import host as host
from modules.utilities import port as port
from modules.utilities import database as database
from modules.utilities import sapusername as sapusername
from modules.utilities import sappassword as sappassword

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'D:\xampp\htdocs\Python\SAPB1_MARUBENI_UPLOADER-DEV\TransactionUploader.ui',self)

        self.setWindowIcon(QtGui.QIcon(r'D:\xampp\htdocs\Python\SAPB1_MARUBENI_UPLOADER-DEV\resources\icons\business.png'))

        self.pushButton_browse.clicked.connect(self.browseFiles)

        # patoolib.extract_archive("C:/Users/Joshua Arman Galvez/Desktop/EBINGGAY/RPL20230101.zip", outdir="C:/Users/Joshua Arman Galvez/Desktop/EBINGGAY/test")
        
        # self.thread={}
        # self.pushButton_show_apinvoice.clicked.connect(self.start_worker_1)
        self.pushButton_show_grpo.clicked.connect(self.loadCsvGrpo)
        self.pushButton_show_apinvoice.clicked.connect(self.loadCsvAPInvoice)
        self.pushButton_show_apcm.clicked.connect(self.loadCsvAPCreditMemo)
        self.pushButton_show_outgoing.clicked.connect(self.loadCsvOutgoingPayments)


        self.pushButton_show_arinvoice.clicked.connect(self.loadCsvARInvoice)
        self.pushButton_show_arinvoice_2.clicked.connect(self.loadCsvBillingStatement)
        self.pushButton_show_arcm.clicked.connect(self.loadCsvARCreditMemo)
        self.pushButton_show_outgoing_2.clicked.connect(self.loadCsvIncomingPayments)


        self.pushButton_show_ojdt.clicked.connect(self.loadCsvJournalEntry)
        # ----------------------------------------------------------------------------
        
        self.pushButton_upload_grpo.clicked.connect(self.postCsvGrpo)
        self.pushButton_upload_apinvoice.clicked.connect(self.postCsvAPInvoice)
        self.pushButton_upload_apcm.clicked.connect(self.postCsvAPCreditMemo)
        self.pushButton_upload_outgoing.clicked.connect(self.postCsvOutgoingPayments)

        self.pushButton_upload_arinvoice.clicked.connect(self.postCsvARInvoice)
        self.pushButton_upload_arinvoice_2.clicked.connect(self.postCsvBillingStatement)
        self.pushButton_upload_arcm.clicked.connect(self.postCsvARCreditMemo)
        self.pushButton_upload_outgoing_2.clicked.connect(self.postCsvIncomingPayments)

        self.pushButton_upload_ojdt.clicked.connect(self.postCsvJournalEntry)



        # --------------------------------------------------------------------------------


        self.pushButton_grpo_clear.clicked.connect(self.clearAPInvoice)
        self.pushButton_apinvoice_clear.clicked.connect(self.clearAPInvoice)




        
        
        
    file_name=''
    

    
    

    def browseFiles(self):
        file_name = QFileDialog.getOpenFileName(self,"Select a CSV File","C:\\Desktop","CSV Files (*.csv)")


        if file_name:
            print(file_name[0])
            self.lineEdit_filename.setText(file_name[0])



    def clearGRPO(self):
        self.tableWidget_grpo.setRowCount(0)
    def clearAPInvoice(self):
        self.tableWidget_apinvoice.setRowCount(0)
    # -----------------------------------------------------------------

    def loadCsvGrpo(self, file_name):
        self.tableWidget_grpo.setRowCount(0)
        try:
            print(file_name)
            print("Loading CSV GRPO")
            Grpo.loadCsv(self,file_name)
        except:
            print(file_name)
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)
        
        
    def loadCsvAPInvoice(self, file_name):
        # try:
        print(file_name)
        print("Loading CSV AP Invoice")

        APInvoice.loadCsv(self,file_name)
        # except Exception as error:
        #     messsage = 'Insert File!'
        #     self.showWarningMessage(messsage)
            # print("An exception occurred:", type(error).__name__)
        
        

        # Output:
        # This will extract all files from 'file.zip'
    
    def loadCsvAPCreditMemo(self, file_name):
        try:
            print(file_name)
            print("Loading CSV AP Credit Memo")
            APCreditMemo.loadCsv(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)

    
    def loadCsvOutgoingPayments(self, file_name):
    # try:
        print(file_name)
        print("Loading CSV Outgoing Payments")
        OutgoingPayments.loadCsv(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)



    def loadCsvARInvoice(self, file_name):
       
            print(file_name)
            print("Loading CSV AR Invoice")
            ARInvoice.loadCsv(self,file_name)
       

    
    def loadCsvBillingStatement(self, file_name):
        # try:
            print(file_name)
            print("Loading CSV Billing Statement")
            BillingStatement.loadCsv(self,file_name)
        # except:
        #     messsage = 'Insert File!'
        #     self.showWarningMessage(messsage)


    def loadCsvARCreditMemo(self, file_name):
        try:
            print(file_name)
            print("Loading CSV AR Credit Memo")
            ARCreditMemo.loadCsv(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)

            
    def loadCsvIncomingPayments(self, file_name):
    # try:
        print(file_name)
        print("Loading CSV Incoming Payments")
        IncomingPayments.loadCsv(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)   

        # self.worker = WorkerThread()
        # self.worker.start()
        # self.worker.load_grpo_csv.connect(self.loadCsv)
        # self.worker.finished.connect(self.showNext)



    def loadCsvJournalEntry(self, file_name):
        # try:
        print(file_name)
        print("Loading CSV Incoming Payments")
        JournalEntry.loadCsv(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)   

    

    def showNext(self):
            print('Finished loading csv')




    def postCsvGrpo(self,file_name):
        try:
            print(file_name)
            Grpo.postGRPO(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)
    
    def postCsvAPInvoice(self,file_name):
        try:
            print(file_name)
            APInvoice.postAPInvoice(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)
    
    def postCsvAPCreditMemo(self,file_name):
        try:
            print(file_name)
            APCreditMemo.postAPCreditMemo(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)

    def postCsvOutgoingPayments(self,file_name):
    # try:
        print(file_name)
        OutgoingPayments.postOutgoingPayments(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)
    
    def postCsvARInvoice(self,file_name):
        # try:
            print(file_name)
            ARInvoice.postARInvoice(self,file_name)
        # except Exception as error:
            # messsage = str(error)
            # self.showWarningMessage(messsage)

    def postCsvBillingStatement(self,file_name):
        # try:
            print(file_name)
            BillingStatement.postBillingStatement(self,file_name)
        # except:
        #     messsage = 'Insert File!'
        #     self.showWarningMessage(messsage)


    def postCsvARCreditMemo(self,file_name):
        try:
            print(file_name)
            ARCreditMemo.postARCreditMemo(self,file_name)
        except:
            messsage = 'Insert File!'
            self.showWarningMessage(messsage)


    def postCsvIncomingPayments(self,file_name):
    # try:
        print(file_name)
        IncomingPayments.postIncomingPayments(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)


    def postCsvJournalEntry(self,file_name):
    # try:
        print(file_name)
        JournalEntry.postJournalEntry(self,file_name)
    # except:
    #     messsage = 'Insert File!'
    #     self.showWarningMessage(messsage)




    def showWarningMessage(self,messsage):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Warning) 
    
        # setting message for Message Box 
        msg.setText(messsage) 
        
        # setting Message box window title 
        msg.setWindowTitle("Warning MessageBox") 
        
        # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 

        retval = msg.exec_() 
    


    
    
       
   

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = App()
    demo.show()


    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window')