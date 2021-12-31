# https://dodona.ugent.be/nl/courses/399/series/8798/activities/1394891023/
class BinaryHeap:

    def __init__(self, max_size=10):
        self.max = max_size
        self.arr = [None]*max_size
        self.nb = 0

    def empty(self):
        return self.nb == 0

    def get_min_elem(self):
        if self.empty():
            return -1
        return self.arr[0]

    def insert_elem(self, item):
        assert self.nb != self.max, "BinaryHeap is full"
        index = self.nb

        self.arr[index] = item
        ouderIndex = (index-1)//2
        while index > 0 and self.arr[index] < self.arr[ouderIndex]:
            temp = self.arr[index]
            self.arr[index] = self.arr[ouderIndex]
            self.arr[ouderIndex] = temp
            index = ouderIndex
            ouderIndex = (index-1)//2
        self.nb += 1

    def remove_min_elem(self):
        assert not self.empty(), "empty BinaryHeap no min element"
        result = self.arr[0]
        self.arr[0] = self.arr[self.nb-1]

        self.nb -= 1
        index = 0
        links = 2*index+1
        rechts = 2*index+2
        while (links < self.nb and self.arr[links] < self.arr[index]) or (rechts < self.nb and self.arr[rechts] < self.arr[index]):
            if self.arr[links] <= self.arr[rechts]:
                temp = self.arr[index]
                self.arr[index] = self.arr[links]
                self.arr[links] = temp
                index = links
            else:
                temp = self.arr[index]
                self.arr[index] = self.arr[rechts]
                self.arr[rechts] = temp
                index = rechts
            links = 2*index+1
            rechts = 2*index+2
        self.arr[self.nb] = None
        return result

    def __str__(self):
        strin = "["
        ind = 0
        if self.arr[ind] is not None:
            strin += str(self.arr[ind])
            ind += 1
        while self.arr[ind] is not None:
            strin += ", "
            strin += str(self.arr[ind])
            ind += 1
        strin += "]"
        return strin
