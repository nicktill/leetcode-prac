import random
 
class MyDS:
    def __init__(self):
        self.arr = []
        self.hashd = {}

def add(self, x):
         
    if x in self.hashd:  
        return

    s = len(self.arr)
    self.arr.append(x)
    self.hashd[x] = s
 
def remove(self, x):
         
    # Check if element is present
    index = self.hashd.get(x, None)
    if index == None:
        return


    del self.hashd[x]

    size = len(self.arr)
    last = self.arr[size - 1]
    self.arr[index], \
    self.arr[size - 1] = self.arr[size - 1], \
                            self.arr[index]

    del self.arr[-1]

    self.hashd[last] = index
 
def getRandom(self):
    index = random.randrange(0, len(self.arr))
    return self.arr[index]

def search(self, x):
    return self.hashd.get(x, None)
 