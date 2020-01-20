import numpy as np

def poziomo(A):
    row=A.shape[0]
    column=A.shape[1]
    dims=(row, column)
    B=np.zeros(dims, dtype=np.integer)
    for i in range(column):
        B[: , i]=A[: , column-i-1]
    return B

M, N = 5, 5
A = np.arange(M*N).reshape((M,N))

print('Macierz A:')
print(A)
print()
print('Macierz B:')
B=poziomo(A)
print(B)
