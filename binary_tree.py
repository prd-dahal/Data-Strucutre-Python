class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self,initialNode = None):
        self.initialNode = initialNode

    def insert(self,item):
        temp = self.initialNode
        while(True):
            if(temp.data>item.data):
                if(temp.left==None):
                    temp.left=item
                    break
                else:
                    temp = temp.left
            elif(temp.data<item.data):
                if(temp.right==None):
                    temp.right = item
                    break
                else:
                    temp = temp.right
    def search(self,value):
        temp = self.initialNode
        traverse = []
        while(temp!=None):
            if(temp.data==value):
                print("The data found at {} ".format(traverse))
                break
            if(value>temp.data):
                temp = temp.right
                traverse.append('Right')
            elif(value<temp.data):
                temp = temp.left
                traverse.append("Left")
            else:
                print("{} not in the tree".format(value))
    


bt = BinaryTree()
bt.initialNode = Node(5)
bt.insert(Node(6))
bt.insert(Node(7))
bt.insert(Node(2))
bt.insert(Node(3))
# print(bt.initialNode.left.right.data)
bt.search(3)
