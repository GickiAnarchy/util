import os, sys, json
from pytube import YouTube, Channel, Search

MagickChannel = Channel("https://youtube.com/user/MindofMagick")

class DownWithYT:
    def __init__(self):
        self.results = []
        self.search = None
        self.urls = []
        self.suggestions = []
        self.song = None
        self.save_file = "./.saved.json"
        self.save_list = {}    #Title, URL


#
#    SAVE FILE AND LIST
#
    def hasSavedFile(self):
        return os.path.exists(self.save_file)

    def saveFile(self):
        with open(self.save_file, "w+") as savefile:
            data = json.loads(self.save_list)
            json.dump(data, savefile, indent = 2)
            print("save success")
            savefile.close()
        print("List saved to file.")

    def loadFile(self, clear = True):
        if not self.hasSavedFile():
            print("There is no save file present")
            return
        if clear:
            self.save_list = {}
        with open(self.save_file, "r") as file:
            self.save_list = json.load(file)
            file.close()
        print("file loaded to list")

    def addToSave(self, song: YouTube):
        t = song.title
        u = song.watch_url
        self.save_list[t] = u
        print(f"{t} added to dictionary")

    def showList(self):
        for t, u in self.save_list.items():
            print(f"{t}:\n")
            print(f"\t{u}")


#
#    SEARCHING
#
    def search_input(self):
        answer = input("What do you want to search for?\n")
        self.search_yt(answer)

    def search_yt(self, msg):
        self.search = Search(msg)
        self.results = self.search.results

    def get_results(self):
        return self.results

    def show_results(self):
        if self.results == None:
            return False
        for res in self.results:
            print(f"{str(self.results.index(res))}: {res.title}")

    def search_more(self):
        self.search.get_next_results()
        self.results += self.search.results

#    BROKEN
    def show_suggestions(self):
        print("SUGGESTIONS") 
        self.suggestions = self.search.completion_suggestions
        for sug in self.suggestions:
            num = self.suggestions.index(sug)
            print(f"{str(num)}: {sug}")
            print(type(sug))

#
#    DOWNLOADING
#
    def download_audio(self, yt):
        audio = yt.streams.get_audio_only()
        destination = "."
        try:
            out_file = audio.download(output_path=destination)
        except:
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        name = os.path.split(new_file)
        return True

    def download_video(self, yt: YouTube):
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        destination = "."
        try:
            out_file = video.download(output_path=destination)
        except:
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        name = os.path.split(new_file)
        return True

#
#    CLI
#
    def _debug_show_results(self):
        for res in self.results:
            print(f"{str(self.results.index(res))}: {res.title}")
        poss = input("Select a song # to choose.\n")
        if poss.isdigit() and int(poss) <= len(self.results):
            song = self.results[int(poss)]
            self.song = YouTube(song.watch_url, use_oauth=True, allow_oauth_cache=True)
            AV = input("Press /'a/' for Audio or /'v/' for Video:\n\"add\" to add to save_list\n")
            if AV.lower() == "add":
                self.addToSave(self.song)
                return
            if AV.lower() == "a":
                good = self.download_audio(self.song)
                input()
            if AV.lower() == "v":
                good = self.download_video(self.song)
                input()
            if AV.lower() not in ("v", "a"):
                good = False
            if good:
                print(f"{self.song.title} downloaded")
            if not good:
                print(f"{self.song.title} failed during download")

    def _debug_main(self):
        options = ["1: Search YouTube", "2: Show Results", "3: Get more results", "4: Show Suggestions", "5: Change Directory", "6: Up a Directory", "0: Exit"]
        i = 0
        while True:
            if i == 1:
                os.system("clear")
                i = 0
            print(f"DOWN WITH YOUTUBE :: FatherAnarchy\t\t{os.getcwd()}")
            print(f"\n\tSave File Present?: {self.hasSavedFile()}")
            if self.hasSavedFile():
                print("\t\t Enter \"read\" or \"r\" to load the saved file.\n")
            for option in options:
                print(option)
            action = input("What will you do?\n")
            if action == "1":
                self.search_input()
                self._debug_show_results()
            if action == "2":
                if self.search != None:
                    self._debug_show_results()
            if action == "3":
                if self.search != None:
                    self.search_more()
                    self._debug_show_results()
            if action == "4":
                print("Suggestions are broken temporarily/")
            if action == "5":
                dir_list = []
                for item in os.listdir("."):
                    if os.path.isdir(item):
                        dir_list.append(item)
                print(f"Choose a directory:\n{os.getcwd()}/*****")
                for d in dir_list:
                    print(f"{dir_list.index(d)}: {d}")
                choice = input("Enter # of directory")
                if choice.isdigit():
                    if len(dir_list) >= int(choice):
                        os.chdir(dir_list[int(choice)])
            if action == "6":
                os.chdir("..")
            if action.lower() in ("r", "read") and self.hasSavedFile():
                self.loadFile()
                self.showList()
            if action == "0":
                break
            i += 1
        sys.exit()


#    END
#
#
if __name__ == "__main__":
    dwyt = DownWithYT()
    dwyt._debug_main()