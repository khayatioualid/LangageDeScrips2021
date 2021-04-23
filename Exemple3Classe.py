class personne:
    nbrInstance=0
    # constructeur
    def __init__(self,nom,prenom,age):
        self.nom=nom   #attribut d'instance
        self.prenom=prenom
        self.age=age
        if (self.age > 18):
            self.salaire = 1000
            self.affiche = self.afficheMajeur
        else:
            self.affiche = self.afficheMineur
        personne.nbrInstance=personne.nbrInstance+1

    """
    # methode1
    def affiche(self):
        if (self.age > 18):
            self.afficheMajeur()
        else:
            self.afficheMineur()
    """
    def afficheMajeur(self):
        print(self.nom, self.prenom, self.age, self.salaire)
    def afficheMineur(self):
        print(self.nom, self.prenom, self.age)
    # destructeur
    def __del__(self):
        print(self.nom, "est detruit")
        personne.nbrInstance = personne.nbrInstance - 1

print(personne.nbrInstance)
p1 = personne("n1", "p1", 15)
p1.affiche()
p2 = personne("n2", "p2", 25)
p2.affiche()
print(personne.nbrInstance, p2.nbrInstance)





