

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

def bigrammes():
    L = []
    A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(A)):
        for k in range(len(B)):
            L.append(A[i] + B[k])
    return L

print(bigrammes())

def motsCommun(t1,t2):
   L = t1.split()
   M = t2.split()
   R = []
   for i in range(len(L)):
       for j in range(len(M)):
           if L[i] == M[j]:
               R.append(L[i])
   return R

print(motsCommun("Python est un langage de programmation","Python est orienté objet"))

def indexImpair(s):
    s = list(s)
    for i in range(len(s)):
        if i % 2 != 0:
            s[i] = '#'
    return ''.join(s)

print(indexImpair("jqsfdjoijr"))

def compte_mots_ligne(s1):
    dic = {}
    for i in range(len(s1)):
        dic[s1[i]]=0
        for j in range(len(s1)):
            if s1[i] == s1[j]:
                dic[s1[i]]+=1
    return dic
print(compte_mots_ligne("sjdfhrehfrhe"))

def equivalent(L1,L2):
    M=[]
    if len(L1)<len(L2):
        for i in range(len(L1)):
            L = []
            for j in range(len(L2)):
                L.append(L1[i] == L2[j])
            if True in L:
                M.append(True)
            else:
                M.append(False)
    else:
        for i in range(len(L2)):
            L = []
            for j in range(len(L1)):
                L.append(L2[i] == L1[j])
            if True in L:
                M.append(True)
            else:
                M.append(False)
    return not(False in M)




print(equivalent([1,2,3,33],[1,3,2,33,33]))

