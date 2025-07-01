
import sys
import subprocess
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout,QWidget,QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from utils import session  # Assuming session.py is in the same directory
class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A S T O R")
        self.setGeometry(700, 320, 750, 650)
        self.setWindowIcon(QIcon("assets/SmallLogo.png"))
        self.setStyleSheet("background-color: white;") 


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.heading = QLabel("Enter Your Cedentials", self)
        
        self.username_text = QLabel("Username", self)
        self.login_email = QLineEdit()
        self.login_email.setPlaceholderText("username / email")
        

        self.password_text = QLabel("Password", self)
        self.login_pass = QLineEdit()
        self.login_pass.setPlaceholderText("password")

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.handle_login)
        

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.heading)
        main_layout.addWidget(self.username_text)
        main_layout.addWidget(self.login_email)
        main_layout.addWidget(self.password_text)
        main_layout.addWidget(self.login_pass)
        main_layout.addWidget(self.login_btn)
        main_layout.addStretch()


        central_widget.setLayout(main_layout)
        

    def handle_login(self):
        username = self.login_email.text()
        password = self.login_pass.text()

        # Replace this with real authentication logic
        if username == "1" and password == "1":
            session.saving_key()
            session.loading_key()
            session.session_token()
            session.WCM_upload()
            self.close()
            subprocess.run(["python", "gui/main_window.py"])  # Open main_window
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password")



       






def login_main():
    app = QApplication(sys.argv)
    window = login()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    login_main()