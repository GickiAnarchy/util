# Audio Converter
#author: FatherAnarchy
from pydub import AudioSegment
import PySimpleGUI as sg
import ffmpeg
import os


class ConvertToFlac:
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
def run():
    pass


def converter():
    print = sg.Print
    exts = [".mp3", ".wav", ".flac", ".ogg"]
    songs = []    
    radio_row = [[sg.Text("Conversion Format", justification = "center", expand_x = True)],
                        [sg.Radio("-> mp3", "FORMAT", default = False, size = (10,1), key = "TO_MP3"), 
                        sg.Radio("-> wav", "FORMAT", default = True, size = (10,1), key = "TO_WAV"), 
                        sg.Radio("-> flac", "FORMAT", default = False, size = (10,1), key = "TO_FLAC")]]
    browse = [[sg.InputText(size=(50,1), key='-FILENAME-'), sg.FileBrowse()], [sg.Listbox(songs, key = "SONGS_LIST")]]
    layout = [[sg.Frame(None, radio_row)], [sg.Frame(None, browse)], [sg.Button("Convert", key = "CONVERT")]]
    window = sg.Window("Audio Converter", layout, element_justification = "center", alpha_channel = 1, finalize = True)
    
    while True:
        event, values = window.read()
        s_list = values["SONGS_LIST"]
        mp3 = values["TO_MP3"]
        wav = values["TO_WAV"]
        flac = values["TO_FLAC"]
        
        
        if event in (None, sg.WINDOW_CLOSED):
            break

        if event == "-FILENAME-":
            for s in values["-FILENAME-"]:
                songs.append(s)
                sg.popup_quick_message(s)

        if event == "CONVERT" and len(songs) != 0:
            song = songs[0]
            base, ext = os.path.splitext(song)
            if ext == ".mp3":
                if flac == True:
                    ConvertToFlac.mp3_to_flac(song)
                if wav == True:
                    ConvertToFlac.mp3_to_wav(song)
            if ext == ".wav":
                if flac == True:
                    ConvertToFlac.wav_to_flac(song)
                if wav == True:
                    ConvertToFlac.wav_to_mp3(song)
            if ext == ".flac":
                pass
            
                    

    window.close()


if __name__ == "__main__":
    run()