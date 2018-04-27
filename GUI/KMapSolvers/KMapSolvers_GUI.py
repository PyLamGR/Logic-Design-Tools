import sys

from .KMapSolvers import Ui_KMapSolvers
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

from Solvers.KMapSolver.KMapSolver import KMapSolver2, KMapSolver3, KMapSolver4


class KMapSolvers_GUI(QMainWindow, Ui_KMapSolvers):
    def __init__(self, parent=None):
        super(KMapSolvers_GUI, self).__init__(parent)

        self.setupUi(self)

        self.map_data = None
        self.all_vars = None
        self.KMapSolver = None

        self.connectButtons()
        self.howToUseKMapSolverButton.clicked.disconnect(self.changeValues)



    def connectButtons(self):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for member in members:
            memb = getattr(self, member)
            if isinstance(memb, QPushButton):
                memb.clicked.connect(self.changeValues)


    def changeValues(self):
        obj = self.sender()
        if isinstance(obj, QPushButton):
            obj_name = obj.objectName()

            if obj_name.startswith('buttonSolve'):
                karnaugh_type = (obj_name.replace('buttonSolve', ''))[0]
                self.solve(karnaugh_type)
            elif obj_name.startswith('clear'):
                self.clear(obj_name.replace('clear', ''), True)
            else:
                next_val = self.getValue(obj.text())
                obj.setText(next_val)
                if obj_name.startswith('but_'):
                    other_obj = 'KMap_'+obj_name.replace('but_', '')
                else:
                    other_obj = 'but_'+obj_name.replace('KMap_', '')
                other_obj = getattr(self, other_obj)
                if isinstance(other_obj, QPushButton):
                    other_obj.setText(next_val)

    def getValue(self, current_value):
        values = ['0', '1', 'X']
        index = values.index(current_value) + 1
        index = index if index < len(values) else 0
        return values[index]

    def valueToInt(self, current_value):
        values = ['0', '1', 'X']
        return values.index(current_value)

    def solve(self, size):
        size = int(size)
        if size == 2:
            self.solveKMap2()
        elif size == 3:
            self.solveKMap3()
        elif size == 4:
            self.solveKMap4()

    def solveKMap2(self):
        self.map_data = [
                         [self.valueToInt(self.but_2__0_0.text()), self.valueToInt(self.but_2__0_1.text())],
                         [self.valueToInt(self.but_2__1_0.text()), self.valueToInt(self.but_2__1_1.text())]
                        ]
        self.all_vars = 'A, B'
        self.KMapSolver = KMapSolver2
        self.result2VarsEditText.setText("F({0}) = {1}".format(self.all_vars, self.calc_result(2)))

    def solveKMap3(self):
        self.map_data = [
                         [self.valueToInt(self.but_3__0_0.text()), self.valueToInt(self.but_3__0_1.text()), self.valueToInt(self.but_3__0_2.text()), self.valueToInt(self.but_3__0_3.text())],
                         [self.valueToInt(self.but_3__1_0.text()), self.valueToInt(self.but_3__1_1.text()), self.valueToInt(self.but_3__1_2.text()), self.valueToInt(self.but_3__1_3.text())]
                        ]

        self.all_vars = 'A, B, C'
        self.KMapSolver = KMapSolver3
        self.result3VarsEditText.setText("F({0}) = {1}".format(self.all_vars, self.calc_result(3)))

    def solveKMap4(self):
        self.map_data = [
                         [self.valueToInt(self.but_4__0_0.text()), self.valueToInt(self.but_4__0_1.text()), self.valueToInt(self.but_4__0_2.text()), self.valueToInt(self.but_4__0_3.text())],
                         [self.valueToInt(self.but_4__1_0.text()), self.valueToInt(self.but_4__1_1.text()), self.valueToInt(self.but_4__1_2.text()), self.valueToInt(self.but_4__1_3.text())],
                         [self.valueToInt(self.but_4__2_0.text()), self.valueToInt(self.but_4__2_1.text()), self.valueToInt(self.but_4__2_2.text()), self.valueToInt(self.but_4__2_3.text())],
                         [self.valueToInt(self.but_4__3_0.text()), self.valueToInt(self.but_4__3_1.text()), self.valueToInt(self.but_4__3_2.text()), self.valueToInt(self.but_4__3_3.text())]
                        ]
        self.all_vars = 'A, B, C, D'
        self.KMapSolver = KMapSolver4
        self.result4VarsEditText.setText("F({0}) = {1}".format(self.all_vars, self.calc_result(4)))

    def calc_result(self, size):
        k = self.KMapSolver(self.map_data)
        k.solve()
        res = k.get_result()
        self.clear(size)
        if '1' in res:
            self.colorPATCH(size, k.result_group_set)
            res = '1'
        else:
            self.colorGroups(size, k.result_group_set)
        return res

    def clear(self, p_int, cleanText=False):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for member in members:
            memb = getattr(self, member)
            if isinstance(memb, QPushButton) and (memb.objectName().startswith('KMap_'+str(p_int)) or memb.objectName().startswith('but_'+str(p_int))):
                memb.setStyleSheet('')
                if cleanText:
                    memb.setText('0')
        if cleanText:
            getattr(self, 'result{0}VarsEditText'.format(p_int)).setText('')

    def colorGroups(self, size, group_set):
        colors = ['#B71C1C', '#9C27B0', '#3F51B5', '#00897B', '#4CAF50', '#CDDC39', '#FFEB3B', '#FF9800']
        overlap_colors = ['background: #FF4081;', 'background: #FF3D00;', 'background: #76FF03;']
        for g_set in group_set:
            for cords in g_set:
                attr = 'but_{0}__{1}_{2}'.format(size, cords[0], cords[1])
                btn = getattr(self, attr)
                if btn.styleSheet() == '':
                    btn.setStyleSheet('background: {0};'.format(colors[0]))
                    continue
                if btn.styleSheet() in overlap_colors:
                    btn.setStyleSheet(overlap_colors[overlap_colors.index(btn.styleSheet()) + 1])
                else:
                    btn.setStyleSheet(overlap_colors[0])
            colors.remove(colors[0])

    def colorPATCH(self, size, group_set):
        for g_set in group_set:
            for cords in g_set:
                attr = 'but_{0}__{1}_{2}'.format(size, cords[0], cords[1])
                btn = getattr(self, attr)
                btn.setStyleSheet('background: #B71C1C;')


    @QtCore.pyqtSlot()
    def on_howToUseKMapSolverButton_clicked(self):
        QMessageBox.about(self, "Usage Instructions", \
                          ("Karnaugh Maps Solver Usage Instructions\n\n"
                           "  \u2022 Step 1: Select the map variable size.\n"
                           "  \u2022 Step 2: Select the minterms either on the map or on the right side table.\n"
                           "  \u2022 Step 3: Press 'solve Map' button.\n"
                           "  \u2022 Step 4: If you want to clear the results press 'clear' button.\n\n"
                           "Note that the the colors indicate the grouped minterms"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = KMapSolvers_GUI()
    ui.show()
    sys.exit(app.exec_())