mat1=[]
rowwise=[]
row=int(input("enter the number of rows you want :-"))
col=int(input("enter the number of columns you want:-"))
print("MATRIX :-")
for mt1 in range(0,row):
    matrix1=[]
    for j in range(col):
      x=int(input("enter the elements in column:-"))
      matrix1.append(x)
    mat1.append(matrix1)

for i in range(row):
    ad=0
    for j in range (col):
        ad+=mat1[i][j]
    rowwise.append(ad)   
print("MATRIX  IS:-")
for i in mat1:
    for elements in i:
     print(elements,end=" ")
    print() 
print("ROW-WISE SUM OF  MATRIX:-")        
for i in rowwise:
        print(i)