def somme(a,b):
    return a+b

def produit(a,b):
    return a*b

def applyFunction(L,f):
    r=L[0]
    for v in L[1:]:
        r=f(r,v)
    return r

L=[1,2,3,4,5,6,7,8,9]

print(applyFunction(L, somme))
print(applyFunction(L, lambda x, y: x+y))
print(applyFunction(L, produit))
print(applyFunction(L, lambda x, y: x*y))

