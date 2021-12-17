
array=[]
for i in range(0,100):
    array.append(0)

n=int(input("Enter the no of elements you want to enter"))

for i in range(0,n):
    element=int(input())
    array[i]=element

pos=int(input("Enter the Position of Element you Want to enter: "))

if(pos<0 or pos>n+1):
    print("Invalid Position")
    exit(0)

newelement=int(input("Enter The Element: "))
if(pos==n+1):
    array[pos-1]=newelement
else:
    for i in range(n-1,pos-2,-1):
        array[i+1]=array[i]

n+=1
array[pos-1]=newelement

for i in range(0,n):
    print(array[i])