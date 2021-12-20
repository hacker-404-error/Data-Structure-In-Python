


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

    def delete_from_position(self,n):
        if(self.head is None):
            print("No Element To Delete")
            return 0
        else:
            pos=int(input("Enter The Position To Delete: "))
            if(pos == 1):
                self.head=self.head.next
                return 1
            elif(pos==n):
                current=self.head
                while(current.next.next is not None):
                    current=current.next
                self.Tail=current
                current=current.next
                current=None
                self.Tail.next=None
                return 1
            elif(pos<1 or pos>n):
                print("Invalid Position !! ")
                return 0
            else:
                current=self.head
                for i in range(1,pos-1):
                    current=current.next
                temp=current.next
                current.next=current.next.next
                temp.next=None
                temp=None
                return 1



if __name__=='__main__':
    system("cls")
    Ll=Linked_List()
    n=int(input("Enter the no of element you want to enter: "))
    temp=n
    while(n!=0):
        element=int(input("Enter Data: "))
        Ll.insert(element)
        n-=1
    Ll.display()
    print(end="\n")
    c=input("Do you want to Delete Data: ")
    while(c=='y' or c=='Y'):
        x=Ll.delete_from_position(temp)
        if(x==1):
            temp=temp-1
        Ll.display()
        print(end="\n")
        c=input("Want to delete Again : ")
