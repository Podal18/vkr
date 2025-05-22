from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from vhod import Ui_login_widget
from registration_window import Ui_registration_widget


class AuthWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_widget()
        self.ui.setupUi(self)
        self.ui.to_register_button.clicked.connect(self.reg)

    def reg(self):
        self.reg = Registration_window(self)
        self.reg.show()
        self.close()

class Registration_window(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_registration_widget()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.back)
        self.ex = ex

    def back(self):
        self.ex.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec())
