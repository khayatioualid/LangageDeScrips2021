class Vecteur:
    def __init__(self, *T):
        self.valeurs=T
    def __add__(self, other):
        if(type(other)!=Vecteur):
            print("erreur une valeur vecteur est attendue.")
        if(len(self.valeurs)!=len(other.valeurs)):
            print("erreur de dimension")
            return None
        R=[0]*len(self.valeurs)
        for i in range(len(self.valeurs)):
            R[i]=self.valeurs[i]+other.valeurs[i]
        V=Vecteur(*R)
        return V

    def __mul__(self, other):
        if(type(other)!=Vecteur):
            print("erreur une valeur vecteur est attendue.")
        if(len(self.valeurs)!=len(other.valeurs)):
            print("erreur de dimension")
            return None
        R=[0]*len(self.valeurs)
        for i in range(len(self.valeurs)):
            R[i]=self.valeurs[i]*other.valeurs[i]
        V=Vecteur(*R)
        return V
    def __pow__(self, power, modulo=None):
        R = [0] * len(self.valeurs)
        for i in range(len(self.valeurs)):
            R[i] = self.valeurs[i] ** power
        V = Vecteur(*R)
        return V

    def affiche(self):
        print(self.valeurs)



v1 = Vecteur(1, 2, 3)
v2 = Vecteur(3, 2, 1)
v3 = v1 + v2 # v3 = v1.__add__(v2)
v3.affiche()
v4 = v1 * v2 # v3 = v1.__add__(v2)
v4.affiche()
v5=v1**0.5
v5.affiche()