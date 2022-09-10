import os
from pytube import YouTube, Search, Playlist

#PYTUBE WRAPPER FOR KIVY GUI
#gui :kivy_main

#TODO
'''
    - Create a container to handle many aYouTube objects
    - Create func(poss class) outside of aYouTube class to pass playlists to aYT container
    
'''

T7 = "https://youtu.be/R44K3tUFh60"

class aYouTube():
    def __init__(self, yt = None):
        ''' aYT Initialization '''
        if type(yt) == YouTube:
            pass
        elif type(yt) == str:
            if yt.startswith("https"):
                self.YouTube = YouTube(yt)
        self.YouTube = yt
        
        self.title = ""
        self.url = ""
        self.thumbnail = None
        self.video_id = None
        self.length = None
        self.author = ""
        self.channel_url = ""
        self.channel_id = None
        self.views = 0
        self.desc = ""
        print(yt.isinstance())

        self.var_dict = {}
        self.var_list = [self.title,self.url,self.thumbnail,self.video_id,self.length,self.author,self.channel_url,self.channel_id,self.views,self.desc]


#    CLI Display
    def __dict__(self):
        if len(self.var_dict.keys()) <= 0:
            self.var_dict = {
                "title" : self.title,
                "url" : self.url,
                "thumbnail" : self.thumbnail,
                "video_id" : self.video_id,
                "length" : self.length,
                "author" : self.author,
                "channel_url" : self.channel_url,
                "channel_id" : self.channel_id,
                "views" : self.views,
                "desc" : self.desc}
        return self.var_dict


    def __repr__(self):
        return self.title


#    Adding YouTube
    def add_youtube(self, yt):
        yt = YouTube(yt)
        self.title = yt.title
        self.url = yt.watch_url
        self.thumbnail = yt.thumbnail_url
        self.video_id = yt.video_id
        self.length = yt.length
        self.author = yt.author
        self.channel_url = yt.channel_url
        self.channel_id = yt.channel_id
        self.views = yt.views
        self.desc = yt.description


#    Downloading and OAuth
    def set_oauth(self, allow=True):
        self.YouTube.use_oauth = True
        self.YouTube.allow_oauth_cache = allow



##    PROPERTIES    ##
    @property
    def YouTube(self):
    	return self._YouTube
    @YouTube.setter
    def YouTube(self, newYouTube):
    	self._YouTube = newYouTube

    @property
    def title(self):
    	return self._title
    @title.setter
    def title(self, newtitle):
    	self._title = newtitle
    
    @property
    def url(self):
    	return self._url
    @url.setter
    def url(self, newurl):
    	self._url = newurl
    
    @property
    def thumbnail(self):
    	return self._thumbnail
    @thumbnail.setter
    def thumbnail(self, newthumbnail):
    	self._thumbnail = newthumbnail
    
    @property
    def video_id(self):
    	return self._video_id
    @video_id.setter
    def video_id(self, newvideo_id):
    	self._video_id = newvideo_id
    
    @property
    def length(self):
    	return self._length
    @length.setter
    def length(self, newlength):
    	self._length = newlength
    
    @property
    def author(self):
    	return self._author
    @author.setter
    def author(self, newauthor):
    	self._author = newauthor
    
    @property
    def channel_url(self):
    	return self._channel_url
    @channel_url.setter
    def channel_url(self, newchannel_url):
    	self._channel_url = newchannel_url
    
    @property
    def channel_id(self):
    	return self._channel_id
    @channel_id.setter
    def channel_id(self, newchannel_id):
    	self._channel_id = newchannel_id
    
    @property
    def views(self):
    	return self._views
    @views.setter
    def views(self, newviews):
    	self._views = newviews
    
    @property
    def desc(self):
    	return self._desc
    @desc.setter
    def desc(self, newdesc):
    	self._desc = newdesc



#    DEBUG VARS & FUNCS
global fempty
fempty: aYouTube = aYouTube()
track7 = YouTube(T7)

def makeEmpty():
    fempty = aYouTube()

def fillEmpty(f: aYouTube = fempty):
    fempty = f.add_youtube(track7)

def showdebug():
    d = dict(fempty)
    for k in d.keys():
        v = d.get(k)
        print(f"{k}\t---\t{v}")
    
    
    




if __name__ == "__main__":
    fillEmpty()
    showdebug()

"""
    def download_video(self, outdir=".'"):
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
        exts = [".mp3", ".mp4"]
        for file in os.listdir(save_dir):
            base, name = os.path.split(file)
            if self.title in name:
                print(f"{self.title} matches {name}")
                return True
        return False
"""