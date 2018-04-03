Apache
====== 
+ Apache Spark is a fast and general purpose engine 
    for large-scale data processing.
    + user can write code in Scala or Python and Spark will
        automatically parallelize itself on top of Hadoop.
    + It basically run map/reduce.
+ Hadoop is a software library, which is a framework that allows for
    the distributed processing of large data sets clusters of computers
    using simple programming models.
    + It is really a common library called Hadoop Common and 
        a framework called Haddoop MapReduce that sits on top
        of a distributed file system, called HDFS.


Apache Spark
------------
+ big data analytics
    + batch analytics
        + analytics based on the data collected over a period of time
    + realtime analytics
+ why spark when we have Hadoop?
    + spark process data in real-time, while hadoop can only do batch analytics
    + spark is much faster.
    + spark is easier to user, simple programming
+ MapReduce has 3 steps
    + mapper
    + sort & shuffle
    + reducer
    + note: there are input, output operations between these 3 steps,
        therefore MapReduce is fairly **slow**.
+ why spark is fast?
    + during mapreduce, all data sit inside memory    
+ RDD (resilient distributed data)
    + distributed data in **memory**
+ spark operation
    + transformation
        + transformation of different types of RDD
        + depedencies of transformations are describted 
            by DAG (directed acylic graph)
    + action
        + print
+ relationship between Spark and Hadoop
    + Spark is not intended to replace Hadoop 
        but it can be regarded as an extension to it
    + MapReduce and Spark are used together 
        where MapReduce is used for batch processing and 
        Spark for real-time processing.
+ features of Spark
    + 100 faster than MapReduce
    + polygot: R, Python, Java, Scala
    + lazy execution: nothing is executed until an action happens
    + real-time analysis
    + Hadoop integration
    + Machine Learning for iterative tasks
+ Spark Ecosystem
    + Spark Core Engine
    + Spark Streaming
    + Spark SQL
    + MLlib
    + GraphX



Explanation 2
-------------
+ advantages
    + easy to develop
        + rich API in Java, Scala, Python
        + Interactive Shell
    + fast to run
        + general execution graphs
        + in-memory storage
    + ecosystem
        + Spark SQL
        + Spark MLlib
        + Spark Streaming
+ lazy execcution
+ MLlib
    + dataframe
        + need schema
    + feature extraction
+ pyspark
+ workflow
    + preprocess using Spark Core and SQL
        + dataframe
    + pipeline estimator
    + prediction and evalution
