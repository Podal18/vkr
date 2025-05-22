from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login_widget(object):
    def setupUi(self, login_widget):
        login_widget.setObjectName("login_widget")
        login_widget.resize(400, 500)
        login_widget.setWindowTitle("Авторизация")

        # Прозрачность и безрамочный стиль
        login_widget.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        login_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # Фон как градиентный прямоугольник (можно заменить на QFrame, если потребуется)
        self.background = QtWidgets.QFrame(parent=login_widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ff9a9e, stop:1 #fad0c4);
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

        self.login_button = QtWidgets.QPushButton(parent=login_widget)
        self.login_button.setGeometry(QtCore.QRect(120, 280, 160, 50))
        self.login_button.setObjectName("login_button")

        self.to_register_button = QtWidgets.QPushButton(parent=login_widget)
        self.to_register_button.setGeometry(QtCore.QRect(70, 350, 261, 41))
        self.to_register_button.setObjectName("to_register_button")

        self.exit_button = QtWidgets.QPushButton(parent=login_widget)
        self.exit_button.setGeometry(QtCore.QRect(360, 10, 30, 30))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("✕")
        self.exit_button.clicked.connect(login_widget.close)

        self.quit_button = QtWidgets.QPushButton("⏻", parent=login_widget)
        self.quit_button.setGeometry(QtCore.QRect(120, 420, 160, 40))
        self.quit_button.setObjectName("quit_button")
        self.quit_button.clicked.connect(QtWidgets.QApplication.quit)

        # Стиль
        login_widget.setStyleSheet("""
            * {
                font-family: 'Segoe UI';
            }
            QLabel#label {
                font-size: 26px;
                font-weight: 600;
                color: white;
                background: transparent;
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
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #ff9a9e, stop:1 #fad0c4);
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e55b50;
            }
            QPushButton#to_register_button {
                background: none;
                border: none;
                color: white;
                font-size: 14px;
                text-decoration: underline;
            }
            QPushButton#to_register_button:hover {
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
            
            QPushButton#quit_button {
                border-radius: 20px;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #ff9a9e, stop:1 #fad0c4);
                color: white;
                font-size: 16px;
            }
            QPushButton#quit_button:hover {
                background-color: #e55b50;
}


        """)

        self.retranslateUi(login_widget)
        QtCore.QMetaObject.connectSlotsByName(login_widget)

        # Плавное появление
        self.fade_animation(login_widget)

    def fade_animation(self, widget):
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(700)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def retranslateUi(self, login_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("login_widget", "Вход"))
        self.login_email_input.setPlaceholderText(_translate("login_widget", "Логин"))
        self.login_password_input.setPlaceholderText(_translate("login_widget", "Пароль"))
        self.login_button.setText(_translate("login_widget", "Вход"))
        self.to_register_button.setText(_translate("login_widget", "Нет аккаунта? Зарегистрируйтесь"))
        self.quit_button.setText(_translate("login_widget", "Выход"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_widget = QtWidgets.QWidget()
    ui = Ui_login_widget()
    ui.setupUi(login_widget)
    login_widget.show()
    sys.exit(app.exec())
