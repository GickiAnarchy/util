###
'''
A function to remove all tabs ("\t") and replacing them with 4 spaces.
    To help with PEP8 issues
'''
###

import os
import PySimpleGUI as sg

def fixfile():
    file = sg.popup_get_file("Fix what?")
    inputfile = open(file, "r")
    outfile = open(f"{file}.fix", "w")
    for line in inputfile:
        print(line)
        nline = line.replace("\t", "    ")
        outfile.write(nline)
        print(nline)
    inputfile.close()
    outfile.close()

if __name__ == "__main__":
    fixfile()