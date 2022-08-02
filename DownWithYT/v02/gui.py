''' GUI For v.0.2 '''
import PySimpleGUI as sg
from b64_images import *

menu = [["&File",["&New", "&Open", "&Save"]],
                ["About", ["Contact"]],
                ["Exit",["&Quit"]],]


layout = [[sg.Menu(menu)]]


window = sg.Window("Down with YouTube", layout, size = (768, 400), finalize = True)



if __name__ == "__main__":
    while True:
        event, values = window.read()
        
        if event in ("Quit", sg.WINDOW_CLOSED):
            break

    window.close()