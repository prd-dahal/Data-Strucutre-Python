class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SinglyLinkedList:
    def __init__(self):
        self.headval = None
    def display(self):
        #print(self.headval.nextval.dataval)
        temp = self.headval
        while(temp!= None):
             print(temp.dataval)
             temp = temp.nextval

    def addatlast(self, item=None):
        temp = self.headval
        while(temp.nextval != None):
            temp = temp.nextval
        temp.nextval = item
        item.nextval = None

    def addatbeginning(self,item):
        item.nextval = self.headval
        self.headval = item

    def addatposition(self,pos,item):
        temp = self.headval

        for i in range(pos-1):
            temp = temp.nextval
        item.nextval = temp.nextval
        temp.nextval = item

    def delete_beg(self):
        temp = self.headval
        self.headval = temp.nextval

    def delete_last(self):
        temp = self.headval
        while(temp.nextval.nextval!=None):
            temp = temp.nextval
        temp.nextval = None

    def delete_at_pos(self,pos):
        temp = self.headval
        for i in range(pos-1):
            temp = temp.nextval
        temp.nextval = temp.nextval.nextval


sl = SinglyLinkedList()
sl.headval = Node("Monday")
sl.addatlast(Node("Tuesday"))
sl.addatbeginning(Node("Sunday"))
sl.addatposition(1,Node("Inserted"))
sl.display()
sl.delete_at_pos(1)
print("After deleteing at position 1")
sl.display()



# print("After Deleteing the first element")
# sl.delete_beg()
# sl.display()
# sl.delete_last()
# print("After deleteing the last element")
# sl.display()
