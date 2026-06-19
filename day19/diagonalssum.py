# THIS IS FOR THE SQUARE MATRIX
mat1=[]
row=int(input("enter the number of rows you want :-"))
col=int(input("enter the number of columns you want:-"))
print("MATRIX :-")
for mt1 in range(0,row):
    matrix1=[]
    for j in range(col):
      x=int(input("enter the elements in column:-"))
      matrix1.append(x)
    mat1.append(matrix1)
print("MATRIX  IS:-")
for i in mat1:
    for elements in i:
     print(elements,end=" ")
    print()

print("THE SUM OF THE LEFT DIAGONAL:-")
diag1=0 
for i in range(row):
    for j in range(col):
        if i == j:
            diag1+= mat1[i][j]
print(diag1)

print("THE SUM OF THE RIGHT DIAGONAL:-")
diag2=0
for i in range(row):
    for j in range(col):
        if i+j==row-1:
            diag2+= mat1[i][j]
print(diag2)
print("THE SUM OF THE DIAGONAL IS:-")
print(diag1+diag2)