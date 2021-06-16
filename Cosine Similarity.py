from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy

X=numpy.loadtxt("ACTUAL MATRIX.txt", dtype=float)
Y=numpy.loadtxt("movie.txt", dtype=str, delimiter='|')

num_of_movies=1681

text=[]
moviename={}
movieid={}


'''
Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
'''
for j in range(num_of_movies):
    moviename[int(Y[j][0])-1]=str(Y[j][1]);
   
    movieid[str(Y[j][1])]=int(Y[j][0])-1;
    s=" "
    if (Y[j][5]=='1'): s+='Action '
    if (Y[j][6]=='1'): s+='Adventure '
    if (Y[j][7]=='1'): s+='Animation '
    if (Y[j][8]=='1'): s+='Childrens '
    if (Y[j][9]=='1'): s+='Comedy '
    if (Y[j][10]=='1'): s+='Crime '
    if (Y[j][11]=='1'): s+='Documentary '
    if (Y[j][12]=='1'): s+='Drama '
    if (Y[j][13]=='1'): s+='Fantasy '
    if (Y[j][14]=='1'): s+='Film-Noir '
    if (Y[j][15]=='1'): s+='Horror '
    if (Y[j][16]=='1'): s+='Musical '
    if (Y[j][17]=='1'): s+='Mystery '
    if (Y[j][18]=='1'): s+='Romance '
    if (Y[j][19]=='1'): s+='Sci-fi '
    if (Y[j][20]=='1'): s+='Thriller '
    if (Y[j][21]=='1'): s+='War '
    if (Y[j][22]=='1'): s+='Western '
    text.append(str(s));


cv=CountVectorizer()
count_matrix = cv.fit_transform(text)
similarity_scores=cosine_similarity(count_matrix)

user=int(input("Enter your USER ID: "))
user=user-1
movee=str(input("Enter the name of the movie you would like your recommendations to be like: "))

id=movieid[movee]
ls=[]

for j in range(num_of_movies):
    if (X[user-1][j]==float(0)): ls.append(j)

def compare(itemID):
    return similarity_scores[id][itemID]      
        
ls = sorted(ls, key= compare)



print("The top 10 movies similar to ", movee, "not seen by user ", user+1, " are ");
for j in range(10):
    print (moviename[ls[j]])
