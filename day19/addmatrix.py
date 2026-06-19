mat1=[]
mat2=[]
row=int(input("enter the number of rows you want :-"))
col=int(input("enter the number of columns you want:-"))
print("MATRIX 1:-")
for mt1 in range(0,row):
    matrix1=[]
    for j in range(col):
      x=int(input("enter the elements in column:-"))
      matrix1.append(x)
    mat1.append(matrix1)
print("MATRIX 2:-")
for mt2 in range(0,row):
    matrix2=[]
    for j in range(0,col):
      elements=int(input("enter the elementa in column:-"))
      matrix2.append(elements)
    mat2.append(matrix2) 
print("MATRIX 1 IS:-")
for i in mat1:
    for ele in i:
     print(ele,end=" ")
    print()
print("MATRIX 2 IS:-")
for j in mat2:
    for element in j:
        print(element,end=" ")
    print()
print("ADDITION OF GIVEN MATRIX:-")
add=[]
for i in range(row):
    matrix3=[]
    for j in range (col):
        ad=mat1[i][j]+mat2[i][j]
        matrix3.append(ad)
    add.append(matrix3)      
        
for i in add:
    for j in i:
        print(j,end=" ")
    print()
    