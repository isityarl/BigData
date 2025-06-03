#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()

    if line.startswith("App"):
        continue

    fields = line.split(",")

    if len(fields) < 11:
        continue

    last_updated = fields[10]

    month = last_updated.split(" ")[0]

    month = re.sub(r'[^a-zA-Z]', '', month)

    print(f"{month}\t1")
