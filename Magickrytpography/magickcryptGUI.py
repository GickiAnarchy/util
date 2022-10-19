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

SIZE_LIMIT = (1024 * 1024 * 100)    #100MB
thisfile = os.path.basename(__file__)

class Crypt:
    def __init__(self):
        self.files = []
        self.hasKey = False
        self.no_ncrip = 0    #number of decrypted files
        self.no_dcrip = 0    #number of encrypted files
        self.pk = PassKey()
        self.setupLayouts()
        self.dir = "."
        self.no_files = 0


    def readFolder(self):
        self.hasKey = False
        self.no_dcrip = 0
        self.no_ncrip = 0
        self.files.clear()
        for file in os.listdir(self.dir):
            if file == thisfile:
                continue
            if file == ".roo.pk":
                continue
            if file == ".key.fa":
                self.hasKey = True
                continue
            if os.path.isfile(f"{self.dir}/{file}"):
                if not file.endswith(".ncrippled"):
                    self.no_ncrip += 1
                elif file.endswith(".ncrippled"):
                    self.no_dcrip += 1
                self.files.append(file)
        self.no_files = len(self.files)
        self.getPassKey()
    
    def Ncrip(self):
        i = 1
        if self.pk.key == "":
            return
        for file in self.files:
            file_size = os.path.getsize(f"{self.dir}/{file}")
            time.sleep(.25)
            sg.one_line_progress_meter('Encrypting', i, self.no_files, f"{file}")
            i += 1
            if file.endswith(".ncrippled"):
                continue
            with open(f"{self.dir}/{file}", "rb") as thefile:
                contents = thefile.read()
                thefile.close()
            en_contents = Fernet(self.pk.key).encrypt(contents)
            time.sleep(.30)
            with open(f"{self.dir}/{file}", "wb") as thefile:
                thefile.write(en_contents)
                thefile.close()
            os.rename(f"{self.dir}/{file}", f"{self.dir}/.{file}.ncrippled")
        self.readFolder()

    def Dcrip(self):
        i = 1
        key = self.pk.key
        for file in self.files:
            file_size = os.path.getsize(f"{self.dir}/{file}")
            time.sleep(.25)
            sg.one_line_progress_meter('Decrypting', i, self.no_files, f"{file}")
            i += 1
            if not file.endswith(".ncrippled"):
                continue
            with open(f"{self.dir}/{file}", "rb") as thefile:
                contents = thefile.read()
                thefile.close()
            de_contents = Fernet(self.pk.key).decrypt(contents)
            with open(f"{self.dir}/{file}", "wb") as thefilew:
                thefilew.write(de_contents)
                thefilew.close()
            new_name = file[1:-10]
            os.rename(f"{self.dir}/{file}", f"{self.dir}/{new_name}")
        self.readFolder()

    def getPassKey(self):
        if not self.hasKey:
            self.pk.key = Fernet.generate_key()
            self.createpwWindow()
            self.serializePk()
        elif self.hasKey:
            self.deserializePk()

    def deserializePk(self):
        with open(f"{self.dir}/.key.fa", "rb") as ff:
            pkey = pickle.load(ff)
            self.pk = pkey
            ff.close()

    def serializePk(self):
        if self.pk.isComplete:
            with open(f"{self.dir}/.key.fa", "wb") as keyfile:
                pickle.dump(self.pk, keyfile)
                keyfile.close()
            with open(f"{self.dir}/.roo.pk", "w") as tf:
                tf.write(f"{self.pk.key}\n")
                tf.close()

    def writeTest(self):
        with open(thisfile, "rb") as rfile, \
            open(thisfile, "wb") as wfile:
                con = rfile.read()
                wfile.write(f"{con}\n{self.pk.key}")

    def setupLayouts(self):
        self.lo_main = [
        [sg.Text("What are you here for?")],
        [sg.Text("Enter Password:"), sg.Input(key = "-PASSKEY-", do_not_clear = False, password_char = "*")],
        [sg.Button("Encrypt", key = "-NCRIP-"), sg.Button("Decrypt", key = "-DCRIP-"), sg.Button("Leave", key = "-EXIT-"), sg.Button("Choose Folder", key = "-GETFOLDER-", disabled = False)],
        [sg.StatusBar(f"Targeted Directory is {os.getcwd()}", font="Helvetica 7", key = "-DIR-")],
        [sg.StatusBar(f"Encrypted files: {str(self.no_dcrip)}\tNon-encrypted files: {str(self.no_ncrip)}", font="Helvetica 6", key = "-STATUS-")]
        ]
        self.lo_createpw = [
        [sg.Text("Passwords have to be atleast 6 characters long", font="Helvetica 6")],
        [sg.Text("Enter Passkey: "), sg.Input("", key = "-PASS1-", password_char = "*")],
        [sg.Text("Verify Passkey: "), sg.Input("", key = "-PASS2-", password_char = "*" )],
        [sg.Button("Create", key = "-CREATEPW-")]
        ]

    def createpwWindow(self):
        cpw_win = sg.Window("Create a Password", layout = self.lo_createpw, element_justification = "Center")
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
        self.readFolder()
        win_title = "Magickryption"
        self.main_window = sg.Window(win_title, layout = self.lo_main, element_justification = "Center", finalize = True)
        self.main_window["-STATUS-"].update(f"Encrypted files: {str(self.no_dcrip)}\tNon-encrypted files: {str(self.no_ncrip)}")
        while True:
            event, values = self.main_window.read()
            if event in (None, "-EXIT-"):
                break
            if event == "-GETFOLDER-":
                folder = sg.popup_get_folder("Choose the folde to encrypt: ")
                self.dir = folder
                self.main_window["-DIR-"].update(f"{self.dir}")
                self.readFolder()
                self.main_window["-STATUS-"].update(f"Encrypted files: {str(self.no_dcrip)}\tNon-encrypted files: {str(self.no_ncrip)}")
            if event == "-NCRIP-":
                answer = sg.popup_yes_no(f"Are you sure you want to\nencrypt {str(self.no_ncrip)} files?")
                if answer == "Yes":
                    self.Ncrip()
                    self.main_window["-STATUS-"].update(f"Encrypted files: {str(self.no_dcrip)}\tNon-encrypted files: {str(self.no_ncrip)}")
            if event == "-DCRIP-":
                if values["-PASSKEY-"] == self.pk.passkey:
                    self.Dcrip()
                    os.remove(f"{self.dir}/.key.fa")
                    os.remove(f"{self.dir}/.roo.pk")
                    self.main_window["-STATUS-"].update(f"Encrypted files: {str(self.no_dcrip)}\tNon-encrypted files: {str(self.no_ncrip)}")
                    break
                else:
                    sg.popup("Password isn't correct", keep_on_top = True)
        self.main_window.close()
        
    def run(self):
        print(str(SIZE_LIMIT))
        self.mainWindow()


#    #    #    #    #    #    #    #
class PassKey():
    def __init__(self, key, passwd, folder):
        self.key = key
        self.passkey = passwd
        self.directory = folder
        self.isComplete = True
    def __init__(self):
        self.key = ""
        self.passkey = ""
        self.directory = ""


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

    @property
    def directory(self):
        return self._directory
    @directory.setter
    def directory(self, new_directory):
        self._directory = new_directory



if __name__ == "__main__":
    ncrip = Crypt()
    ncrip.run()


"""
def read_in_chunks(file_object, chunk_size=1024):
    #Lazy function (generator) to read a file piece by piece.
    #   Default chunk size: 1k.
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

with open('really_big_file.dat') as f:
    for piece in read_in_chunks(f):
        process_data(piece)

############

with open("source.txt", 'r') as src, \
  open("sink.txt", 'w') as sink:
  chunk_size = 1024 * 1024 # 1024 * 1024 byte = 1 mb
  while True:
    chunk = src.read(chunk_size)
    if not chunk:
      break
    sink.write(chunk)  
"""