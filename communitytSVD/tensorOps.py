# Python tensor operations

import numpy as np
import networkx as nx
from random import random, shuffle
import itertools
from L_svd import L_svd
from numpy.fft import fft, ifft
from scipy.linalg import svd

# to multiply two tensors
def t_prod(A, B):
    [a1 ,a2 ,a3] = A.shape
    [b1 ,b2 ,b3] = B.shape
    A = fft(A, axis = -1)
    B = fft(B, axis = -1)
    C = np.zeros((a1,b2,b3), dtype = complex)
    for i in np.arange(b3):
        C[:,:,i]=np.dot(A[:,:,i],B[:,:,i])
    C = ifft(C, axis = -1)
    return C


# tensor circulant
def t_circ(A):
    n, m, p = A.shape
    res = np.zeros((n*p, m*p))
    
    res[:, 0:m] = unfold(A)
    
    for j in range(1, p):
        first_thing = res[(p-1)*n:p*n, (j-1)*m:(j)*m]
        second_thing = res[0:(p-1)*n, (j-1)*m:j*m]
        the_thing = np.concatenate((first_thing, second_thing), axis=0)
        res[:, j*m:(j+1)*m] = the_thing
    
    return res


# tensor unfold
def unfold(A):
    n, m, p = A.shape
    v_res = np.zeros((n*p, m))
    
    for i in range(0, p):
        temp = A[:,:,i]
        v_res[i*n:(i+1)*n,0:m] = A[:,:,i]
    
    return v_res


# tensor fold up
def fold_up(A, n1, n2, n3):
    
    knt = 0
    res = np.zeros((n1,n2,n3))
    
    for i in range(0, int(n3)):
        #print(knt, knt+n1, 0, n2)
        res[:,:,i] = A[knt:knt+n1, 0:n2]
        knt += n1
        
    return res


# tensor transpose
def t_tran(A):
    ten_circ = t_circ(A)
    #print(ten_circ.shape)
    ten_circ = ten_circ.transpose()
    #print(ten_circ.shape)
    n2,n1,n3 = A.shape
    #print(n1,n2,n3)
    res = fold_up(ten_circ, n1, n2, n3)
    return res 


def printFrontalSlices(A):
    _, _, p = A.shape
    rep = "\n"
    for i in range(0,p):
        vals = A[:,:,i:i+1].reshape(2,2)
        rep += str(vals)
        rep += "\n"
        
    return rep


def t_svd(A, k = None):
    n1, n2, n3 = A.shape
    
    trans_flag = False
    print(A.shape)
    
    # transpose and swap if wrong shape
    if(n2 > n1):
        trans_flag = True
        A = t_tran(A)
        swap = n1
        n1 = n2
        n2 = swap
        
    A = fft(A, axis=2)
    
    # flag to compute compact or full
    fl = 1
    if k is not None:
        fl = 0
    
    K = min(n1, n2)
    
    if (fl == 0):
        U = np.zeros((n1, n1, n3))
        S = np.zeros((K, K, n3))
        V = np.zeros((K, n2, n3))
    else:
        U = np.zeros((n1, n1, n3))
        S = np.zeros((n2, n2, n3))
        V = np.zeros((n2, n2, n3))
    
    for i in range(0, n3):
        if (fl == 0):
            U1, S1, V1 = svd(A[:,:,i], full_matrices = True)
            U[:,:,i] = U1
            S_mat = np.diag(S1.tolist())
            S[:,:,i] = S_mat
            V[:,:,i] = np.flip(V1)
        else:
            U1, S1, V1 = svd(A[:,:,i])
            U[:,:,i] = U1
            S_mat = np.diag(S1.tolist())
            S[:,:,i] = S_mat
            V[:,:,i] = np.flip(V1)
            
    if trans_flag:
        Uold = U
        U = V
        S = t_tran(S)
        V = Uold
    
    return np.real(ifft(U, axis=2)), np.real(ifft(S, axis=2)), np.real(ifft(V, axis=2))
