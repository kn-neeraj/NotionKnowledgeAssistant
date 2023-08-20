# MLBM - Machine Learning for Business Managers

## Lecture 1

- Data Preprocessing
    - Check distributions of each feature and look for
        - was there some censoring of the data
        - non-standard units
        - attribute scaling -
        - skewed distributions - may need to use some transformations of the feature
        - Stratified sampling for critical features
            - It is used to highlight differences between groups in a population, as opposed to simple random sampling, as opposed to simple random sampling which treats all members of a population equal, with an equal likelihood of being sampled
            - Dividing the population into homogeneous groups called strata. Random samples are selected for from each stratum
            - RESULT : training and testing data mimics the distribution of the overall data
        - Visualizing Data for insight
            - Correlations, one hot encoding, handling missing values
            

## Lecture 2

## SUPERVISED ALGORITHMS

**KNN** - K-nearest neighbours (NOT K MEANS CLUSTERING!!) (average of teh K nearest neighbours)

- Supervised learning classification & regression algorithm
- Technique is non-parametric - it does not make any assumptions on the underlying data distribution. Should be useful when there is no prior knowledge about the distribution data
- Applications
    - predict a new customer's credit rating
    - should the bank give a loan to an individual
    - image recongnitions..
- Pros
    - no assumptions about data, simple algorithm,
- Cons
    - computationally expensive, high memory requirement, prediction stage might be slow, sensitive to irrelevant features and the scale of the data
    

**Decision Trees**

- hyperparameters
    - min samples leaf - minimum number of samples a leaf node should have
    - mandate the tree to some levels deep
    - look for transformations!
    - unrestricted tree might lead to overfitting

**Ensemble -** [https://towardsdatascience.com/simple-guide-for-ensemble-learning-methods-d87cc68705a2](https://towardsdatascience.com/simple-guide-for-ensemble-learning-methods-d87cc68705a2)

- Ensemble models
    - multiple learning algorithms at the same time
    - Random forest is ensemble of decision trees
    - popular ensemble methods
        - Voting classifiers - chose multiple ML algorithms and it predicts based on "mode" of predictions on each sample [Stacking]
        - Bagging (bootstrap aggregating) ensembles
            - better for strong learned algorithms
            - multiple models of same learning algorithm trained with subsets of data randomly picked from the training dataset, split data randomly in bags and train the learning models, take the vote in their outputs
        - Boosting ensembles
            - better for weak learner algorithms
            - learning from mistakes
            - adaboost classifiers
            - learning_rate - less learning rate means slower learning of the model, weights are increased slowly

[Untitled Database](MLBM%20-%20Machine%20Learning%20for%20Business%20Managers%2001b93b229d4d4eb5b7629685a81af85f/Untitled%20Database%207356c1aef3fb4291b596e27153cdd056.csv)

- Advantages - better accuracy, higher consistency by avoiding overfitting
- disadvantages - computation and design time is high

## Session - 3

- **MODEL EVALUATION PARAMETERS**
    
    ![MLBM%20-%20Machine%20Learning%20for%20Business%20Managers%2001b93b229d4d4eb5b7629685a81af85f/Confusion_Matrix6.png](MLBM%20-%20Machine%20Learning%20for%20Business%20Managers%2001b93b229d4d4eb5b7629685a81af85f/Confusion_Matrix6.png)
    
    - Precision (How many of predicted as positive are actually positive) = TP/(TP + FP)
    - Recall (How many of actual positive value is predicted as positive or sensitivity) = TP/(TP + FN)
    - F1score = 2 * Precision * Recall / (Precision + Recall)
    - ROC Curve = Recall (TP/(TP+FN)) or True Positive rate is plotted against False Positive Rate (or Inverse Recall) = FP/(FP + TN)
    
- Model evaluation for regression and classification
- Cross Validation
    - train and re-train model on the different cuts of the data and test model on different test samples
    - k-fold cross validation
        - partition data in k different equi-sized folds
        - one fold of data is held out as test sample and model is trained on k-1 folds
        - We obtain k sets of validation test results. Variance in these results is informative
        - 
- Precision and Recall
    - imbalanced classification problem - 1 class is highly imbalanced
    - **Recall (sensitivity)** can be thought as of a model’s ability to find all the data points of interest in a dataset. (true positives/ (true positive + false negative))
    - **Precision** - portion of data points our model says relevant are actually relevant (true positives / (true positive + false positive))
    - Blend of both - F1 score - harmonic mean of precision and recall
- ROC curve - curve of true positive rate and false positive rate for a number of different candidate thresholds between 0.0 and 1.0
- AUC - Area under the curve, the more it is the better the classification
- ROC vs PR curves
    - The reason for this is to provide the capability to choose and even calibrate the threshold for how to interpret the predicted probabilities.
    - [https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/)

<aside>
💡 When to prefer ROC over P-R curves? • Rule of thumb is if the positive class is rare and you care more about FPs, go for P-R curves because you want to see with how much recall precision is still high because with high recall precision falls drastically!                              Else go for ROC and AUC, when the observations are balanced in each class

</aside>

<aside>
💡 When the positive class is imbalanced you don't optimise for true negative but rather optimise for true positive, false positive and false negative. Precision and Recall optimise for positive class and hence are a better predictor in case of imbalanced data sets

</aside>

### Regression variants with interactions and polynomials

- Binned regressions
    - break the data into n bins and create linear regressions for each
- Polynomial regressions
    - sklearn.preprocessing.polynomialfeatures
        - get the polynomialfeatures of a degree
        - do fit and transform X
- Regularized regressions
    
    <aside>
    💡 In exploratory work; with wide and shallow datasets (e.g. medical or purch history);
    Most ML models including ANNs have regulzn modes built-in.
    
    </aside>
    
    - Unregularized regressions - OLS
    - **we force model simplicity to regularization**
    - Ridge regressions
        - Forces coefficients to be as small as possible. each feature should have little effect on Y as possible.
        - Hyperparameter "alpha" means higher it is more the model forces coeff to be zero
        - It makes coefficients for features which are not relevant zero or closer to zero
        - Training score is higher than test score throughout. Expectedly.
        - Because ridge is constrained, its training score tends to be lower than OLS across the board. However, test score for ridge is way better than OLS.
        - Ridge outperforms in test samples of small size.
        - OLS, on the other hand, **learns nothing** for datasets with < 400 observations.
        - **Bottomline:** With enough training data, regularization becomes less important and OLS converges to the same performance.
        
    - **Lasso Regression**
        - Whereas Ridge was 'L2' in that it minimizes the square of coeff magnitude, lasso is 'L1' in that it minimzes the absolute value of a coeff.
        - Implication is that lasso can be used as a form of automated feature selection and point to us the most important features in a large dataset.
    

 

## Session - 4 - Data Collection for ML Applications

- DC from static web pages
    - beautifulsoup
- DC from dynamic web pages
    - selenium webdriver for web-scraping
    - 
- DC using APIs
    - quandl

## Session - 5

- Dimensionality Reduction
    - Data lies on smaller dimensional subspace
    - Helps in speeding up ML training
    - Dropping noise improves learner preferences
    - Approaches
        - Projection (FactorAn, PCA)
        - pManifold learning (t-SNE, Isomap)
    - PCA
        - Principle One - Captures the maximum variance explained in the data
        - PCA example - 3D space in 2D plane maximizing variance explained with PC1 and PC2
    - Manifold - tSNE (tDistributed Stochastic Neighbour Embedding)
    

## Session - 6

- Word2vec
    - efficiently create word embeddings, used in recommendation engine
    - Words can be represented as vectors
    - similar vectors can be found using cosign similarity
    - Example of NLP prediction - next word prediction
    - skipgram and negative sampling
    - hyperparameters - window size, number of negative samples
    
    ## Session 7 - Topic Analysis
    
    - [https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1](https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1)
    - 
    

## Session - 9  - Neural Networks and Deep Learning

- **What are Neural Networks and their structure** - input layer matrix, multiple hidden layers, output layers
    - each layer has 'n' number of neurons with value (0-1)
    - Whole of previous layer passes to each of neurons in next layer using a linear combination of weights and sigmoid function and bias.
    - sigmoid(w(1)a(1)+...w(n)a(n) + b(0))
    - Ex- hello world of neural networks - hand written images on of 28X28 grayscale

![MLBM%20-%20Machine%20Learning%20for%20Business%20Managers%2001b93b229d4d4eb5b7629685a81af85f/WhatsApp_Image_2020-02-13_at_4.10.06_PM.jpeg](MLBM%20-%20Machine%20Learning%20for%20Business%20Managers%2001b93b229d4d4eb5b7629685a81af85f/WhatsApp_Image_2020-02-13_at_4.10.06_PM.jpeg)

- **Gradient descent - how neural networks learn**
    - Basically it is finding minimum of a certain function
    - Cost function - gradient of a function gives in which direction the function increases the most, gradient descent (converge towards a local minimum) gives in which direction the funcion decreases the most
    - Algorithm for learning the apt. weights to find global minima of loss function is terms Backpropogation
    - Initialize the weights with random values and biases and keep optimizing them through gradient descent of loss function
    - Simplest ANN is called Multilayer Perceptron (but outdated)
- **Backpropogation** - what it is really doing
    - from output layer to second last layer all the nudges that are required to a neuron in weights and biases.
    - Keep going backwards
    - Keep doing for every batch of input
    - Avg. of nudges is the negative gradient
    - Take batches of data and computer forward and backward propogration
    
    <aside>
    💡 Need lot of labelled data for neural networks - How do you get labelled data for your field
    
    </aside>
    
- CNN - Convolutional Neural Networks a type of ANN
    - Used for detection of classification of sensory stimuli (vision, auditory) - image classification, speech recognition, object detection
    - pattern detection - it has hidden convolutional layers with specific filters apart from normal hidden layers
    - Some filters can detect edges, circles etc
    - 
- Data growth and its impact
    - 50% data on cloud
    - 80% of the data unstructured - audio, video, documents (how to find out that 10% of it that is useful)
    - 30gb per human genome
    - Types
        - BI and ad-hoc - descriptive
        - predictive
        - deep learning AI - realtime
        - DataOps
        - Case - SHoppers Stop increase revenue in its private label brands
            - loyalty members data from single store
            - RFM analysis and multiple segments
        
    
    ## CNNs/ANNs - Convolutional Neural Networks
    
    -