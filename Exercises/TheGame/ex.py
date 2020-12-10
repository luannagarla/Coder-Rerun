# Time ran out before this code ended.

N = int(input())

for c in range(0,N):
    f = str(input()).strip().lower().replace(" ", "")

    for palavra in f:
        if palavra != "jogo":
            f2 = [].append(palavra)
        if palavra == "jogo":
            f2 = [].append(palavra)
            break
        f2.strip().replace(" ", "")
    print(f"{len(f2)}")

    if 'jogo' in f:
        time = 0 
    else:
        print(f"{len(f)}")

