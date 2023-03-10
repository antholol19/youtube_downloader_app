from pytube import YouTube
from moviepy.editor import *

class Audio_downloader:

    def __init__(self, link: str):
        self.link = link

    def Download_Audio(self) -> YouTube:
        yt = YouTube(self.link)
        yt.streams.get_highest_resolution()
        stream = yt.streams.filter(only_audio=True, subtype="mp4").last()
        try:
            stream.download() 
        except:
            print("Download error")
            
        print("Download successful")
        return stream

    def Clip(self, start: int , end: int) -> AudioFileClip:
        audio = AudioFileClip(self.link).subclip(start,end)
        
        #You cannot write a soundfile with a mp4 extension. Instead, use ".mp3", ".wav", ".ogg"
        filename = self.link.split('/')[-1].split('.')[0]
        filepath = self.link.split('/')[1:-1]
        editedPath = ""
        for dir in filepath:
            editedPath += dir + '/'
            
        final_path = editedPath+"edited/"+filename+".mp3"   
        audio.to_audiofile(final_path)