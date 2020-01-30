import numpy as np

def roz(A):
    row=A.shape[0]
    col=A.shape[1]
    
    if row>col:
        w=abs(row-col)
        for i in range(int(w/2)):
            A=np.delete(A,(0),axis=0)
            row=A.shape[0]
            A=np.delete(A,(row-1),axis=0)
        return A
    
    elif row<col:
        w=abs(row-col)
        for i in range(int(w/2)):
            A=np.delete(A,(0),axis=1)
            col=A.shape[1]
            A=np.delete(A,(col-1),axis=1)
        return A

M, N = 9, 5
A = np.arange(M*N).reshape((M,N))

if M!=N:
    print('Macierz:',M,'x',N,':')
    print(A)
    print()
    print('Macierz',M,'x',N,'przycięta:')
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
    print('Macierz',M,'x',N,'przycięta:')
    B=roz(B)
    print(B)
else:
    print()
    print('Macierz wejściowa',M,'x',N,'jest kwadratowa!')
