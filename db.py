from uuid import uuid4

from tinydb import TinyDB, Query, operations

db = TinyDB('./.db.json')


def list_queue():
    queue = Query()
    items = db.search(queue.progress >= 0)
    return items


def list_unstarted_queue():
    queue = Query()
    items = db.search(queue.progress == 0)
    return items


def add_queue(url):
    key = str(uuid4())
    data = {'key': key, 'url': url, 'progress': 0}
    db.insert({'key': key, 'url': url, 'progress': 0})
    return data


def get_queue_by_key(key):
    queue = Query()
    items = db.search(queue.key == key)
    try:
        return items[0]
    except IndexError:
        return None


def get_progress(key):
    queue = get_queue_by_key(key)
    if queue:
        return queue['progress']
    return 0


def set_progress(key, value):
    queue = Query()
    db.update(operations.set('progress', value), queue.key == key)
