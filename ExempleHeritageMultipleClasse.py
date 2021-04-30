class personne:
    nbrInstance = 0

    # constructeur
    def __init__(self, nom, prenom, age):
        self.nom = nom  # attribut d'instance
        self.prenom = prenom
        self.age = age
        if (self.age > 18):
            self.salaire = 1000
        personne.nbrInstance = personne.nbrInstance + 1

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


class bachelier:
    def __init__(self, moyennebac):
        self.moyennebac = moyennebac

    def affiche(self):
        print(self.moyennebac)


class etudiant(bachelier, personne ):
    def __init__(self, nom, prenom, age, specialite,moyennebac):
        # methode1 appel direct
        personne.__init__(self, nom, prenom,age)
        bachelier.__init__(self, moyennebac)

        self.specialite = specialite


print(personne.nbrInstance)
p1 = personne("n1", "p1", 15)
#personne.affiche(p1)

p1.affiche()
e1 = etudiant("en1", "ep1", 15, "ingenieur",15)
e1.affiche()

