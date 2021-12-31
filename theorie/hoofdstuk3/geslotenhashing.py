# https://dodona.ugent.be/nl/courses/399/series/8797/activities/1385084508/
class HashSet:
    DELETED = 99999

    def __init__(self, max_size=10):
        self.max = max_size
        self.arr = [None]*max_size
        self.nb = 0

    def add(self, item):
        if self.nb == self.max:
            raise ValueError("max Value")
        indx = hash(item) % self.max
        while self.arr[indx] != None and self.arr[indx] != HashSet.DELETED:
            print(indx)
            indx = (indx+1) % self.max
        self.arr[indx] = item
        self.nb += 1
        return indx

    def index_of(self, item):
        index = hash(item) % self.max
        startIndex = index
        while(self.arr[index] != item):
            if self.arr[index] == None:
                return -1
            print(index)
            index = (index+1) % self.max
            if startIndex == index:
                return -1
        return index

    def delete(self, item):
        index = self.index_of(self, item)
        if index == -1:
            return False
        self.arr[index] = HashSet.DELETED
        self.nb -= 1
        return True
