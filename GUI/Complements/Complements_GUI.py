import sys

from Solvers.Complement import Complement
from .Complements import Ui_Complements
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

from Solvers.helper import check_base


class Complements_GUI(QMainWindow, Ui_Complements):
    def __init__(self, parent=None):
        super(Complements_GUI, self).__init__(parent)

        self.setupUi(self)

        actionInputs = QAction('Usage Instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)



        self.cmp = Complement(int(self.spinBox.text()))

    def on_InputNumberEditText_textChanged(self):
        self.findComplements()

    def on_spinBox_valueChanged(self):
        self.cmp = Complement(int(self.spinBox.text()))
        self.findComplements()

    def findComplements(self):
        if self.InputNumberEditText.toPlainText() == '':
            return
        if self.verifyInput():
            number = int(self.InputNumberEditText.toPlainText())
            base = str(self.cmp.base_compliment(number))
            reduced_base = str(self.cmp.reduced_base_compliment(number))
            self.OutputNumberBaseEditText.setText(base)
            self.OutputNumberReducedBaseEditText.setText(reduced_base)
        else:
            self.OutputNumberBaseEditText.setText('Invalid input. Check base?')
            self.OutputNumberReducedBaseEditText.setText('')


    def verifyInput(self):
        return check_base(self.InputNumberEditText.toPlainText(), int(self.spinBox.text()))


    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("Complements Finder Usage Instructions\n\n"
                           "  \u2022 Step 1: Type the number in the field.\n"
                           "  \u2022 Step 2: Select the appropriate base.\n"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = Complements_GUI()
    ui.show()
    sys.exit(app.exec_())

