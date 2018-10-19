# Dictionary Data Type
What is a dictionary in our common understanding?  A list of words and
definitions associated with each of those words:

* day:  the time between sunset and sundown
* food:  any nutritious substance that people or animals eat or drink

### Creating Dictionaries in Python
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out"}
    return new_dictionary
    
def output_dictionary(in_dictionary):
    print("Variable type:")
    print(type(in_dictionary))
    print("Dictionary contents:")
    print(in_dictionary)

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    output_dictionary(my_dictionary)
    
OUTPUT:
Variable type:
<class 'dict'>
Dictionary contents:
{'day': 'between sunrise and sunset', 'food': 'something to eat', 
    'night': 'when the moon is out'}
```


* Dictionary maps a `key` to a `value`.  In the example above, keys are the
words and values are the definitions.

* Lookups in a dictionary using a key are very efficient -- no matter how large 
a dictionary is, asking for the value corresponding to a key happens in the 
same amount of time.

### Retrieving values form a dictionary 
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out"}
    return new_dictionary
    
def retrieve_definitions(in_dictionary):
    x = in_dictionary["day"]
    print(x)
    y = in_dictionary.get("food")
    print(y)

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    retrieve_definitions(my_dictionary)
    
OUTPUT:
between sunrise and sunset
something to eat
```

* `dictionary["key"]` returns the corresponding value for "key", but will raise
 a `KeyError` if key does not exist.  
* `dictionary.get("key")` will also return the value for "key", but will NOT 
throw an error if key does not exist, but rather return `None`.

### Adding values to a dictionary
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night": "when the moon is out"}
    return new_dictionary

def add_to_dictionary(in_dictionary):
    in_dictionary["drink"] = "swallowing a liquid"
    return in_dictionary

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    my_dictionary = add_to_dictionary(my_dictionary)
    print(my_dictionary["drink"])

OUTPUT:
swallowing a liquid
```

### Dictionaries have many built-in methods.
<https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>

### Contents of Dictionaries
Keys are usually strings, but the values can be any python type.  In the
example below, a dictionary is created that has values containing strings,
numbers, and booleans.
```
def create_person():
    bob = {"First Name": "Robert",
           "Last Name":  "Smith",
           "Age": 35,
           "Ave Heart Rate": 65,
           "HIPPA On File": True}
    return bob
    
def output_person_info(person):
    x = full_name(person)
    print("Full name = {}".format(x))
    a = person["Age"]
    print("Age = {}".format(a))
    m = minor_or_adult(person)
    print(m)

def full_name(person):
    return person["First Name"] + " " + person["Last Name"]

def minor_or_adult(person):
    if person["Age"] > 17:
        return "Adult"
    else:
        return "Minor"
    
if __name__ == "__main__":
    newPerson = create_person()
    print(type(newPerson))
    print(newPerson)
    output_person_info(newPerson)
    
OUTPUT:
<class 'dict'>
{'First Name': 'Robert', 'Last Name': 'Smith', 'Age': 35, 'Ave Heart Rate': 65,
    'HIPPA On File': True}
Full name = Robert Smith
Age = 35
Adult

```

Values in a dictionary can also be tuples, lists, or dictionaries.
```
bob = {"First Name": "Robert",
           "Last Name":  "Smith",
           "Age": 35,
           "Visits": ["1/3/2014", "2/15/2015", "5/22/2016"]}
print(bob["Visits"])
print(bob["Visits"][1])

OUTPUT:
['1/3/2014', '2/15/2015', '5/22/2016']
2/15/2015
           
```
In the examples above, we have made dictionaries to contain definitions and
dictionaries to contain personal information.  We have written functions that
are designed to manipulate the data in those dictionaries.

Now, imagine that you have a very large code base with many different types of
dictionaries, and each type of dictionary has specific functions to manipulate
or act on those dictionaries.  It could start to get confusing about which
functions are meant to act on which dictionaries.  Also, when a second version
of a dictionary is made (for example, a new person dictionary), we need to 
ensure that it contains the same information.  

"Classes" exist to address some of these concerns. 

# Classes
* Classes can group together a set of variables and functions that are related.
* Variables associated with the class are called attributes or properties.
* Functions associated with the class are called methods.

## Creating a Class

A class is defined with the following heading:
```
class Person(object):
```
`Person` is the name of the class.  `(object)` specifies the type of class from
which this new class inherits.  Inheritance will be covered later in the course.

The properties (variables) of the class are created and populated in a special
function called `__init__`.

```
class Person(object):

    def __init__(self, first_name_arg, last_name_arg)
        self.firstname = first_name_arg
        self.lastname = last_name_arg
```
The `__init__` function is called immediately upon creating a new instance 
(or manifestation) of the class in a variable as shown here:
```
x = Person("Robert", "Smith")
```

The first parameter in the definition of all functions in a class is `self` 
and is required.
`self` represents the instance of the class that will be made and is how the
code accesses the properties and methods that are defined in the
class.  After `self` in the definition of `__init__`, include any other 
parameters you 
want to have available when creating a new object of this class.  In the 
example above, we include two parameters that are used for initializing the 
class properties of `self.firstname` and `self.lastname`.  The inclusion of 
`self.` in the variable name makes it available to all of the functions in 
the class.  

Note that the `__init__` function can do more than just assign variables.  It
can do other calculations or call other functions in the class as needed.

While `self` must be included in the parameter list when defining
the function in the class, it is not included in the call to create an
instance of the class.

In sum, `x = Person("Robert", "Smith")` will
create an object (an instance of a class) in the variable x, and will put the 
value "Robert" into
the `self.firstname` property in the object and "Smith" into the `self.lastname`
property in the object.

## Accessing Class Properties

To access the class properties in our code, we reference the object variable name, 
followed by a `.` and the property name:
```
x = Person("Robert", "Smith")
print(x.firstname)
print(x.lastname)

OUTPUT:
Robert
Smith
```

## Class Methods
In addition to variables or properties, classes can have functions, called
methods, that act on the variables found in the class.  Consider the
following function added to the `Person` class.
```
    def return_full_name(self):
        return self.firstname + " " + self.lastname
```
This function can be called from our code as follows:
```
x = Person("Robert", "Smith")
print(x.firstname)
print(x.lastname)
print(x.return_full_name())

OUTPUT:
Robert
Smith
Robert Smith
```
Notice that when we refer to a method, we need to include `()` after the name
as it is a function call.  If the method needs parameters, they would be 
included inside the parentheses.

## Default Parameters

Let's add Age as a property in our Class definition.
```
class Person(object):

    def __init__(self, first_name_arg, last_name_arg, age_arg)
        self.firstname = first_name_arg
        self.lastname = last_name_arg
        self.age = age_arg
```
But, let's say we forgot to update our line of code that read 
`x = Person("Robert", "Smith")`.  Python will return 
```
TypeError: __init__() missing 1 required positional argument: 'age_arg'
```
We can avoid this error by giving the `__init__` function a default
value for the age parameter as follows:
```
    def __init__(self, first_name_arg, last_name_arg, age_arg=None):
``` 
Now, if no value is provided for age, the `__init__` procedure will give fill
it with `None` and avoid an error.  We can then later set the age by
directly accessing the property of the class as such:
```
x = Person("Robert", "Smith")`
x.age = 35
```

## Creating and storing multiple objects

A Class is a blueprint/template for a collection of properties and methods.
We can then make may different instances of a class, called objects.  Each
object will have its own set of values for the properties and does not know
the contents or properties of other objects.  

Using the example `Person` class above, we can now make a database of Person
objects.
```
def create_persons_database():
    database = []
    new_person = Person("Ann", "Jones", 35)
    database.append(new_person)
    new_person = Person("Bruce", "Wayne", 40)
    database.append(new_person)
    for x in database:
        print(x.return_full_name())
    print(database[0].age)

```
The function above creates an empty list called `database`.  An instance of
the `Person` class is created in the variable `new_person` and then
appended to the `database` list.  Then, a new instance of the `Person`
class is created also using the `new_person` variable.  While `new_person`
now points to this new instance, the first instance still exists inside the
`database` list.  The second instance is then appended to the `database`
list.

The objects found in the `database` list can be access as shown by the two
example:  one using a `for` loop and one accessing a specific item via an
index.

# Hidden Properties and Set/Get Functions
There may be times when, upon the setting of a property in a class, I may
want to do some calculations on that input before storing it in the 
property.  

Let's assume that I want to add the persons weight to the `Person` class. 
And, let's imagine that I have a really old
scale that, depending on how it is used, might record a negative weight.  I
would want this converted to a positive weight in the persons file.

First, I need to define the weight property in the class.  But, unlike
other properties, I don't want the user to be able to access it directly
because I don't want a negative number to be used.  So, I "hide" the
property by including double underscore before its name when creating it
in the `__init__` function.
```
    def __init__(self, first_name_arg, last_name_arg, age_arg=None):
        self.firstname = first_name_arg
        self.lastname = last_name_arg
        self.age = age_arg
        self.__weight = None

```
This property `__weight` is not accessible outside of the class.  So, in 
order for the code outside of the class to set or return the weight , 
I need to define specific functions in the class to perform those functions.
```
    def set_weight(self, weight_arg):
        if weight_arg < 0:
            self.__weight = -weight_arg
        else:
            self.__weight = weight_arg

    def get_weight(self):
        return self.__weight
```
With these functions, some code is now run to manipulate the inputs before
setting the property of the class.
```
john = Person("John", "Smith", 45)
john.set_seight(-150)
x = john.get_weight()
print(x)

OUTPUT:
150
```

Let's say that John has gained 17 pounds.  Adding 17 to the weight would
require the following `get_weight` and `set_weight` calls.
```
john.set_weight(john.get_weight()+17)
print(john.get_weight())

OUTPUT:
167
```
That is a very ugly way to add 17 to a variable.
  
# Property Decorator
 Property decorators allow the use of functions when getting and setting
 class properties. 
 
 First, the `@property` decorator is used before a class function that gets 
 (or returns) the property of interest. 
 ``` 
    @property
    def weight(self):
        return self.__weight
  ```
Now that `weight` is defined as a property, we use the `@weight.setter`
decorator before a class function that sets the weight.
```
  @weight.setter
  def weight(self, weight_arg):
      if weight_arg < 0:
          self.__weight = -weight_arg
      else:
          self.__weight = weight_arg
```

Now, in the code, we can get and set the weight as follows:
```
joan = Person("Joan", "Stevens", 45)
joan.weight = -150
x = joan.weight
print("Before weight = {}".format(x))
joan.weight =+ 17
y = joan.weight
print("After weight = {}".format(y))
```  
The `weight` property created by the `@property` decorator can now be used
like any other kind of property or variable, but the setting and getting
are now controlled by functions that we can control.

The generic format is:
```
    @property
    def name(self):
        {CODE THAT RETURNS YOUR HIDDEN VARIABLE}
        
    @name.setter
    def name(self,input):
        {CODE THAT TAKES INPUT, DOES DESIRED MANIPULATION,
           AND STORES RESULT IN HIDDEN VARIABLE}
```
where `name` can be choosen by user.
  
  # Numpy
 Finally, as discussed in class, here are the Numpy documentation websites
 that demonstrate how to create numpy arrays in the code and from input
 files:
  <https://docs.scipy.org/doc/numpy/user/basics.html>
  <https://docs.scipy.org/doc/numpy/user/basics.creation.html>
  <https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html>
