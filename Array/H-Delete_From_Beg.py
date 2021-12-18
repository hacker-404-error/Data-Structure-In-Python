
array=[]

for i in range(0,100):
    array.append(0)

n=int(input("Enter the no of element you want to enter"))
print("Enter the Elements : ")

for i in range(0,n):
    element=int(input())
    array[i]=element

print("Element Deleted From beginning")
for i in range(0,n):
     array[i]=array[i+1]

n=n-1

for i in range(0,n):
    print(array[i])
