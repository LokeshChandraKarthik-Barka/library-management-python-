print('''MAIN MENU
To add book enter 1
To view books enter 2
To serch books enter 3
To borrow book enter 4
To return book enter 5
To remove book enter 6
# ''')
library={}
borrowedbooks={}
#1 adding book to library
n=int(input("enter refering above:"))
if n==1:
    title=input("\nenter title of the book:")
    author=input("\nenter author of the book:")
    isbn=input("\nenter ISBN of the book:")
    no=input("\nenter no of books:")
    def addBook(lib,title,author,isbn,no):
        d={
            'title':title,
            'author':author,
            'isbn':isbn,
            'available books':no
        }
        lib[isbn]=d
    addBook(library,title,author,isbn,no)
    f=open('library.txt','a')
    for i in library:
        for j in library[i]:
            f=open('library.txt','a')
            f.write(library[i][j]+" ")
        f.write("\n")
        

#2 view books
if n==2:
    j=0
    f=open('library.txt','r')
    a=f.readlines()
    for i in a:
        j+=1
        b=i.split()
        print(j,".","title:",b[0]," ","author:",b[1]," ","isbn:",b[2]," ","available books:",b[3])
    print()    
    
#3 search books
if n==3:
    isbn=input("\nenter the isbn of the book you want to search:")
    f=open('library.txt','r')
    a=f.readlines()
    for i in a:
        b=i.split()
        if isbn==b[2]:
            print("title:",b[0]," ","author:",b[1]," ","isbn:",b[2]," ","available books:",b[3])
# #4 borrow books
if n==4:
    name=input("\nenter name:")
    rollno=input("\nenter your roll no:")
    book=input("\nenter book name:")
    isbn=input("\nenter book isbn:")
    no=input("\nenter no of books you need:")
    def borrowBook(lib,isbn,book,name,rollno,no):
        c={
            'isbn':isbn,
            'book':book,
            'name':name,
            'rollno':rollno,
            'no':no
         }
        lib[isbn]=c
    borrowBook(borrowedbooks,isbn,book,name,rollno,no)
    f=open('borrowedBooks.txt','a')
    for i in borrowedbooks:
        for j in borrowedbooks[i]:
            f=open('borrowedBooks.txt','a')
            f.write(borrowedbooks[i][j]+" ")
        f.write("\n")
    f=open("library.txt",'r')
    a=f.readlines()
    f=open("library.txt",'w')
    for i in a:
        b=i.split()
        if isbn!=b[2]:
            f.write(i)
    for i in a:
        b=i.split()
        if isbn==b[2]:
            if int(b[3])-int(no)>=0:
                k=int(b[3])-int(no)
                b[3]=str(k)
                f.write("\n")
                for j in b:
                    f.write(j+" ")
                print("\nborrowed status successfully uploaded")
            else:
                print("\nsorry only ",b[3]," books are available")
                f.write(i)
#return book:
if n==5:
    isbn=input("\nenter isbn of book:")
    rollno=input("\nenter your rollno:")
    no=int(input("\nenter no of books you are returning:"))
    f=open('borrowedBooks.txt','r')
    a=f.readlines()
    f=open('borrowedBooks.txt','w')
    for i in a:
        b=i.split()
        if isbn!=b[0] or rollno!=b[3]:
            f.write(i)
    f=open("library.txt",'r')
    a=f.readlines()
    f=open("library.txt",'w')
    for i in a:
        b=i.split()
        if isbn!=b[2]:
            f.write(i)
    for i in a:
        b=i.split()
        if isbn==b[2]:
            if int(b[3])-int(no)>=0:
                k=int(b[3])+int(no)
                b[3]=str(k)
                f.write("\n")
                for j in b:
                    f.write(j+" ")
                print("\nreturned status successfully uploaded")
            else:
                print("\nsorry only ",b[3]," books are available")
                f.write(i)
#6 remove book
if n==6:
    password='1234'
    p=input("enter password:")
    isbn=input("\nenter isbn of the book to be removed:")
    if p==password:
        f=open("library.txt",'r')
        a=f.readlines()
        f=open("library.txt",'w')
        for i in a:
            b=i.split()
            if isbn!=b[2]:
                f.write(i)
# isbn=input("enter book isbn:")
# no=int(input("enter no of books you need:"))
# f=open("library.txt",'r')
# a=f.readlines()
# f=open("library.txt",'w')
# for i in a:
#     b=i.split()
#     if isbn!=b[2]:
#         f.write(i)
# for i in a:
#     b=i.split()
#     if isbn==b[2]:
#         if int(b[3])-no>=0:
#             k=int(b[3])-no
#             b[3]=str(k)
#             f.write("\n")
#             for j in b:
#                 f.write(j+" ")
#             print("borrowed status successfully uploaded")
#         else:
#             print("sorry only ",b[3]," books are available")
#             f.write(i)
