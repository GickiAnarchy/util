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
                    cmd = line[-5:]
                    fig = pyf.figlet_format(f"{cmd}", font = "letters")
                    write_src.writelines(fig)
                    continue

                write_src.write(line)
                print(str(ln_count))
                ln_count += 1

            read_src.close()
            write_src.close()
            print(".done.")

