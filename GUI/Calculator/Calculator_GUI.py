import sys

from Solvers.BaseConverter import BaseConverter
from .Calculator import Ui_Calculator
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

from Solvers.helper import check_base


class Calculator_GUI(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):

        super(Calculator_GUI, self).__init__(parent)

        self.setupUi(self)
        self.base = int(self.setBaseSpinBox.text())
        self.result = 0

        actionInputs = QAction('Usage instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)




    @QtCore.pyqtSlot()
    def on_Button_add_clicked(self):
        self.lockBase()
        self.result += BaseConverter.any_to_dec(self.inputText.toPlainText(), self.base)
        self.print_result()

    @QtCore.pyqtSlot()
    def on_Button_sub_clicked(self):
        self.lockBase()
        self.result -= BaseConverter.any_to_dec(self.inputText.toPlainText(), self.base)
        if self.result < 0:
            self.OutputText.setText('Overflow!')
        else:
            self.print_result()

    @QtCore.pyqtSlot()
    def on_Button_mul_clicked(self):
        self.lockBase()
        self.result *= BaseConverter.any_to_dec(self.inputText.toPlainText(), self.base)
        print(self.result)
        self.print_result()

    @QtCore.pyqtSlot()
    def on_Button_div_clicked(self):
        self.lockBase()
        self.result //= BaseConverter.any_to_dec(self.inputText.toPlainText(), self.base)
        self.print_result()

    @QtCore.pyqtSlot()
    def on_clear_clicked(self):
        self.result = 0
        self.OutputText.setPlainText('0')
        self.inputText.setPlainText('')
        self.lockBase(False)

    def print_result(self):
        self.OutputText.setText(BaseConverter.dec_to_any(self.result, self.base))
        self.inputText.setText('')

    def lockBase(self, p_bool=True):
        self.setBaseSpinBox.setDisabled(p_bool)

    def on_setBaseSpinBox_valueChanged(self):
        self.base = int(self.setBaseSpinBox.text())
        self.checkButtons()

    def on_inputText_textChanged(self):
        self.checkButtons()

    def checkButtons(self):
        flag = not self.verifyInput()
        self.Button_add.setDisabled(flag)
        self.Button_sub.setDisabled(flag)
        self.Button_mul.setDisabled(flag)
        div_flag = flag or self.inputText.toPlainText() == '' or self.inputText.toPlainText() == '0'
        self.Button_div.setDisabled(div_flag)

    def verifyInput(self):
        return self.inputText.toPlainText() != '' and check_base(self.inputText.toPlainText(), int(self.setBaseSpinBox.text()))


    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("Calculator Usage Instructions\n\n"
                           "  \u2022 Step 1: Type the number in the field.\n"
                           "  \u2022 Step 2: Select the appropriate base.\n"
                           "  \u2022 Step 3: Press any operation button.\n\n"
                           "Note that once you make the first operation the base gets locked. To change the base you have to clear the results."))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Calculator_GUI()
    ui.show()
    sys.exit(app.exec_())