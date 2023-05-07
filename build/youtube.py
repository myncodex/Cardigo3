import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore    
    

class MainWindow1(QMainWindow):
    def closing(self):
        
        sys.exit(app.exec_())

        

        


    def __init__(self):
        super(MainWindow1, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://youtube.com'))
        self.setCentralWidget(self.browser)
        self.uicomp()
        self.showMaximized()


    def uicomp(self):
        button = QPushButton(self,clicked= lambda: self.closing())
        button.setGeometry(QRect(14,25,40,40))
        button.setStyleSheet("background-color:#ffffff")
        button.setIcon(QtGui.QIcon("C:/Users/User/Desktop/New folder/build/assets/frame3/button_9.png"))
        button.setIconSize(QtCore.QSize(40,40))
    
if __name__=="__main__":
    app = QApplication(sys.argv) 
    QApplication.setApplicationName('Youtube')
    window = MainWindow1()
    app.exec_()
    
    


