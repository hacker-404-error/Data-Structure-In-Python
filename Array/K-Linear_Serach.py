

array=[]
for i in range(100):
    array.append(0)

n=int(input("Enter the no of element you Want to Enter: "))
for i in range(n):
    element=int(input())
    array[i]=element

search=int(input("Enter the Element You Want To Search: "))

for i in range(n):
    if(search==array[i]):
        print(f"Element Found At Index: {i+1}")