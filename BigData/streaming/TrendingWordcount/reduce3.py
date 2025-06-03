import sys


def reducer():
    current_word = None
    total_count = None

    for line in sys.stdin:
        line = line.strip()
        word, value = line.split('\t', 1)

        if value.startswith("total_count"):
            total_count = float(value.split(',')[1].strip())
            current_word = word
        else:
            date, count_day = value.split(',', 1)
            count_day = float(count_day.strip())

            if word == current_word and total_count is not None:
                percentage = (count_day / total_count) * 100
                print(f"{word}, {date}, {count_day:g}, {total_count:g}, {percentage:.1f}%")


if __name__ == "__main__":
    reducer()
