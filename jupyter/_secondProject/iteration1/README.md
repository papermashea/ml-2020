##Iteration 1
###Process notes
- multi-layer perceptron seems to be performing significantly better on training data, but about the same on test data
- test hog code clarified additional reading implementation: https://kapernikov.com/tutorial-image-classification-with-scikit-learn/
- hog produced no false positives for perceptron model training data
- hog produced better results for the neural network test data
- applying StandardScaler() takes forever to process somehow
- hog transformation still slow when scaler is removed
- tried playing with the size of the images and it loaded way slower
- nn has fewer FP than pc (1 vs. 0)
- uploaded cropped images, images with no plane and images with planes to teachable machine for feature exploration
