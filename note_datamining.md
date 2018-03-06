classification
--------------

+ decision tree
    + random forest
        + data bagging
        + feature bagging
+ naive bayes
    + bayesian belief network
        + graph: DAG
        + CPTs
+ support vector machine
    + svm searchse for the hyperplane with the largest margin, 
        i.e. maximum marginal hyperplane (MMH)
+ neural network
+ ensemble methods
    + defintion: use a combination of models to increase accuracy
    + methods
        + bagging: sample training set
        + boosting: emphasize mis-classified data
+ evaluation
    + holdout
    + cross validation: randomly partition data into k folds; 
        at i-th iteration, use Di as test set, and others as train set
    + bootstrap: sample training set with replacement
    + AUC: true positive, false positive
+ issues affecting model selection
    + accuracy
    + speed: train, predict
    + robustness: handling noise and missing values
    + scalability
    + interpretability


Clustering
----------
+ k-means
    + k-means++, k-medoids, k-medians, k-modes, kernel k-means
+ hierarchical methods (tree-like)
    + BIRCH: scan DB to build a cluster feature tree;
        use an arbitrary clustering algorithm to cluster the leaf nodes
+ density based
    + DBSCAN
        + 2 parameters: Eps, MinPts
    + OPTICS
        + identify clustering structure
+ grid-based
    + STING
    + CLIQUE
        + subclustering
