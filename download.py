import requests
import youtube_dl

import db

import eel


DOWNLOAD_PATH = './downloads/'

"""
{u'status': u'downloading', u'downloaded_bytes': 1024, u'_percent_str': u'  0.0%', u'_speed_str': u'249.82KiB/s', u'elapsed': 0.732759952545166, u'total_bytes': 6645678, u'tmpfilename': u'WGO judges pity Souma - Shokugeki no Souma Season 3 Episode 23 [English Subs]-LSli0Dg1L6E.mp4.part', u'speed': 255820.31663589255, u'_total_bytes_str': u'6.34MiB', u'filename': u'WGO judges pity Souma - Shokugeki no Souma Season 3 Episode 23 [English Subs]-LSli0Dg1L6E.mp4', u'eta': 26, u'_eta_str': u'00:26'}
"""


def download(key):
    queue = db.get_queue_by_key(key)
    if not queue:
        return
    db.set_status(key, 'downloading')
    url = queue['url']

    def hook(d):
        if d['status'] == 'finished':
            donwloadInfo = db.set_status(key, 'finished')
        else:
            donwloadInfo = db.set_download_info(key, d)

        def nothing(n):
            pass

        eel.updateDownloads(donwloadInfo)(nothing)

    opts = {'progress_hooks': [hook]}
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])


def _get_meta(content, identifier):
    i = content.find(identifier)
    content = content[i + len(identifier):]
    i = content.find('"')
    return content[:i]


def get_meta(url):
    response = requests.get(url)
    if response.status_code != 200:
        return False
    content = response.content
    title_identifier = '<meta name="title" content="'
    title = _get_meta(content, title_identifier)
    image_identifier = '<meta property="og:image" content="'
    image_url = _get_meta(content, image_identifier)
    return {'title': title, 'image_url': image_url}
