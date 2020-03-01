import youtube_dl
import os
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


class MyLogger(object):
    """Logger class for youtube_dl Logger to tell yt-dl to print errors"""

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    """Helper function for printing, when youtube-dl has finished downloading content."""

    if d['status'] == 'finished':
        print('Done downloading')

def create_download_directory():
    """Tries to create download directory at startup."""

    path = Path(os.getcwd()).joinpath('download')
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except (OSError,FileExistsError,FileNotFoundError) as error:
        print("Creation of downlaod directory failed")
        print(error)

def get_useful_information(info):
    """Extracts useful information from video."""

    result = {}
    result['description'] = info['description']
    result['id'] = info['id']
    result['thumbnail'] = info['thumbnail']
    result['title'] = info['title']
    result['uploader'] = info['uploader']
    return result

@app.route('/download/<path>',methods=['GET'])
def get_download_files(path):
    """Allows all content of download folder to be served"""
    
    return send_from_directory('download',path)


@app.route('/download',methods=['GET'])
def download():
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "progress_hooks": [my_hook],
        "outtmpl":"download/%(title)s.%(ext)s",
        "postprocessors": [{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'320'
        }]
    }
    try:
        video_url = request.json['download_url']
    except TypeError as error:
        return jsonify({'error':'problem with getting parameter download url','text':str(error)})

    with youtube_dl.YoutubeDL({"progress_hooks":[my_hook],"skip_download":"True"}) as ydl:
        try:
            info = get_useful_information(ydl.extract_info(video_url))
        except youtube_dl.utils.ExtractorError as error:
            return jsonify({'error':'problem with extracting', 'text':str(error)})
        except youtube_dl.utils.DownloadError as error:
            return jsonify({'error':'problem with downloading','text':str(error)})  


    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    return jsonify({"message":"downloading","info":info})

if __name__ == "__main__":
    create_download_directory()

    app.run(debug=True)

