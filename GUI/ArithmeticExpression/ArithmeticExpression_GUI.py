from Solvers.ArithmeticExpression import ArithmeticExpression
from .ArithmeticExpression import Ui_ArithmeticExpression
from PyQt5.QtWidgets import *

from Solvers.helper import check_base


class ArithmeticExpression_GUI(QMainWindow, Ui_ArithmeticExpression):

    def __init__(self, parent=None):
        super(ArithmeticExpression_GUI, self).__init__(parent)

        self.setupUi(self)
        self.findExpressionButton.setDisabled(True)
        self.findExpressionButton.clicked.connect(self.findExpression)

        actionInputs = QAction('Usage Instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)


        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)


    def on_baseFromSpinBox_valueChanged(self, i):
        self.findExpressionButton.setDisabled(not check_base(self.numberText.toPlainText(), int(self.baseFromSpinBox.text())))

    def on_numberText_textChanged(self):
        self.findExpressionButton.setDisabled(not check_base(self.numberText.toPlainText(), int(self.baseFromSpinBox.text())))

    def findExpression(self):
        expr = ArithmeticExpression.get_expression(self.numberText.toPlainText(), int(self.baseFromSpinBox.text()), int(self.baseToSpinBox.text()))
        print(str(expr))
        self.resultText.setPlainText(str(expr))



    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions",\
                          ("Arithmetic Expression Usage Instructions\n\n"
                           "  \u2022 Step 1: Type the number in the field.\n"
                           "  \u2022 Step 2: Select the appropriate 'base from'.\n"
                           "  \u2022 Step 3: Select the preferred 'base to'.\n"
                           "  \u2022 Step 4: Press 'Find Expression' button.\n"))