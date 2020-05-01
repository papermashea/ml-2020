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
- added 
- could not get string to float "UK", line 27
	- removed country_of_origin
	- get the same error with basically every variable including a string
- tried using only "date", text is included in the 
- binary columns work well
- playing with bertin variables and binary options now
- worked on minimizing variables to clarify clusters
	/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:9: ConvergenceWarning: Number of distinct clusters (90) found smaller than n_clusters (100). Possibly due to duplicate points in X.
  if __name__ == '__main__':


Iteration 1 Cluster Analysis
*** Cluster 0:  The Colorful Boundaries Collection ***
Images in cluster 0 can be identified with their colorful, primarily primary, palettes. The shapes have strong, 

*** Cluster 1: The Deep Monotonous Dream Collection  ***
Images in cluster 1 are consistent with their ambiguous lines and sharp perspectives. This collection is noted by the varied depth of the images, as well as their limited coloration.

