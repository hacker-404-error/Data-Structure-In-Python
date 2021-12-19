
array=[]
for i in range(100):
    array.append(0)

n=int(input("Enter the no of element you Want to Enter: "))
for i in range(n):
    element=int(input())
    array[i]=element

pos=int(input("Enter the position of element to delete: "))
for i in range(pos-1,n):
    array[i]=array[i+1]

n=n-1
for i in range(n):
    print(array[i])

