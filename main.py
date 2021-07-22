import numpy as np
from numpy import linalg as LA

eps=0.00001

def matrix_factorization(X , P, Q, K, inter, alpha, beta):
    Q = Q.T
    N=X.shape[0]
    M=X.shape[1]
    for step in range(inter):
       print("step ", step)
       for i in range(N):
            for j in range(M):
                if X[i][j] > 0 :
                    #error corresponding element X[i][j]
                    eij = X[i][j] - np.dot(P[i,:],Q[:,j])
                    sum_of_norms = 0        
                    sum_of_norms += LA.norm(P) + LA.norm(Q)                
                    eij += ((beta/2) * sum_of_norms)
                             
                    #compute the gradient from the error
                    for k in range(K):
                        tempP=P[i][k]
                        tempQ=Q[k][j]
                        P[i][k] = tempP + alpha * ( 2*eij*tempQ-(beta*tempP))
                        Q[k][j] = tempQ + alpha * (2*eij*tempP-(beta*tempQ))
        #compute total error
       error = 0
       for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                if X[i][j] > 0:
                    error += np.power(X[i][j] - np.dot(P[i,:],Q[:,j]),2)
       if error < eps:
            break
    return P, Q.T

def inputData():
    l1=np.loadtxt("data.txt", dtype=int)
    users=943
    movies=1682
    X = np.zeros(shape=(users,movies))
    
    for j in range(10000):
        X[l1[j][0]-1][l1[j][1]-1]=int(l1[j][2]);
    return X

X=inputData();

K=50

N=X.shape[0]
M=X.shape[1]
P = np.random.rand(N,K)
Q = np.random.rand(M,K)
steps=1000
alpha=0.00002
beta=float(0.002)
P, Q=matrix_factorization(X, P, Q, K, steps, alpha, beta)

new_X=np.dot(P, Q.T)

np.savetxt('ACTUAL MATRIX.txt', X)
np.savetxt('PREDICTED_RATING_MATRIX.txt', new_X)
