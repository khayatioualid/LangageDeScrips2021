from functools import reduce

L=[x for x in range(100)]
Limpaire=[x for x in range(100) if x%2!=0]
#L=[expression en fonction de x pour x dans une sequence eventuellement vérifiant une certaine condition]
print(L)
print(Limpaire)

s=reduce(lambda x,y:x+y,L)
#p=reduce(lambda x,y:x*y,Limpaire)
p=reduce(lambda x,y:x*y,[x for x in range(100) if x%2!=0])
print(s)
print(p)
"""
L1=list(map(lambda x:2*x,L))
print(L1)
"""
m=map(lambda x:2*x,L)
for v in m:
    print(v)

L1=[1,2,3,4]
L2=[10,20,30,40]
L3=[100,200,300,400]
LR=list(zip(L1,L2,L3))
print(LR)