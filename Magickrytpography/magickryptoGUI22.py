#
#    Misuse could cause irreversible file damage. Use with caution.
#
#    *For educational purposes 
#
from cryptography.fernet import Fernet
import PySimpleGUI as sg
from zipfile import ZipFile
import os
import pickle
import time


SIZE_LIMIT = (1024 * 1024 * 150)    #150MB
thisfile = os.path.basename(__file__)
keyfile = ".key.fa"


class Crypt:
    def __init__(self):
        self.target_dir = ""
        self.files = []

        self.key_present = False
        self.pk = PassKey()

        self.setupLayouts()



    def readFolder(self):
        self.files.clear()
        for root, directories, files in os.walk(self.target_dir):
            for filename in files:
                if filename == thisfile or filename == ".pk.fa":
                    continue
                if filename == keyfile:
                    self.key_present = True
                    continue
                filepath = os.path.join(root, filename)
                self.files.append(filepath)
        self.pk.filelist = self.files
        if self.key_present:
            self.deserializePk()

    def read_in_chunks(self, file, SIZE_LIMIT = SIZE_LIMIT):
        while True:
            data = file.read(SIZE_LIMIT)
            if not data:
                break
            yield data

    def Ncrip(self):
        self.savePK()
        for file in self.files:
            if file.endswith(".ncripped"):
                continue
            if os.path.getsize(file) <= SIZE_LIMIT:
                with open(file, "rb") as en_read:
                    content = en_read.read()
                    en_read.close()
                en_content = Fernet(self.pk.key).encrypt(content)
                with open(f"{file}.ncripped", "wb") as en_write:
                    en_write.write(en_content)
                    en_write.close()
            else:
                with open(file, "rb") as f:
                    i = 0
                    for chunk in self.read_in_chunks(f):
                        i += 1
                        en_content = Fernet(self.pk.key).encrypt(chunk)
                        with open(f"{file}.{str(i)}", "wb") as w:
                            w.write(en_content)
                            w.close()
                    f.close()

    def Dcrip(self):
        pass

    def savePK(self, serialize = True):
        self.pk.filelist = self.files
        self.pk.root = self.target_dir
        self.createPW()
        if self.pk.key == "":
            self.pk.key = Fernet.generate_key()
        if serialize:
            self.serializePk()
        else:
            self.pk.saveInfo()

    def createPW(self):
        input_pw = sg.popup_get_text("Enter a password:")
        if input_pw == None:
            return False
        if len(input_pw) < 6:
            sg.popup_auto_close("Password needs to be 6 or more characters", auto_close_duration = 3)
            return False
        self.pk.passkey = input_pw
        sg.popup_auto_close("Password updated!", auto_close_duration = 2)
        return True

    def deserializePk(self):
        with open(f"{self.target_dir}/.key.fa", "rb") as keyfile:
            self.pk = pickle.load(keyfile)

    def serializePk(self):
        with open(f"{self.target_dir}/.key.fa", "wb") as keyfile:
            pickle.dump(self.pk, keyfile)
            keyfile.close()

    def setupLayouts(self):
        self.col1 =[
            [sg.Button("Choose Directory", key = "-CHOOSE-")],
            [sg.Button("Encrypt", key = "-EBTN-", disabled = True)],
            [sg.Button("Decrypt", key = "-DBTN-", disabled = True)],
            [sg.Button("Save File List", key = "-SAVEFILES-")]
        ]
        self.col2 =[
            [sg.Checkbox("Key in target directory", disabled = True, key = "-HASKEY-")],
            [sg.Text("Number of files in target directory: "), sg.Text("", key = "-FILECOUNT-")]
        ]
        self.lo_main =[
            [sg.Text("MAGICKRYPTION")],
            [
                [sg.Column(layout = self.col1, element_justification = "Center"),
                sg.VSeperator(),
                sg.Column(layout = self.col2, element_justification = "Center")]
            ],
                [sg.StatusBar("", font="Helvetica 6", key = "-DIRECTORY-")],
                [sg.StatusBar("", font="Helvetica 10", key = "-CURSTAT-")]
        ]

    def mainWindow(self):
        self.readFolder()
        win_title = "Magickryption"
        self.main_window = sg.Window(win_title, layout = self.lo_main, element_justification = "Center", finalize = True)
        while True:
            event, values = self.main_window.read()
            
            if event in (None, "-EXIT-"):
                break

            if event == "-CHOOSE-":
                folder = sg.popup_get_folder("Choose the folde to encrypt: ")
                if folder == None:
                    folder = "."
                self.target_dir = folder
                self.readFolder()
                self.main_window["-DIRECTORY-"].update(f"{self.target_dir}")
                self.main_window["-FILECOUNT-"].update(f"{str(len(self.files))}")
                if self.key_present == True:
                    self.main_window["-DBTN-"].update(disabled = False)
                    self.main_window["-EBTN-"].update(disabled = True)
                elif self.key_present == False:
                    self.main_window["-EBTN-"].update(disabled = False)
                    self.main_window["-DBTN-"].update(disabled = True)

            if event == "-SAVEFILES-":
                self.savePK(serialize = False)
            
            if event == "-EBTN-":
                self.Ncrip()

    def run(self):
        self.mainWindow()


#    #    #    #    #    #    #    #
class PassKey():
    def __init__(self):
        self.key = ""
        self.passkey = ""
        self.root = ""
        self.filelist = []


    def saveInfo(self):
        if self.key == "" or len(self.filelist) == 0:
            return False
        with open(".pk.fa", "w") as saveinfo:
            saveinfo.write(f"{self.key}\n")
            for file in self.filelist:
                sz = str(os.path.getsize(file))
                saveinfo.write(f"{file} - {sz}\n")
            saveinfo.close()
        return True


    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, new_key):
        self._key = new_key

    @property
    def filelist(self):
        return self._filelist
    @filelist.setter
    def filelist(self, new_filelist):
        self._filelist = new_filelist

    @property
    def passkey(self):
        return self._passkey        
    @passkey.setter
    def passkey(self, new_passkey):
        self._passkey = new_passkey

    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, new_root):
        self._root = new_root



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

"""
def read_in_chunks(file_object, chunk_size=1024):
    #Lazy function (generator) to read a file piece by piece.
    #Default chunk size: 1k.
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

with open('really_big_file.dat') as f:
    for piece in read_in_chunks(f):
        process_data(piece)

"""