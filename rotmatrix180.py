import numpy as np

def obroto180(A):
    row=A.shape[0]
    column=A.shape[1]
    dims=(row,column)
    B=np.zeros(dims,dtype=np.integer)
    for i in range(row):
        for j in range(column):   
         B[i , j]=A[row-i-1 ,column-j-1]
    return B

M, N = 6, 4
A = np.arange(M*N).reshape((M,N))

print('Macierz A:')
print(A)
print()
print('Macierz B:')
B=obroto180(A)
print(B)
