import winreg

def toggle_theme():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        new_value = 0 if value == 1 else 1
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, new_value)
        winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, new_value)
        winreg.CloseKey(key)
        print(f"Theme switched to {'Dark' if new_value == 0 else 'Light'} Mode.")
    except Exception as e:
        print("Error:", e)

