# Python Data Structures

## Python Dictionaries
* Often called "dicts" for short
* Map a `key` to a corresponding `value`. 
* Keys are usually strings, values can be any python type.
* Lookups are very efficient -- no matter how large a dictionary is, asking for the value corresponding to a key happens in the same amount of time.
* `myDict["key"]` retreives the corresponding value for "key" in the dictionary `myDict`. If "key" is not a valid key that exists in `myDict`, then a `KeyError` exception will be thrown.
* `myDict.get("key")` will do the above but will NOT throw a `KeyError` if the key does not exist--instead it will return `None`. 

Example:
```python
# Instantiate dictionary called instructor
instructor = {
  "name": "Mark Palmeri",
  "degrees": ["MD", "PhD", "BSE"],
  "age": 21,
}

temp = instructor["name"] # retreives the value corresponding to "name" key in the instructor dictionary
temp = instructor["key-doesnt-exist"] # throws a KeyError exception!
temp = instructor.get("name") # retreives the value corresponding to "name" key in the instructor dictionary
temp = instructor.get("key-doesnt-exist") # doesn't throw any errors but returns None because key doesn't exist
```

Advantages of dicts:
```python
teams_csv = [
  ["Suyash", "Kumar", "sk317", "suyashkumar", "Instructors"],
  ["Mark", "Palmeri", "mlp6", "mlp6", "Instructors"],
  ...
]

# Representing as dictionaries with team keys will lead to more efficient queries of who is on a team:
teams = {
  "Instructors": ["sk317", "mlp6"],
  "CoolKids": ["kmc97", "deeptig94", "souhaila30"],
  ...
}

# Will always take the same amount of time no matter how many teams exist
def whos_on_team_dict(team):
  return teams[team] 

# Will take longer to iterate the more teams there are
def whos_on_team_csv(team):
  net_ids = []
  for row in team_csv: 
    if row[4] == team:
      net_ids.append(row[2])
  return net_ids
```

## Pandas DataFrames
* A useful container for data (essentially a table)
* Provides many useful and efficient functions out of the box to operate on the table of data
* Some useful functions: `pandas.read_csv("test.csv")` and `pandas.to_csv("file.csv")`
