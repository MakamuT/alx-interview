#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys
status_codes = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}
count = 0
total_size = 0

def stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for c in sorted(status_codes):
        if status_codes[c] > 0:

try:
    for line in sys.stdin:
        count += 1
        s = line.split()

        if len(s) < 7:
            continue

    try:
        status_code = int(s[-2])
        file_size = int(s[-1])
    except (ValueError, IndexError):
        continue

    if status_code in status_codes:
        status_codes[status_code] += 1
    total_size += file_size

    if count % 10 == 0:
        stats(total_size, status_codes)

except KeyboardInterrupt:
    stats(total_size, status_codes)
    raise

stats(total_size, status_codes)
