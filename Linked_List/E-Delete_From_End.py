


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
        if(self.head is None):
            print("Linked List is Empty Now")
        else:
            current=self.head
            while(current is not None):
                print(current.data,end="->")
                current=current.next

    def delete_from_end(self):
        if(self.head is None):
            print("No Element To Delete")
        else:
            if(self.head.next is None):
                self.head=None
            else:
                current=self.head
                while(current.next.next is not None):
                    current=current.next
                self.Tail=current
                current=current.next
                current=None
                self.Tail.next=None


if __name__=='__main__':
    system("cls")
    Ll=Linked_List()
    n=int(input("Enter the no of element you want to enter: "))
    while(n!=0):
        element=int(input("Enter Data: "))
        Ll.insert(element)
        n-=1
    Ll.display()
    print(end="\n")
    c=input("Do you want to Delete Data: ")
    while(c=='y' or c=='Y'):
        Ll.delete_from_end()
        Ll.display()
        print(end="\n")
        c=input("Want to delete Again : ")
