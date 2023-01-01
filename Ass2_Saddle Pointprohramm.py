M=[]
def matrix(M):
    print("enter order of matrix:-")
    r=int(input("enter the number of rows : "))
    c=int(input("enter the number of columns : "))
    print("Enter the elemnets of matrix:-\n")

    for i in range(r):
        row = []
        for j in range(c):
            y=int(input())
            row.append(y)
        M.append(row)
    print("matrix accepted")
    
    
def display(M,r,c):
    for i in range(r):
        
        for j in range(c):
            print(M[i][j],end=" ")
        print()

def saddle_point(M,r,c): 
    count=0;
    for i in range(r):                                      #to find minimun element of the row
        min=M[i][0]

        ci=0

        for j in range(1,c):
            if  (min > M[i][j]):
                min=M[i][j];
                ci=j;                                       #to check if minimun element in the row is also the
                                                            # maximun element in the column
        flag=1
        for ri in range(r):
            if (min < M[ri][ci]):
                flag=0
                break
        if (flag==1):
            count+=1
            print(min,"is the saddle point in the given matrix")    
    if(count==0):
        print("No saddle point found in the given matrix")
    else:
        print("saddle point found in the given matrix")    
def main():
    while True :
        print(" 1. To accept the matrix")
        print(" 2. To display the Matrix")
        print(" 3. To find saddle point of the given Matrix")
        print(" 4. Exit ")
        ch = int(input("Enter your Choice : "))
        if (ch==4):
            print("End the program")
            break;
        elif (ch==1):
            M =[]
            print("input matrix")
            matrix(M)
            r=len(M)
            c=len(M[0])
        elif (ch==2):
            display(M,r,c)
        elif (ch==3):
            display(M,r,c)
            saddle_point(M,r,c)

        else:
            print("Please enter the correct choice")
main()