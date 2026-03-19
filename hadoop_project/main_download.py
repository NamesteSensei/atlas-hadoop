#!/usr/bin/env python3

download = __import__('6-download').download

l = ["/holbies/input/lao.txt"]
download(l)

with open("/tmp/lao.txt", "r") as f:
    print(f.read())
