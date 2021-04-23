class personne:
    nbrInstance=0
    # constructeur
    def __init__(self,nom,prenom,age):
        self.nom=nom   #attribut d'instance
        self.prenom=prenom
        self.age=age
        if (self.age > 18):
            self.salaire = 1000
        personne.nbrInstance=personne.nbrInstance+1

    # methode d'instance
    def affiche(self):
        if (self.age > 18):
            print(self.nom, self.prenom, self.age, self.salaire)
        else:
            print(self.nom, self.prenom, self.age)

    # destructeur
    def __del__(self):
        print(self.nom, "est detruit")
        personne.nbrInstance = personne.nbrInstance - 1

print(personne.nbrInstance)
p1 = personne("n1", "p1", 15)
print(personne.nbrInstance, p1.nbrInstance)
p2 = personne("n2", "p2", 25)
print(personne.nbrInstance, p2.nbrInstance)
p3 = personne("n3", "p3", 25)
print(personne.nbrInstance, p3.nbrInstance)
p1.affiche()
del p1
print(personne.nbrInstance)

