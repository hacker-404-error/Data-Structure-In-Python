
array=[]
row=int(input("Enter the no of Rows: "))
col=int(input("Enter the no of Coloumns: "))


#Creating 2D Array
for i in range(row):
    array.append([0 for j in range(col)])
       
# Printing 2D Array
for i in range(row):
    for j in range(col):
        print(array[i][j],end=" ")
    print(end="\n")




    
