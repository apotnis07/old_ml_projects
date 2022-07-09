import os
while True:
    print("1.Read contents of one file and write to another file")
    print("2.Append data at the end of existing file")
    print("3.Count the number of lines, words and characters in a file")
    print("4.Display files in a current directory")
    ch=int(input("Enter the choice"))
    if ch==1:
        f1=open("C:\\Users\\Admin\\Desktop\\Project\\testfile.txt",'r')
        f2=open("C:\\Users\\Admin\\Desktop\\Project\\New.txt",'w')
        st=f1.read()
        f2.write(st)
        f1.close()
        f2.close()
    elif ch == 2:
        f=open("C:\\Users\\Admin\\Desktop\\Project\\testfile.txt",'a+')
        st=input("Enter a string")
        f.write(st)
        f.seek(0,0)
        st=f.read()
        print(st)

    elif ch == 3:
        c=0
        w=0
        l=0
        f = open("C:\\Users\\Admin\\Desktop\\Project\\testfile.txt", 'r')
        for x in f:
            words=x.split()
            print(words)
            w+=len(words)
            c+=len(x)
            l+=1

        print("CHar:",c)
        print("word:",w)
        print("line:",l)