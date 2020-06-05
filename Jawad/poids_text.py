
def nettoyer(texte): #tokenization
    import string
    return texte.translate(
        str.maketrans('’\n','  ', string.punctuation + '…\t' )
    )

def decouper(texte): #texte sans ponctuation
    return texte.split()

def trier(liste_mots):
    liste_mots.sort()

def occurences(liste_mots):
    D = {}
    for mot in liste_mots:
        D[mot.lower()] = 1 if mot.lower() not in D else D[mot.lower()]+1
    return D

def occurences_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8" ) as fichier :
        mots = decouper( nettoyer( fichier.read() ) )
        trier(mots)


        with open("alphabetic_"+ nom_fichier.split("/")[-1], 'w+', encoding="utf-8") as file:
            file.write('\n')
            for mot in mots: file.write( mot +'\n')

        dic  = occurences( mots )
        for cle in dic :
            if dic[cle]>1 : print(cle, ":", dic[cle])
