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

B =np.array([[0,0,0,0,0],
 [1,0,0,0,0],
 [1,0,0,1,0],
 [1,1,0,0,0],
 [1,1,0,0,0]],dtype = float)

def puissanceIteree (A,e) :
    Xn = np.random.rand(len(A))
    XnOld = 0
    while (norme(Xn - XnOld) > e) :
        XnOld = Xn
        AXn = A.dot(Xn)
        Xn = AXn / norme(AXn)
    return Xn, norme(A.dot(Xn))

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

def matriceTransistion(A) :
    a = 0.85
    M = np.zeros((A.shape[0],A.shape[0]))
    for i in range (A.shape[0]):
        for j in range (A.shape[0]) :
            if (sommeTableau(j,A) != 0):    
                M[i][j] = a*A[i][j] + (1-a)/A.shape[0]
            else:
                M[i][j] = 1/A.shape[0]
    return M       

def transposee(A) :
    return A.T

def sommeTableau(j,A) :
    temp = 0
    for i in range (A.shape[0]):
        temp += A[i][j]
    return (temp)
    

Q = (stochastique(transposee(A)))
print(Q)

def verification(Q,e = 1e-10) : 
    r = puissanceIteree(Q,e)[0]
    # r est notre vecteur retourné dans l'algorithme ci-dessus
    R = norme(r - Q.dot(r))
    #R va nous afficher l'écart (sensé tendre vers le nul) entre r et Q*r
    if (R > 1e-5):     #ici, 1e-10 est la marge d'erreur
        return "le vecteur retourné n'est pas solution de l'équation : r = Qr", R
    else : 
        return "le vecteur retourné est solution de l'équation : r = Qr", R

print (verification(Q))
P = matriceTransistion(transposee(B))
print(P)
print(verification(P))
