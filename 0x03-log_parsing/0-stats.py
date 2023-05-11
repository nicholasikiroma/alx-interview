#!/usr/bin/python3
"""Module contains python function
   for computing metrics
"""
import sys
import re
from collections import defaultdict

pattern = r'''
^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
\s-\s\[(.*?)\]
\s"GET\s/projects/260\sHTTP/1\.1"
\s(\d{3})
\s(\d+)'''

count_status_code = defaultdict(int)
total_size = 0
line_count = 0

try:
    for lines in sys.stdin:
        line = lines.strip()

        match = re.match(pattern, line, re.VERBOSE)

        if match:
            file_size = int(match.group(4))
            status_code = match.group(3)

            total_size += file_size

            if status_code.isdigit():
                count_status_code[int(status_code)] += 1

            line_count += 1

            if line_count % 10 == 0:
                print("File size:", total_size)
                for status in sorted(count_status_code):
                    print("{}: {}".format(status, count_status_code[status]))

        else:
            continue

except KeyboardInterrupt:
    print("File size:", total_size)
    for status in sorted(count_status_code):
        print("{}: {}".format(status, count_status_code[status]))
