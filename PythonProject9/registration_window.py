from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_registration_widget(object):
    def setupUi(self, registration_widget):
        registration_widget.setObjectName("registration_widget")
        registration_widget.resize(400, 600)
        registration_widget.setWindowTitle("Регистрация")

        registration_widget.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        registration_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # Фон
        self.background = QtWidgets.QFrame(parent=registration_widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ff9a9e, stop:1 #fad0c4);
            }
        """)

        # Заголовок
        self.label = QtWidgets.QLabel(parent=registration_widget)
        self.label.setGeometry(QtCore.QRect(80, 30, 240, 50))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setText("Регистрация")
        self.label.setObjectName("label")

        # Поле ФИО
        self.full_name_input = QtWidgets.QLineEdit(parent=registration_widget)
        self.full_name_input.setGeometry(QtCore.QRect(100, 100, 200, 45))
        self.full_name_input.setPlaceholderText("ФИО")

        # Логин
        self.login_input = QtWidgets.QLineEdit(parent=registration_widget)
        self.login_input.setGeometry(QtCore.QRect(100, 160, 200, 45))
        self.login_input.setPlaceholderText("Логин")

        # Пароль
        self.password_input = QtWidgets.QLineEdit(parent=registration_widget)
        self.password_input.setGeometry(QtCore.QRect(100, 220, 200, 45))
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Подтверждение пароля
        self.confirm_password_input = QtWidgets.QLineEdit(parent=registration_widget)
        self.confirm_password_input.setGeometry(QtCore.QRect(100, 280, 200, 45))
        self.confirm_password_input.setPlaceholderText("Подтвердите пароль")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Роль
        self.role_combo = QtWidgets.QComboBox(parent=registration_widget)
        self.role_combo.setGeometry(QtCore.QRect(100, 340, 200, 40))
        self.role_combo.addItems(["HR", "Foreman", "SafetyEngineer"])

        # Кнопка регистрации
        self.register_button = QtWidgets.QPushButton(parent=registration_widget)
        self.register_button.setGeometry(QtCore.QRect(120, 410, 200, 50))
        self.register_button.setText("Зарегистрироваться")

        self.exit_button = QtWidgets.QPushButton(parent=registration_widget)
        self.exit_button.setGeometry(QtCore.QRect(360, 10, 30, 30))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("✕")
        self.exit_button.clicked.connect(registration_widget.close)

        # Кнопка назад
        self.back_button = QtWidgets.QPushButton(parent=registration_widget)
        self.back_button.setGeometry(QtCore.QRect(120, 470, 200, 50))
        self.back_button.setText("Назад")

        # Стили
        registration_widget.setStyleSheet("""
        * {
            font-family: 'Segoe UI';
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
        QLabel#label {
            font-size: 26px;
            font-weight: 600;
            color: white;
            background: transparent;
        }
        QLineEdit, QComboBox {
            border: 2px solid #ffb6c1;
            border-radius: 20px;
            background-color: white;
            padding: 10px;
            font-size: 15px;
        }
        QLineEdit:focus, QComboBox:focus {
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
        QPushButton#back_button {
            background: none;
            border: none;
            font-size: 14px;
            text-decoration: underline;
        }
        QPushButton#back_button:hover {
            color: #ffe6e6;
        }
        """)

        self.fade_animation(registration_widget)

    def fade_animation(self, widget):
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(700)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration_widget = QtWidgets.QWidget()
    ui = Ui_registration_widget()
    ui.setupUi(registration_widget)
    registration_widget.show()
    sys.exit(app.exec())


