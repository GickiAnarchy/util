import os
import sys
import json
from pytube import YouTube, Channel, Search

MagickChannel = Channel("https://youtube.com/user/MindofMagick")

class DownWithYT:
    def __init__(self):
        self.results = []
        self.search = None
        self.urls = {}
        self.save_file = "./.saved.json"


#
#    SEARCHING
#
    def searchYT(self, inquiry):
        self.search = Search(inquiry)
        self.results = self.search.results

    def search_more(self):
        self.search.get_next_results()
        self.results += self.search.results

    @property
    def results(self):
        return self._results
    @results.setter
    def results(self, new_results):
        self._results = new_results


#
#    SAVE FILE
#
    def hasSavedFile(self):
        return os.path.exists(self.save_file)

    def saveFile(self):
        with open(self.save_file, "w+") as savefile:
            data = json.loads(self.urls)
            json.dump(data, savefile, indent = 2)
            print("save success")
            savefile.close()
        print("List saved to file.")

    def loadFile(self, clear = True):
        if not self.hasSavedFile():
            print("There is no save file present")
            return
        if clear:
            self.urls = {}
        with open(self.save_file, "r") as file:
            self.urls = json.load(file)
            file.close()
        print("file loaded to list")

#
#    URL DICTIONARY
#
    def addUrl(self, url: YouTube):
        t = url.title
        u = url.watch_url
        self.urls[t] = u
        print(f"{t} added to dictionary")

    def removeUrl(self, url: YouTube):
        if url.watch_url in self.urls.values():
            self.urls.popitem(url.title)
            print(f"{url.title} removed from urls dictionary")

    @property
    def urls(self):
        return self._urls
    @urls.setter
    def urls(self, new_urls):
        self._urls = new_urls

#
#    DOWNLOADING
#
    def addOAuth(self, yt: YouTube):
        return YouTube(yt.watch_url, use_oauth=True, allow_oauth_cache=True)

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

#    END
#
#

#
#    CLI
#

def ask_user(question):
    return input(question)


def run_cli():
    dyt = DownWithYT()
    print()
    look_for = input("Searching YouTube for.....?? ")
    if look_for in ("exit", "x"):
        return
    dyt.searchYT(look_for)
    while True:
        print()
        for r in dyt.results:
            print(f"{str(dyt.results.index(r))} | {r.title}")
        
        print()
        choose = input("Choose the number to select the video or press \'m\' to search more")
        if choose.isdigit():
            if int(choose) <= len(dyt.results):
                choice = dyt.results[int(choose)]
                print(f"{choice.title} was chosen\nPress \'1\' for Audio or \'2\' for Video")
                dl = input("::")
                if dl == "1":
                    dyt.download_audio(choice)
                if dl == "2":
                    dyt.download_video(choice)
        
        if choose == "m":
            dyt.search_more()
        
        if choose.lower() in ("x", "exit", "quit"):
            break



#    END
#
#
if __name__ == "__main__":
    print(f"{os.path.basename(__file__)} loaded")
    run_cli()