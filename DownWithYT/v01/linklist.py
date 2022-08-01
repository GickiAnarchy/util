import os
import time

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".", ".data"))

#
#
class LinkList:
    def __init__(self):
        self.current = []
        self.completed = {}


    @property
    def current(self):
        return self._current
    @current.setter
    def current(self,new_current):
        self._current = new_current

    def add_cur(self, link: str):
        if link.startswith("http"):
            x = link.replace("\n", "")
            link = x.rstrip(" ")
            if link in self.current:
                print("adding to current failed")
                return False
            self.current.append(link)
            print(f"{link} \nadded to current list")
            return True
    
    def genCurrent(self):
        for link in self.current:
            strLink = f"{link}"
            yield strLink

    def showCurrent(self):
        i = 0
        for link in self.genCurrent():
            i += 1 
            print(f"{i}: {link}")


    @property
    def completed(self):
        return self._completed
    @completed.setter
    def completed(self, new_comp):
        self._completed = new_comp

    def add_com(self, link, name):
        if link in self.completed.keys():
            print("adding to completed failed")
            return False
        else:
            if link in self.current:
                self.current.remove(link)
                print(f"{link} removed from current list")
            print(f"{name}\n\t{link} \nadded to completed list")
            self.completed[link] = name
            return True

    def genCompleted(self):
        for item in self.completed.items():
            yield item

    def showCompleted_Links(self):
        i = 0
        for item in self.genCompleted():
            i += 1
            print(f"{i}: {item[0]}")

    def showCompleted_Names(self):
        i = 0
        for item in self.genCompleted():
            i += 1
            print(f"{i}: {item[1]}")

    def completedLinks(self):
        links = []
        for item in self.genCompleted():
            links.append(item[0])
        return links

    def completedNames(self):
        names = []
        for item in self.genCompleted():
            names.append(item[1])
        return names

#
#    SAVE/LOAD
#
    def writeCompleted(self):
        with open(f"{data_dir}/completed.txt") as file:
            for item in self.genCompleted():
                link = item[0]
                name = item[1]
                s = f"{name}\n\t{link}"
                file.write(s)
            file.close()



def _Tests():
    print("TEST #1")
    time.sleep(2)
    LL = LinkList()
    LL.add_cur("All spaces     should be      removed  from the right side.. and shouldnt be added twice             ")
    LL.add_cur("All spaces     should be      removed  from the right side.. and shouldnt be added twice             ")
    LL.add_cur("The newline should \nbe removed as well")
    LL.showCurrent()
    del(LL)
    input("Press Enter To Contnue...")
    print("TEST #2")
    LL = LinkList()
    LL.add_cur("One")
    LL.add_cur("Two")
    LL.add_com("One", "NAME")
    LL.add_com("Two", "SECONDNAME")
    print(LL.completedLinks())
    print(LL.completedNames())
    input("Press Enter To Contnue...")
    os.system("clear")


if __name__ == "__main__":
    _Tests()