jvm memory management
=====================

+ java virtual machine has an automatic memory management.
+ jvm examples:
    + oracle Java HotSpot Virtual Machine

###for all threads
+ method area
    + stores class information
        + runtime constant pool
        + method code
        + attributes
+ heap
    + manages instances of classes and arrays at runtime

###for individual thread
+ PC Register (Program counter register)
+ jvm stack
+ nativ method stack


other explanation
-----------------

+ heap
    + young generation
        + include Eden memory and two survivor memory spaces
        + most of the newly create objects are located in the 
            Eden memory space
        + when Eden space is filled with objects, **Minor GC** is 
            performed and all the survivor objects are moved 
            to one of the survivor spaces
        + Minor GC also checks the survivor objects and move them to
            the other survivor space. 
            So at a time, one of the survivor is always empty.
        + objects that are survived after many cycles of GC, 
            are moved to the Old generation objects.
    + old generation
        + usually **Major GC** is performed when old Generation is full.
        + all GC operations are 'stop the world' events because
            all application thread are stopped until the operation completes.
+ Permant Generation
    + Perm Gen is not part of Java Heap memory
    + includes method area.

###garbage Collection
+ delete all unreferenced objects


another explantation 
--------------------

+ stack
    + methods
+ heap
