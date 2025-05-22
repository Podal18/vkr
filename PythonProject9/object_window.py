from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ObjectWindow(object):
    def setupUi(self, ObjectWindow):
        ObjectWindow.setObjectName("ObjectWindow")
        ObjectWindow.resize(1000, 600)
        ObjectWindow.setWindowTitle("Объекты")
        ObjectWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        ObjectWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(ObjectWindow)
        ObjectWindow.setCentralWidget(self.centralwidget)

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(0, 0, 1000, 600)
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #a1c4fd, stop:1 #c2e9fb);
                border-radius: 10px;
            }
        """)

        # ✕ Кнопка
        self.exit_button = QtWidgets.QPushButton(parent=ObjectWindow)
        self.exit_button.setGeometry(QtCore.QRect(960, 10, 30, 30))
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
        self.exit_button.clicked.connect(ObjectWindow.close)

        # Заголовок
        self.title_label = QtWidgets.QLabel(self.background)
        self.title_label.setGeometry(30, 20, 600, 40)
        self.title_label.setText("Список объектов")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")

        # Панель фильтров
        self.filter_frame = QtWidgets.QFrame(self.background)
        self.filter_frame.setGeometry(30, 70, 940, 60)
        self.filter_frame.setStyleSheet("background-color: rgba(255,255,255,0.9); border-radius: 10px;")

        self.search_input = QtWidgets.QLineEdit(self.filter_frame)
        self.search_input.setPlaceholderText("Поиск по названию или адресу")
        self.search_input.setGeometry(20, 10, 250, 40)

        self.search_button = QtWidgets.QPushButton("🔍 Найти", self.filter_frame)
        self.search_button.setGeometry(290, 10, 100, 40)

        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #a1c4fd;
                color: white;
                border-radius: 20px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #7da2f2;
            }
        """)

        # Таблица объектов
        self.object_table = QtWidgets.QTableWidget(self.background)
        self.object_table.setGeometry(30, 150, 940, 330)
        self.object_table.setColumnCount(4)
        self.object_table.setHorizontalHeaderLabels(["Название", "Адрес", "Прораб", "Сотрудники"])
        self.object_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.object_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.object_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #b0d4ff;
                padding: 4px;
                font-weight: bold;
                border: 1px solid white;
            }
        """)

        # Кнопки
        self.add_button = QtWidgets.QPushButton("➕ Добавить", self.background)
        self.add_button.setGeometry(100, 500, 160, 50)

        self.edit_button = QtWidgets.QPushButton("✏️ Изменить", self.background)
        self.edit_button.setGeometry(290, 500, 160, 50)

        self.delete_button = QtWidgets.QPushButton("🗑️ Удалить", self.background)
        self.delete_button.setGeometry(480, 500, 160, 50)

        self.view_staff_button = QtWidgets.QPushButton("👷‍♂️ Сотрудники объекта", self.background)
        self.view_staff_button.setGeometry(670, 500, 200, 50)

        for btn in [self.add_button, self.edit_button, self.delete_button, self.view_staff_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #a1c4fd;
                    color: white;
                    border-radius: 20px;
                    font-size: 15px;
                }
                QPushButton:hover {
                    background-color: #7da2f2;
                }
            """)

        self.fade_animation(ObjectWindow)

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
    ui = Ui_ObjectWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
