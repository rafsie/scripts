import numpy as np

def obrotwlewo90(A):
    row=A.shape[0]
    column=A.shape[1]
    dims=(column,row)
    B=np.zeros(dims, dtype=np.integer)
    for i in range(column):
        for j in range(row):   
         B[i , j]=A[j ,column - i-1]
    return B

M, N = 8, 4
A = np.arange(M*N).reshape((M,N))

print('Macierz A:')
print(A)
print()
print('Macierz B:')
B=obrotwlewo90(A)
print(B)
