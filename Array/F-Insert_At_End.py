


array=[]
n=int(input("Enter the no of element you want to enter"))

for i in range(0,100):
    array.append(0)

print("Enter the elements: ")
for i in range(0,n):
    element=int(input())
    array[i]=element

newelement=int(input("enter the element to insert at end : "))

array[n]=newelement

for i in range(0,n+1):
    print(array[i])