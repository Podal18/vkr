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


from PyQt6 import QtWidgets
from db.db import get_connection

class ObjectWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ObjectWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.load_objects()
        self.setup_table()

    def setup_connections(self):
        """Подключение сигналов"""
        self.ui.search_button.clicked.connect(self.apply_filters)
        self.ui.search_input.textChanged.connect(self.apply_filters)
        self.ui.add_button.clicked.connect(self.add_object)
        self.ui.edit_button.clicked.connect(self.edit_object)
        self.ui.delete_button.clicked.connect(self.delete_object)
        self.ui.view_staff_button.clicked.connect(self.view_staff)

    def setup_table(self):
        """Настройка таблицы"""
        self.ui.object_table.setColumnWidth(0, 200)  # Название
        self.ui.object_table.setColumnWidth(1, 250)  # Адрес
        self.ui.object_table.setColumnWidth(2, 150)  # Прораб
        self.ui.object_table.setColumnWidth(3, 100)  # Сотрудники

    def load_objects(self):
        """Загрузка объектов из БД"""
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                    p.id,
                    p.name,
                    p.address,
                    u.login as foreman,
                    COUNT(a.id) as staff_count
                FROM projects p
                JOIN assignments a ON p.id = a.project_id
                JOIN employees e ON e.id = a.employee_id 
                JOIN users u ON e.created_by = u.id
                GROUP BY p.id, p.name, p.address, u.login
                """)
                self.all_objects = cursor.fetchall()
                self.apply_filters()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки: {str(e)}")
        finally:
            connection.close()

    def apply_filters(self):
        """Применение фильтров"""
        search_text = self.ui.search_input.text().lower()
        filtered = [obj for obj in self.all_objects
                   if search_text in obj["name"].lower()
                   or search_text in obj["address"].lower()]
        self.update_table(filtered)

    def update_table(self, objects):
        """Обновление таблицы"""
        self.ui.object_table.setRowCount(0)
        for row_idx, obj in enumerate(objects):
            self.ui.object_table.insertRow(row_idx)
            self.ui.object_table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(obj["name"]))
            self.ui.object_table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(obj["address"]))
            self.ui.object_table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(obj["foreman"] or "-"))
            self.ui.object_table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(obj["staff_count"])))

    # Заглушки для обработчиков
    def add_object(self):
        pass

    def edit_object(self):
        pass

    def delete_object(self):
        pass

    def view_staff(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ObjectWindow()
    window.show()
    sys.exit(app.exec())
