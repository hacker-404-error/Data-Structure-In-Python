
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
        current=self.tail
        while(current!=None):
            print(current.data, end="->")
            current=current.pre

    def insert_at_pos(self,n):
        pos=int(input("Enter the position for inserting Data: "))
        if(self.head==None):
            if(pos==1):
                element=int(input("Enter Data: "))
                self.head=node(element)
                return 1
            else:
                print("List is empty!!")
        else:
            if(pos==1):
                element=int(input("Enter data: "))
                current=node(element)
                current.next=self.head
                self.head.pre=current
                self.head=current
                current=None
                return 1
            elif(pos==n+1):
                element=int(input("Enter Data: "))
                current=node(element)
                self.tail.next=current
                current.pre=self.tail
                self.tail=current
                current=None
                return 1
            elif(pos<1 or pos>n+1):
                print("INvalid position")
            else:
                element=int(input("Enter data: "))
                current=node(element)
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                current.next=temp.next
                current.pre=temp
                temp.next=current
                temp.next.pre=current
                return 1




if __name__ == "__main__":
    
    system("cls")
    dll=Doubly_Linked_List()
    n=int(input("Enter the no. of element you want to enter: "))
    temp=n
    while(n!=0):
        element=int(input("Enter Data: "))
        dll.insertion(element)
        n=n-1
    print("Element from Head to Tail: ")
    dll.display()
    print(end="\n")
    c=input("Do you want to Insert Data: ")
    while(c=='y' or c=='Y'):
        x=dll.insert_at_pos(temp)
        if(x==1):
            temp=temp+1
        dll.display()
        print(end="\n")
        c=input("Want to Insert Again : ")


    print(end="\n")
    print("Element from Head to Tail: ")
    dll.display()
    print(end="\n")
    print("Element From Tail to Head: ")
    dll.reverse()
