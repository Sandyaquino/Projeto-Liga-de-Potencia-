import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QHBoxLayout, QMessageBox, QPushButton, QTableView, QTextEdit)
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import QtCore, QtGui, QtSql
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TABLE OF DATABASE'
        self.left = 200
        self.top = 200
        self.width = 1000
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setWindowIcon(QIcon('logo.png'))		
        self.show()

class MyTableWidget(QWidget):        
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)			
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300,200) 
        # Add tabs
#########################################################################################       
		# Create first tab
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1," Sources ")		
        self.model1 = QSqlTableModel(self)	
        self.model1.setTable("Sources")
        self.model1.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model1.select()
        self.layout = QVBoxLayout(self)
        self.view1 = QTableView()
        self.view1.setModel(self.model1)       	
        self.tab1.layout = QVBoxLayout(self)		
        self.submitButton = QPushButton("Submit")
        self.submitButton.setDefault(True)
        self.revertButton = QPushButton("&Revert")
        self.quitButton = QPushButton("Quit")		
        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(self.submitButton, QDialogButtonBox.ActionRole)	
        buttonBox.addButton(self.revertButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)
        self.submitButton.clicked.connect(self.submit1)
        self.revertButton.clicked.connect(self.model1.revertAll)
        self.quitButton.clicked.connect(self.close)		
        mainLayout1 = QHBoxLayout()
        mainLayout1.addWidget(self.view1)
        mainLayout1.addWidget(buttonBox)
        self.setLayout(mainLayout1)
        self.tab1.layout.addWidget(self.view1)
        self.tab1.layout.addWidget(self.submitButton)
        self.tab1.layout.addWidget(self.revertButton)
        self.tab1.layout.addWidget(self.quitButton)		
        self.tab1.setLayout(self.tab1.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
#################################################################################################
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2,"Lines")		
        self.model2 = QSqlTableModel(self)	
        self.model2.setTable("Lines")
        self.model2.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model2.select()
        self.layout = QVBoxLayout(self)
        self.view2 = QTableView()
        self.view2.setModel(self.model2)       	
        self.tab2.layout = QVBoxLayout(self)		
        self.submitButton2 = QPushButton("Submit")
        self.submitButton2.setDefault(True)
        self.revertButton2 = QPushButton("&Revert")
        self.quitButton2 = QPushButton("Quit")		
        buttonBox2 = QDialogButtonBox(Qt.Vertical)
        buttonBox2.addButton(self.submitButton2, QDialogButtonBox.ActionRole)	
        buttonBox2.addButton(self.revertButton2, QDialogButtonBox.ActionRole)
        buttonBox2.addButton(self.quitButton2, QDialogButtonBox.RejectRole)
        self.submitButton2.clicked.connect(self.submit2)
        self.revertButton2.clicked.connect(self.model2.revertAll)
        self.quitButton2.clicked.connect(self.close)		
        mainLayout2 = QHBoxLayout()
        mainLayout2.addWidget(self.view2)
        mainLayout2.addWidget(buttonBox2)
        self.setLayout(mainLayout2)
        self.tab2.layout.addWidget(self.view2)
        self.tab2.layout.addWidget(self.submitButton2)
        self.tab2.layout.addWidget(self.revertButton2)
        self.tab2.layout.addWidget(self.quitButton2)		
        self.tab2.setLayout(self.tab2.layout)
#########################################################################################################################		
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
#################################################################################################
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3,"LineCode")		
        self.model3 = QSqlTableModel(self)	
        self.model3.setTable("LineCode")
        self.model3.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model3.select()
        self.layout = QVBoxLayout(self)
        self.view3 = QTableView()
        self.view3.setModel(self.model3)       	
        self.tab3.layout = QVBoxLayout(self)		
        self.submitButton3 = QPushButton("Submit")
        self.submitButton3.setDefault(True)
        self.revertButton3 = QPushButton("&Revert")
        self.quitButton3 = QPushButton("Quit")		
        buttonBox3= QDialogButtonBox(Qt.Vertical)
        buttonBox3.addButton(self.submitButton3, QDialogButtonBox.ActionRole)	
        buttonBox3.addButton(self.revertButton3, QDialogButtonBox.ActionRole)
        buttonBox3.addButton(self.quitButton3, QDialogButtonBox.RejectRole)
        self.submitButton3.clicked.connect(self.submit3)
        self.revertButton3.clicked.connect(self.model3.revertAll)
        self.quitButton3.clicked.connect(self.close)		
        mainLayout3= QHBoxLayout()
        mainLayout3.addWidget(self.view3)
        mainLayout3.addWidget(buttonBox3)
        self.setLayout(mainLayout3)
        self.tab3.layout.addWidget(self.view3)
        self.tab3.layout.addWidget(self.submitButton3)
        self.tab3.layout.addWidget(self.revertButton3)
        self.tab3.layout.addWidget(self.quitButton3)		
        self.tab3.setLayout(self.tab3.layout)
#########################################################################################################################		
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
#################################################################################################
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4,"Transformers")		
        self.model4 = QSqlTableModel(self)	
        self.model4.setTable("Transformers")
        self.model4.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model4.select()
        self.layout = QVBoxLayout(self)
        self.view4 = QTableView()
        self.view4.setModel(self.model4)       	
        self.tab4.layout = QVBoxLayout(self)		
        self.submitButton4 = QPushButton("Submit")
        self.submitButton4.setDefault(True)
        self.revertButton4 = QPushButton("&Revert")
        self.quitButton4 = QPushButton("Quit")		
        buttonBox4= QDialogButtonBox(Qt.Vertical)
        buttonBox4.addButton(self.submitButton4, QDialogButtonBox.ActionRole)	
        buttonBox4.addButton(self.revertButton4, QDialogButtonBox.ActionRole)
        buttonBox4.addButton(self.quitButton4, QDialogButtonBox.RejectRole)
        self.submitButton4.clicked.connect(self.submit4)
        self.revertButton4.clicked.connect(self.model4.revertAll)
        self.quitButton4.clicked.connect(self.close)		
        mainLayout4= QHBoxLayout()
        mainLayout4.addWidget(self.view4)
        mainLayout4.addWidget(buttonBox4)
        self.setLayout(mainLayout4)
        self.tab4.layout.addWidget(self.view4)
        self.tab4.layout.addWidget(self.submitButton4)
        self.tab4.layout.addWidget(self.revertButton4)
        self.tab4.layout.addWidget(self.quitButton4)		
        self.tab4.setLayout(self.tab4.layout)
#########################################################################################################################		
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
#################################################################################################
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab5,"Load")		
        self.model5 = QSqlTableModel(self)	
        self.model5.setTable("Load")
        self.model5.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model5.select()
        self.layout = QVBoxLayout(self)
        self.view5 = QTableView()
        self.view5.setModel(self.model5)       	
        self.tab5.layout = QVBoxLayout(self)		
        self.submitButton5 = QPushButton("Submit")
        self.submitButton5.setDefault(True)
        self.revertButton5 = QPushButton("&Revert")
        self.quitButton5 = QPushButton("Quit")		
        buttonBox5= QDialogButtonBox(Qt.Vertical)
        buttonBox5.addButton(self.submitButton5, QDialogButtonBox.ActionRole)	
        buttonBox5.addButton(self.revertButton5, QDialogButtonBox.ActionRole)
        buttonBox5.addButton(self.quitButton5, QDialogButtonBox.RejectRole)
        self.submitButton5.clicked.connect(self.submit5)
        self.revertButton5.clicked.connect(self.model5.revertAll)
        self.quitButton5.clicked.connect(self.close)		
        mainLayout5= QHBoxLayout()
        mainLayout5.addWidget(self.view5)
        mainLayout5.addWidget(buttonBox5)
        self.setLayout(mainLayout5)
        self.tab5.layout.addWidget(self.view5)
        self.tab5.layout.addWidget(self.submitButton5)
        self.tab5.layout.addWidget(self.revertButton5)
        self.tab5.layout.addWidget(self.quitButton5)		
        self.tab5.setLayout(self.tab5.layout)
#########################################################################################################################		
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
#################################################################################################
        self.tab6 = QWidget()
        self.tabs.addTab(self.tab6,"Capacitors")		
        self.model6 = QSqlTableModel(self)	
        self.model6.setTable("Capacitors")
        self.model6.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model6.select()
        self.layout = QVBoxLayout(self)
        self.view6= QTableView()
        self.view6.setModel(self.model6)       	
        self.tab6.layout = QVBoxLayout(self)		
        self.submitButton6 = QPushButton("Submit")
        self.submitButton6.setDefault(True)
        self.revertButton6 = QPushButton("&Revert")
        self.quitButton6 = QPushButton("Quit")		
        buttonBox6= QDialogButtonBox(Qt.Vertical)
        buttonBox6.addButton(self.submitButton6, QDialogButtonBox.ActionRole)	
        buttonBox6.addButton(self.revertButton6, QDialogButtonBox.ActionRole)
        buttonBox6.addButton(self.quitButton6, QDialogButtonBox.RejectRole)
        self.submitButton6.clicked.connect(self.submit6)
        self.revertButton6.clicked.connect(self.model6.revertAll)
        self.quitButton6.clicked.connect(self.close)		
        mainLayout6= QHBoxLayout()
        mainLayout6.addWidget(self.view6)
        mainLayout6.addWidget(buttonBox6)
        self.setLayout(mainLayout6)
        self.tab6.layout.addWidget(self.view6)
        self.tab6.layout.addWidget(self.submitButton6)
        self.tab6.layout.addWidget(self.revertButton6)
        self.tab6.layout.addWidget(self.quitButton6)		
        self.tab6.setLayout(self.tab6.layout)
#########################################################################################################################		
#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    def submit1(self):
        self.model1.database().transaction()
        if self.model1.submitAll():
            self.model1.database().commit()
        else:
            self.model1.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model1.lastError().text())
    def submit2(self):
        self.model2.database().transaction()
        if self.model2.submitAll():
            self.model2.database().commit()
        else:
            self.model2.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model2.lastError().text())
    def submit3(self):
        self.model3.database().transaction()
        if self.model3.submitAll():
            self.model3.database().commit()
        else:
            self.model3.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model3.lastError().text())
    def submit4(self):
        self.model4.database().transaction()
        if self.model4.submitAll():
            self.model4.database().commit()
        else:
            self.model4.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model4.lastError().text())
    def submit5(self):
        self.model5.database().transaction()
        if self.model5.submitAll():
            self.model5.database().commit()
        else:
            self.model5.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model5.lastError().text())
    def submit6(self):
        self.model6.database().transaction()
        if self.model6.submitAll():
            self.model6.database().commit()
        else:
            self.model6.database().rollback()
            QMessageBox.warning(self, "Transformers Table",
                        "The database reported an error: %s" % self.model6.lastError().text())						

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
ex = App()
#    sys.exit(app.exec_())