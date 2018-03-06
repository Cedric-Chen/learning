Python Notes
============

11.20
-----
### use built-in type as base class
+ this syntax is used in python 2.x; 
    in python 3.x this is not used becuase it is set as default.

### __slots__
+ In Python every class can have instance attributes. 
    By default Python uses a dict to store an object’s instance attributes.
    + For __small classes__ with known attributes it might be a bottleneck. 
        The dict wastes a lot of RAM. 
    + It involves the usage of __slots__ to tell Python not to use a dict, 
        and only allocate space for a fixed set of attributes. 
    + example: 

```
        class MyClass(object):
            __slots__ = ['name', 'identifier']
            def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier
                self.set_up()
            # ...
```

### __repr__
+ specify the reusult of str(class name) or repr(class name)

11.28
-----
### @property
+ example 

    ```Python
    class Celsius:
        def __init__(self, temperature = 0):
            self.temperature = temperature

        def get_temperature(self):
            return self._temperature

        def set_temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            self._temperature = value

        temperature = property(get_temperature,set_temperature)
    ```

    ```Python
    c = Celsius()
    c.temperature = 100     
    # this will automatically call member funtion 'set_temperature'.
    print(c.temperature)
    # this will automatically call member function 'get_temperature'.
    ```

+ signature of property

    ```Python
    property(fget=None, fset=None, fdel=None, doc=None)
    ```

+ using decorator is recommended.

    ```Python
    class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
    ```

+ use for loop in one line

```Python
sum(c.size() for c in self._children)
```

+ all, any

```
all(c is None for c in self._children)
```

12.21
-----

+ @classmethod, @staticmethod
    + ``classmethod`` works like another constrcutor;
        it needs ``cls`` as non-optional input parameter.

    ```
    class Date(object):
        def __init__(self, day=0, month=0, year=0):
            self.day = day
            self.month = month
            self.year = year

        @classmethod
        def from_string(cls, date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            date1 = cls(day, month, year)
            return date1

    date2 = Date.from_string('11-09-2012')
    ```

    + ``staticmethod`` is used for common method for this class
        which is not bounded to any instantiation of it.
        It has no non-optional input parameters.

    ```
    class Date(object):
        #...

        @staticmethod
        def is_date_valid(date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            return day <= 31 and month <= 12 and year <= 3999

    # usage
    is_date = Date.is_date_valid('11-09-2012')
    ```

3.4
---

### ____call____
Implementing the __call__ magic method in a class causes its 
instances to become callables.

```Python
class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-'*80

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
```

Expected output:

```
(1, 2, 3)
{}
--------------------------------------------------------------------------------
()
{'a': 1, 'c': 3, 'b': 2}
--------------------------------------------------------------------------------
(4, 5, 6)
{'e': 5, 'd': 4, 'f': 6}
--------------------------------------------------------------------------------
```

### in Python2.x, class needs inherit 'object'
In Python2.x, there are 2 styles of classes:

+ classic style: they have no built-in type as a base class.
+ new style: they have a built-in type as a base class meaning 
    that, directly or indirectly, they have object as a base class.

There are many benefits to use __new style__. 
[Please see here.](https://stackoverflow.com/questions/4015417/python-class-inherits-object)
It is highly recommended.

In Python3.x, only new-style classes exist.

### ____enter____ ____exit____
Using these magic methods (__enter__, __exit__) allows you to 
implement objects which can be used easily with the with statement.

```Python
class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()

with DatabaseConnection() as mydbconn:
    # do stuff
```

3.5
---
### iterator and generator
+ The built-in function `iter` takes an iterable object 
    and returns an iterator. Each time we call the next method 
    on the iterator gives us the next element. If there are no more 
    elements, it raises a StopIteration.
    + The `__iter__` method is what makes an object iterable. 
        Behind the scenes, the iter function calls `__iter__` method 
        on the given object.
    
    ```Python
    class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()   
    ```

+ Generators simplifies creation of iterators. A generator is 
    a function that produces a sequence of results instead of a single value.

    ```Python
    def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
    ```

