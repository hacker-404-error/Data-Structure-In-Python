
# finding Minimum Element In The Array

array=[]
n=int(input("Enter the no of elements you want to enter"))
print("Enter the Elements")
for i in range(0,n):
    element=int(input())
    array.append(element)


min=array[0]
for i in range(0,n):
    if(min>array[i]):
        min=array[i]
    
print(f"Minimum Elements Is: {min}")
