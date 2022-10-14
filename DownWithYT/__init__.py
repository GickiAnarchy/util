from pytube import YouTube, Search
import os


track_7 = "https://youtu.be/R44K3tUFh60"

#FA YouTube Manager
class YT:
    def __init__(self, url):
        if type(url) == YouTube:
            self.tube = url
        if type(url) == str:
            try:
                self.tube = YouTube(url)
            except Exception as e:
                print(f"ERROR:\n{e}")
                del self
        self.init2()

    def init2(self):
        yt: YouTube = self.tube
        self.title  = yt.title()
        self.url = yt.watch_url()
        self.id = yt.video_id
        self.author = yt.author()
        self.channel_url = yt.channel_url()
        self.channel_id = yt.channel_id()
        self.length = yt.length()
        self.description = yt.description()
        self.tags = yt.keywords()
        self.search = Search(self.title)
        self.related = []
        self.set_oauth()


#
#        OVERRIDES
    def __repr__(self):
        ret = f"{self.title}\n\t{self.url}"
        print(ret)
        return ret

#
#        METHODS
    def set_oauth(self, allow = True):
        self.tube.use_oauth=allow
        self.tube.allow_oauth_cache=allow

    def download_video(self, outdir = ".'"):
        '''    download video from yt url'    '''
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

    def get_related(self):
#        if self.search == None:
#            self.search = Search(self.title)
        if len(self.related) > 0:
            self.search.get_next_results()
        self.related = self.search.results()
        return self.related


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
    yt = YT(track_7)
