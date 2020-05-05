## Iteration 1  
Notebook:  [papermashea/_secondProject/iteration1](https://github.com/papermashea/ml-2020/tree/master/jupyter/_secondProject/iteration1)  
- [final CSV](https://github.com/papermashea/ml-2020/blob/master/jupyter/_secondProject/iteration1/airplane_submission.csv)  

### Overall approach  
For this project I attempted to warp the image as much as I could, focusing on feature extraction and transformations rather than model tweaking. I worked with texture and color features and in future iterations would like to work with blob detection and color channels. My most consistent-performing submission focuses on the following:  

- image resizing
- image warping
- coloration
- exposure
- alpha
- learning rate


### Transformation explortion  
In my initial parameter and input explorations, I experimented heavily with resizing, shape and color to attempt to warp the image as much as possible. Tensorflow and teachable machine showed me that varying the input data as much as possible would greatly affect model reliability.  

I found models assessing color to be generally more reliable than greyscale models however, I ended up going grey images in the end. I tested a lot of combinations of parameters and inputs including changing the changing all of the resize parameters, altering the resize inputs, switching as_gray=True to False, warping the image, and I attempted to convert the [RGB images to HSV](https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_rgb_to_hsv.html#sphx-glr-auto-examples-color-exposure-plot-rgb-to-hsv-py). This led to a lot of attempts at applying transformations like matrix_transform and various matrices such as the [Hessian matrix](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.hessian_matrix) to images in an attempt to get a viable output section by color channels.  



### Feature exploration  
For this iteration, I explored canny edge detection, [greycoprops](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.greycoprops) to assest contrast and texture, daisy, and max peak detection to learn more about the differences in the images in the training set.  

#### Canny  
Working with canny edge detection yeilded terrible results with and without additional hog features, with varying size transformations, and with varying thresholds. After trying canny edge detection with a few transformations, dropped it. 

#### Greycoprops  
Greycoprops initially produced outstanding results with the parameters symmetric and normed both set to true. However, they performed this way inconsisently without a gradient descent. When I attempted to apply the histogram of oriented gradients, I found myself unable to apply the hog to the greycoprops feature because it produced negative numbers. I was unable to resolve this even after attempting to normalize blocks as a parameter of greycoprops. Sadly, I had to give up. I would like to find another way to normalize greycoprops in the future as this feature was occassionally very exciting for these images.  
![greycoprops1](https://github.com/papermashea/ml-2020/blob/master/jupyter/_secondProject/iteration1/_comparisons/_greycoprops_symmetric-true_normed-true.png "Greycoprops was exciting when it wanted to be")
![greycoprops1](https://github.com/papermashea/ml-2020/blob/master/jupyter/_secondProject/iteration1/_comparisons/_greycoprops_symmetric-true_normed-true2.png "Greycoprops was exciting when it wanted to be")

#### Daisy  
I was interested in working with daisy for the density of the histogram extraction, given the similarity and blurriness of our sample images. I tried working with daisy in conjunction with the hessian matrix and rgb/hsv conversion since the daisy ndarray inputs and outputs did't align with the array needed.  



### Process notes  
See "_comparisons" for process examples and plots  
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

