import os
import pyfiglet as pyf


original = None
orig_2 = None

def add_figs(src):
    ln_count = 0
    if os.path.isfile(src):
        with open(src, "r") as read_src, open("figd_" + src, "w") as write_src:
            while True:
                line = read_src.readline()
                
                if not line:
                    break
                
                if "##fig" in line:
                    cmd = line[6:]
                    print(cmd)
                    fig = pyf.figlet_format(f"{cmd}", font = "Stampatello")
                    print(fig)
                    input()
                    write_src.write("\t'''\n")
                    write_src.writelines(fig)
                    write_src.write("\t'''\n")
                    continue
                write_src.write(line)
                print(str(ln_count))
                ln_count += 1

            read_src.close()
            write_src.close()
            print(".done.")

if __name__ == "__main__":
    add_figs("yt.py")
    '''
    fonts_dir = os.path.join(os.path.dirname(pyf.__file__), "fonts")
    fnts = os.listdir(fonts_dir)
    l = len(fnts)
    print(fnts)
    input()
    print(pyf.figlet_format("lildevil", font = "lildevil"))
    input()
    print(pyf.figlet_format("Nipples", font = "Nipples"))
    input()
    print(pyf.figlet_format("tanja", font = "tanja"))
    input()
    print(pyf.figlet_format("Stampatello", font = "Stampatello"))
    input()
    
#    for f in fnts:
#        print(str(l))
#        l -= 1
#        if f.startswith("."):
#            continue
#        if f.endswith(".py") or f.endswith(".flc"):
#            continue
#        print(f)
#        fnt, ext = os.path.splitext(f)
#        print(fnt)
#        fig = pyf.figlet_format(f"YouTube", font = "The Edge")
#        print(fig)
#        input()
eoz'''
