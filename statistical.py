# -*- coding: utf-8 -*- 

'''
Three most common errors on copying process: 

    1. Substitution of an amino acid
    2. Insertion of one or more new amino acids
    3. Deletion of one or more amino acids

Example:
    
    CGGSLI------FLTAAHC (Ancestor cell)
    CGGSLIREDSSKVL-AAHC (Daughter cell)
    1 3 5 7 9 11 14   19

    Substitution: 13
    Insertion: 7 -12
    Deletion: 15
'''

from numpy  import *

a = array(["C", "C", "G", "T", "L"]) ;
b = array(["C", "G", "H", "S", "V"]) ;
c = array(["G", "C", "G", "S", "L"]) ;
d = array(["C", "G", "G", "T", "L"]) ;
e = array(["C", "C", "G", "S", "S"]) ;

m = matrix([a, b, c, d, e]) ;
m_shape = m.shape

aminos = ("C", "G", "H", "S", "T", "L", "V") ;

probs = []
for x in range(0, m_shape[0]):
    for y in range(0, len(aminos)):
        count = m[m[0:,x] == aminos[y],].shape[1]
        probs.append(float(count) / m_shape[1])

probs = matrix(probs)
row = len(aminos)
col = m_shape[1]
probs = probs.reshape(col, row).T ;

print probs

'''
Result:
      1    2   3    4    5
C [[ 0.8  0.6  0.   0.   0. ]
G  [ 0.2  0.4  0.8  0.   0. ]
H  [ 0.   0.   0.2  0.   0. ]
S  [ 0.   0.   0.   0.6  0.2]
T  [ 0.   0.   0.   0.4  0. ]
L  [ 0.   0.   0.   0.   0.6]
V  [ 0.   0.   0.   0.   0.2]]

MOST Ancestor: 
    CCGSL = 0.8 * 0.6 * 0.8 * 0.6 * 0.6 
          = 0.13824
'''
print 0.8 * 0.6 * 0.8 * 0.6 * 0.6
