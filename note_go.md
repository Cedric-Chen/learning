GO
==

4.3
---

+ defer
    + The deferred call's arguemts are evaluated immediately,
        but the function call is not executed 
        until the surrounding function returns.
    + Deferred funtion called are pushed onto a stack. 
        When a function returns, its deferred calls are executed in 
        last-in-first-out order.
+ dynamically-size array - slice
    + A slice does not store any data, it just describes a section 
        of an underlying array.
+ nil is the zero value for pointers, interfaces, maps, slices, 
    channels and function types, representing an uninitialized value.


4.4
---

+ GO does not have classes. However, we can define methods on types.
    + methods with pointer or value receivers take either a value
        or a pointer as the receiver when they are called.
    + using `pointer receiver` is recommended.
+ goroutines, channels, mutex
    + ?????
