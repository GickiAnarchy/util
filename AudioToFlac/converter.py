# Audio Converter to .flac
#author: FatherAnarchy
from pydub import AudioSegment
import ffmpeg
import os


class ConvertToFlac:
    def __init__(self):
        pass

    @staticmethod
    def convertWav(audio):
        if audio.endswith(".wav"):
            print("convertWav needs to be in wav format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"{base[0]}.flac", format = "flac")
        print(f"{song} exported")

    @staticmethod
    def convertMp3(audio):
        if not audio.endswith(".mp3"):
            print("convertMp3 needs to be in mp3 format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"{base[0]}.flac", format = "flac")
        print(f"{song} exported")

#
#

exts = [".mp3", ".wav"]

def run():
    converter = ConvertToFlac()
    f_path = os.getcwd()
    
    print("CONVERT TO FLAC")
    print("————————————————")
    files = os.listdir(f_path)
    while True:
        i = 0
        for f in files:
            base, ext = os.path.splitext(f)
            if ext not in exts:
                continue
            print(f"{str(i)}: {base}{ext}")
            i += 1
        choice = input("Enter the file you want to convert:\n")
        if choice == "cd":
            print(f"Current Directory:\n{f_path}")
            new_dir = input("Where do you want to look?\n")
            if os.path.isdir(new_dir):
                os.chdir(new_dir)
                f_path = os.getcwd()
                files = os.listdir(f_path)
            elif not os.path.isdir(new_dir):
                print(f"{new_dir} is not a directory")

        if choice.isdigit():
            if int(choice) < len(files):
                print(f"{choice}")
                song = files[int(choice)]
                print(song)
                if song.endswith("mp3"):
                    ConvertToFlac.convertMp3(song)
                if song.endswith("wav"):
                    ConvertToFlac.convertWav(song)

        if choice in ("quit", "exit"):
            break



if __name__ == "__main__":
    run()