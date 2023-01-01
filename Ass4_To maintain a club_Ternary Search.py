def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   print("Input roll numbers in sorted order")
   for i in range(n):
      x = int(input("Enter the  roll no of student %d : "%(i+1)))
      A.append(x)
   print("Student Info accepted successfully\n\n")
   return n

def display_array(A,n): 
   if(n == 0) :
      print("\nNo records in the database")
   else :
      print("Students  Array : ",end=' ')
      for i in range(n) :
         print("%d  "%A[i],end=' ')
      print("\n")

      
def Ternary_Search(A,l,r,key)  :
   if (r >= l) :
      mid1 = l + int((r - l) / 3)
      mid2 = r - int((r - l) / 3)
      if (A[mid1] == key) :
         return mid1
      if (A[mid2] == key) :
         return mid2
      if (key < A[mid1]) :
         return Ternary_Search(A,l, mid1 - 1, key)   #key lies between l & mid1
      elif (key > A[mid2]) :
         return Ternary_Search(A,mid2 + 1, r, key)  #key lies between mid2 & r
      else :
         return Ternary_Search(A,mid1 + 1, mid2 - 1, key) #key lies between mid1 & mid2       
   return -1   # Key not found


def Main() :   
   A = []
   while True :
      print ("\t1 : Accept & Display Students info ")      
      print ("\t2 : Ternary Search")
      print ("\t3 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 3):
         print ("End of Program")
         quit()
      elif (ch==1):
         A = []
         n = accept_array(A)
         display_array(A,n)
      elif (ch==2):
         X = int(input("Enter the roll_no to be searched : "))
         flag  = Ternary_Search(A,0,n-1,X)
         if(flag == -1) :
            print("\t%d Roll no is not a member of the club\n"%X)
         else :
            print("\t%d Roll no is a member of the club stored at location %d"%(X,flag + 1))
      else :
         print ("Wrong choice entered !! Try again")


Main()

