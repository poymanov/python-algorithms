class ksort:
    def __init__(self, data):
        self.data = data
        self.hash_table = [None] * (len(data) + 25)

    def sort(self):
        for item in self.data:
            hash = self.hash_fun(item)
            self.set_hash(hash, item)
        return self.get_sorted_data()

    def hash_fun(self, value):
        rules = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                 'f': 5, 'g': 6, 'h': 7}

        letter = value[0]
        digits_list = []

        for item in value:
            if item in rules:
                digit_value = rules[item]
            else:
                digit_value = int(item)
            digits_list.append(digit_value)

        return sum(digits_list)

    def set_hash(self, hash, value):
        if self.hash_table[hash] is None:
            self.hash_table[hash] = value
        elif self.hash_table is list:
            self.hash_table[hash].append(value)
        else:
            current_value = self.hash_table[hash]
            self.hash_table[hash] = [current_value, value]

    def get_sorted_data(self):
        sorted_data = []
        for item in self.hash_table:
            if item is None:
                continue
            elif item is list:
                sorted_data += item
            else:
                sorted_data.append(item)

        return sorted_data
