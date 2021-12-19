
from os import system

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:

    def __init__(self):
        self.head=None
        self.Tail=None

    def insert(self,element):
        if (self.head==None and self.Tail==None):
            self.head=node(element)
            self.Tail=self.head
        else:
            self.Tail.next=node(element)
            self.Tail=self.Tail.next
    def display(self):
        current=self.head
        while(current is not None):
            print(current.data,end="->")
            current=current.next


if __name__=='__main__':
    system("cls")
    Ll=Linked_List()
    n=int(input("Enter the no of element you want to enter: "))
    while(n!=0):
        element=int(input("Enter Data: "))
        Ll.insert(element)
        n-=1
    Ll.display()
