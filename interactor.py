import numpy as np

N=943
M=1682

movie_dict={}
l1=np.loadtxt("movies.txt", dtype=str, delimiter='|', )

for i in range(M):
    movie_dict[int(l1[i][0])-1]=l1[i][1];

l1=np.loadtxt("data.txt", dtype=int)

X = np.zeros(shape=(N,M))
for j in range(10000):
    X[l1[j][0]-1][l1[j][1]-1]=int(l1[j][2]);
    

Y=np.loadtxt("PREDICTED_RATING_MATRIX.txt", dtype=float)



user=int(input("Enter the user ID: "))
user-=1

ls=[]
for j in range(M):
    if (X[user][j]==0):
        ls.append(j)

def compare(itemID):
    return Y[user][itemID]
        
        
ls = sorted(ls, key= compare)

print("Top 10 recommendations for User", user+1, " are : ")
for j in range(10):
    print(movie_dict[ls[j]])