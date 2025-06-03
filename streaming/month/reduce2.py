#!/usr/bin/env python
import sys
from collections import defaultdict

hour_counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        hour, count = line.split("\t")
        hour = int(hour)
        count = int(count)
        hour_counts[hour] += count
    except ValueError:
        continue

sorted_hours = sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)

for hour, count in sorted_hours:
    print(f"{hour}\t{count}")
