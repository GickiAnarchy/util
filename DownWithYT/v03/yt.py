#!/usr/bin/env python3
import os
import json
from pytube import YouTube, Search

TRACK_7 = "https://youtu.be/R44K3tUFh60"


class YT:
    """Class by FA to wrap pytubes YouTube module"""

    def __init__(self, url=""):
        if type(url) == YouTube:
            self.tube = url
        if type(url) == str:
            if url == "":
                return
            try:
                self.tube = YouTube(url)
            except Exception as e:
                print(f"ERROR:\n{e}")
                del self
        self.init2()

    def init2(self):
        yt: YouTube = self.tube
        self.title = yt.title
        self.url = yt.watch_url
        self.id = yt.video_id
        self.author = yt.author
        self.channel_url = yt.channel_url
        self.channel_id = yt.channel_id
        self.length = yt.length
        self.description = yt.description
        self.tags = yt.keywords
        self.search = Search(self.title)
        self.related = []
        self.set_oauth()

    def __repr__(self):
        return f"{self.title}"

    def set_oauth(self, allow=True):
        """Sets <use_oauth> and <allow_oauth_cache> to @param:allow (defaults to True)"""
        self.tube.use_oauth = allow
        self.tube.allow_oauth_cache = allow

    def download_video(self, outdir=".'"):
        """download video from yt url"""
        yt = self.tube
        video = (
            yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
            .download()
        )
        try:
            out_file = video.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp4"
        os.rename(out_file, new_file)
        return True

    def download_audio(self, outdir="."):
        """download audio from video"""
        yt = self.tube
        if self.does_exist():
            return False
        audio = yt.streams.get_audio_only()
        try:
            out_file = audio.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        return True

    def does_exist(self, save_dir="."):
        """Checks in directory for a file with the title + and ext"""
        exts = [".mp3", ".mp4"]
        for file in os.listdir(save_dir):
            base, name = os.path.split(file)
            if self.title in name:
                print(f"{self.title} matches {name}")
                return True
        return False

    def get_related(self):
        """returns the seach results"""
        if len(self.related) != 0:
            self.search.get_next_results()
        self.related = self.search.results
        return self.related

    def related_titles(self):
        titles = []
        self.get_related()
        for y in self.related:
            titles.append(y.title)
        return titles

    def show_related(self):
        """prints the search results"""
        for r in self.get_related():
            print(r.title)

    def get_dict(self):
        """returns a dict of variables"""
        fa_dict = {
            "Title": self.title,
            "URL": self.url,
            "ID": self.id,
            "Author": self.author,
            "Channel URL": self.channel_url,
            "Channel ID": self.channel_id,
            "Length": self.length,
            "Description": self.description,
            "Keywords": self.tags,
        }
        return fa_dict

    def show_dict(self):
        """prints the dictionary"""
        data = json.dumps(self.get_dict(), indent=2)
        print(data)

    def write_file(self):
        """writes dict of video to json"""
        file = self.title + ".json"
        if os.path.isfile(file):
            return False
        with open(file, "w") as j:
            data = json.dumps(self.get_dict(), indent=2)
            j.write(data)
            j.close()
        return True

    def read_file(self):
        """reads dict of video from json"""
        file = self.title + ".json"
        if os.path.isfile(file):
            with open(file, "r") as j:
                infile = json.loads(j.read())
                infile = json.dumps(infile, indent=2)
                j.close()
        return infile

    def compare_json(self, infile=None):
        """compare json to YT dict"""
        if infile is None:
            infile = self.read_file()
        file = self.title + ".json"
        if infile == self.get_dict():
            return True
        if infile != self.get_dict():
            return False
        if not os.path.isfile(file):
            return False

    # GETTERS
    @property
    def tube(self):
        """the parent YouTube object"""
        return self._tube

    @property
    def title(self):
        """Title of the video"""
        return self._title

    @property
    def url(self):
        """watch url of video"""
        return self._url

    @property
    def id(self):
        """YouTube ID of video"""
        return self._id

    @property
    def author(self):
        """channel name of video"""
        return self._author

    @property
    def channel_url(self):
        """url of video authors channel"""
        return self._channel_url

    @property
    def channel_id(self):
        """YouTube ID of the channel"""
        return self._channel_id

    @property
    def length(self):
        """length of video --in ms/60--"""
        mins = self._length / 60
        return mins

    @property
    def description(self):
        """description of video"""
        return self._description

    @property
    def tags(self):
        """list of the tags/keywords for the video"""
        return self._tags

    @property
    def related(self):
        """list of Search(<video_title>) results"""
        return self._related

    # SETTERS
    @tube.setter
    def tube(self, new):
        self._tube = new
        self.init2()

    @title.setter
    def title(self, new):
        self._title = new

    @url.setter
    def url(self, new):
        self._url = new

    @id.setter
    def id(self, new):
        self._id = new

    @author.setter
    def author(self, new):
        self._author = new

    @channel_url.setter
    def channel_url(self, new):
        self._channel_url = new

    @channel_id.setter
    def channel_id(self, new):
        self._channel_id = new

    @length.setter
    def length(self, new):
        self._length = new

    @description.setter
    def description(self, new):
        self._description = new

    @tags.setter
    def tags(self, new):
        self._tags = new

    @related.setter
    def related(self, new):
        self._related = new

    @staticmethod
    def track7():
        """return YT instance with "Track 7b - Mind of Magick" video"""
        return YT(TRACK_7)
##########
##########
##########




###################################
def test_main():
    ''' function for testing ''' 
    yt = YT(TRACK_7)
    yt.show_dict()
    input()
    yt.show_related()
    input()
    yt.set_oauth(True)
    yt.download_audio()
    print(yt)
    if yt.read_file():
        print("json 100% matched")
    if not yt.read_file():
        print("json doesn't match")
    input()


###    EOF    ###
if __name__ == "__main__":
    pass
