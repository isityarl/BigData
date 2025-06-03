#!/usr/bin/env python
import sys

valid_months = set([
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
])

month_count = {}

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        month, count = line.split("\t")
        count = int(count)
    except ValueError:
        continue

    if month in valid_months:
        if month in month_count:
            month_count[month] += count
        else:
            month_count[month] = count

for month in month_count:
    print(f"{month}\t{month_count[month]}")
