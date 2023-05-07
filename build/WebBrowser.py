import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow1(QMainWindow):
    def closing(self):
        sys.exit(app.exec_())
    def __init__(self):
        super(MainWindow1, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://programming-hero.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
    def uicomp(self):
        button = QPushButton(self,clicked= lambda:self.closing())
        button.setGeometry(QRect(14,25,40,40))
        button.setStyleSheet("background-color:#ffffff")
        button.setIcon(QtGui.QIcon("C:/Users/User/Desktop/New folder/build/assets/frame3/button_9.png"))
        button.setIconSize(QtCore.QSize(40,40))

if __name__=="__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('My Cool Browser')
    window = MainWindow1()
    app.exec_()