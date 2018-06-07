import youtube_dl

import db


DOWNLOAD_PATH = './downloads/'


def download(key):
    queue = db.get_queue_by_key(key)
    print(queue)
    if not queue:
        return
    db.set_progress(key, 1)
    url = queue['url']

    def hook(d):
        if d['status'] == 'finished':
            db.set_progress(key, 100)
        else:
            percentage = d['_percent_str'].strip().replace('%', '')
            percentage = int(float(percentage.strip().replace('%', '')))
            if percentage > 1:
                db.set_progress(key, percentage)
            print(dir(d))
            print(d)

    opts = {'progress_hooks': [hook]}
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])
