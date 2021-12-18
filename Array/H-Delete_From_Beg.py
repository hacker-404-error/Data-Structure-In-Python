
array=[]
n=int(input("Enter the no of element you want to enter"))

for i in range(0,100):
    array.append(0)

print("Enter the Elements : ")

for i in range(0,n):
    element=int(input())
    array[i]=element

print("Elemnt Deleted From beginning")
for i in range(0,n):
     array[i+1]=array[i]

n=n-1

for i in range(0,n):
    print(array[i])
