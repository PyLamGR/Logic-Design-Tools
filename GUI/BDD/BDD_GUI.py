import sys

from .BDDGUI import Ui_BDDGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

from Solvers.BDD.BDD import *


class BDD_GUI(QMainWindow, Ui_BDDGui):

    def __init__(self, parent=None):
        super(BDD_GUI, self).__init__(parent)
        self.setupUi(self)

        self.problemChecker.setVisible(False)
        self.solveButton.setEnabled(False)

        actionInputs = QAction('Usage Instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)
        actionResult = QAction('Result Explanation', self)
        actionResult.triggered.connect(self.on_result_clicked)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)
        fileMenu.addAction(actionResult)

        self.bddSolver = BDD()



    """clear and solve buttons listeners"""
    @QtCore.pyqtSlot()
    def on_solveButton_clicked(self):


        # set bdd's params
        self.bddSolver.num = int(self.numOfVarsEdit.text())
        self.bddSolver.order = self.orderOfVarsEdit.text()
        self.bddSolver.function = self.functionEdit.text()

        # check for problems
        if self.validityNumberChecker() and self.validityChecker():
            self.bddSolver.main()
            self.bddTreeView.clear()
            for i in self.bddSolver.result:
                print(i + ': ' + str(self.bddSolver.result[i]))
                self.bddTreeView.setText(self.bddTreeView.text() + str("\n" + i + ': ' + str(self.bddSolver.result[i])))
                pass

            self.problemChecker.setVisible(True)
            self.problemChecker.setStyleSheet("color: green;")
            self.problemChecker.setText("BDD solved!")
        else:
            self.problemChecker.setStyleSheet("color: red;")
            self.problemChecker.setVisible(True)
            self.problemChecker.setText("Please enter correct inputs!")


    @QtCore.pyqtSlot()
    def on_clearButton_clicked(self):

        """
        function (listener for clear button)
        :return: erase everything and start from scratch
        """

        self.functionEdit.clear()
        self.numOfVarsEdit.clear()
        self.orderOfVarsEdit.clear()

        self.problemChecker.setVisible(False)

        self.solveButton.setEnabled(False)
        self.bddTreeView.clear()
        self.bddTreeView.setText("Here your bdd result will appear.")



    """editTexts listeners"""
    def on_numOfVarsEdit_textChanged(self):
        if not self.numOfVarsEdit.text().isdigit():
            self.numOfVarsEdit.clear()

        if self.numOfVarsEdit.text()!= "" and self.orderOfVarsEdit.text()!="" and self.functionEdit.text()!="":
            self.solveButton.setEnabled(True)
        else:
            self.solveButton.setEnabled(False)

    def on_orderOfVarsEdit_textChanged(self):
        if self.numOfVarsEdit.text()!="" and self.orderOfVarsEdit.text()!="" and self.functionEdit.text()!="":
            self.solveButton.setEnabled(True)
        else:
            self.solveButton.setEnabled(False)

    def on_functionEdit_textChanged(self):
        if self.numOfVarsEdit.text()!="" and self.orderOfVarsEdit.text()!="" and self.functionEdit.text()!="":
            self.solveButton.setEnabled(True)
        else:
            self.solveButton.setEnabled(False)



    """some useful functions"""
    def validityNumberChecker(self):
        """
        function to find the number of vars problem
        :return: true or false depends if there is a problem or not
        """
        if self.bddSolver.validityForNumbers(self.orderOfVarsEdit.text()):
                return True
        else:
            # use command line to print the problem
            print("validity number checker false")
            return False

    def validityChecker(self):
        """
            function to find the vars problem
            :return: true or false depends if there is a problem or not
        """
        if self.bddSolver.validityChecker(self.functionEdit.text()):
            return True

        else:
            print("validity checker false")
            return False

    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("BDD Solver Usage Instructions\n\n"
                           "  \u2022 Step 1: Give the number of variables (only numbers).\n"
                           "  \u2022 Step 2: Give the order of variables.\n"
                           "  \u2022 Step 3: Enter the Function.\n"
                           "  \u2022 Step 4: Press Solve Button.\n\n"
                           "Note that capital letters in the output represent complements.\n"
                           ))
    def on_result_clicked(self):

        explenationText = "The result of this Simplification is given through various lists. Each element represents a function and every following list representsthis function's simplified form. Every Simplification is done by replacingthe variable from each step. For better understanding of the result note that each element from a previous list corresponds in two elements of the following list.  "
        QMessageBox.about(self, 'Result Explanation',explenationText)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = BDD_GUI()
    ui.show()
    sys.exit(app.exec_())
