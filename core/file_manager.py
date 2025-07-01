
from ast import Return
import os
from tkinter import BROWSE
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from  gui import main_window




def getApp(self,parent):
    self.file_path = QFileDialog.getOpenFileName(
        None, 
        "Select a file", 
        "", 
        "exe file (*.exe)"
    )

    if self.file_path:
        print(self.file_path)
        return self.LE_0LS.setText(self.file_path[0])


BROWSER_PATHS = {
    "Google Chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "Mozilla Firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "Microsoft Edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "Brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "Opera": r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera\launcher.exe"
}

def get_installed_browsers():
    installed = {}
    for name, path in BROWSER_PATHS.items():
        expanded = os.path.expandvars(path)
        if os.path.isfile(expanded):
            installed[name] = expanded
    return installed


 
