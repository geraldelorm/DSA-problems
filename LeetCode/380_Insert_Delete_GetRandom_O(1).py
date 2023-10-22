import random

class RandomizedSet:

    def __init__(self):
        '''
        Initialize a hashmap and an array
        map: val -> index in array
        '''
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        '''
        if val in already present return False
        else: add value to both dict and list
        point dict[val] -> list index i.e. where val was just added (len(list) - 1)
        '''
        if val in self.dict:
            return False

        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            #to delete list index in O(1) swap in with last index and pop 
            #~ since order of list elements is not important for this problem
            last_ele, idx = self.list[-1], self.dict[val]
            self.list[idx] = last_ele
            self.dict[last_ele] = idx


            #after swap delete the last index in O(1) with pop and  del val in dict
            self.list.pop()
            del self.dict[val]
            return True
        #just return false is val is not present 
        return False

    def getRandom(self) -> int:
        '''
        Pick random choice from list
        '''        
        return choice(self.list)

        
    # TC: O(1)
    # SC: O(N)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()