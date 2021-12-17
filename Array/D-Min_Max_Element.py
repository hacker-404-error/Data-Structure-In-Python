
array=[]
n=int(input("Enter the no of element you want to enter"))
for i in range(0,n):
    array.append(0)

# for i in range(0,n):
#     print(array[i])

print("Enter the elements: ")
for i in range(0,n):
    element=int(input())
    array[i]=element

min=array[0]
max=array[0]

print("elements are: ")
for i in range(0,n):
    if(min>array[i]):
        min=array[i]
    if(max<array[i]):
        max=array[i]

print(f"Max Element :{max}")
print(f"Min Element :{min}")