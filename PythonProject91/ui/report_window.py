from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReportWindow(object):
    def setupUi(self, ReportWindow):
        ReportWindow.setObjectName("ReportWindow")
        ReportWindow.resize(1000, 600)
        ReportWindow.setWindowTitle("Отчёты")
        ReportWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        ReportWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(ReportWindow)
        ReportWindow.setCentralWidget(self.centralwidget)

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(0, 0, 1000, 600)
        self.background.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #fbc2eb, stop:1 #a6c1ee);
                border-radius: 10px;
            }
        """)

        # ✕ Кнопка
        self.exit_button = QtWidgets.QPushButton(parent=ReportWindow)
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
        self.exit_button.clicked.connect(ReportWindow.close)

        # ← Назад
        self.back_button = QtWidgets.QPushButton("←", self.background)
        self.back_button.setGeometry(30, 540, 60, 40)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #333;
                font-size: 14px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        self.back_button.clicked.connect(ReportWindow.close)

        # Заголовок
        self.title_label = QtWidgets.QLabel(self.background)
        self.title_label.setGeometry(30, 20, 600, 40)
        self.title_label.setText("Аналитика и отчёты")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")

        # Панель фильтров
        self.filter_frame = QtWidgets.QFrame(self.background)
        self.filter_frame.setGeometry(30, 70, 940, 60)
        self.filter_frame.setStyleSheet("background-color: rgba(255,255,255,0.9); border-radius: 10px;")

        self.report_type_combo = QtWidgets.QComboBox(self.filter_frame)
        self.report_type_combo.setGeometry(20, 10, 200, 40)
        self.report_type_combo.addItems([
            "Выберите тип отчёта", "По профессиям", "По объектам", "Истекающие документы", "Нарушения"
        ])

        self.period_combo = QtWidgets.QComboBox(self.filter_frame)
        self.period_combo.setGeometry(240, 10, 200, 40)
        self.period_combo.addItems(["Все даты", "За месяц", "За квартал", "За год"])

        self.generate_button = QtWidgets.QPushButton("📊 Построить", self.filter_frame)
        self.generate_button.setGeometry(460, 10, 140, 40)

        self.export_button = QtWidgets.QPushButton("⬇️ Экспорт", self.filter_frame)
        self.export_button.setGeometry(620, 10, 120, 40)

        for btn in [self.generate_button, self.export_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #a6c1ee;
                    color: white;
                    border-radius: 20px;
                    font-size: 15px;
                }
                QPushButton:hover {
                    background-color: #8aa8e3;
                }
            """)

        # Область отчёта (заглушка)
        self.report_area = QtWidgets.QFrame(self.background)
        self.report_area.setGeometry(30, 150, 940, 370)
        self.report_area.setStyleSheet("background-color: white; border-radius: 10px;")
        self.report_placeholder = QtWidgets.QLabel("Здесь будет отображаться отчёт...", self.report_area)
        self.report_placeholder.setGeometry(0, 0, 940, 370)
        self.report_placeholder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.report_placeholder.setStyleSheet("font-size: 16px; color: #888;")

        self.fade_animation(ReportWindow)

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
    ui = Ui_ReportWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
