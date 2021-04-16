# passage de parametre Simple
def somme0(x, y):
    return x + y


# passage de parametre avec valeur par defaut
def somme1(x, y=0, z=0, w=0):
    return x + y + z + w

# appel de fonction avec nombre de parametres variable
def somme2(*T):
    s = 0
    print(T)
    for v in T:
         s = s + v
    return s

# appel de fonction avec des parametres nommes
def somme31(**D):
    s = 0
    print(D)
    for k in D:
        s = s + D[k]
    return s

# appel de fonction avec des parametres nommes
def somme32(**D):
    print(D)
    x = D.get("x", 0)
    y = D.get("y", 0)
    z = D.get("z", 0)
    w = D.get("w", None)
    if(w == None):
        print("erreur : le parametre w est obligatoire")
        raise ValueError("erreur : le parametre w est obligatoire")

    s = x + y + z + w
    return s

# print(somme0(5, 10))

#print(somme1(5, 10, 10))

#print(somme2(5, 10, 10, 25))

print(somme31(x=5, w=10, y=10, z=25))
print(somme32(y=10, z=25, x=5))
