def longestword():
    str=input("Enter a string: ")
    long = ""
    i = 0
    while(i < len(str)):
        str1 = ""
        if(i != len(str)):
            while(str[i] == " "):
                i=i+1
        while(str[i] != " "):    
            str1 = str1 + str[i]
            i=i+1
            if(i == len(str)):
                break
        if(len(str1)>len(long)):        
            long = str1
    print("Longest word is:",long) 

def character():
    str1 = input("Enter the string: ")
    char = input("Enter the character: ")
    print(str1)
    counter = 0
    for i in range(len(str1)):
        if char == str1[i]:
            counter = counter + 1
    print("The occrurance of ",char," is: ",counter)


def palindrome():
    str2 = input("Enter string: ")
    lenstr2 = len(str2)
    j = lenstr2 - 1
    flag = 0
    for i in range(int(lenstr2 / 2 + 1)):
        if (str2[i] == str2[j]):
            j -= 1
            flag = 1
        else:
            flag = 0
            break
            

    if (flag == 1):
        print("Entered string is Palindrome")
    else:
        print("Entered string is not Palindrome")


def substring():
    str1 = input("Enter the string: ")
    sub1 = input("Enter the substring: ")
    m = len(sub1)
    n = len(str1)
    if(n>=m):
        for i in range((n-m+1)):
            I=1
            for j in range(m):
                if(str1[i+j]!=sub1[j]):
                    I=0
                    break
            if(I==1):
                print("Index of the substring is: ",i)
                break
        if(I==0):
            print("Not found")


def occword():
    str = input("Enter the string:")
    i=0
    word_array=[]
    count=[]
    while(i<len(str)):
        word=""
        while(str[i]!=" "):
            word+=str[i]
            i=i+1
            if(i==len(str)):
                break
        if(i!=len(str)):
            while(str[i]==" "):
                i=i+1
        if(len(word_array)==0):
            word_array.append(word)
            count.append(1)
        else:
            flag=1
            for j in range(len(word_array)):
                if(word_array[j]==word):
                    count[j]+=1
                    flag=0
                    break
            if(flag==1):
                word_array.append(word)
                count.append(1)
    for i in range(len(word_array)):
        print("\t%15s : %d "%(word_array[i],count[i]))


while True:
    print("\n1. To display word with the longest length\
           \n2. To determine the frequency of occurrence of particular character in the string\
           \n3. To check whether the given string is palindrome or not\
           \n4. To display index of first appearance of the substring\
           \n5. To count the occurance of each word in a given string\
           \n6. Exit")

    ch = int(input("Enter your choice:"))
    if (ch == 1):
        print("To display word with the longest length: ")
        longestword()
    elif (ch == 2):
        print("To determine the frequency of occurrence of particular character in the string: ")
        character()
    elif (ch == 3):
        print("To check whether the given string is palindrome or not: ")
        palindrome()
    elif (ch == 4):
        print("To display index of first appearance of the substring: ") 
        substring()
    elif (ch == 5):
        print("To count the occurance of each word in a given string: ")
        occword()
    elif (ch == 6):
        print("You've exited from the program!")
        break