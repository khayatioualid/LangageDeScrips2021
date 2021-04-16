def createList1D(d1):
    return [0]*d1
def createList2D(d1,d2):
    L=createList1D(d1)
    for i in range(len(L)):
        L[i]=createList1D(d2)
    return L
def createList3D(d1, d2, d3):
    L=createList1D(d1)
    for i in range(len(L)):
        L[i]=createList2D(d2, d3)
    return L
def createList4D(d1,d2, d3, d4):
    L=createList1D(d1)
    for i in range(len(L)):
        L[i]=createList3D(d2, d3, d4)
    return L

print(createList4D(2, 3, 2, 4))
"""
L1 = createList(4)
print(L1)   # ==> [0, 0, 0, 0]
L2 = createList(2, 4)
print(L2)   # ==> [[0, 0, 0, 0], [0, 0, 0, 0]]
L3 = createList(3, 2, 4)
print(L2)   # ==> [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
"""