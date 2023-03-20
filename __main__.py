from flask import Flask, redirect, url_for, render_template, request
import downloader


app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def handle_url():
    if request.method == "POST":
        link = request.form.get("url")
        yt = downloader.Audio_downloader(link)
        yt.Download_Audio()
        #path = yt.title+".mp4"
        #clip = Clip(path, 40, 60)
    return render_template('home.html')

if __name__ == "__main__":
    app.run() 