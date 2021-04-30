class etudiant:
    def __init__(self,nom,note1,note2):
        self.nom=nom
        self.note1=note1
        self.note2=note2
        self.moyenne=str((float(note1)+float(note2))/2)

    def tocsv(self):
        return self.nom+";"+self.note1+";"+self.note2+";"+self.moyenne

    @staticmethod
    def clean(ch):
        ch = ch.replace("\n", "")
        ch = ch.replace(",", ".")
        ch = ch.replace("\ufeff", "")
        return ch

    @staticmethod
    def parseLine(ligne,colonnes):
        tab = etudiant.clean(ligne).split(";")
        D = {}
        for i in range(len(tab)):
            D[colonnes[i]]=tab[i]
        p=etudiant(D["Etudiant"], D["Note1"], D["Note2"])
        return p

    @staticmethod
    def loadfromfile(filename):
        f = open(filename, "r", encoding="utf-8")
        ligne = etudiant.clean(f.readline())
        L=[]
        colonnes = ligne.split(";")
        for ligne in f:
            p=etudiant.parseLine(ligne,colonnes)
            L.append(p)
        f.close()
        return L
    @staticmethod
    def savetofile(filename, data):
        f = open(filename, "w", encoding="utf-8")
        colonnes = "Etudiant;Note1;Note2;Moyenne"
        f.write(colonnes + "\n")
        for e in data:
            f.write(e.tocsv() + "\n")
        f.close()


#L=etudiant.loadfromfile("./data/notes1.csv")
#etudiant.savetofile("./data/Moyennes.csv", L)

etudiant.savetofile("./data/Moyennes.csv", etudiant.loadfromfile("./data/notes1.csv"))

#print(L)