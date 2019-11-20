import csv


def transpose_csv(input, output):
    with open(input, 'rt', encoding='utf-8-sig') as reader:
        a = zip(*csv.reader(reader))
        with open(output, 'w', encoding='utf-8-sig') as writer:
            csv.writer(writer).writerows(a)