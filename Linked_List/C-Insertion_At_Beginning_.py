
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
    def Insertion_At_Beg(self):
        x=int(input("Enter Data: "))
        current=node(x)
        current.next=self.head
        self.head=current


if __name__=='__main__':
    system("cls")
    List1=Linked_List()
    n=int(input("Enter the no of element you want to enter: "))
    while(n!=0):
        element=int(input("Enter Data: "))
        List1.insert(element)
        n-=1
    List1.display()

    print(end="\n")
    x=input("Do you want to insert at Beginning: ")
    while(x=='y' or x=='Y'):
        List1.Insertion_At_Beg()
        x=input("Want to Enter Again? : ")
        
    print("Updated list is : ")
    List1.display()