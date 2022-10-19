#
#    Misuse could cause irreversible file damage. Use with caution.
#
#    *For educational purposes 
#
from cryptography.fernet import Fernet
import PySimpleGUI as sg
import os
import pickle
import time


class Crypt:
    def __init__(self):
        self.files = []
        self.hasKey = False
        self.no_ncrip = 0    #number of encrypted files
        self.no_dcrip = 0    #number of decrypted files
        self.pk = PassKey()
        self.setupLayouts()
        self.no_files = 0


    def readFolder(self):
        self.files.clear()
        for file in os.listdir():
            if file == os.path.basename(__file__):
                continue
            if file == ".roo.pk":
                continue
            if file == ".key.fa":
                self.hasKey = True
                continue
            if os.path.isfile(file):
                if not file.endswith(".ncrippled"):
                    self.no_ncrip += 1
                elif file.endswith(".ncrippled"):
                    self.no_dcrip += 1
                self.files.append(file)
        self.no_files = len(self.files)
    
    def Ncrip(self):
        i = 1
        if self.pk.key == "":
            return
        for file in self.files:
            if file.endswith(".ncrippled"):
                continue
            with open(file, "rb") as thefile:
                contents = thefile.read()
                thefile.close()
            en_contents = Fernet(self.pk.key).encrypt(contents)
            time.sleep(.30)
            with open(file, "wb") as thefile:
                thefile.write(en_contents)
                thefile.close()
            os.rename(file, f".{file}.ncrippled")
        self.readFolder()

    def Dcrip(self):
        i = 1
        key = self.pk.key
        for file in self.files:
            time.sleep(.25)
            sg.one_line_progress_meter('Decrypting', i, self.no_files, f"{file}")
            i += 1
            if not file.endswith(".ncrippled"):
                continue
            with open(file, "rb") as thefile:
                contents = thefile.read()
                thefile.close()
            de_contents = Fernet(key).decrypt(contents)
            with open(file, "wb") as thefilew:
                thefilew.write(de_contents)
                thefilew.close()
            new_name = file[1:-10]
            os.rename(file, new_name)
        self.readFolder()

    def getPassKey(self):
        if not self.hasKey:
            self.pk.key = Fernet.generate_key()
            self.createpwWindow()
            self.serializePk()
        elif self.hasKey:
            self.deserializePk()

    def deserializePk(self):
        with open(".key.fa", "rb") as ff:
            pkey = pickle.load(ff)
            self.pk = pkey
            ff.close()

    def serializePk(self):
        if self.pk.isComplete:
            with open(".key.fa", "wb") as keyfile:
                pickle.dump(self.pk, keyfile)
                keyfile.close()
            with open(".roo.pk", "w") as tf:
                tf.write(f"{self.pk.key}\n")
                tf.close()

    def setupLayouts(self):
        self.lo_main = [
        [sg.Text(),sg.Text("What are you here for?")],
        [sg.Text("Enter Password:"), sg.Input(key = "-PASSKEY-", do_not_clear = False)],
        [sg.Button("Encrypt", key = "-NCRIP-"), sg.Button("Decrypt", key = "-DCRIP-"), sg.Button("Leave", key = "-EXIT-")],
        [sg.StatusBar(f"Targeted Directory is {os.getcwd()}", font="Helvetica 7")],
        [sg.StatusBar(f"Encrypted files: {str(self.no_ncrip)}\tNon-encrypted files: {str(self.no_dcrip)}", font="Helvetica 6")]
        ]
        self.lo_createpw = [
        [sg.Text("Passwords have to be atleast 6 characters long", font="Helvetica 6")],
        [sg.Text("Enter Passkey: "), sg.Input("", key = "-PASS1-")],
        [sg.Text("Verify Passkey: "), sg.Input("", key = "-PASS2-")],
        [sg.Button("Create", key = "-CREATEPW-")]
        ]

    def createpwWindow(self):
        cpw_win = sg.Window("Create a Password", layout = self.lo_createpw)
        next_win = False
        while True:
            event, values = cpw_win.read()        
            if event == "-CREATEPW-":
                if values["-PASS1-"] == "" or values["-PASS2-"] == "":
                    sg.popup("Can't leave passwords blank", keep_on_top = True)
                elif values["-PASS1-"] == "" or values["-PASS2-"] == "":
                    sg.popup("Can't leave passwords blank", keep_on_top = True)
                elif values["-PASS1-"] != values["-PASS2-"]:
                    sg.popup("Passwords do not match", keep_on_top = True)
                elif values["-PASS1-"] == values["-PASS2-"] and len(values["-PASS1-"]) >= 6:
                    next_win = True
                    self.pk.passkey = values["-PASS1-"]
                    break
            if event == None:
                break
        if not next_win:
            exit()
        else:
            cpw_win.close()

    def mainWindow(self):
        win_title = "Magickryption"
        self.main_window = sg.Window(win_title, layout = self.lo_main, element_justification = "Center")
        while True:
            event, values = self.main_window.read()            
            if event in (None, "-EXIT-"):
                break
            if event == "-NCRIP-":
                answer = sg.popup_yes_no(f"Are you sure you want to\nencrypt {str(self.no_ncrip)} files?")
                if answer == "Yes":
                    self.Ncrip()
            if event == "-DCRIP-":
                if values["-PASSKEY-"] == self.pk.passkey:
                    self.Dcrip()
                    os.remove(".key.fa")
                    os.remove(".roo.pk")
                    break
                else:
                    sg.popup("Password isn't correct", keep_on_top = True)
        self.main_window.close()
        
    def run(self):
        self.readFolder()
        self.getPassKey()
        self.mainWindow()


#    #    #    #    #    #    #    #
class PassKey():
    def __init__(self, key, passwd):
        self.key = key
        self.passkey = passwd
        self.isComplete = True
    def __init__(self):
        self.key = ""
        self.passkey = ""


    @property
    def isComplete(self):
        comp = False
        if self.key != "" and self.key != None and self.passkey != "" and self.passkey != None:
            comp = True
        return comp
 
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, new_key):
        self._key = new_key

    @property
    def passkey(self):
        return self._passkey        
    @passkey.setter
    def passkey(self, new_passkey):
        self._passkey = new_passkey


if __name__ == "__main__":
    ncrip = Crypt()
    ncrip.run()