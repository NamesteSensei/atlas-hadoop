#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

# Skip header
header = next(reader, None)

for row in reader:
    try:
        id = row[0]
        company = row[1]
        salary = row[2]

        print(f"{id}\t{company},{salary}")
    except:
        continue
