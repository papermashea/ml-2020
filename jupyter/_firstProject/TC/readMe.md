v1: 20200311
- removed feedback loop incorporating toxic and severely toxic ratings as toxic
	tested insult/threat/hate speech/identity hate
- removed 
- removed word count as per twitter civility (see article in "research" folder: https://academic.oup.com/joc/article-abstract/69/4/345/5547032?redirectedFrom=fulltext
- removed punctuation count (.)
- added exclamation point count (!!!)
- added isupper count
- converted isupper boolean to integers (False = 0.0, True = 1.0)	
- added sjw count

notes
+ it is hard to quantify language parameters without censoring speech or punctuation parameters without overfitting
+ a lot of the false positives in data seems very concerned about toxicity policing
	false positives still seem pretty toxic
+ models improved (with 4 qual features and 3 quant)
	logistical regression
	linear svm
	ols 
	naive bayes
	perceptron
+ accuracy in isolating features in qualitative data (logistical regression model)
	all qualitative + qualitative features: 0.998817133546406
	obscene: 0.9991931440747007
	threat: 0.9998981638152535
	insult: 0.997877107225669
	identity hate: 0.9985821269662217
+ random forest classifier decreased accurcy drastically when all but obscene feature was removed
+ best features + model combination: = Accuracy: 0.9998276618411982 
	threat
	exclamation
	allCaps
	sjw_count
	model: logistical regression




