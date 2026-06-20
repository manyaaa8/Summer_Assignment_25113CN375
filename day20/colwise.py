mat1=[]
colwise=[]
row=int(input("enter the number of rows you want :-"))
col=int(input("enter the number of columns you want:-"))
print("MATRIX :-")
for mt1 in range(0,row):
    matrix1=[]
    for j in range(col):
      x=int(input("enter the elements in column:-"))
      matrix1.append(x)
    mat1.append(matrix1)

for i in range(col):
    ad=0
    for j in range (row):
        ad+=mat1[j][i]
    colwise.append(ad)   
print("MATRIX  IS:-")
for i in mat1:
    for elements in i:
     print(elements,end=" ")
    print() 
print("COLUMN-WISE SUM OF  MATRIX:-")        
for i in colwise:
        print(i)