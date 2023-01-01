def accept_array(A):
    n=int(input("Enter the total no. of students: "))
    for i in range(n):
        x=float(input("Enter the percentage of students of class 12th %d: "%(i+1)))
        A.append(x)
    print("Array accepted successfully\n\n");
    
def display_array(A):
    n=len(A)
    if(n==0):
        print("\nNo Records in the database")
    else:
        print("Array of 12th class percentage scored by student: ",end=' ')
        for i in range(n):
            print("%.2f "%A[i],end=' ')
        print("\n");
        
def find_max_digit(A,n):
    max_element=max(A)
    count=0
    while(max_element>0):
        count=count+1
        max_element=max_element//10
    return count

def combinebucket(A,B):
    c=0
    for i in range(10):
        for j in range(len(B[i])):
            A[c]=B[i][j]
            c=c+1

def initialize_bucket(B):
    for i in range(10):
        T=[]
        B.append(T)
                       
def Bucket_sort(A,n):
    shift=1
    keysize=find_max_digit(A,n)
    for loop in range(keysize):
        B=[]
        initialize_bucket(B)
        for i in range(n):
            b_no=int((A[i]/shift)) % 10
            B[b_no].append(A[i])
        combinebucket(A,B)
        shift=shift*10 
                       
def Main():
    A=[]
    while True:
        print("\t1 : Accept & display students FE marks")
        print("\t2 : Bucket sort ascending order and display top five scores")
        print("\t3 : Exit")
        choice=int(input("Enter your choice: "))
        if(choice==3):
            print("End of program")
            quit()
        elif(choice==1):
            A=[]
            accept_array(A)
            display_array(A)
        elif(choice==2):
            print("Marks before sorting")
            display_array(A)
            n=len(A)
            Bucket_sort(A,n)
            print("Marks after sorting")
            display_array(A)
            if(n>=5):
                    print("Top five scores: ")
                    for i in range(n-1,n-6,-1):
                        print("\t%.2f"%A[i])
            else:
                print("Top scorers: ")
                for i in range(n-1,-1,-1):
                    print("\t%.2f"%A[i])
        else:
            print("Wrong choice entered!! Try again.")
                       

Main()