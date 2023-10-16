class Livre:
    def __init__(self, titre,auteur):
        self.titre = titre
        self.auteur = auteur

class Auteur:
    def __init__(self, nom):
        self.nom = nom

auteur1 = Auteur("J.K. Rowling")
livre1= Livre("Harry Potter and the Sorcerer's Stone",auteur1)


class Bibliotheque:
    def __init__(self):
        self.collection = []
        
    def emprunter_livre(self, livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return f"{livre.titre} a ete emprunte"
        else:
            return "Le livre n'est pas disponible"
            
bibliotheque = Bibliotheque()
resultat = bibliotheque.emprunter_livre(livre1)

print(resultat)

        