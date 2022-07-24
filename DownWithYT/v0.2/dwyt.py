import os
import sys
from pytube import YouTube, Playlist, Channel, Search

MagickChannel = "https://youtube.com/user/MindofMagick"

class DownWithYT:
    def __init__(self):
        self.results = []
        self.search = None
        self.urls = []
        self.suggestions = []


    def test_search(self):
        options = ["1: Search YouTube", "2: Show Results", "3: Get more results", "4: Show Suggestions", "5: Exit"]
        while True:
            for option in options:
                print(option)
            action = input("What will you do?")
            if action == "1":
                self.search_input()
            if action == "2":
                self.show_results()
            if action == "3":
                self.search_more()
                self.show_results()
            if action == "4":
                self.show_suggestions()
            if action == "5":
                break
        sys.exit()

#
#    SEARCHING
#
    def get_results(self):
        return self.results
    
    def show_results(self):
        for res in self.results:
            print(f"{str(self.results.index(res))}: {res.title}")

    def search_input(self):
        answer = input("What do you want to search for?\n")
        self.search_yt(answer)

    def show_suggestions(self):
        print("SUGGESTIONS")
        for sug in self.suggestions:
            num = self.suggestions.index(sug)
            print(f"{str(num)}: {sug}")
            print(type(sug))

    def search_yt(self, msg1):
        msg = msg1.replace(" ", "+")
        print(msg)
        self.search = Search(msg)
        self.results = self.search.results
        self.suggestions += self.search.completion_suggestions

    def search_more(self):
        self.results.clear()
        self.search.get_next_results()
        self.results = self.search.results

#
#    DOWNLOADING
#
    def download_audio(self, link):
        yt = YouTube(link)
        audio = yt.streams.get_audio_only()
        destination = "."
        try:
            out_file = audio.download(output_path=destination)
        except:
            err_link = f"::ERROR::\n{link}"
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        name = os.path.split(new_file)
        return True


    def download_video(self, link):
        yt = YouTube(link)
        video = yt.streams.first()
        destination = "."
        try:
            out_file = video.download(output_path=destination)
        except:
            err_link = f"::ERROR::\n{link}"
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        name = os.path.split(new_file)
        return True


if __name__ == "__main__":
    dwyt = DownWithYT()
    dwyt.test_search()