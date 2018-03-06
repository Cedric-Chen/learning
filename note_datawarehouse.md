### RDD - Resilient Distributed Dataset
+ A RDD is a resilient(fault-tolerant) and distributed collection of records 
    spread over one or many partitions.
+ feature
    + in-memory
    + immutable or read-only
    + lazy evaluated
    + cacheable
    + parallel
    + typed
    + partitioned
    + location-stickiness

### ETL
+ ETL (Extract, Transform and Load) is a process in data warehousing 
    responsible for pulling data out of the source systems 
    and placing it into a data warehouse.
+ transforming the data:
    + apply business rules
    + cleaning
    + filtering (selecting only certain columns)
    + joining data from multiple sources
    + apply data validation
+ loading the data
    + loading the data into a data warahouse or data repository 


11.24
-----

###Data Warehouse
+ definition
    + a decision support database that is manitained separately from
        the organization's operational database
    + support information processing by providing a solid platform of 
        consolidated, historical data for analysis
+ features
    + subject-oriented: excluding data that are not useful in 
        decision support process
    + integrated: from multiple, heterogeneous data sources;
        data cleaning and data integration techniques are applied.
    + time-variant: providing information from a historical perspective.
    + nonvolatile: independence (physically seperate from operational 
        database); static
+ importance
    + high performance for both OLTP and OLAP
+ Data Warehouse is a multi-tiered architecture
    + data: ETL
    + bottom tier: data warehouse server
    + middle layer: OLAP server
    + top tier: fron-end tools
+ virtual warahouse
    + a set of views over operational databases
    + only some of the possible summary views may be materialized
+ ETL
    + extraction: get data from multiple, heterogeneous and external sources
    + cleaning: detect errors and recitify them
    + transformation: convert data into warahouse format
    + load: sort, summarize, consolidate, compute views,
        check integrity, and build indices and partitions
    + refresh
+ data warehouse usage
    + information processing
    + analytical processing: OLAP operations
    + data mining

### Data Cubes
+ components
    + dimension tables
    + fact table: keys to each of the related dimension tables and measures
+ concenptual modeling
    + star schema
    + snowflake schema
    + fact constellations
+ typical OLAP operations
    + roll/drill up: summarize data
    + roll/drill down: from higher level to lower level (detailed data)
    + slice and dice: project and select
    + pivot/rotate
+ SQL-like language
    + CUBE BY
+ indexing OLAP data
    + bitmap index
+ cube materialization
    + full cube
    + icerberg cube
    + closed cube
    + cube shell
+ computing data cube
    + bottom-up: multi-way array aggregation
    + top-down: BUC
    + shell-fragment: high-dimension OLAP
