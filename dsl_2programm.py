print("Enter the no. of rows & no. of columns of 1st matrix: ")
r1=int(input("No. of rows of 1st matrix: "))
c1=int(input("No. of columns of 1st matrix: "))
print("Enter the elements of the 1st matrix")
FirstMatrix=[]
for i in range(r1):
    ElementsOfMatrix1=[]
    for j in range(c1):
        elements1=int(input())
        ElementsOfMatrix1.insert(j,elements1)
    FirstMatrix.insert(i,ElementsOfMatrix1)
print("The 1st matrix is:")
for i in range(r1):
    for j in range(c1):
        print(FirstMatrix[i][j],end=' ')
    print()


#Taking second matrix from user

print("Enter the no. of rows & no. of columns of 2nd matrix: ")
r2=int(input("No. of rows of 2nd matrix:"))
c2=int(input("No. of columns of 2nd matrix: "))
print("Enter the elements of the 2nd matrix")
SecondMatrix=[]
for i in range(r2):
    ElementsOfMatrix2=[]
    for j in range(c2):
        elements2=int(input())
        ElementsOfMatrix2.insert(j,elements2)
    SecondMatrix.insert(i,ElementsOfMatrix2)
print("The 2nd matrix B is:")
for i in range(r2):
    for j in range(c2):
        print(SecondMatrix[i][j],end=' ')
    print()


#Asking user the operation he wants to perform

print("Enter 1 for the addition of two matrices\n",
      "Enter 2 for substraction of two matrices\n",
      "Enter 3 for multiplication of two matrices\n",
      "Enter 4 for transpose of the matrix\n")
operation=int(input("Enter the no.: "))


#Addition

if operation==1:
    AdditionOfMatrix=[]
    if r1==r2 and c1==c2:
        for i in range(r1):
            add=[]
            for j in range(c1):
               x=FirstMatrix[i][j]+SecondMatrix[i][j]
               add.insert(j,x)
            AdditionOfMatrix.append(add)
        print("The addition of two matrix is:")
        for i in range(r1):
            for j in range(c1):
                print(AdditionOfMatrix[i][j], end=' ')
            print()
    else:
        print("The no. of rows & columns must be equal of both the matrices for addition.Please try again.")


#Substraction

if operation==2:
    SubstractionOfMatrix=[]
    if r1==r2 and c1==c2:
        for i in range(r1):
            sub=[]
            for j in range(c1):
                x=FirstMatrix[i][j]-SecondMatrix[i][j]
                sub.insert(j,x)
            SubstractionOfMatrix.append(sub)
        print("The sunstraction of two matrix is:")
        for i in range(r1):
            for j in range(c1):
                print(SubstractionOfMatrix[i][j], end=' ')
            print()
    else:
        print("The no. of rows & columns must be equal of both the matrices for substraction.Please try again.")


#Multiplication

if operation==3:
    MultiplicationOfMatrix=[]
    for i in range(r1):
        u = []
        for j in range(c1):
            result=0
            for k in  range(c1):
                result=result+FirstMatrix[i][k]*SecondMatrix[k][j]
            u.insert(j,result)
        MultiplicationOfMatrix.insert(i,u)
    print("The multiplication of the two matrices is:")
    for i in range(r1):
        for j in range(c1):
            print(MultiplicationOfMatrix[i][j], end=' ')
        print()
#Transpose of matrix
if operation==4:

    print("The 1st matrix A is:")
    for i in range(r1):
        for j in range(c1):
            print(FirstMatrix[i][j], end=' ')
        print()
    print("The transpose of 1st matrix A is: ")
    for i in range(r1):
        for j in range(c1):
            print(FirstMatrix[j][i], end=' ')
        print()
    print("The 2nd matrix B is:")
    for i in range(r2):
        for j in range(c2):
            print(SecondMatrix[i][j], end=' ')
        print()
    print("The transpose of 2nd matrix B is:")
    for i in range(r2):
        for j in range(c2):
            print(SecondMatrix[j][i], end=' ')
        print()