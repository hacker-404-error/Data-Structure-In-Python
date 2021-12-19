
import math

array=[]
for i in range(100):
    array.append(0)

n=int(input("Enter the no of element you Want to Enter: "))
for i in range(n):
    element=int(input())
    array[i]=element

search=int(input("Enter the Element You Want To Search: "))

Low=0
High=n-1
Mid=math.floor((Low+High)/2)


while(array[Mid]!=search and Low<=High):
    if(search<array[Mid]):
        High=Mid-1
    else:
        Low=Mid+1
    Mid=math.floor((Low+High)/2)


if(search==array[Mid]):
    print(f"Element Found At Index:{Mid+1}")

else:
    print(f"Element Not Found")
