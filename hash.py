size = 10

class DataItem:
    def __init__(self, key, data):
        self.key = key
        self.data = data


hashArray = [None] * size


def hashIndex(key):
    return key % size


def insert(key, data):
    item = DataItem(key, data)
    index = hashIndex(key)

    if hashArray[index] is None:
        hashArray[index] = item
        print(f"The Data {data} is stored at Index {index} Having key {key}")
    else:
        print(f"The Index {index} is Already Occupied by an item.")


# Different insert data
insert(23, 120)
insert(56, 340)
insert(91, 560)
insert(37, 780)
insert(64, 900)
insert(73, 450)