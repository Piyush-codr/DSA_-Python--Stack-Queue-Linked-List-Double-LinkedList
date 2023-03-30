class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        c=0
        while temp is not None:
            temp=temp.next
            c+=1
        return c
    def insertatbeginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous==new_node
            self.head=new_node
    def insertatend(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertatbeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp
   
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=' ')
            temp=temp.next
x=DoublyLinkedList()
print(x.isEmpty())
x.insertatend(5)
x.insertatend(15)
x.insertatend(25)
x.insertatend(35)
x.insertatend(45)
x.printlist()
x.insertatbeginning(50)
print("After inserting")
x.printlist()
print("No of nodes",x.length())
