import os
from pytube import YouTube

class Downloader:

    def __init__(self, url: str):
        self.url = url
        self._output_path = None
    
    def Download_Video(self) -> YouTube:
        yt = YouTube(self.url)
        yt.streams.get_highest_resolution()
        stream = yt.streams.filter(progressive=True, file_extension="mp4").last()
        try:
            stream.download(output_path=self._output_path)
        except:
            print("Download error")
        print("Download successful")
        return stream
    
    def Download_Video_only(self) -> YouTube:
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_video=True, file_extension='webm').first()
        try:
            stream.download(filename_prefix='video_only_', output_path=self._output_path)
        except:
            print("Download error")
        print("Download successful")
        return stream
        
    
    def Download_Audio_only(self) -> YouTube:
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_audio=True, subtype="mp4").last()
        try:
            stream.download(filename_prefix='audio_only_', output_path=self._output_path) 
        except:
            print("Download error")
            
        print("Download successful")
        return stream
    
    def output_path(self):
        if os.name == "nt":
            self._output_path = f"{os.getenv('USERPROFILE')}\\Downloads"
        else:  # PORT: For *Nix systems
            self._output_path = f"{os.getenv('HOME')}/Downloads"
    
    