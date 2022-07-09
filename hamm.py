print("Hamming code")
print("by even parity")
a = [0]*8
#0  1   2   3   4   5   6   7
#p1 p2  d3  p4  d5  d6  d7  p8

a[2] = int(input("Enter the first bit of the number"))
a[4] = int(input("Enter the second bit of the number"))
a[5] = int(input("Enter the third bit of the number"))
a[6] = int(input("Enter the last bit of the number"))

print(a)


x = a[2] + a[4] + a[6]
if x%2 == 0:
    a[0] = 0
else:
    a[0] = 1

y = a[2] + a[5] + a[6]
if y%2 == 0:
    a[1] = 0
else:
    a[1] = 1

z = 





