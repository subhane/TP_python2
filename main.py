a = (1, 2, 3, 4)

b= [1, 2, 3, 4]

c = {"djessy": 12, "walid": 14}

def armstrong(n):
    L = []
    for i in range(1, n+1):
        a = str(i)
        S = []
        z = 0
        for k in range(len(a)):
            z = z + int(a[k])**3
            if i == z:
                L.append(i)
    return L

print(armstrong(2000))




