while True:
    print("1.Display Tuple")
    print("2.Print name, roll no, Marks of Python")
    print("3.Nested tuple")
    print("4.Exit")

    ch = int(input("Enter the choice"))
    tuple1=(1,"X",0,0,0)
    tuple2=(2,"B",1,2,3)
    tuple3=(3,"Python",5,6,7)
    if ch == 1:
        print(tuple1)
        print(tuple2)
        print(tuple3)
    elif ch==2:
        if "Python" in tuple1:
            print(tuple1)
        elif "Python" in tuple2:
            print(tuple2)
        elif "Python" in tuple3:
            print(tuple3)
    elif ch==3:
        tuple4=(tuple1,tuple2,tuple3)
        print("Unsorted tuple:\r")
        print(tuple4)
        tuple5=(sorted(tuple4,key=lambda x:x[1]))
        print("Sorted tuple:\r")
        print(tuple5)
    else:
        print("Invalid")

