class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for key_list in self.data_map[index]:
                if key == key_list[0]:
                    return key_list[1]
                
    def keys(self):
        keys_list = [key_value[0] for table in self.data_map if table is not None for key_value in table]
        return keys_list
                    
            


my_hash = HashTable()
my_hash.set_item("bolts", 1400)
my_hash.set_item("washers", 50)
my_hash.set_item("lumber", 70)
print(my_hash.keys())

my_hash.print_table()


        