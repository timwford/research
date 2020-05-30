"""
Created on Thu Apr 26 10:46:08 2018
@author: lsj
Heavily modified by Riley Kopp
"""
import numpy as np
from numpy import *
from scipy.fftpack import fft,ifft,dct,idct
from scipy.signal import hilbert
from sympy.core import S, Symbol, sympify



def my_dct(A):
    C=dct(A, axis =-1 , norm = 'ortho')
    return C
def my_idct(A):
    C=dct(A, axis =-1 , norm = 'ortho')
    return C

def my_fft(A):
    a = fft(A, axis = -1)
    return a
def my_ifft(A):
    a = ifft(A, axis = -1)
    return a

def hwtTensor(A):
    x, z, y = A.shape

    a = np.zeros((x, z, y))

    # O(ufta)
    for xIndex in range(0, x):
        for zIndex in range(0, z):
            a[xIndex, zIndex, :] = hwt(A[xIndex, zIndex, :], inverse=False)

    return a

def ihwtTensor(A):
    x, z, y = A.shape

    a = np.zeros((x, z, y))

    # O(ufta)
    for xIndex in range(0, x):
        for zIndex in range(0, z):
            a[xIndex, zIndex, :] = hwt(A[xIndex, zIndex, :], inverse=True)

    return a

def trans(A, flag = 'fft'):
    [n1, n2, n3] = A.shape
    a = np.zeros((n1, n2, n3))
    if flag == 'fft':
        a = my_fft(A)
    elif flag  == 'dct':
        a = my_dct(A)
    elif flag  == 'hwt':
        a = hwtTensor(A)
    return a


def invtrans(A, flag = 'fft'):
    [n1, n2, n3] = A.shape
    a = np.zeros((n1, n2, n3))
    if flag  == 'fft':
        a = my_ifft(A)
    elif flag == 'dct':
        a = my_idct(A)
#        print(a.dtype, flag)
    elif flag  == 'hwt':
        a = ihwtTensor(A)
    return a

def hwt(seq, inverse=False):
    """Utility function for the Walsh Hadamard Transform"""

    if not iterable(seq):
        raise TypeError("Expected a sequence of coefficients "
                        "for Walsh Hadamard Transform")

    a = [sympify(arg) for arg in seq]
    n = len(a)
    if n < 2:
        return a

    if n&(n - 1):
        n = 2**n.bit_length()

    a += [S.Zero]*(n - len(a))
    h = 2
    while h <= n:
        hf, ut = h // 2, n // h
        for i in range(0, n, h):
            for j in range(hf):
                u, v = a[i + j], a[i + j + hf]
                a[i + j], a[i + j + hf] = u + v, u - v
        h *= 2

    if inverse:
        a = [x/n for x in a]

    return a

