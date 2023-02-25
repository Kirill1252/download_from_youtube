import os
import time

import eel
from pytube import YouTube

eel.init('web')


@eel.expose
def view_url(url: str):
    yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
    title = yt.title
    author = yt.author
    img = yt.thumbnail_url

    views_url = f'<img src="{img}" class="img_info">' \
                f'<div class="op_info"><p>Track: {title}</p>' \
                f'<p>Author: {author}</p></div>' \

    return views_url


@eel.expose
def download_audio(url: str):
    try:
        yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
        name = f"{yt.title}.mp3"
        audio = yt.streams.get_audio_only()
        if os.path.exists('download_mp3') is not True:
            os.mkdir('download_mp3')
        audio.download(filename=name, output_path='download_mp3')

        res = f'<h3>Audio file download successfully verified</h3>\n' \
              f'<p><b>Path:</b> "{os.path.abspath("download_mp3")}"</p>\n' \
              f'<p><b>File name:<b/> {name}\n</p>' \
              f'<p><b>Time:</b> {time.strftime("%T")}</p>'

        return res

    except FileNotFoundError:
        yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
        name = f"{yt.title[0:20]}.mp3"
        audio = yt.streams.get_audio_only()
        if os.path.exists('download_mp3') is not True:
            os.mkdir('download_mp3')

        audio.download(filename=name, output_path='download_mp3')

        res = f'<p>Audio file download successfully verified</p>\n' \
              f'<p>Path:"{os.path.abspath("download_mp3")}</p>"\n' \
              f'<p>File name: {name}\n</p>' \
              f'<p>Time {time.strftime("%T")}</p>'

        return res

    except KeyError:
        return "<p>I'm sorry but I can't download it...</p>"


@eel.expose
def download_video(url: str):
    try:
        yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
        print(f"[Open URL]: {url}")
        name = f"{yt.title}.mp4"
        video = yt.streams.filter(file_extension='mp4', res='720p').first()

        if os.path.exists('download_video_mp4') is not True:
            os.mkdir('download_video_mp4')

        video.download(filename=name, output_path='download_video_mp4')

        res = f'<p>Video file download successful</p>\n' \
              f'<p>Path:"{os.path.abspath("download_video_mp4")}</p>"\n' \
              f'<p>File name: {name}\n</p>' \
              f'<p>Time {time.strftime("%T")}</p>'

        return res

    except FileNotFoundError:
        yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
        name = f"{yt.title[0:20]}.mp4"
        video = yt.streams.filter(file_extension='mp4', res='720p').first()
        if os.path.exists('download_video_mp4') is not True:
            os.mkdir('download_video_mp4')
        video.download(filename=name, output_path='download_video_mp4')

        res = f'<p>Video file download successful</p>\n' \
              f'<p>Path:"{os.path.abspath("download_video_mp4")}</p>"\n' \
              f'<p>File name: {name}\n</p>' \
              f'<p>Time {time.strftime("%T")}</p>'
        return res

    except KeyError:
        return "<p>I'm sorry but I can't download it...</p>"


eel.start('index.html', size=(650, 600))
