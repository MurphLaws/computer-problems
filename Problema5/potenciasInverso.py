import numpy as np
import scipy.linalg as sla




def normaInfinito(v):
    maxv: float
    maxv = v[0]
    for i in range(0, len(v)):
        if abs(v[i]) >= maxv:
            maxv = abs(v[i])
    return maxv


def normalizarVector(v):
    w = [0]*len(v)
    for i in range(0, len(v)):
        w[i] = v[i] / normaInfinito(v)
    return w



def maxNoZero(v):
    return max([x for x in v if x !=0])



def productoMatrizVector(m, v):
    rows = len(m)
    w = [0]*rows
    suma = 0
    for j in range(rows):
        mi = m[j]
        for i in range(len(v)):
            suma += mi[i]*v[i]
        w[j], suma = suma, 0

    return w






def metodoPotenciasInverso(A, x, M,):
    y = []
    r =  0
    r0: float
    i: int
    (P, L, U) = sla.lu(A)
    UInversa = sla.inv(U)
    LInversa = sla.inv(L)
    for i in range(0, M):

        print(i, ":")
        print("r =", r)
        print("x =", np.around(x, 5))
        r0 = x[0]
        x = productoMatrizVector(UInversa, productoMatrizVector(LInversa, x))
        r = x[0]/r0
        x = normalizarVector(x)

metodoPotenciasInverso([[6, 5, -5],
                        [2, 6, -2],
                        [2, 5, -1]], [3, 7, -13], 12)






