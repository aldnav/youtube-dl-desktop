import eel
import db
from download import download


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
            download(item['key'])
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
