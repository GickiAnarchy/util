import os
from pytube import Playlist, YouTube


plist = Playlist("https://youtube.com/playlist?list=PLXS7fy2pHgKch6L4xtvybDqxo4tVWAoKK")

with open("magickurls.txt", "w") as urlfile:
    for s in plist.videos:
        urlfile.write(f"{s.watch_url}\n")
        print(f"{s.title} is done")
    urlfile.close()

exit()