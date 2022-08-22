import os


props = ["yt", "title", "url", "id ", "author", "channel_url", "channel_id", "length", "description", "tags"]



def print_props():
    with open(fname, "w") as file:
        for p in props:
            file.write(f"#\t{p.upper()}\n")
            file.write(f"\t@property\n\tdef {p}(self):\n\'\'\'{p} Getter\'\'\'\n\t\treturn self._{p}\n\t@{p}.setter\n\tdef {p}(self, new):\n\'\'\'{p} Setter\'\'\'\n\t\tself._{p} = new\n\n\n")
        file.close()



if __name__ == "__main__":
    fname = input("Filename: ")
    if not fname.endswith(".txt"):
        fname = fname + ".txt"
    if not os.path.isfile(fname):
        with open(fname, "w") as f:
            f.close()
    print_props()
    