
def division(x,y):
    return x/y

def verifierParametre(f):
    def newFunction(x,y):
        if(y==0):
            print("y doit etre differente de zero")
        else:
            f(x,y)
    return newFunction

division=verifierParametre(division)

print(division(10,0))