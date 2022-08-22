import os
import json
from pytube import YouTube, Search


TRACK_7 = "https://youtu.be/R44K3tUFh60"


#FA YouTube Manager
class YT:
    ''' Class by FA to wrap pytubes YouTube module '''
    def __init__(self, url = ""):
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
        self.title  = yt.title
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


#
#        OVERRIDES
    def __repr__(self):
        ret = f"{self.title}\n\t{self.url}"
        return ret

#
#        METHODS
    def set_oauth(self, allow = True):
        '''Sets <use_oauth> and <allow_oauth_cache> to @param:allow (defaults to True)'''
        self.tube.use_oauth=allow
        self.tube.allow_oauth_cache=allow

    def download_video(self, outdir = ".'"):
        '''    download video from yt url    '''
        yt = self.tube
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        try:
            out_file = video.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        return True

    def download_audio(self, outdir = "."):
        '''    download audio from video    '''
        yt = self.tube
        if self.does_exist():
            return
        audio = yt.streams.get_audio_only()
        try:
            out_file = audio.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return True

    def does_exist(self, save_dir = "."):
        ''' Checks in directory for a file with the title + and ext '''
        exts = [".mp3", ".mp4"]
        for file in os.listdir(save_dir):
            base, name = os.path.split(file)
            if self.title in name:
                print(f"{self.title} matches {name}")
                return True
        return False

    def get_related(self):
        ''' returns the seach results '''
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
        ''' prints the search results '''
        for r in self.get_related():
            print(r.title)

    def get_dict(self):
        ''' returns a dict of variables '''
        fa_dict = {
                        "Title" : self.title,
                        "URL" : self.url,
                        "ID" : self.id,
                        "Author" : self.author,
                        "Channel URL" : self.channel_url,
                        "Channel ID" : self.channel_id,
                        "Length" : self.length,
                        "Description" : self.description,
                        "Keywords" : self.tags
                        }
        return fa_dict

    def show_dict(self):
        ''' prints the dictionary '''
        d = self.get_dict()
        data = json.dumps(d, indent = 2)
        print(data)

#
#        PROPERTIES
#    TUBE
    @property
    def tube(self):
        return self._tube
    @tube.setter
    def tube(self, new):
        self._tube = new
        self.init2()
#    TITLE
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new):
        self._title = new
#    URL
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, new):
        self._url = new
#    ID
    @property
    def id (self):
        return self._id 
    @id .setter
    def id (self, new):
        self._id  = new
#    AUTHOR
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, new):
        self._author = new
#    CHANNEL_URL
    @property
    def channel_url(self):
        return self._channel_url
    @channel_url.setter
    def channel_url(self, new):
        self._channel_url = new
#    CHANNEL_ID
    @property
    def channel_id(self):
        return self._channel_id
    @channel_id.setter
    def channel_id(self, new):
        self._channel_id = new
#    LENGTH
    @property
    def length(self):
        mins = ( self._length / 60)
        return mins
    @length.setter
    def length(self, new):
        self._length = new
#    DESCRIPTION
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, new):
        self._description = new
#    TAGS
    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, new):
        self._tags = new
#    RELATED
    @property
    def related(self):
        return self._related
    @related.setter
    def related(self, new):
        self._related = new

    @staticmethod
    def track7():
        return YT(TRACK_7)


#
#
#
if __name__ == "__main__":
    yt = YT(TRACK_7)
    yt.show_dict()
    input()
    yt.show_related()
    input()
    yt.show_related()
    input()
    yt.set_oauth(True)
    yt.download_audio()
    print(yt)     