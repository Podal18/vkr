from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_AddEditEmployeeWindow(object):
    def setupUi(self, AddEditEmployeeWindow, mode="add"):
        AddEditEmployeeWindow.setObjectName("AddEditEmployeeWindow")
        AddEditEmployeeWindow.resize(500, 450)
        AddEditEmployeeWindow.setWindowTitle("Добавить сотрудника" if mode == "add" else "Редактировать сотрудника")
        AddEditEmployeeWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        AddEditEmployeeWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(AddEditEmployeeWindow)
        AddEditEmployeeWindow.setCentralWidget(self.centralwidget)

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(0, 0, 500, 450)
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff9a9e, stop:1 #fad0c4);
                border-radius: 10px;
            }
        """)

        # ✕ кнопка
        self.exit_button = QtWidgets.QPushButton(parent=AddEditEmployeeWindow)
        self.exit_button.setGeometry(QtCore.QRect(460, 10, 30, 30))
        self.exit_button.setText("✕")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                font-size: 18px;
                color: white;
            }
            QPushButton:hover {
                color: #ffdddd;
            }
        """)
        self.exit_button.clicked.connect(AddEditEmployeeWindow.close)

        # Заголовок
        self.title_label = QtWidgets.QLabel(self.background)
        self.title_label.setGeometry(30, 20, 440, 40)
        self.title_label.setText("Добавить сотрудника" if mode == "add" else "Редактировать сотрудника")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: white;")

        # Поля
        self.fullname_input = self.create_input("ФИО", 90)

        self.birthdate_input = QtWidgets.QDateEdit(self.background)
        self.birthdate_input.setGeometry(50, 150, 400, 40)
        self.birthdate_input.setCalendarPopup(True)
        self.birthdate_input.setStyleSheet(self.input_style())

        self.profession_combo = QtWidgets.QComboBox(self.background)
        self.profession_combo.setGeometry(50, 210, 400, 40)
        self.profession_combo.addItems(["Электрик", "Слесарь", "Монтажник", "Инженер", "Мастер"])
        self.profession_combo.setStyleSheet(self.input_style())

        # Кнопки
        self.save_button = QtWidgets.QPushButton("💾 Сохранить", self.background)
        self.save_button.setGeometry(80, 320, 150, 50)

        self.cancel_button = QtWidgets.QPushButton("❌ Отмена", self.background)
        self.cancel_button.setGeometry(270, 320, 150, 50)

        for btn in [self.save_button, self.cancel_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ff9a9e;
                    color: white;
                    border-radius: 20px;
                    font-size: 15px;
                }
                QPushButton:hover {
                    background-color: #e55b50;
                }
            """)

        self.fade_animation(AddEditEmployeeWindow)

    def create_input(self, placeholder, y):
        input_field = QtWidgets.QLineEdit(self.background)
        input_field.setGeometry(50, y, 400, 40)
        input_field.setPlaceholderText(placeholder)
        input_field.setStyleSheet(self.input_style())
        return input_field

    def input_style(self):
        return """
            QLineEdit, QComboBox, QDateEdit {
                border: 2px solid #ffb6c1;
                border-radius: 20px;
                background-color: white;
                padding: 10px;
                font-size: 15px;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border: 2px solid #ff6f61;
            }
        """

    def fade_animation(self, widget):
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

# Пример запуска
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_AddEditEmployeeWindow()
    ui.setupUi(window, mode="add")
    window.show()
    sys.exit(app.exec())
