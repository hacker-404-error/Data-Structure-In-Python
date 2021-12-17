# finding Maximum Element In The Array

array=[]
n=int(input("Enter the no of elements you want to enter"))
print("Enter the Elements")
for i in range(0,n):
    element=int(input())
    array.append(element)


max=array[0]
for i in range(0,n):
    if(max<array[i]):
        max=array[i]
    
print(f"Minimum Elements Is: {max}")
