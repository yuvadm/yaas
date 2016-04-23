import os
import youtube_dl

from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    vids = os.listdir('static/vids')
    return render_template('index.html', vids=vids)


@app.route('/upload', methods=['POST'])
def upload():
    url = request.form['url']
    if url:
        ydl_opts = {
            'outtmpl': 'static/vids/%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            ydl.download([url])

    return redirect('/')

if __name__ == '__main__':
    app.run()
