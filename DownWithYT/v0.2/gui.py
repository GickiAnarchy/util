''' GUI For v.0.2 '''

import PySimpleGUI as sg


menu = [["&File",["&New", "&Open", "&Save"]],
                ["About", ["Contact"]],
                ["Exit",["&Quit"]],]


layout = [[sg.Menu(menu)]]


window = sg.Window("DWYT", layout, finalize = True, size = (300, 300))


def run():
    while True:
        event, values = window.read()
        
        if event in ("Quit", sg.WINDOW_CLOSED):
            break

    window.close()


if __name__ == "__main__":
    run()