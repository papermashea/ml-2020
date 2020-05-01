    # function that takes raw data and completes all preprocessing required before model fits
    def process_raw_data(fn, my_random_seed, test=False):
        # read and summarize data




    # QUALITATIVE FEATURES
    # remove self-identifying toxic measures
        toxic_data = pd.read_csv(fn)
        if (not test):
            # add an indicator for obscene, threat, insult, or indentity hate
            
            # testing removing all but one feature
            # toxic_data['any_toxic'] = ( toxic_data['obscene'] > 0 )
            # toxic_data['any_toxic'] = ( toxic_data['threat'] > 0 )     
            # toxic_data['any_toxic'] = ( toxic_data['insult'] > 0 )       
            # toxic_data['any_toxic'] = ( toxic_data['identity_hate'] > 0 )     

            toxic_data['any_toxic'] = (toxic_data['obscene'] + toxic_data['threat'] + toxic_data['insult'] + toxic_data['identity_hate'] > 0 )
            # print("toxic_data is:", type(toxic_data))
            # print("toxic_data has", toxic_data.shape[0], "rows and", toxic_data.shape[1], "columns", "\n")
            # print("the data types for each of the columns in toxic_data:")
            # print(toxic_data.dtypes, "\n")
            # print("The first 10 rows in toxic_data:")
            # print(toxic_data.head(10))
            # if (not test):
            #     print("The rate of 'toxic' Wikipedia comments in the dataset: ")
            #     print(toxic_data['any_toxic'].mean())

        # vectorize Bag of Words from review text; as sparse matrix
        hv = HashingVectorizer(n_features=2 ** 17, alternate_sign=False)
        X_hv = hv.fit_transform(toxic_data.comment_text)
        print("Shape of HashingVectorizer X:")
        print(X_hv.shape)
        
        # http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
        transformer = TfidfTransformer()
        X_tfidf = transformer.fit_transform(X_hv)
        



    # QUANTITATIVE FEATURES
    # number-based features from toxic comments to add to feature set

        # count of excessive exclamation points
        toxic_data['exclamations'] = toxic_data['comment_text'].str.count("\!\!\!")

        # boolean all-caps responses
        toxic_data_isupper = toxic_data['comment_text'].str.isupper(
                # if isupper_count is False
                #     print('0')
                # else:
                #     print('1')
                    )  

        # transform booleans to integers
        def boolstr_to_floatstr(b):
          if b == 'True':
              return '1'
          elif b == 'False':
              return '0'
          else:
              return b

        toxic_data['allCaps'] = np.vectorize(boolstr_to_floatstr)(toxic_data_isupper).astype(float)


        # count of use of the slang "sjw"
        toxic_data['sjw_count'] = toxic_data['comment_text'].str.count("sjw")


        X_quant_features = toxic_data[["exclamations", "allCaps", "sjw_count"]]
        print("Quantitative features include exclamation point count, uppercase usage, and count of disparaging language: ")
        print(X_quant_features.head(10))




    #COMBINING FEATURES    
    # Combine all quantitative features into a single sparse matrix
        
        X_quant_features_csr = csr_matrix(X_quant_features)
        X_combined = hstack([X_tfidf, X_quant_features_csr])
        X_matrix = csr_matrix(X_combined) # convert to sparse matrix
        print("Size of combined bag of words and new quantitative variables matrix:")
        print(X_matrix.shape)
        
        # Create `X`, scaled matrix of features
        # feature scaling
        sc = StandardScaler(with_mean=False)
        X = sc.fit_transform(X_matrix)
        print(X.shape)
        if (not test):
            y = toxic_data['any_toxic']
        



    # CREATING DATA SETS
    # Create Training and Test Sets

        # enter an integer for the random_state parameter; any integer will work
        if (test):
            X_submission_test = X
            print("Shape of X_test for submission:")
            print(X_submission_test.shape)
            print('SUCCESS!')
            return(toxic_data, X_submission_test)
        else: 
            X_train, X_test, y_train, y_test, X_raw_train, X_raw_test = train_test_split(X, y, toxic_data, test_size=0.2, random_state=42)
            print("Shape of X_train and X_test:")
            print(X_train.shape)
            print(X_test.shape)
            print("Shape of y_train and y_test:")
            print(y_train.shape)
            print(y_test.shape)
            print("Shape of X_raw_train and X_raw_test:")
            print(X_raw_train.shape)
            print(X_raw_test.shape)
            print('SUCCESS!')
            return(X_train, X_test, y_train, y_test, X_raw_train, X_raw_test)