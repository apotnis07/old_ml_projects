import re

st = "This is a random statement for testing the the regular expression"

while True:
    print("1.To search")
    print("2.To match")
    print("3.To findall")
    print("4.Exit")
    ch = int(input("Enter the choice:"))
    if ch == 1:
        res = re.search(r't[\w]*', st)
        print(res.group())
    if ch == 2:
        res = re.match(r'This[\w]*', st)
        if res == "This":
            print(res)
        else:
            print(res.group())
    if ch == 3:
        res = re.findall(r'the[\w]*', st)
        print(res)
    if ch == 4:
        break
