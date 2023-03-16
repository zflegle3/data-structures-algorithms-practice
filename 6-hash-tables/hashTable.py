
class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            #ord gets the asci number for each letter as looped through
            #multiply by 23 b/c prime #
            #mod returns remainder 0 to 6
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys







my_hash_table = HashTable()


my_hash_table.set_item("cans", 12)
my_hash_table.set_item("bolts", 41)
my_hash_table.set_item("washers", 69)
my_hash_table.print_table()

print(my_hash_table.get_item("cans"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))
print(my_hash_table.keys())