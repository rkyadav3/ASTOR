import json, uuid, keyring
import sys
from cryptography.fernet import Fernet
from gui import main_window as mw
from gui import loginUi


def startup():
    data = {
        "Login_Time" : 1
        }
    with open("login.json","w") as f:
        json.dump(data,f,indent=4)
        loginUi.login_main()             
def checking():

        try:
            with open("login.json","r") as f:
                login_time = json.load(f)["Login_Time"]
        except Exception as e:
            print("Session Timeout , Login Again", e)
            startup()
            return
        try:
            if login_time == 1:
                print("Checking Session Id")
                sessionID_verification()
            elif login_time != 1:
                print("Welcome")
                startup()
        except Exception as e:
            print("Session Timeout , Login Again", e)
        return


def saving_key():
    genkeY = Fernet.generate_key()
    with open("key.json", "w") as key:
        json.dump({"genkey": genkeY.decode()}, key, indent=4)

def loading_key():
    with open("key.json", "r") as key:
        return json.load(key)["genkey"].encode()

def session_token():
    session_token = str(uuid.uuid4())
    data = {"session_token": session_token}
    with open("session.json", "w") as f:
        json.dump(data, f, indent=4)

def WCM_upload():
    with open("session.json", "r") as f:
        session_token = json.load(f)["session_token"]
    key = loading_key()
    fernet = Fernet(key)
    encoded_key = fernet.encrypt(session_token.encode())
    keyring.set_password("ASTOR", "sessionID", encoded_key.decode())

def sessionID_verification():
    with open("session.json", "r") as f:
        mainSessionID = json.load(f)["session_token"]
    key = loading_key()
    fernet = Fernet(key)
    encoded_key = keyring.get_password("ASTOR", "sessionID")

    if encoded_key is None:
        print("No session found in credential manager.")
        return

    try:
        decrypted_session = fernet.decrypt(encoded_key.encode()).decode()
    except Exception as e:
        print("Failed to decrypt session:", e)
        startup()
        return

    if decrypted_session == mainSessionID:
        mw.main()
        print("Valid session!")
    else:
        print("Session mismatch (possible tampering).")

# Run flow
#saving_key()
#session_token()
#WCM_upload()
#sessionID_verification()
checking()