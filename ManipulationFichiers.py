def ChargerFichierCSV(fileName):
    f = open(fileName, "r", encoding="utf-8")
    ligne = clean(f.readline())
    L=[]
    colonnes = ligne.split(";")
    for ligne in f:
        ligne=parseLine(ligne,colonnes)
        L.append(ligne)
    f.close()
    return L

def parseLine(ligne,colonnes):
    tab = clean(ligne).split(";")
    D = {}
    for i in range(len(tab)):
        D[colonnes[i]]=tab[i]
    return D

def clean(ch):
    ch = ch.replace("\n", "")
    ch = ch.replace(",", ".")
    ch = ch.replace("\ufeff", "")
    return ch

def calculerMoyenne(notes):
    for note in notes :
        note["Moyenne"]=str((float(note["Note1"])+float(note["Note2"]))/2)

def extractColonnes(data):
    R=list(data[0].keys())
    return R

def EnregistrerFichierCSV(fileName,data):
    f = open(fileName, "w", encoding="utf-8")
    colonnes = extractColonnes(data)
    f.write(";".join(colonnes) + "\n")
    for ligne in data[1:]:
        tab=[]
        for col in colonnes:
            tab.append(ligne[col])
        ch = ";".join(tab)
        f.write(ch + "\n")
    f.close()


notes=ChargerFichierCSV("./data/notes1.csv")
calculerMoyenne(notes)
EnregistrerFichierCSV("./data/Moyennes.csv", notes)
#print(notes)
