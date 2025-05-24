from PyQt6 import QtCore, QtWidgets
from logic.auto_func import authenticate_user
from ui.safety_main_window import Ui_SafetyMainWindow
from ui.foreman_main_window import Ui_ForemanMainWindow
from ui.admin_main_window import Ui_AdminMainWindow
from ui.hr_main_window import Ui_HRMainWindow


class Ui_login_widget(object):
    def setupUi(self, login_widget, parent_stack=None, parent_window=None):
        self.centralwidget = login_widget
        self.parent_stack = parent_stack
        self.parent_window = parent_window

        login_widget.setObjectName("login_widget")
        login_widget.resize(400, 500)
        login_widget.setWindowTitle("Авторизация")

        # Фон
        self.background = QtWidgets.QFrame(parent=login_widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff9a9e, stop:1 #fad0c4);
                border-radius: 0px;
            }
        """)

        self.label = QtWidgets.QLabel(parent=login_widget)
        self.label.setGeometry(QtCore.QRect(110, 40, 180, 50))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.login_email_input = QtWidgets.QLineEdit(parent=login_widget)
        self.login_email_input.setGeometry(QtCore.QRect(100, 150, 200, 45))
        self.login_email_input.setObjectName("login_email_input")

        self.login_password_input = QtWidgets.QLineEdit(parent=login_widget)
        self.login_password_input.setGeometry(QtCore.QRect(100, 210, 200, 45))
        self.login_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login_password_input.setObjectName("login_password_input")

        self.login_button = QtWidgets.QPushButton("Вход", parent=login_widget)
        self.login_button.setGeometry(QtCore.QRect(120, 280, 160, 50))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.try_login)

        self.to_register_button = QtWidgets.QPushButton("Нет аккаунта? Зарегистрируйтесь", parent=login_widget)
        self.to_register_button.setGeometry(QtCore.QRect(70, 350, 261, 41))
        self.to_register_button.setObjectName("to_register_button")
        self.to_register_button.clicked.connect(self.open_reg)

        self.forgot_password_button = QtWidgets.QPushButton("Забыли пароль?", parent=login_widget)
        self.forgot_password_button.setGeometry(QtCore.QRect(70, 390, 261, 41))
        self.forgot_password_button.setObjectName("forgot_password_button")
        self.forgot_password_button.clicked.connect(self.open_password_reset)

        self.exit_button = QtWidgets.QPushButton("✕", parent=login_widget)
        self.exit_button.setGeometry(QtCore.QRect(360, 10, 30, 30))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(QtWidgets.QApplication.quit)

        self.quit_button = QtWidgets.QPushButton("⏻", parent=login_widget)
        self.quit_button.setGeometry(QtCore.QRect(120, 440, 160, 40))
        self.quit_button.setObjectName("quit_button")
        self.quit_button.clicked.connect(QtWidgets.QApplication.quit)

        login_widget.setStyleSheet("""
            * {
                font-family: 'Segoe UI';
            }
            QLabel#label {
                font-size: 26px;
                font-weight: 600;
                color: white;
            }
            QLineEdit {
                border: 2px solid #ffb6c1;
                border-radius: 22px;
                background-color: white;
                padding: 10px;
                font-size: 15px;
            }
            QLineEdit:focus {
                border: 2px solid #ff6f61;
            }
            QPushButton {
                border-radius: 25px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #ff9a9e, stop:1 #fad0c4);
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #e55b50;
            }
            QPushButton#to_register_button,
            QPushButton#forgot_password_button {
                background: none;
                border: none;
                color: white;
                font-size: 14px;
                text-decoration: underline;
            }
            QPushButton#to_register_button:hover,
            QPushButton#forgot_password_button:hover {
                color: #ffe6e6;
            }
            QPushButton#exit_button {
                background: none;
                border: none;
                font-size: 18px;
                color: white;
            }
            QPushButton#exit_button:hover {
                color: #ffdddd;
            }
        """)

        self.retranslateUi(login_widget)
        QtCore.QMetaObject.connectSlotsByName(login_widget)

    def try_login(self):
        try:
            login = self.login_email_input.text().strip()
            password = self.login_password_input.text().strip()

            if not login or not password:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите логин и пароль.")
                return

            user = authenticate_user(login, password)
            if not user:
                QtWidgets.QMessageBox.critical(None, "Ошибка", "Неверный логин, пароль или пользователь заблокирован.")
                return

            self.open_main_window(user)

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Системная ошибка: {str(e)}")

    def open_main_window(self, user):
        try:
            self.main_window = QtWidgets.QMainWindow()
            role = user["role"]
            full_name = user["full_name"]
            user_id = user["id"]

            if role == "HR":
                ui = Ui_HRMainWindow()
            elif role == "Foreman":
                ui = Ui_ForemanMainWindow()
            elif role == "SafetyEngineer":
                ui = Ui_SafetyMainWindow()
            elif role == "Admin":
                ui = Ui_AdminMainWindow()
            else:
                QtWidgets.QMessageBox.warning(None, "Ошибка", f"Неизвестная роль: {role}")
                return

            ui.setupUi(self.main_window, full_name=full_name, user_id=user_id)
            self.main_window.show()
            self.centralwidget.parent().close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Системная ошибка: {str(e)}")

    def open_reg(self):
        if self.parent_stack and self.parent_window:
            self.parent_window.animate_to_index(1)

    def open_password_reset(self):
        if self.parent_stack and self.parent_window:
            self.parent_window.animate_to_index(2)

    def retranslateUi(self, login_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("login_widget", "Вход"))
        self.login_email_input.setPlaceholderText(_translate("login_widget", "Логин"))
        self.login_password_input.setPlaceholderText(_translate("login_widget", "Пароль"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_widget = QtWidgets.QWidget()
    ui = Ui_login_widget()
    ui.setupUi(login_widget)
    login_widget.show()
    sys.exit(app.exec())