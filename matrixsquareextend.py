import numpy as np

def roz(A):
    row=A.shape[0]
    col=A.shape[1]
    if row>col:
        w=abs(row-col)
        dim=(row,1)
        C=np.zeros(dim,dtype=np.integer)
        for i in range(int(w/2)):
            A=np.hstack((C,A))
            A=np.hstack((A,C))
        return A
    
    elif row<col:
        w=abs(row-col)
        dim=(1,col)
        C=np.zeros(dim,dtype=np.integer)
        for i in range(int(w/2)):
            A=np.vstack((C,A))
            A=np.vstack((A,C))
        return A
    
M, N = 9, 5
A = np.arange(M*N).reshape((M,N))

if M!=N:
    print('Macierz:',M,'x',N,':')
    print(A)
    print()
    print('Macierz',M,'x',N,'rozszerzona:')
    A=roz(A)
    print(A)
else:
    print('Macierz wejściowa',M,'x',N,'jest kwadratowa!')

M, N = 5, 9
B = np.arange(M*N).reshape((M,N))

if M!=N:
    print()
    print('Macierz',M,'x',N,':')
    print(B)
    print()
    print('Macierz',M,'x',N,'rozszerzona:')
    B=roz(B)
    print(B)
else:
    print()
    print('Macierz wejściowa',M,'x',N,'jest kwadratowa!')
