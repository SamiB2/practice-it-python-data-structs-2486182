import csv
from collections import namedtuple


def main():
    with open('/workspaces/practice-it-python-data-structs-2486182/data/Customer.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        Row = namedtuple('Row', headers)
        for r in reader:
            row = Row(*r)
            print(row)
    return

if __name__ == "__main__":
    main()