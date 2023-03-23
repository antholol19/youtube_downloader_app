from flask import Flask, redirect, url_for, render_template, request
import downloader


app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def handle_download():
    if request.method == "POST":
        link = request.form.get('url')
        yt = downloader.Downloader(link)
        yt.output_path()
        if request.form['audio'] == "yes":
            yt.Download_Audio_only()
        if request.form['video'] == "yes":
            yt.Download_Video_only()
        if request.form['audio'] == "no" and request.form['video'] == 'no':
            yt.Download_Video()
    return render_template('home.html')

if __name__ == "__main__":
    app.run() 
