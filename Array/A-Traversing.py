

# METHOD 1: Give enter after every input element
array=[]
n=int(input("Enter the number of elements you want to enter "))

for i in range(0,n):
    element=int(input())
    array.append(element)

print("Elemets are: ")

for i in range(0,n):
    print(array[i])



# METHOD 2: Give space after every input element
n=int(input("Enter the no of elements you want to enter "))
element=list(map(int , (input("Enter the elements").strip().split() )))
print(element)