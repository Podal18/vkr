from PyQt6 import QtWidgets, QtCore
from ui.vhod import Ui_login_widget
from ui.registration_window import Ui_registration_widget
from ui.password_reset_window import Ui_PasswordResetWindow
import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 500)

        self.stack = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Авторизация
        self.login_widget = QtWidgets.QWidget()
        self.login_ui = Ui_login_widget()
        self.login_ui.setupUi(self.login_widget, parent_stack=self.stack, parent_window=self)
        self.stack.addWidget(self.login_widget)

        # Регистрация
        self.register_widget = QtWidgets.QWidget()
        self.register_ui = Ui_registration_widget()
        self.register_ui.setupUi(self.register_widget, parent_stack=self.stack, parent_window=self)
        self.stack.addWidget(self.register_widget)

        # Сброс пароля
        self.reset_widget = QtWidgets.QWidget()
        self.reset_ui = Ui_PasswordResetWindow()
        self.reset_ui.setupUi(self.reset_widget, parent_stack=self.stack, parent_window=self)
        self.stack.addWidget(self.reset_widget)

        self.stack.setCurrentIndex(0)

    def animate_to_index(self, target_index):
        current_widget = self.stack.currentWidget()
        next_widget = self.stack.widget(target_index)

        current_rect = self.stack.geometry()
        offset = current_rect.width()

        # Вычисляем направление
        direction = 1 if target_index > self.stack.currentIndex() else -1
        next_widget.setGeometry(current_rect.adjusted(direction * offset, 0, direction * offset, 0))
        next_widget.show()

        # Анимация текущего окна
        current_anim = QtCore.QPropertyAnimation(current_widget, b"geometry")
        current_anim.setDuration(300)
        current_anim.setStartValue(current_rect)
        current_anim.setEndValue(current_rect.adjusted(-direction * offset, 0, -direction * offset, 0))

        # Анимация нового окна
        next_anim = QtCore.QPropertyAnimation(next_widget, b"geometry")
        next_anim.setDuration(300)
        next_anim.setStartValue(next_widget.geometry())
        next_anim.setEndValue(current_rect)

        # Группа анимации
        self.anim_group = QtCore.QParallelAnimationGroup()
        self.anim_group.addAnimation(current_anim)
        self.anim_group.addAnimation(next_anim)
        self.anim_group.finished.connect(lambda: self.stack.setCurrentIndex(target_index))
        self.anim_group.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
