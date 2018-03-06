Neural Networks Notes
=====================

Lecture 1
---------

+ why do we need machine learning?
    + the problem cannot be solved by written explicit programs.
        + vision recognition
        + speech recognition
    + the computer needs to learn by itself.
        + there are so many parameters which are impossible to
            write a explicit program.
+ what are NN good at?
    + what the brain is good at, such as vision and speech recognition.
+ neurons
    + linear neurons
    + binary threshold neurons
    + recitified linear neurons: 0 under threshold, z above threshold
    + sigmoid neurons: z = b + sum(x * w), p = 1 / (1+z)


Lecture 2
---------

+ nn type
    + feed-forward nn
    + recurrent nn
        + model sequential data
        + able to remember information in hidden state for a long time
    + symmetric connected nn

### Perceptron

+ typical __perceptron__ paradigm
    + convert the raw input vector into a vector of feature activations
        + use hand-written programs to define features
    + __learn__ how to weight each of the feature activations to 
        get a single scalar quantity
    + if the quantity is above some threshold, we decide the input
        vector is a positive example of the target class
+ difficulty: finding appropriate featutres, learning is easy.
+ convergence procedure
    + add '1' to input vector to find bias
    + how to change weights
        + output is correct, leave its weights alone
        + outputs is incorrectly 0, add the input vector to the weight vector
        + outputs is incorrectly 1, minus the input vector to the weight vector
+ limitation of perceptrons
    + the tricky part of pattern recognition must be solved by
        the hand-coded feature detectors, not the learning procedure.
    + nn can learn feature dectoectors!


lecture 3
---------

### linear neurons / linear filters
+ iterative approach
    + start with random guesses for weights
    + adjust those weights to get a better fit
+ delta rule
    + squared resuduals: E = 1/2 * sumoveri( (yi-ti)^2 )
    + dE/dwi = -sumoverj( xij * (tj-yj) )
    + delta wi = - epsilon * dE/dwi = epsilon * sumoverj( (xij * (tj-yj)) )
        + epsilon: learning rate
    + this is gradient descent method
    
### logistic neurons
+ using chain rule to get gradient

### backpropagation
+ dE/dwij = dE/dzj * dzj/dwij = yi * dE/dzj
+ dE/dzj = dE/dyj * dyj/dzj = yj * (1-yj) * dE/dyj
+ the backpropagation algorithm is an efficient way of computing the error
    derivative dE/dw for every weight on a single training case.
+ other decisions to make
    + optimization issues: how to use weight derivatives
        + how often to update the weights
            + online: after each training case
            + full batch: after a full sweep through the training data
            + mini-batch: after a samll sample of training cases, 
                this method is the typical method in large datasets
        + how much to update
            + a fixed learning rate
            + adapt the learning rate
    + generalization issues


Lecture 4
---------
+ feature vector representation of concepts
+ softmax unit 
    + forcing sum of probability equals to 0
    + yi = e^zi / sum(e^zj)
+ cost funtion
    + linear unit: square error
    + softmax unit: cross-entropy ( C = -sum(tj * log(yj)) )
+ speech recognition
    + predicting next word helps us understand the sentence
    + methods to get the probability of next word
        + trigram method
            + build a table of frequencies of many triples of word

1.15
----
+ advantages of nn
    + high tolerance of noisy data
    + be able to classify patterns on which they have not been trained
    + can be used when users have little knowledge of the relationships
        between attributes and classes
    + inherently parallel
+ There are no clear rules as to the 'best' number of hidden layer units.
    Network design is a trial-and-error process and may affect the
    accuracy of the resulting trained network.
+ The initial values of the weights may also affect the resulting accuracy.

### recurrent neural network
+ output is related to both input and last output
+ application (sequential data)
    + sequential generation
    + stock prediction
    + text generation
    + voice recogniton    

### convolutional neural network
+ components
    + convolution layer
    + pooling layer
    + fully connected layer
        + check which filter gives the highest score
+ filter 
    + for a specific patter
    + treshold

### deep learning
+ Relu is better than sigmoid
    + sigmoid is slow


Lecture 5 - Object Recognition
------------------------------

+ difficulty
    + segmentation: real scenes are cluttered with other objects
    + lighting: the intensities of the pixels are affected by the lighting
    + deformation
    + affordances: object classes are often defined by how they are used
    + viewpoint

### viewpoint invariance
+ how to achieve viewpoint invariance
    + normalization approach
        + put a box around objects
    + convolutional neural nets
        + replicated features with pooling
    + use a hierarchy of parts that have explicit poses relative to the camera
+ replicated feature detector
+ convolutional nn
    + feature maping
    + subsampling/pooling
+ how to take prior knowledge into account
    + connectivity betweeen neurons
    + weight constraints
    + synthetic data
+ 3D object recognition case
    + ImageNet
