import sys, keyring
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
        self.setStyleSheet("""    border: none;
    background: transparent;
    margin: 10px 5px 10px 5px;
background-color: white;""") 

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
        self.H_Box_Layout.addSpacing(1)
        self.H_Box_Layout.addWidget(self.T_0RS)

        # LE_0LS = Line Edit Level 0 Left Side
        self.LE_0LS = QLineEdit()
        self.LE_0LS.setPlaceholderText("Enter app URL or file path...")
        self.LE_0LS.setStyleSheet("""
    QLineEdit {
        background-color: rgba(0, 0, 0, 0); /* LightBlue transparent */
        border: 2px solid #ADD8E6;                 /* LightBlue border */
        border-radius: 15px;                       /* Rounded corners */
        padding: 6px 6px;
  
        color: black;
        font-size: 14px;
    }

    QLineEdit:hover {
        background-color: rgba(0, 0, 0, 0);
    }

    QLineEdit:focus {
        border: 2px solid #5dade2;                 /* Slightly deeper blue on focus */
        background-color: rgba(0, 0, 0, 0);
    }
""")
      
        # BTN_0LS = Button Level 0 Left Side
        self.BTN_0LS = QPushButton("Browse")
        self.BTN_0LS.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)

        

        # CB_0RS = ComboBox Level 0 Right Side
        self.CB_0RS = QComboBox()
        self.CB_0RS.setEditable(True)
        self.CB_0RS.lineEdit().setReadOnly(True)
        self.CB_0RS.lineEdit().setPlaceholderText("Select Time & Date...")
        
        self.CB_0RS.setPlaceholderText("Select Time & Date...")
        self.CB_0RS.addItems(["At Startup", "Daily", "Custom Date & Time"])
        self.CB_0RS.currentIndexChanged.connect(self.CB_0RS_currentIndexChanged)
        self.CB_0RS.setStyleSheet("""
QComboBox {
    background-color: white; /* LightBlue transparent */
    border: 2px solid #ADD8E6;
    border-radius: 15px;
    padding: 6px 35px 6px 12px; /* Add space on right for arrow */
    color: black;
    font-size: 14px;
}




QComboBox::drop-down {
    border: none;
    background: transparent;
    width: 25px;
    subcontrol-origin: padding;
    subcontrol-position: center right;  /* Vertically center the arrow */
    margin-right: 5px;
}

QComboBox::down-arrow {
    image: url(assets/down-arrows.png);  /* Make sure image path is correct */
    width: 14px;
    height: 14px;
    margin: 0;
}

QComboBox QAbstractItemView {
    background-color: rgba(255, 255, 255, 240);
    border: 1px solid #ADD8E6;
    selection-background-color: #ADD8E6;
    selection-color: black;
    border-radius: 10px;
}
""")

        # Picker (DateTime Edit) for appSchedule
        self.picker_dt_appSchedule = QDateTimeEdit()
        self.picker_dt_appSchedule.setDisplayFormat("dd/MM/yyyy HH:mm:ss")
        self.picker_dt_appSchedule.setCalendarPopup(True)
        self.picker_dt_appSchedule.hide()
        self.picker_dt_appSchedule.setStyleSheet("""
    QDateTimeEdit {
        background-color: white; /* LightBlue, semi-transparent */
        border: 2px solid #ADD8E6;
        border-radius: 15px;
        padding: 6px 12px;
        color: #0F0F0F;
        font-size: 14px;
    }

    QDateTimeEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #ADD8E6;
    }

    QDateTimeEdit::down-arrow {
        image: url(calendar_icon.png);  /* Optional: Use your own calendar icon */
        width: 12px;
        height: 12px;
    }

    QDateTimeEdit:hover {
        background-color: white;
    }

    QDateTimeEdit:focus {
        border: 2px solid #4FC3F7;
    }
""")

        self.H_Box_Layout0 = QHBoxLayout()
        self.H_Box_Layout0.addWidget(self.LE_0LS)
        self.H_Box_Layout0.setSpacing(1)
        self.H_Box_Layout0.addWidget(self.BTN_0LS)
        self.H_Box_Layout0.setSpacing(2)
        self.H_Box_Layout0.addWidget(self.CB_0RS)
        # Picker (Time Edit) for appSchedule
        self.picker_t_appSchedule = QTimeEdit()
        self.picker_t_appSchedule.setDisplayFormat("HH:mm:ss")
        self.picker_t_appSchedule.hide()
        self.picker_t_appSchedule.setStyleSheet("""
QTimeEdit {
    background-color: rgba(173, 216, 230, 100);  /* LightBlue with transparency */
    border: 2px solid #ADD8E6;
    border-radius: 15px;
    padding: 6px 12px;
    color: black;
    font-size: 14px;
}

QTimeEdit::drop-down {
    background: transparent;
    subcontrol-origin: padding;
    subcontrol-position: center right;
    width: 30px;
    border-left: 1px solid #ADD8E6;
}

QTimeEdit::down-arrow {
    image: url(assets/down-arrows.png);  /* Customize this path to your arrow image */
    width: 18px;
    height: 12px;
    margin: 0px 0px 0px 0px;
}
""")


        # T_1M = Text (Level 1) Mid
        self.T_1M = QLabel("Enter Web Page Url, Select Browser & Time", self)
        self.T_1M.setFont(QFont("Arial", 11))
        self.T_1M.setStyleSheet("color: #292929; background-color: white;")


        # LE_1M = Line Edit Level 1 Mid
        self.LE_1M = QLineEdit()
        self.LE_1M.setPlaceholderText("Enter app URL or file path...")
        self.LE_1M.setStyleSheet("""
    QLineEdit {
        background-color: white; /* LightBlue transparent */
        border: 2px solid #ADD8E6;                 /* LightBlue border */
        border-radius: 15px;                       /* Rounded corners */
        padding: 6px 12px;
        color: black;
        font-size: 14px;
    }

    QLineEdit:hover {
        background-color: white);
    }

    QLineEdit:focus {
        border: 2px solid #5dade2;                 /* Slightly deeper blue on focus */
        background-color: white;
    }
""")

        # BTN_0LS = Button Level 1 Mid
        self.BTN_1M = QPushButton("Choose Browser (Defualt)")
        self.BTN_1M.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)


        # CB_0RS = ComboBox Level 1 Left Side
        self.CB_1LS = QComboBox()
        self.CB_1LS.setEditable(True)
        self.CB_1LS.lineEdit().setReadOnly(True)
        self.CB_1LS.lineEdit().setPlaceholderText("Select Time & Date...")
        self.CB_1LS.setPlaceholderText("Select Time & Date...")
        self.CB_1LS.addItems(["At Startup", "Daily", "Custom Date & Time"])
        self.CB_1LS.currentIndexChanged.connect(self.CB_1LS_currentIndexChanged)
        self.CB_1LS.setStyleSheet("""
QComboBox {
    background-color: rgba(0, 0, 0, 0); /* LightBlue transparent */
    border: 2px solid #ADD8E6;
    border-radius: 15px;
    padding: 6px 35px 6px 12px; /* Add space on right for arrow */
    color: black;
    font-size: 14px;
}

QComboBox:hover {
    background-color: rgba(0, 0, 0, 0);
}

QComboBox::drop-down {
    border: none;
    background: transparent;
    width: 25px;
    subcontrol-origin: padding;
    subcontrol-position: center right;  /* Vertically center the arrow */
    margin-right: 5px;
}

QComboBox::down-arrow {
    image: url(assets/down-arrows.png);  /* Make sure image path is correct */
    width: 14px;
    height: 14px;
    margin: 0;
}

QComboBox QAbstractItemView {
    background-color: rgba(255, 255, 255, 240);
    border: 1px solid ;
    selection-background-color: #ADD8E6;
    selection-color: black;
    border-radius: 10px;
}
""")


        # Picker (DateTime Edit) for webSchedule
        self.picker_dt_webSchedule = QDateTimeEdit()
        self.picker_dt_webSchedule.setDisplayFormat("dd/MM/yyyy HH:mm:ss")
        self.picker_dt_webSchedule.setCalendarPopup(True)
        self.picker_dt_webSchedule.hide()
        self.picker_dt_webSchedule.setStyleSheet("""
    QDateTimeEdit {
        background-color: white; /* LightBlue, semi-transparent */
        border: 2px solid #ADD8E6;
        border-radius: 15px;
        padding: 6px 12px;
        color: #0F0F0F;
        font-size: 14px;
    }

    QDateTimeEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #ADD8E6;
    }

    QDateTimeEdit::down-arrow {
        image: url(calendar_icon.png);  /* Optional: Use your own calendar icon */
        width: 12px;
        height: 12px;
    }

    QDateTimeEdit:hover {
        background-color: white;
    }

    QDateTimeEdit:focus {
        border: 2px solid #4FC3F7;
    }
""")
        
        # Picker (Time Edit) for webSchedule
        self.picker_t_webSchedule = QTimeEdit()
        self.picker_t_webSchedule.setDisplayFormat("HH:mm:ss")
        self.picker_t_webSchedule.hide()
        self.picker_t_webSchedule.setStyleSheet("""
QTimeEdit {
    background-color: rgba(173, 216, 230, 100);  /* LightBlue with transparency */
    border: 2px solid #ADD8E6;
    border-radius: 15px;
    padding: 6px 12px;
    color: black;
    font-size: 14px;
}

QTimeEdit::drop-down {
    background: transparent;
    subcontrol-origin: padding;
    subcontrol-position: center right;
    width: 30px;
    border-left: 1px solid #ADD8E6;
}

QTimeEdit::down-arrow {
    image: url(assets/down-arrows.png);  /* Customize this path to your arrow image */
    width: 18px;
    height: 12px;
    margin: 0px 0px 0px 0px;
}
""")


        # T_2LS = Text (Level 2) Left Side
        self.T_2LS = QLabel("Dark Mode & Light Mode", self)
        self.T_2LS.setFont(QFont("Arial", 11))
        self.T_2LS.setStyleSheet("color: #292929; background-color: white;")

        self.toggle_btn = QPushButton("Dark Mode")
        self.toggle_btn.setCheckable(True)  # Make it toggleable
        self.toggle_btn.clicked.connect(self.toggle_clicked)
        self.toggle_btn.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 3px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 16px 16px;                          /* Spacing */
                    margin : 8px 0px 8px 0px    }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)

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
        self.BTN_4LS.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)

        # LE_4RS = Line Edit Level 4 Rigth Side
        self.LE_4RS = QLineEdit()
        self.LE_4RS.setPlaceholderText("Choose Light Mode WallPaper")

        # BTN_4RS = Button Level 4 Right Side    
        self.BTN_4RS = QPushButton("Browse")
        self.BTN_4RS.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)

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
        self.T_5M.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)

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
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: rgba(173, 216, 230, 180); /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)
        self.to_do_btn.setCheckable(True) 

        self.logout_btn = QPushButton("Logout")
        self.logout_btn.setStyleSheet("""
             QPushButton {
                    background-color: rgba(173, 216, 230, 100); /* LightBlue with transparency */
                    color: #0F0F0F;                             /* Text color */
                    border: 2px solid #ADD8E6;                 /* LightBlue border */
                    border-radius: 15px;                       /* Rounded corners */
                    padding: 8px 16px;                         /* Spacing */
                        }
            QPushButton:hover {
                    background-color: #f44336; /* More visible on hover */
                    }
                    QPushButton:pressed {
                    background-color: rgba(173, 216, 230, 220); /* Almost solid when clicked */
                    }
                """)
        self.logout_btn.clicked.connect(self.logout)



        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.H_Box_Layout)
        main_layout.addLayout(self.H_Box_Layout0)
    
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
        main_layout.addWidget(self.logout_btn)
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
    def logout(self):
        """Handle the logout action."""
        # Here you can implement the logic to clear session data or perform any logout actions
        print("Logging out...")
        keyring.delete_password("ASTOR", "sessionID")
        self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
