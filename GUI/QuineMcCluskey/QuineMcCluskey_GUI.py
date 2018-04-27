import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

"""import quineMcCluskey script"""
from Solvers.QuineMcCluskey.QuineMcCluskey import *

from GUI.QuineMcCluskey.QuineMcCluskeySolverGUI import Ui_QuineMcCluskeyGui

class QuineMcCluskey_GUI(QMainWindow, Ui_QuineMcCluskeyGui):

    def __init__(self, parent=None):
        super(QuineMcCluskey_GUI, self).__init__(parent)
        self.setupUi(self)

        self.solveButton.setEnabled(False)
        self.addMintermButton.setEnabled(False)

        self.min_term = []
        self.dc_term = []

        self.counterForMinterms = 0

        self.quineSolver = None

        actionInputs = QAction('Usage instructions', self)
        actionInputs.triggered.connect(self.on_action_clicked)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Help')
        fileMenu.addAction(actionInputs)

        """create two columns for minterms and results"""
        self.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.finalTable.setEditTriggers(QAbstractItemView.NoEditTriggers)




    def solver(self):
        self.quineSolver = QuineMcV3(self.min_term, self.dc_term)
        self.quineSolver.sort_first_list()
        self.quineSolver.get_last_list()
        self.quineSolver.final_step()





    @QtCore.pyqtSlot()
    def on_ClearButton_clicked(self):

        """
        function to handle clear button click
        :return: clear all widgets imports
        """
        self.resultTable.setRowCount(0)

        self.finalTable.setRowCount(0)
        self.finalTable.setColumnCount(0)
        self.editResultFunction.clear()

        self.min_term = []
        self.dc_term = []

        self.counterForMinterms = 0

        self.quineSolver = None

        self.minterms.clear()
        self.editDCMinterm.clear()
        self.editMinterm.clear()

        self.addMintermButton.setEnabled(False)


        self.enableAfterClearPressed()



    @QtCore.pyqtSlot()
    def on_addMintermButton_clicked(self):

        if not self.editMinterm.text() == "":
            self.min_term.append(self.editMinterm.text())

        if not self.editDCMinterm.text() == "":
            self.dc_term.append(self.editDCMinterm.text())

        self.editDCMinterm.clear()
        self.editMinterm.clear()

        self.counterForMinterms = self.counterForMinterms + 1
        if self.counterForMinterms > 1:
            self.solveButton.setEnabled(True)
        else:
            self.solveButton.setEnabled(False)

        self.minterms.clear()
        for i in range(len(self.min_term)):
            self.minterms.addItem(str(self.min_term[i]))

        print(self.min_term)


    @QtCore.pyqtSlot()
    def on_solveButton_clicked(self):

        self.solver()

        self.resultTable.setRowCount(len(self.min_term))

        for i in range(len(self.quineSolver.bin_array_of_min_terms)):
             self.resultTable.setItem(i, 0, QTableWidgetItem(self.quineSolver.bin_array_of_min_terms[i]))

        for i in range(len(self.quineSolver.final_list)):
            self.resultTable.setItem(i, 1, QTableWidgetItem(self.quineSolver.final_list[i]))

        for i in range(len(self.quineSolver.final_char_min_terms)):
            self.resultTable.setItem(i, 2, QTableWidgetItem(self.quineSolver.final_char_min_terms[i]))

        print(self.quineSolver.final_table_of_min_terms)

        for i in range(len(self.quineSolver.final_table_of_min_terms)):
            for j in range(len(self.quineSolver.final_table_of_min_terms[i])):
                self.finalTable.setRowCount(i + 1)
                self.finalTable.setColumnCount(j + 1)


        for i in range(len(self.quineSolver.final_table_of_min_terms)):
            for j in range(len(self.quineSolver.final_table_of_min_terms[i])):
                self.finalTable.setItem(i, j, QTableWidgetItem(self.quineSolver.final_table_of_min_terms[i][j]))


        self.editResultFunction.setText("F({0}) = {1}".format(', '.join([x.upper() for x in self.quineSolver.letters]), ''.join([x.upper() for x in self.quineSolver.translated_version])))

        self.disableAfterSolution()







    def disableAfterSolution(self):
        self.solveButton.setEnabled(False)
        self.editMinterm.setEnabled(False)
        self.editDCMinterm.setEnabled(False)
        self.addMintermButton.setEnabled(False)

    def enableAfterClearPressed(self):
        self.solveButton.setEnabled(False)
        self.editMinterm.setEnabled(True)
        self.editDCMinterm.setEnabled(True)


    def on_editMinterm_textChanged(self):
        if not self.editMinterm.text()=="":
            self.editDCMinterm.setEnabled(False)
        else:
            self.editDCMinterm.setEnabled(True)


        if self.editMinterm.text().isdigit():
            self.addMintermButton.setEnabled(True)
        else:
            self.addMintermButton.setEnabled(False)

        for i in range(len(self.min_term)):
            if (self.editMinterm.text() == str(self.min_term[i])):
                self.addMintermButton.setEnabled(False)

        for i in range(len(self.dc_term)):
            if (self.editMinterm.text() == str(self.dc_term[i])):
                self.addMintermButton.setEnabled(False)

    def on_editDCMinterm_textChanged(self):
        if not self.editDCMinterm.text()=="":
            self.editMinterm.setEnabled(False)
        else:
            self.editMinterm.setEnabled(True)

        if self.editDCMinterm.text().isdigit():
            self.addMintermButton.setEnabled(True)
        else:
            self.addMintermButton.setEnabled(False)

        for i in range(len(self.min_term)):
            if (self.editDCMinterm.text() == str(self.min_term[i])):
                self.addMintermButton.setEnabled(False)

        for i in range(len(self.dc_term)):
            if (self.editDCMinterm.text() == str(self.dc_term[i])):
                self.addMintermButton.setEnabled(False)



    def on_action_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("Quine McCluskey Usage Instructions\n\n"
                           "  \u2022 Step 1: Type the minterms in the input or DC(Don't care) input .\n"
                           "  \u2022 Step 2: Press 'Add Minterm' button to add the given minterm.\n"
                           "  \u2022 Step 3: Press 'Solve' button.\n\n"
                           "Note that if you want to clear the results you can press 'Clear' button."))











if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = QuineMcCluskey_GUI()
    ui.show()
    sys.exit(app.exec_())
