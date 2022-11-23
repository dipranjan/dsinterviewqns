# Theoretical

<details>

<summary>Built in Datatypes</summary>

What are the _built-in types_ available In Python?

**Answer**

Common _immutable_ type:

1. numbers: `int()`, `float()`, `complex()`
2. immutable sequences: `str()`, `tuple()`, `frozenset()`, `bytes()`

Common _mutable_ type (almost everything else):

1. mutable sequences: `list()`, `bytearray()`
2. set type: `set()`
3. mapping type: `dict()`
4. classes, class instances
5. etc.

You have to understand that Python represents all its data as objects. Some of these objects like lists and dictionaries are mutable, meaning you can change their content without changing their identity. Other objects like integers, floats, strings and tuples are objects that can not be changed.

</details>

<details>

<summary>Lambda</summary>

What is _Lambda Functions_ in Python?

**Answer**

A **Lambda Function** is a small anonymous function. A lambda function can take _any_ number of arguments but can _only_ have _one_ expression.

```python
x = lambda a : a + 10
print(x(5)) # Output: 15
```

</details>

<details>

<summary><code>tuple</code> vs <code>list</code> vs <code>dictionary</code></summary>

When to use a `tuple` vs `list` vs `dictionary` in Python?

**Answer**

* Use a `tuple` to store a sequence of items that _will not change_.
* Use a `list` to store a sequence of items that _may change_.
* Use a `dictionary` when you want to associate _pairs_ of two items.

</details>

<details>

<summary>local vs global</summary>

What are the rules for local and global variables in Python?

**Answer**

While in many or most other programming languages variables are treated as global if not declared otherwise, Python deals with variables the other way around. They are local, if not otherwise declared.

* In Python, variables that are only referenced inside a function are implicitly _global_.
* If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a _local_ unless explicitly declared as global.

Requiring global for assigned variables provides a bar against unintended side-effects.

</details>

<details>

<summary>Descriptors</summary>

What are descriptors?

**Answer**

Descriptors were introduced to Python way back in version 2.2. They provide the developer with the ability to add managed attributes to objects. The methods needed to create a descriptor are `__get__`, `__set__` and `__delete__`. If you define any of these methods, then you have created a descriptor.

Descriptors power a lot of the magic of Python’s internals. They are what make properties, methods and even the super function work. They are also used to implement the new style classes that were also introduced in Python 2.2.

</details>

<details>

<summary>switch case</summary>

Does Python have a _switch-case_ statement?

**Answer**

In Python before 3.10, we **do not hav**e a switch-case statement. Here, you may write a switch function to use. Else, you may use a set of if-elif-else statements. To implement a function for this, we may use a dictionary.

```python
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print switcher.get(argument, "Invalid month")
```

Python 3.10 (2021) introduced the [`match`-`case`](https://www.python.org/dev/peps/pep-0634/) statement which provides a first-class implementation of a "switch" for Python. For example:

For example:

```python
def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
```

The `match`-`case` statement is considerably more powerful than this simple example.

</details>

<details>

<summary>static methods</summary>

Is it possible to have static methods in Python?

**Answer** ([Source](https://www.digitalocean.com/community/tutorials/python-static-method))

Static methods in Python are extremely similar to [python class](https://www.digitalocean.com/community/tutorials/python-classes-objects) level methods, the difference being that a static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it. Let’s see how we can create static methods in Python.

Static methods have a very clear use-case. When we need some functionality not w.r.t an Object but w.r.t the complete class, we make a method static. This is pretty much advantageous when we need to create Utility methods as they aren’t tied to an object lifecycle usually. Finally, note that in a static method, we don’t need the `self` to be passed as the first argument.

</details>
