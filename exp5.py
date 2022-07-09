mydict={}
list1=[1,2,3]
list2=[4,5,6]
def create():
    n=int(input("Enter the number of elements"))
    for i in range(n):
        key=input("Enter the key value")
        value=int(input("Enter the value"))
        mydict[key]=value
    print(mydict)

def update():
    print(mydict.keys())
    key = input("Enter the key value")
    value = int(input("Enter the value"))
    mydict[key] = value
    print(mydict)

while True:
    print("1.Create a dictionary")
    print("2.Update")
    print("3.Map two list into dictionary")
    ch=int(input("Enter your choice"))
    if ch==1:
        create()
    elif ch==2:
        update()
    elif ch==3:
        key1=input("Enter the key for list 1")
        mydict[key1]=list1
        print(mydict)
        key2 = input("Enter the key for list 2")
        mydict[key2] = list2
        print(mydict)

