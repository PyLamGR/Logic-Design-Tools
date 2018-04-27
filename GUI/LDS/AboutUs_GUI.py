import sys
import webbrowser

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

from .AboutUs import Ui_AboutPage


class AboutUs_GUI(QMainWindow,Ui_AboutPage):
    def __init__(self, parent=None):
        super(AboutUs_GUI, self).__init__(parent)
        self.setupUi(self)
        self.imageView.setPixmap(QPixmap("GUI/PyLamLogo.png"))


    @QtCore.pyqtSlot()
    def on_visitUsButton_clicked(self):
        webbrowser.open("http://pylam.gr")

    @QtCore.pyqtSlot()
    def on_SourceCodeButton_clicked(self):
         webbrowser.open("https://bitbucket.org/pylamgr/logic-design-solver/src")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = AboutUs_GUI()
    ui.show()
    sys.exit(app.exec_())