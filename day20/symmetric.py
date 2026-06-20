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
flag=0
if row!=col:
    flag=1
else:
  for i in range(row):
    for j in range (i+1,col):
        if mat1[i][j]!=mat1[j][i]:
         flag=1
         break
print("MATRIX  IS:-")
for i in mat1:
    for elements in i:
     print(elements,end=" ")
    print() 
if flag==0:
    print("symmetric matrix")
else:
    print("not symmetrical")