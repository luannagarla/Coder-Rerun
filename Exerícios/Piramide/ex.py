a,b,c,d = input().split(" ") 

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a+b+c+d != 0):
    res = ((a/2) + b) * c / d
    print(f"{res:.5f}")

