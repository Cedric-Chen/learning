Memory Management
=================

Python
------
[视频链接](https://www.youtube.com/watch?v=arxWaw-E8QQ)

Everything is a object in Python.

Python is a dynamically typed language. So there is no need to specify the type.

### memory component

+ heap
    + the objects and instance variables are created on heap
    + when an onject in heap is not reference anymore, 
        it is removed __immediately__.
        The algorithm used for `Garbage Collection` is called
        `Reference Counting`.
+ stack
    + the methods and variables are created on stack.
    + store reference to __object on heap__
    + a new stack frame is created on invocation of a funcition/method.


JAVA
----

+ stack
    + method invocations
    + local variables: variables declared inside a method
        + primitive variable: integers, decimals or characters
        + reference to non-primitive variable
+ heap (garbagr-collectable heap)
    + all objects live here.
    + garbage collector
        + generations: 
            + young generation
                + minor garbage collection: young generations, 
                'stop the world event' - all thread stop and wait
            + old generation
                + major garbage collection: 'Stop the World' event
            + permanent generation
        
Variables stored in stacks are only visible to the owner Thread,
while objects created in heap are visible to all thread.

C++
---
Operation on stack is one CPU instruction, which is easy and efficient.

Operation on heap is a bunch of things.
