copo = [0,0,0]

def m1():
    aux = copo[1]
    copo[1] = copo[0]
    copo[0] = aux; 

def m2():
    aux = copo[2]
    copo[2] = copo[1]
    copo[1] = aux

def m3():
    aux = copo[2]
    copo[2] = copo[0]
    copo[0] = aux; 

n = int(input())
L = str(input())

if (L == 'A'):
    copo[0] = 1
elif(L == 'B'):
    copo[1] = 1
elif(L == 'C'):
    copo[2] = 1

for c in range(0,n):
    aux = int(input())
    if (aux == 1):
        m1()
    elif(aux == 2):
        m2()
    elif(aux == 3):
        m3()

if (copo[0] == 1):
    print("A")
elif(copo[1] == 1):
    print("B")
else:
    print("C")
