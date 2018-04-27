import sys

from Solvers.BaseConverter import BaseConverter
from Solvers.helper import check_base
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from .BaseConverter import Ui_BaseConverter


class BaseConverter_GUI(QMainWindow, Ui_BaseConverter):

    def __init__(self, parent=None):
        super(BaseConverter_GUI, self).__init__(parent)
        self.setupUi(self)

        self.label.setText("Primary Number")
        self.label_4.setText("Secondary Number")

        actionInputs = QAction('Usage Instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)


    @QtCore.pyqtSlot()
    def on_primaryNumberText_textChanged(self):
        self.tryConvertion()


    def on_baseFromN1_valueChanged(self):
        self.tryConvertion()

    def on_baseToN2_valueChanged(self):
        self.tryConvertion()


    def tryConvertion(self):
        number_from = self.primaryNumberText.toPlainText()
        base_from = int(self.baseFromN1.text())
        base_to = int(self.baseToN2.text())

        if check_base(number_from, base_from):
            self.secondaryNumberText.setPlainText(BaseConverter.any_to_any(number_from, base_from, base_to))
        else:
            self.secondaryNumberText.setPlainText('Invalid number! Check base?')


    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("Base Converter Usage Instructions\n\n"
                           "  \u2022 Step 1: Type the number in the input field.\n"
                           "  \u2022 Step 2: Select the appropriate 'base from'.\n"
                           "  \u2022 Step 3: Select the preferred 'base to'.\n"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = BaseConverter_GUI()
    ui.show()
    sys.exit(app.exec_())