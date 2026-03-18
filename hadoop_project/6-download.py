#!/usr/bin/env python3

from snakebite.client import Client
import os

def download(l):
    client = Client('localhost', 9000)

    for path in l:
        filename = os.path.basename(path)
        local_path = f"/tmp/{filename}"

        for result in client.copyToLocal([path], local_path):
            print({
                'path': local_path,
                'result': result.get('result', False),
                'error': result.get('error', ''),
                'source_path': path
            })
