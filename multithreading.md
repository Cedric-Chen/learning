Multithreading and MultiProcessing
==================================

Doing sevearl work at the same time.

Python
------
### `threading` moudle

```Python
import threading

def square():
    pass

def cube():
    pass

arr = [1, 2]

t1 = threading.Thread(target = square, args = (arr,) )
t1 = threading.Thread(target = cube, args = (arr,) )

t1.start()  # start threading 1
t2.start()  # start threadign 2 
t1.join()   # main thread waits here until threading 1 is finished
t2.join()   # main thread waits here until threading 2 is finished
```

### `multiprocessing` module

```Python
import multiprocessing 

def square():
    pass

def cube():
    pass

arr = [1, 2]

t1 = multiprocessing.Multiprocessing(target = square, args = (arr,) )
t1 = multiprocessing.Multiprocessing(target = cube, args = (arr,) )

t1.start()  # start 1
t2.start()  # start 2

t1.join()   # wait here until 1 is finished
t2.join()   # wait here until 2 is finished
```

#### Difference between `multiprocessing` and `multithreading`:

+ In multiprocessing, different processes use different memory space, 
    and they do not share them;
+ Multiple threads are within one single process, 
    and they have different stack memories, but they share heap memory.

#### multiprocessing pool (map reduce)

```Python
from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5])
```


C++
---

`thread` package

```C++
#include <iostrem>
#include <thread>

using namespace std;

void fn(){
    cout << "hello world" <<endl;
}

int main(){
    thread t1(fn);  // t1 starts running
    
    // t1.join();   // main thread waits for t1 to fininsh
    // t1.detach(); // t1 become free on its own

    // if (t1.joinable())
    //      t1.join();

    return 0;
}
```


Java
----

Extending a class by `Thread` class.
