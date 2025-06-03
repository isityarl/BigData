import sys

for line in sys.stdin:
    line = line.strip()
    if ',' not in line:
        continue

    try:
        index, value = line.split(',')
        print(f"{index}\t{value}")
    except ValueError as e:
        print(f"Skipping line due to error: {e}", file=sys.stderr)
