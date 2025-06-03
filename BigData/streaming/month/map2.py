#!/usr/bin/env python
import sys
from datetime import datetime


def extract_hour(timestamp):
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return dt.hour
    except ValueError:
        return None


for line in sys.stdin:
    line = line.strip()

    if not line or line.startswith("App"):
        continue

    fields = line.split(",")

    timestamp = fields[1]
    hour = extract_hour(timestamp)

    if hour is not None:
        print(f"{hour}\t1")
