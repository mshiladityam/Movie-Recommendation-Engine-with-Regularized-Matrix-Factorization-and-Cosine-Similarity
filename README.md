#Movie Recommendation Engine using Regularized Matrix Factorization and Cosine Similarity

This project consists of two parts:
1) Collaborative Filtering
For the first part, I downloaded the MovieLens dataset (100K), which has 1681 movies and 943 users, and 100K user-movie rating pairs.
I sanitized the data into a 2D matrix MAT[USER][MOVIE] where MAT[i][j] represents rating of movie j by user i, if user i has seen the movie j.

Now, using regularized matrix factorization with gradient descent, IMPLEMENTED COMPLETELY FROM SCRATCH, I wrote a generator script in Python [generator.py], which interpolated the values and predicted the user-rating (i, j) pairs for such users i such that they had not
rated movie j. The script performed 1000 iterations and I set the value of alpha to 0.0002 after some experimentation. The result is stored in PREDICTED_RATING_MATRIX.txt.

In interactor.py, one can enter user ID and the interactor outputs the PREDICTED top-10 highest rated movies, that the user has not seen.

![Interaction](https://github.com/mshiladityam/Movie-Recommendation-Engine-with-Regularized-Matrix-Factorization-and-Cosine-Similarity/blob/main/MatrixFactorisationSS1.png)



2) Content-Based Filtering
For the second part of the Movie Recommendation Engine, I exploited the Genre-based classification of the movies in the dataset. 
I modelled the problem as such: consider each movie as a m-dimensional vector V[m] where V[i]=1 if ith feature is on, V[i]=0 otherwise.

Then we can immediately model the similarity between two vectors as the cosine distance between them in m-dimensional space. 
I built a 2D matrix M[][] where M[i][j] represents the cosine similarity between movies i and j.

After computing this matrix, [Cosine Similarity.py] takes in user ID and one movie, and outputs top-10 movies, similar to the input, which the user hasn't seen.

![Interaction](https://github.com/mshiladityam/Movie-Recommendation-Engine-with-Regularized-Matrix-Factorization-and-Cosine-Similarity/blob/main/CosineSimilaritySS.png)
