from numpy.random import randint 
import numpy as np
from math import sqrt

def norme(X) :
    return np.sqrt(np.sum(X**2))

A = np.array([
 [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]],dtype = float)

a = 0.85

def creeMatriceAleatoire (i):
    return np.random.rand(i)

def puissanceIteree (A,e,Xo) :
    Xn = Xo.copy()
    XnOld = np.zeros(len(A))
    if (estStochastique(A)) :
        while (norme(Xn - XnOld) > e) :
            XnOld = Xn.copy()
            AXn = A.dot(Xn)
            Xn = AXn.copy()
        return Xn;
    else :
        while (norme(Xn - XnOld) > e) :
            XnOld = Xn.copy()
            AXn = A.dot(Xn)
            Xn = AXn / norme(AXn)
        return Xn;

def stochastique(A) :
    for i in range (A.shape[0]):
        temp = 0
        for j in range (A.shape[0]) :
            if (A[j][i] == 1) :
                temp += 1
        for k in range (A.shape[0]) :
            if (A[k][i] == 1) :
                A[k][i] /= temp
    return A

def estStochastique(A) :
    for i in range (A.shape[0]):
        temp = 0
        for j in range (A.shape[0]) :
            temp += A[j][i]
        if (temp != 1.0):
            return False
    return True

def transposee(A) :
    return A.T

def solutionEquation(V,W) :
    return norme(V - W)

# r est notre vecteur retourné dans l'algorithme ci-dessus
def verification(Q,e,Xo) : 
    r = puissanceIteree(Q,e,Xo)
    # r est notre vecteur retourné dans l'algorithme ci-dessus
    R = solutionEquation(r, Q.dot(r))
    #R va nous afficher l'écart (sensé tendre vers le nul) entre r et Q*r
    if (R > 1e-5):     #ici, 1e-5 est la marge d'erreur
        return "le vecteur retourné n'est pas solution de l'équation : r = Qr", R
    else : 
        return "le vecteur retourné est solution de l'équation : la norme de r = Qr = ", R
    
def matriceTransition(A,B,a) :
    M = np.zeros((A.shape[0],A.shape[0]))
    for i in range (A.shape[0]):
        for j in range (A.shape[0]) :
            if (sommeTableau(j,A) != 0):    
                M[i][j] = a*B[i][j] + (1-a)/A.shape[0]
            else:
                M[i][j] = 1/A.shape[0]
    return M            

def sommeTableau(j,A) :
    temp = 0
    for i in range (A.shape[0]):
        temp += A[i][j]
    return (temp)

def equation(Q,e) : 
    r = puissanceIteree(Q,e)
    # r est notre vecteur retourné dans l'algorithme ci-dessus
    return solutionEquation(r, Q.dot(r))



def partie3() :
    H1 = np.array([
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
             ,dtype = float)
    
    #ajout de 2 hubs pointés par aucune page 
    
    H2 = np.array([
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
         ,dtype=float)
    
    #ajout d'une autoritée ne pointant aucune page 
    
    A1 = np.array([
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
         ,dtype=float)
    
    #ajout de 2 autorités ne pointant aucune page 
    
    A2 = np.array([
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
         ,dtype = float)
    
    M = matriceTransition(transposee(A),stochastique(transposee(A)),a)
    MH1 = matriceTransition(transposee(H1),stochastique(transposee(H1)),a)
    MH2 = matriceTransition(transposee(H2),stochastique(transposee(H2)),a)
    MA1 = matriceTransition(transposee(A1),stochastique(transposee(A1)),a)
    MA2 = matriceTransition(transposee(A2),stochastique(transposee(A2)),a)
    
    Xo = creeMatriceAleatoire(14)
    print("\nPour une matrice sans hub ni autorité :\n")
    print (puissanceIteree (M,e,Xo))
    
    Xo = creeMatriceAleatoire(15)
    print("\nEn ajoutant un hub pointé par aucune page :\n")
    print (puissanceIteree (MH1,e,Xo))
    
    Xo = creeMatriceAleatoire(16)
    print("\nEn ajoutant 2 hubs pointés par aucune page :\n")
    print (puissanceIteree (MH2,e,Xo))
    
    Xo = creeMatriceAleatoire(15)
    print("\nEn ajoutant une autorité ne pointant aucune page:\n")
    print (puissanceIteree (MA1,e,Xo))
    
    Xo = creeMatriceAleatoire(16)
    print("\nEn ajoutant 2 autorités ne pointant aucune page:\n")
    print (puissanceIteree (MA2,e,Xo))
    print("\n")

e = 10**(-10)
a= 0.85

Xo = creeMatriceAleatoire(len(A))
print (Xo)
print (puissanceIteree(matriceTransition(transposee(A),stochastique(transposee(A)),a),e,Xo))
print (verification(stochastique(transposee(A)),e,Xo))