
from os import link, system


class node:
    def __init__(self,element):
        self.data=element
        self.next=None


class linked_list:
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
        while(current!=None):
            print(current.data,end="->")
            current=current.next
    def Insertion_At_end(self):
        x=int(input("Enter the element: "))
        self.tail.next=node(x)
        self.tail=self.tail.next


if __name__ == '__main__':

    system("cls")
    list1=linked_list()
    n=int(input("Enter the no of element you want to enter: "))

    while(n!=0):
        element=int(input("Enter Data: "))
        list1.insertion(element)
        n=n-1
    list1.display()
    print(end="\n")
    x=input("Do you want to insert at end: ")
    while(x=='y' or x=='Y'):
        list1.Insertion_At_end()
        x=input("Want to Enter Again? : ")
        
    print("Updated list is : ")
    list1.display()
