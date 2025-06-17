# Add this to your MainWindow class or create a new QWidget-based LoginWindow class

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QStackedWidget
from main_window import main
class LoginPanel(QWidget):
    def __init__(self, switch_to_main_callback):
        super().__init__()
        self.switch_to_main = switch_to_main_callback
        self.init_ui()
        self.main = main
    def init_ui(self):
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Login to ASTOR"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace this with real authentication logic
        if username == "admin" and password == "1234":
            self.switch_to_main()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password")


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASTOR Main App")
        self.resize(800, 600)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.show_login)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(QLabel("Welcome to ASTOR!"))
        self.main_layout.addWidget(self.logout_button)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def show_login(self):
        self.hide()
        self.parent().setCurrentIndex(0)


class AppController(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.login_panel = LoginPanel(self.show_main)
        self.main_app = MainApp()

        self.addWidget(self.login_panel)  # index 0
        self.addWidget(self.main_app)    # index 1

        self.setCurrentIndex(0)

    def show_main(self):
        self.setCurrentIndex(1)
        self.main_app.show()


def login_main():
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    controller = AppController()
    controller.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    login_main()
