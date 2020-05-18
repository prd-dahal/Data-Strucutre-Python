class stack:
    def __init__(self,initialstack=[]):
        self.s = initialstack
    def add(self, item):
        self.s.append(item)

    def display(self):
        for i in range(len(self.s)-1,-1,-1):
            print(self.s[i])
    def remove(self):
        print("{} is removed".format(self.s.pop()))

stac = stack()
stac.add(1)
stac.add(2)
stac.display()
stac.remove()
stac.display()
