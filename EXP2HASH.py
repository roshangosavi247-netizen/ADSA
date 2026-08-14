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



n = int(input("Enter number of items: "))

for i in range(n):
    key = int(input("Enter key: "))
    data = int(input("Enter data: "))
    insert(key, data)



print("\nHash Table:")
print("Index\tKey\tData")

for i in range(size):
    if hashArray[i] is None:
        print(i, "\t-\t-")
    else:
        print(i, "\t", hashArray[i].key, "\t", hashArray[i].data)