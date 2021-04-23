class personne:
    # constructeur
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        if (self.age > 18):
            self.salaire = 1000

    # methode d'instance
    def affiche(self):
        if (self.age > 18):
            print(self.nom, self.prenom, self.age, self.salaire)
        else:
            print(self.nom, self.prenom, self.age)

    # destructeur
    def __del__(self):
        print(self.nom, "est detruit")


p = personne("n1", "p1", 15)
p.affiche()
p = personne("n2", "p2", 25)
p.affiche()
x=input("zzz")
