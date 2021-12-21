
from os import system

class node:
    def __init__(self,element):
        self.pre=None
        self.data=element
        self.next=None

class Doubly_Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertion(self,element):
        if self.head is None:
            self.head=node(element)
            self.tail=self.head
        else:
            current=node(element)
            self.tail.next=current
            current.pre=self.tail
            self.tail=current
            current=None

    def display(self):
        current=self.head
        while(current!=None):
            print(current.data, end="->")
            current=current.next

    def reverse(self):
        print("elements from tail to head: ")
        current=self.tail
        while(current!=None):
            print(current.data, end="->")
            current=current.pre

    def Insertion_At_End(self):
        element=int(input("Enter Data: "))
        current=node(element)
        self.tail.next=current
        current.pre=self.tail
        self.tail=current
        current=None



if __name__ == "__main__":
    
    system("cls")
    dll=Doubly_Linked_List()
    n=int(input("Enter the no. of element you want to enter: "))
    while(n!=0):
        element=int(input("Enter Data: "))
        dll.insertion(element)
        n=n-1

    dll.display()
    print(end="\n")
    x=input("Do you want to insert at end: ")
    while(x=='y' or x=='Y'):
        dll.Insertion_At_End()
        x=input("Want to Enter Again? : ")
        
    print("Updated list is : ")
    dll.display()
    print(end="\n")
    dll.reverse()

    