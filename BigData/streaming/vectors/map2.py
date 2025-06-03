#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, value = line.split(',')
        key = "sum"
        value = float(value)

        print(f"DoubleValueSum:{key}\t{value}")

    except ValueError:
        continue
