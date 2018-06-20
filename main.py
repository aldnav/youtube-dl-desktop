import eel
import db
from download import download, get_meta


@eel.expose
def queue_download(url):
    meta = get_meta(url=url)
    data = db.add_queue(url, **meta)
    return data


@eel.expose
def list_downloads():
    items = db.list_queue()
    return items


def download_loop():
    while True:
        items = db.list_unstarted_queue()
        try:
            item = items[0]
            download(item['key'])
            eel.sleep(10)
        except IndexError:
            pass
        eel.sleep(3)


def start_app():
    web_config = {
        'mode': 'chrome-app',
        'host': 'localhost',
        'port': 3060
    }
    eel.init('web')
    eel.start('index.html', options=web_config)


if __name__ == '__main__':
    eel.spawn(download_loop)
    start_app()
