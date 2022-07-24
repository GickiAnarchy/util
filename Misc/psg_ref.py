import PySimpleGUI as sg


if __name__ == "__main__":
    font = sg.DEFAULT_FONT
    myfont = "Helvetica 14"
    sg.set_options(font = myfont, scaling = 0.65)
#    lo = [[sg.Multiline(f"{sg.set_options.__doc__}", k = "VARS", size = (100, 30))]]
#    win = sg.Window("VARS", lo, finalize = True)
#    while True:
#        event, values = win.read()

#        if event == sg.WIN_CLOSED:
#            break
#    win.close()
    sg.main().update()