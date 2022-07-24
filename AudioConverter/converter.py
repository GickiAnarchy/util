# Audio Converter        COPY AND PLACE THIS SCRIPT IN THE AUDIO DIRECTORY, THEN RUN.
#author: FatherAnarchy
from pydub import AudioSegment
import os


class Converter:
    def __init__(self):
        pass

    @staticmethod
    def wav_to_flac(audio):
        if audio.endswith(".wav"):
            print("wav_to_flac needs to be in wav format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"{base[0]}.flac", format = "flac")
        print(f"{song} exported")

    @staticmethod
    def mp3_to_flac(audio):
        if not audio.endswith(".mp3"):
            print("mp3_to_flac needs to be in mp3 format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"{base[0]}.flac", format = "flac")
        print(f"{song} exported")

    @staticmethod
    def mp3_to_wav(audio):
        if not audio.endswith(".mp3"):
            print("mp3_to_wav needs to be in mp3 format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"./{base[0]}.wav", format = "wav")
        print(f"{song} exported")

    @staticmethod
    def wav_to_mp3(audio):
        if not audio.endswith(".wav"):
            print("wav_to_mp3 needs to be in wav format")
        song = AudioSegment.from_file(audio)
        base = os.path.splitext(audio)
        song.export(f"./{base[0]}.mp3", format = "mp3")
        print(f"{song} exported")


#
#
if __name__ == "__main__":
    print("Audio Converter - Under Construction")
    files = os.listdir(".")
    actions = ["0: mp3 to flac", "1: wav to flac", "2: mp3 to wav", "3: wav to mp3"]
    for file in files:
        print(f"{str(files.index(file))}: {file}")
    choice1 = input("Choose an audio file: ")
    con_song = files[int(choice1)]
    for action in actions:
        print(action)
    choice2 = input("Choose a function: ")
    if choice2 == "0":
        Converter.mp3_to_flac(con_song)
    if choice2 == "1":
        Converter.wav_to_flac(con_song)
    if choice2 == "2":
        Converter.mp3_to_wav(con_song)
    if choice2 == "3":
        Converter.wav_to_mp3(con_song)