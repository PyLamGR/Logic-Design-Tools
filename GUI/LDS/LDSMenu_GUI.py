import sys

from ..ArithmeticExpression.ArithmeticExpression_GUI import ArithmeticExpression_GUI
from ..BDD.BDD_GUI import BDD_GUI
from ..BaseConverter.BaseConverter_GUI import BaseConverter_GUI
from ..Calculator.Calculator_GUI import Calculator_GUI
from ..Complements.Complements_GUI import Complements_GUI
from ..KMapSolvers.KMapSolvers_GUI import KMapSolvers_GUI
from ..LDS.AboutUs_GUI import AboutUs_GUI
from ..QuineMcCluskey.QuineMcCluskey_GUI import QuineMcCluskey_GUI
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from .LDSMenu import Ui_LDS


class LDSMenu_GUI(QMainWindow, Ui_LDS):
    def __init__(self, parent=None):
        super(LDSMenu_GUI, self).__init__(parent)
        self.setupUi(self)
        self.bdd.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_arithmetic_expressions_clicked(self):
        ui = ArithmeticExpression_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_calculator_clicked(self):
        ui = Calculator_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_complement_solver_clicked(self):
        ui = Complements_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_base_converter_clicked(self):
        ui = BaseConverter_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_kmap_solver_clicked(self):
        ui = KMapSolvers_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_Quine_McCluskey_clicked(self):
        ui = QuineMcCluskey_GUI(self)
        ui.show()

    @QtCore.pyqtSlot()
    def on_bdd_clicked(self):
        ui = BDD_GUI(self)
        ui.show()


    @QtCore.pyqtSlot()
    def on_ExitButton_clicked(self):
        msg = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Cancel | QMessageBox.Yes, QMessageBox.Cancel)
        if msg == QMessageBox.Yes:
            QApplication.quit()
        else:
            pass

    @QtCore.pyqtSlot()
    def on_AboutUsButton_clicked(self):
        ui = AboutUs_GUI(self)
        ui.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LDSMenu_GUI()
    ui.show()
    sys.exit(app.exec_())