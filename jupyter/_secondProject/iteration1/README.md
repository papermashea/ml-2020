##Iteration 1
###Process notes
- multi-layer perceptron seems to be performing significantly better on training data, but about the same on test data
- nn has fewer FP than pc (1 vs. 0), typically performing higher
- uploaded cropped images, images with no plane and images with planes to teachable machine for feature exploration - json was a little too complex to incorporate into jupyter notebook workflow
- test hog code clarified additional reading implementation: https://kapernikov.com/tutorial-image-classification-with-scikit-learn/
- hog transformation produced no false positives for perceptron model training data
- hog transformation produced better results for the neural network test data
- hog transformation still slow when scaler is removed
- experimenting with greyscale vs. not also takes a long time to load
- color addition drastically improves prc, minorly improves nn
- resize reflect feature drastically decreases nn test set accuracy, doesn't affect prc 
- experimenting the the dims distortion negatively affected the prc but didn't affect the nn at all
- resize wrap mode returns very accurate prc test set results with altered dims and greyscale
- anti-aliasing doesn't do much
- canny with thresholds returned slightly less terrible results
- greycoprops produces unreliable results, fluxuating between low and high accuracy for prc 


###Transformation explortion
####RGB to HSV
	Hessian matrix


###Feature exploration
####Canny
####Greycoprops






