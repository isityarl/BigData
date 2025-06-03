#!/usr/bin/env python
import sys
import math

current_index = None
values = []

for line in sys.stdin:
    index, value = line.strip().split('\t')

    if current_index is not None and index != current_index:
        product = math.prod(values)
        print(f"{current_index},{product}")
        values.clear()

    current_index = index
    values.append(float(value))

if current_index is not None:
    product = math.prod(values)
    print(f"{current_index},{product}")
