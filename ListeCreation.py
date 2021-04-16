def createList(*T):
    L=[0]*T[0]
    if (len(T) >1) :
        for i in range(len(L)):
            L[i]=createList(*T[1:])
    return L


L1 = createList(4)
print(L1)   # ==> [0, 0, 0, 0]
L2 = createList(2, 4)
print(L2)   # ==> [[0, 0, 0, 0], [0, 0, 0, 0]]
L3 = createList(3, 2, 4)
print(L3)   # ==> [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
L4 = createList(2, 3, 2, 4)
print(L4)
