class RandomizedSet:

    def __init__(self):
        self.value_index = {}
        self.randomized_list = []

    def insert(self, val: int) -> bool:
        if val not in self.value_index:
            self.value_index[val] = len(self.randomized_list)
            self.randomized_list.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.value_index:
            index = self.value_index[val]
            self.randomized_list[index] = self.randomized_list[-1]
            self.value_index[self.randomized_list[-1]] = index
            self.value_index.pop(val)
            self.randomized_list.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.randomized_list) - 1)
        random_number = self.randomized_list[index]
        
        return random_number


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()