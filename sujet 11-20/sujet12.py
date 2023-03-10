"""
Écrire une fonction récursive ajoute(cle,a) qui prend en paramètres une clé cle 
et un arbre binaire de recherche a, et qui renvoie un arbre binaire de recherche dans 
lequel cle a été insérée. 
Dans le cas où cle est déjà présente dans a, la fonction renvoie l’arbre a inchangé. 

"""

class ABR:
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self is None:
            return ''
        else:
            return '(' + (self.gauche).__repr__() + ',' + str(self.cle) + ',' +(self.droit).__repr__() + ')'
            
n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
n3 = ABR(n0, 1, n2)

def ajoute(cle,a):
    if a is None:
        a=ABR(None,cle,None)
    elif cle>a.cle:
        a.droit=ajoute(cle,a.droit)
    else:
        a.gauche=ajoute(cle,a.gauche)
    return a

a = ajoute(4, n3)
a
