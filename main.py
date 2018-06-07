import eel

import threading

import db

from download import download

import time


@eel.expose
def queue_download(url):
    data = db.add_queue(url)
    return data


@eel.expose
def list_active_downloads():
    items = db.list_queue()
    return items


def download_loop():
    while True:
        items = db.list_unstarted_queue()
        try:
            item = items[0]
            print(item)
            # loop.call_soon(download, item['key'])
            download(item['key'])
        except IndexError:
            pass
        time.sleep(3)


def start_app():
    web_config = {
        'mode': 'chrome-app',
        'host': 'localhost',
        'port': 3060
    }
    eel.init('web')
    eel.start('index.html', options=web_config)


if __name__ == '__main__':
    t = threading.Thread(target=start_app)
    t.start()
    tt = threading.Thread(target=download_loop)
    tt.start()
