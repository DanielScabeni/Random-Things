X = 0
Y = 1
#A, B
CONTA = 0
MAX_CONTA = 10
while(CONTA < MAX_CONTA):
    CONTA = CONTA +1
    A = X
    B = Y
    X = B
    Y = A+B
    print(A)