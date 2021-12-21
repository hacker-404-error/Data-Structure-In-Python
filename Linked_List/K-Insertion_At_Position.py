
from os import system

class node:

    def __init__(self,element):
        self.data=element
        self.next=None



class linked_list():


    def __init__(self):
        self.head=None
        self.tail=None


    def insertion(self,element):
        if(self.head is None and self.tail is None):
            self.head=node(element)
            self.tail=self.head
        else:
            self.tail.next=node(element)
            self.tail=self.tail.next


    def display(self):
        current=self.head
        print("Elements in the list : ")
        while(current != None):
            print(current.data,end="->")
            current=current.next


    def insert_at_pos(self,n):
        pos=int(input("Enter the position for inserting Data: "))
        if(self.head==None):
            if(pos==1):
                element=int(input("Enter Data"))
                self.head=node(element)
                return 1
            else:
                print("List is Empty!!!")
        else:
            if(pos==1):
                x=int(input("Enter Data: "))
                current=node(x)
                current.next=self.head
                self.head=current
                return 1
            elif(pos==n+1):
                x=int(input("Enter the element: "))
                self.tail.next=node(x)
                self.tail=self.tail.next
                return 1
            elif(pos<1 or pos>n+1):
                print("Invalid position")
            else:
                element=int(input("Enter Data: "))
                current=node(element)
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                current.next=temp.next
                temp.next=current
                return 1




if __name__ == "__main__":

    system("cls")
    l1=linked_list()
    n=int(input("Enter the no of element you want to enter: "))
    temp=n
    while(n!=0):
        element=int(input("Enter Data: "))
        l1.insertion(element)
        n-=1
    l1.display()
    print(end="\n")
    c=input("Do you want to Insert Data: ")
    while(c=='y' or c=='Y'):
        x=l1.insert_at_pos(temp)
        if(x==1):
            temp=temp+1
        l1.display()
        print(end="\n")
        c=input("Want to Insert Again : ")
        