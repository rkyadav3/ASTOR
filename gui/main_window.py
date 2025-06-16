import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton,
    QComboBox, QDateTimeEdit, QTimeEdit, QCheckBox
)
from PyQt5.QtGui import QIcon, QFont




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A S T O R")
        self.setGeometry(700, 320, 750, 650)
        self.setWindowIcon(QIcon("assets/SmallLogo.png"))
        self.setStyleSheet("background-color: white;") 

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # T_0LS = Text (Level 0) Left Side
        self.T_0LS = QLabel("Choose App To Schedule", self)
        self.T_0LS.setFont(QFont("Arial", 11))
        self.T_0LS.setStyleSheet("color: #292929; background-color: white;")

        # T_0RS = Text (Level 0) Right Side
        self.T_0RS = QLabel("Choose Time", self)
        self.T_0RS.setFont(QFont("Arial", 11))
        self.T_0RS.setStyleSheet("color: #292929; background-color: white;")

        self.H_Box_Layout = QHBoxLayout()
        self.H_Box_Layout.addWidget(self.T_0LS)
        self.H_Box_Layout.addSpacing(1)
        self.H_Box_Layout.addWidget(self.T_0RS)

        # LE_0LS = Line Edit Level 0 Left Side
        self.LE_0LS = QLineEdit()
        self.LE_0LS.setPlaceholderText("Enter app URL or file path...")

        # BTN_0LS = Button Level 0 Left Side
        self.BTN_0LS = QPushButton("Browse")

        # CB_0RS = ComboBox Level 0 Right Side
        self.CB_0RS = QComboBox()
        self.CB_0RS.setPlaceholderText("Select Time & Date...")
        self.CB_0RS.addItems(["At Startup", "Daily", "Custom Date & Time"])
        self.CB_0RS.currentIndexChanged.connect(self.CB_0RS_currentIndexChanged)

        # Picker (DateTime Edit) for appSchedule
        self.picker_dt_appSchedule = QDateTimeEdit()
        self.picker_dt_appSchedule.setDisplayFormat("dd/MM/yyyy HH:mm:ss")
        self.picker_dt_appSchedule.setCalendarPopup(True)
        self.picker_dt_appSchedule.hide()
        
        # Picker (Time Edit) for appSchedule
        self.picker_t_appSchedule = QTimeEdit()
        self.picker_t_appSchedule.setDisplayFormat("HH:mm:ss")
        self.picker_t_appSchedule.hide()


        # T_1M = Text (Level 1) Mid
        self.T_1M = QLabel("Enter Web Page Url, Select Browser & Time", self)
        self.T_1M.setFont(QFont("Arial", 11))
        self.T_1M.setStyleSheet("color: #292929; background-color: white;")


        # LE_1M = Line Edit Level 1 Mid
        self.LE_1M = QLineEdit()
        self.LE_1M.setPlaceholderText("Enter app URL or file path...")

        # BTN_0LS = Button Level 1 Mid
        self.BTN_1M = QPushButton("Choose Browser (Defualt)")


        # CB_0RS = ComboBox Level 1 Left Side
        self.CB_1LS = QComboBox()
        self.CB_1LS.setPlaceholderText("Select Time & Date...")
        self.CB_1LS.addItems(["At Startup", "Daily", "Custom Date & Time"])
        self.CB_1LS.currentIndexChanged.connect(self.CB_1LS_currentIndexChanged)


        # Picker (DateTime Edit) for webSchedule
        self.picker_dt_webSchedule = QDateTimeEdit()
        self.picker_dt_webSchedule.setDisplayFormat("dd/MM/yyyy HH:mm:ss")
        self.picker_dt_webSchedule.setCalendarPopup(True)
        self.picker_dt_webSchedule.hide()
        
        # Picker (Time Edit) for webSchedule
        self.picker_t_webSchedule = QTimeEdit()
        self.picker_t_webSchedule.setDisplayFormat("HH:mm:ss")
        self.picker_t_webSchedule.hide()


        # T_2LS = Text (Level 2) Left Side
        self.T_2LS = QLabel("Dark Mode & Light Mode", self)
        self.T_2LS.setFont(QFont("Arial", 11))
        self.T_2LS.setStyleSheet("color: #292929; background-color: white;")

        self.toggle_btn = QPushButton("Dark Mode")
        self.toggle_btn.setCheckable(True)  # Make it toggleable
        self.toggle_btn.clicked.connect(self.toggle_clicked)

        self.H_Box_Layout2 = QHBoxLayout()
        self.H_Box_Layout2.addWidget(self.T_2LS)
        self.H_Box_Layout2.addSpacing(1)
        self.H_Box_Layout2.addWidget(self.toggle_btn)


        # T_3M = Text (Level 3) Mid
        self.T_3M = QLabel("Do You Want to Change Wallpaper With Mode Switching?", self)
        self.T_3M.setFont(QFont("Arial", 11))
        self.T_3M.setStyleSheet("color: #292929; background-color: white;")

        # Checkbox for enabling Changing Wallpaper while Changing Mode
        self.checkbox = QCheckBox("Yes")
        self.checkbox.stateChanged.connect(self.toggle_option)
        
       
        self.H_Box_Layout3 = QHBoxLayout()
        self.H_Box_Layout3.addWidget(self.T_3M)
        self.H_Box_Layout3.addSpacing(1)
        self.H_Box_Layout3.addWidget(self.checkbox)


        # T_4LS = Text (Level 4) Left Side
        self.T_4LS = QLabel("Dark Mode WallPaper", self)
        self.T_4LS.setFont(QFont("Arial", 11))
        self.T_4LS.setStyleSheet("color: #292929; background-color: white;")

        # T_4RS = Text (Level 4) Right Side
        self.T_4RS = QLabel("Light Mode WallPaper", self)
        self.T_4RS.setFont(QFont("Arial", 11))
        self.T_4RS.setStyleSheet("color: #292929; background-color: white;")

        self.H_Box_Layout4 = QHBoxLayout()
        self.H_Box_Layout4.addWidget(self.T_4LS)
        self.H_Box_Layout4.addSpacing(1)
        self.H_Box_Layout4.addWidget(self.T_4RS)
        


        
        # LE_4LS = Line Edit Level 4 Left Side
        self.LE_4LS = QLineEdit()
        self.LE_4LS.setPlaceholderText("Choose Dark Mode WallPaper")

        # BTN_4LS = Button Level 4 left Side    
        self.BTN_4LS = QPushButton("Browse")

        # LE_4RS = Line Edit Level 4 Rigth Side
        self.LE_4RS = QLineEdit()
        self.LE_4RS.setPlaceholderText("Choose Light Mode WallPaper")

        # BTN_4RS = Button Level 4 Right Side    
        self.BTN_4RS = QPushButton("Browse")

        self.H_Box_Layout5 = QHBoxLayout()
        self.H_Box_Layout5.addWidget(self.LE_4LS)
        self.H_Box_Layout5.addWidget(self.BTN_4LS)
        self.H_Box_Layout5.addSpacing(1)
        self.H_Box_Layout5.addWidget(self.LE_4RS)
        self.H_Box_Layout5.addWidget(self.BTN_4RS)

        
        self.T_4LS.hide()
        self.T_4RS.hide()
        self.LE_4LS.hide()
        self.LE_4RS.hide()
        self.BTN_4LS.hide()
        self.BTN_4RS.hide()

        # Show To-do list on desktop btn
        self.todo_toggle_btn = QCheckBox()
        self.todo_toggle_btn.setCheckable(True)  # Make it toggleable

        # T_5M = Text (Level 5) Mid
        self.T_5M = QLabel("Do You Want to Display To-Do List Widgit?", self)
        self.T_5M.setFont(QFont("Arial", 11))
        self.T_5M.setStyleSheet("color: #292929; background-color: white;")

        self.H_Box_Layout6 = QHBoxLayout()
        self.H_Box_Layout6.addWidget(self.T_5M)
        self.H_Box_Layout6.addSpacing(1)
        self.H_Box_Layout6.addWidget(self.todo_toggle_btn)


        # To-Do List Button
        self.to_do_btn = QPushButton()
        self.to_do_btn.setText("T\n\n\nO\n\n\n-\n\nD\n\n\nO\n\n\nL\n\n\nI\n\n\nS\n\n\nT")
        self.to_do_btn.setMinimumWidth(40)
        self.to_do_btn.setMinimumHeight(500)
        self.to_do_btn.setStyleSheet("""
            QPushButton {
                font-size: 12px;
                background-color: #e0e0e0;
                border: none;
                padding: 4px;
            }
            QPushButton:checked {
                background-color: #4caf50;
                color: white;
            }
        """)
        self.to_do_btn.setCheckable(True) 





        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.H_Box_Layout)
        main_layout.addWidget(self.LE_0LS)
        main_layout.addWidget(self.BTN_0LS)
        main_layout.addWidget(self.CB_0RS)
        main_layout.addWidget(self.picker_dt_appSchedule)
        main_layout.addWidget(self.picker_t_appSchedule)
        main_layout.addWidget(self.T_1M)
        main_layout.addWidget(self.LE_1M)
        main_layout.addWidget(self.BTN_1M)
        main_layout.addWidget(self.CB_1LS)
        main_layout.addWidget(self.picker_dt_webSchedule)
        main_layout.addWidget(self.picker_t_webSchedule)
        main_layout.addLayout(self.H_Box_Layout2)
        main_layout.addLayout(self.H_Box_Layout3)
        main_layout.addLayout(self.H_Box_Layout4)
        main_layout.addLayout(self.H_Box_Layout5)
        main_layout.addLayout(self.H_Box_Layout6)
        main_layout.addStretch()


        self.H_Box_Layout_main = QHBoxLayout()
        self.H_Box_Layout_main.addLayout(main_layout)
        self.H_Box_Layout_main.addSpacing(1)
        self.H_Box_Layout_main.addWidget(self.to_do_btn)


        super_layout = self.H_Box_Layout_main

        central_widget.setLayout(super_layout)

    def CB_0RS_currentIndexChanged(self, index):
        selected_option = self.CB_0RS.itemText(index)
        if selected_option == "At Startup":
            self.picker_dt_appSchedule.hide()
            self.picker_t_appSchedule.hide()
        elif selected_option == "Daily":
            self.picker_dt_appSchedule.hide()
            self.picker_t_appSchedule.show()
        elif selected_option == "Custom Date & Time":
            self.picker_dt_appSchedule.show()
            self.picker_t_appSchedule.hide()

    def CB_1LS_currentIndexChanged(self, index):
         """Handle the change in the ComboBox selection for the Web schedule."""
         selected_option = self.CB_1LS.itemText(index)
         if selected_option == "At Startup":
            self.picker_dt_webSchedule.hide()
            self.picker_t_webSchedule.hide()
         elif selected_option == "Daily":
            self.picker_dt_webSchedule.hide()
            self.picker_t_webSchedule.show()
         elif selected_option == "Custom Date & Time":
            self.picker_dt_webSchedule.show()
            self.picker_t_webSchedule.hide()

    def toggle_clicked(self):
        if self.toggle_btn.isChecked():
            self.toggle_btn.setText("Light Mode")
            self.setStyleSheet("background-color: black; color: white;")
        else:
            self.toggle_btn.setText("Dark Mode")
            self.setStyleSheet("background-color: white; color: black;")

    def toggle_option(self, state):
        if state == 2:  # Checked
            print("Ticked ✅")
            self.T_4LS.show()
            self.T_4RS.show()
            self.LE_4LS.show()
            self.LE_4RS.show()
            self.BTN_4LS.show()
            self.BTN_4RS.show()
        else:  # Unchecked
            print("Unticked ❌")
            self.T_4LS.hide()
            self.T_4RS.hide()
            self.LE_4LS.hide()
            self.LE_4RS.hide()
            self.BTN_4LS.hide()
            self.BTN_4RS.hide()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
