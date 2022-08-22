import os
import json
from pytube import YouTube, Search


TRACK_7 = "https://youtu.be/R44K3tUFh60"


#FA YouTube Manager
class YT:
    ''' Class by FA to wrap pytubes YouTube module '''
    def __init__(self):
        self.tube = None
        self.filled = False

#
#        OVERRIDES
    def __repr__(self):
        ret = f"{self.title}\n\t{self.url}"
        return ret

#
#        METHODS
    def fill(self, yt):
        ''' Adds the song '''
        if type(yt) == str:
            try:
                self.tube = YouTube(yt)
            except Exception as e:
                print(e)
                return False
        elif type(yt) == YouTube:
            self.tube = yt
        else:
            return False
        self.title  = self.tube.title
        self.url = self.tube.watch_url
        self.id = self.tube.video_id
        self.author = self.tube.author
        self.channel_url = self.tube.channel_url
        self.channel_id = self.tube.channel_id
        self.length = self.tube.length
        self.description = self.tube.description
        self.tags = self.tube.keywords
        self.search = Search(self.title)
        self.related = []
        self.set_oauth()
        self.filled = True
        return True

    def set_oauth(self, allow = True):
        '''Sets <use_oauth> and <allow_oauth_cache> to @param:allow (defaults to True)'''
        self.tube.use_oauth=allow
        self.tube.allow_oauth_cache=allow

    def download_video(self, outdir = ".'"):
        '''    download video from  url    '''
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
        return self._length
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