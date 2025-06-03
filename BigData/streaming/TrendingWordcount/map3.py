import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        parts = line.split(', ')

        if len(parts) == 3:
            date, word, count_day = parts
            print(f"{word}\t{date},{count_day}")
        elif len(parts) == 2:
            word, total_count = parts
            print(f"{word}\ttotal_count,{total_count}")

if __name__ == "__main__":
    mapper()
