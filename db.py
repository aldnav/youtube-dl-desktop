from uuid import uuid4

from tinydb import TinyDB, Query, operations

db = TinyDB('./.db.json')


def list_queue():
    items = db.all()
    return items


def list_unstarted_queue():
    queue = Query()
    items = db.search(queue.status == 'pending')
    return items


def add_queue(url, title, image_url):
    key = str(uuid4())
    data = {
        'key': key,
        'url': url,
        'title': title,
        'image_url': image_url,
        'status': 'pending',
        'downloadInfo': {}
    }
    db.insert(data)
    return data


def get_queue_by_key(key):
    queue = Query()
    items = db.search(queue.key == key)
    try:
        return items[0]
    except IndexError:
        return None


def set_status(key, status):
    queue = Query()
    db.update({'status': status}, queue.key == key)
    return get_queue_by_key(key)


def set_download_info(key, info):
    queue = Query()
    db.update({'downloadInfo': info}, queue.key == key)
    return get_queue_by_key(key)
