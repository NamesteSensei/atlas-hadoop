#!/usr/bin/env python3

from snakebite.client import Client
from snakebite.errors import FileNotFoundException

def deletedir(l):
    client = Client('localhost', 9000)

    for path in l:
        try:
            for result in client.delete([path], recurse=True):
                print(result)
        except FileNotFoundException:
            print({'path': path, 'result': False, 'error': 'Not found'})
