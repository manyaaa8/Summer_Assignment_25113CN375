mat1=[]
mat2=[]
multiplication=[]
row1=int(input("enter the number of rows you want in martix 1 :-"))
col1=int(input("enter the number of columns you want in matrix 1:-"))
print("MATRIX 1:-")
for mt1 in range(0,row1):
    matrix1=[]
    for j in range(col1):
      x=int(input("enter the elements in column:-"))
      matrix1.append(x)
    mat1.append(matrix1)
row2=int(input("enter the number of rows you want in matrix 2 :-"))
col2=int(input("enter the number of columns you want in matrix 2:-"))
print("MATRIX 2:-")
for mt2 in range(0,row2):
    matrix2=[]
    for j in range(0,col2):
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
if col1==row2:
 for i in range(0,row1):
    third=[]
    for j in range(0,col2):
        mult=0
        for k in range(col1):
            mult+=mat1[i][k]*mat2[k][j]
        third.append(mult)
    multiplication.append(third)
 for j in multiplication:
    for ele in j:
      print(ele,end=" ")
    print()
else:
    print("the multiplication of given matrix is not possible!!")
        