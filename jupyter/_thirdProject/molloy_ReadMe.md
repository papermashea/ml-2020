Sample code notes:
- bertin variables produce very few image cluster results
- tested bertin variables with varying clusters
	- using 4, 8, 12, 16, 20, 24 clusters
	- uneven distribution
	- none of these seem remotely related
ERROR line 15
	/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:9: ConvergenceWarning: Number of distinct clusters (19) found smaller than n_clusters (100). Possibly due to duplicate points in X.
  if __name__ == '__main__':
  - still got clusters?
  - wow literally none of these are even in any way lol


Iteration 1:
- could not get string to float "UK", line 27
	- removed country_of_origin
	- get the same error with basically every variable including a string
- tried using only "date", text is included in the 
- binary columns work well
- playing with bertin variables and binary options now
- worked on minimizing variables to clarify clusters
	/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:9: ConvergenceWarning: Number of distinct clusters (90) found smaller than n_clusters (100). Possibly due to duplicate points in X.
  if __name__ == '__main__':

Iteration 2:
In iteration 2 I would like to work on applying TDIF vectorizor to analyze movement, medium and country of origin
