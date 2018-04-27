import sys
from PyQt5.QtWidgets import QApplication
from GUI.LDS.LDSMenu_GUI import LDSMenu_GUI



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LDSMenu_GUI()
    ui.show()
    sys.exit(app.exec_())