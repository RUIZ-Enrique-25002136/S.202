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

def creeMatriceAleatoire (i):
    return np.random.rand(i);

def puissanceIteree (A,e) :
    Xn = Xo.copy()
    XnOld = np.zeros(len(A))
    if (estStochastique(A)) :
        while (norme(Xn - XnOld) > e) :
            XnOld = Xn.copy()
            AXn = A.dot(Xn)
            Xn = AXn.copy()
        return Xn
    else :
        while (norme(Xn - XnOld) > e) :
            XnOld = Xn.copy()
            AXn = A.dot(Xn)
            Xn = AXn / norme(AXn)
        return Xn

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
        if (temp != 1):
            return False
    return True

def transposee(A) :
    return A.T

def solutionEquation(V,W) :
    return norme(V - W)

# r est notre vecteur retourné dans l'algorithme ci-dessus
def verification(Q,e) : 
    r = puissanceIteree(Q,e)[0]
    # r est notre vecteur retourné dans l'algorithme ci-dessus
    R = solutionEquation(r, Q.dot(r))
    #R va nous afficher l'écart (sensé tendre vers le nul) entre r et Q*r
    if (R > 1e-5):     #ici, 1e-5 est la marge d'erreur
        return "le vecteur retourné n'est pas solution de l'équation : r = Qr", R
    else : 
        return "le vecteur retourné est solution de l'équation : la norme de r = Qr = ", R
    
def matriceTransition(A,B) :
    a = 0.85
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
    r = puissanceIteree(Q,e)[0]
    # r est notre vecteur retourné dans l'algorithme ci-dessus
    return solutionEquation(r, Q.dot(r))

def partie3() :
    C = np.array(
        [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
    ,dtype = float)
    
    D = np.array([
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
     ,dtype=float)
    
    E = np.array([
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]],dtype=float)
    
    F = np.array([
     [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],ss
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]],dtype = float)
    
    Xo = creeMatriceAleatoire(len(A))
    
    e = 10**(-10)
    
    P = matriceTransition(transposee(A),stochastique(transposee(A)))
    Q = matriceTransition(transposee(C),stochastique(transposee(C)))
    R = matriceTransition(transposee(D),stochastique(transposee(D)))
    S = matriceTransition(transposee(E),stochastique(transposee(E)))
    T = matriceTransition(transposee(F),stochastique(transposee(F)))
    
    print ("\nSans HUB ni trucs :\n")
    print (puissanceIteree (P,e))
    print("\nEn ajoutant un HUB pointé par aucune page :\n")
    print (puissanceIteree (Q,e))
    print("\nEn ajoutant 2 HUB pointés par aucune page :\n")
    print (puissanceIteree (R,e))
    print("\nEn ajoutant un TRUC ne pointant aucune page:\n")
    print (puissanceIteree (S,e))
    print("\nEn ajoutant 2 TRUC ne pointant aucune page:\n")
    print (puissanceIteree (T,e))