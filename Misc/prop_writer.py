''' 
    cli that takes properties from a user, then writes the @property getter and setter to a file to copy and paste. Gives the option to add self or not.
'''

import os
import io

props = []
BREAK_KEY = "-"
p_file = "props.txt"


def get_props():
    gathering_props = True
    while gathering_props:
        user_in = input("Enter a property name:  ")

        if user_in == BREAK_KEY:
            gathering_props = False
            break
        if user_in in props or user_in in (None, ""):
            continue
        if user_in == "x":
            exit()
        if user_in.find(",") != -1:
            for p in user_in.split(","):
                if confirm_add(p):
                    props.append(p)            
        else:
            if confirm_add(user_in):
                props.append(user_in)
    return True


def confirm_add(prop):
    if prop in props:
        return False
    if prop.isdigit() is True:
        return False
    else:
        print(f"{prop} added")
        return True


def confirm_print():
    for prop in props:
        print(prop)
    go = input("Press Enter to continue, any other keys will exit.")
    if go in ("",None):
        return True
    else:
        return False


def write_props():
    prop_get = ""
    prop_set = ""
    formed_list = []
    
    add_in = input("add \'self\' to properties?\n(\'y\' for yes)\t")

    if add_in == "y":
        for prop in props:
            prop_get = f"@property\ndef {prop}(self):\n\treturn self._{prop}"
            prop_set = f"@{prop}.setter\ndef {prop}(self, new{prop}):\n\tself._{prop} = new{prop}"
            formed_list.append(f"{prop_get}\n{prop_set}\n\n")

    if add_in != "y":
        for prop in props:
            prop_get = f"@property\ndef {prop}():\n\treturn _{prop}"
            prop_set = f"@{prop}.setter\ndef {prop}(new{prop}):\n\t_{prop} = new{prop}"
            formed_list.append(f"{prop_get}\n{prop_set}")


    with open(p_file, "w") as file:
        for fprop in formed_list:
            print(fprop)
            file.write(fprop)
        file.close()
    print("Done")


def run():
    if not get_props():
        return
    if not confirm_print():
        return
    write_props()
    input()


#####
if __name__ == "__main__":
    run()
