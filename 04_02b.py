from collections import namedtuple
from collections import defaultdict
from pprint import pprint
from csv import reader


def main():
    #add code here
    res = defaultdict(int)
    with open("/workspaces/practice-it-python-data-structs-2486182/data/OrderItems.csv", "r") as open_csv:
        read = reader(open_csv)
        Item = namedtuple("Item", next(read))
        for line in read:
            item = Item(*line)
            res[item.ProductID] += int(item.Quantity)
    pprint(dict(res))
    return



if __name__ == "__main__":
    main()