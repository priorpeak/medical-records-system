# from django_q.tasks import async_task
import sys
import queue
import os

sys.path.insert(1, './medApp/myapi')
sys.path.insert(2, './medApp')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

def test_queue():
    json_payload = {
        'this': 'is',
        'a': 'test',
        'for': 'queueing'
    }

    # async_task(queue.queue_stud, json_payload, 2)
    # async_task(queue.queue_stud, json_payload, 4)
    # async_task(queue.queue_stud, json_payload, 6)
    # async_task(queue.queue_stud, json_payload, 8)

    return print('DONE')