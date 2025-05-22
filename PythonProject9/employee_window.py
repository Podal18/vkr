from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(1000, 600)
        EmployeeWindow.setWindowTitle("Сотрудники")
        EmployeeWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        EmployeeWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(0, 0, 1000, 600)
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff9a9e, stop:1 #fad0c4);
                border-radius: 10px;
            }
        """)

        self.fire_button = QtWidgets.QPushButton("🟥 Уволить", self.background)
        self.fire_button.setGeometry(30, 500, 120, 50)
        self.fire_button.setStyleSheet("""
            QPushButton {
                background-color: #d9534f;
                color: white;
                border-radius: 20px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
        """)
        self.fire_button.clicked.connect(self.fire_employee)

        # ✕ Кнопка
        self.exit_button = QtWidgets.QPushButton(parent=EmployeeWindow)
        self.exit_button.setGeometry(QtCore.QRect(960, 10, 30, 30))
        self.exit_button.setObjectName("exit_button")
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
        self.exit_button.clicked.connect(EmployeeWindow.close)

        # Заголовок
        self.title_label = QtWidgets.QLabel(self.background)
        self.title_label.setGeometry(30, 20, 600, 40)
        self.title_label.setText("Список сотрудников")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")

        # Панель фильтров
        self.filter_frame = QtWidgets.QFrame(self.background)
        self.filter_frame.setGeometry(30, 70, 940, 60)
        self.filter_frame.setStyleSheet("background-color: rgba(255,255,255,0.9); border-radius: 10px;")

        self.search_input = QtWidgets.QLineEdit(self.filter_frame)
        self.search_input.setPlaceholderText("Поиск по ФИО / табельному номеру")
        self.search_input.setGeometry(20, 10, 250, 40)

        self.profession_filter = QtWidgets.QComboBox(self.filter_frame)
        self.profession_filter.setGeometry(290, 10, 180, 40)
        self.profession_filter.addItem("Все профессии")

        self.status_filter = QtWidgets.QComboBox(self.filter_frame)
        self.status_filter.setGeometry(490, 10, 180, 40)
        self.status_filter.addItems(["Все статусы", "Активен", "Уволен"])

        self.search_button = QtWidgets.QPushButton("🔍 Найти", self.filter_frame)
        self.search_button.setGeometry(690, 10, 100, 40)

        # Таблица сотрудников
        self.employee_table = QtWidgets.QTableWidget(self.background)
        self.employee_table.setGeometry(30, 150, 940, 330)
        self.employee_table.setColumnCount(6)
        self.employee_table.setHorizontalHeaderLabels(["ФИО", "Профессия", "Объект", "Статус", "Документы", "Действия"])
        self.employee_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.employee_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.employee_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #ffb6c1;
                padding: 4px;
                font-weight: bold;
                border: 1px solid white;
            }
        """)

        # Нижние кнопки
        self.add_button = QtWidgets.QPushButton("➕ Добавить", self.background)
        self.add_button.setGeometry(160, 500, 160, 50)

        self.edit_button = QtWidgets.QPushButton("✏️ Изменить", self.background)
        self.edit_button.setGeometry(360, 500, 160, 50)

        self.delete_button = QtWidgets.QPushButton("🗑️ Удалить", self.background)
        self.delete_button.setGeometry(560, 500, 160, 50)

        self.view_button = QtWidgets.QPushButton("📄 Профиль", self.background)
        self.view_button.setGeometry(760, 500, 160, 50)

        for btn in [self.add_button, self.edit_button, self.delete_button, self.view_button, self.search_button]:
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

        self.fade_animation(EmployeeWindow)

    def fade_animation(self, widget):
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(600)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def fire_employee(self):
        selected = self.employee_table.currentRow()
        if selected == -1:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Пожалуйста, выберите сотрудника.")
            return

        name_item = self.employee_table.item(selected, 0)  # ФИО
        status_item = self.employee_table.item(selected, 3)  # Статус

        if status_item.text() == "Уволен":
            QtWidgets.QMessageBox.information(None, "Уже уволен", f"{name_item.text()} уже уволен.")
            return

        reply = QtWidgets.QMessageBox.question(None, "Подтверждение",
                                               f"Вы действительно хотите уволить {name_item.text()}?",
                                               QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            # 🔧 Здесь должен быть SQL-запрос: UPDATE employees SET status='Уволен' WHERE id=...
            status_item.setText("Уволен")  # Обновим визуально (временно)
            QtWidgets.QMessageBox.information(None, "Успешно", f"{name_item.text()} уволен.")


# Пример запуска
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_EmployeeWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
