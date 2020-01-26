import numpy as np

def obrotwprawo90(A):
    row=A.shape[0]
    column=A.shape[1]
    dims=(column,row)
    B=np.zeros(dims,dtype=np.integer)
    for i in range(column):
        for j in range(row):   
         B[i , j]=A[row -j-1 ,i]
    return B

M, N = 9, 5
A = np.arange(M*N).reshape((M,N))

print('Macierz A:')
print(A)
print()
print('Macierz B:')
B=obrotwprawo90(A)
print(B)
