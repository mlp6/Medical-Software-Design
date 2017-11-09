# Using Databases

Following up from our overview of databases lecture last class, today we will build a small webservice that utilizes a database. I encourage you to use the database of your choice (SQL, PostgreSQL), but the instructions will be geared towards MongoDB. The in-class assignment will be creating a simple web service allows users to add patients with name, age, and bmi. An endpoint will then be written to return the average bmi of patients in a certain age range. 

## VM Setup
* Install mongodb on your VM by following the instructions [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/). For step 2, everyone in this class should be on Ubuntu 16.04 (you can check by running `lsb_release -a`).
* We will be using the `pymodm` package to interface with MongoDB in a structured way. However, `pymodm` is not a `conda` package (it's a `pip` package only). So we'll have to make sure we're setup to use `virtualenv` and `pip`
    * On your VM (and locally on your machine if you'll be doing development there) go ahead and run `pip install virtualenv`
    * If you don't have `pip` then go ahead and follow the instructions [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/lecture04/pip-and-conda-install.md) to get setup. 
 
## PIP and virtualenv
 As mentioned above, we'll be using `pip` and `virtualenv` instead of `conda`. 
 * Create a new repository for this project
 * Setup a virtual environment __inside your repository__. You can do this by running `virtualenv env` which will create a virtual environment called `env`. You can then activate the virtual environment by running `source env/bin/activate` from inside your repo. To deactivate it later, you can run `deactivate`.
 * Setup `requirements.txt` -- create the file and add:
   ```
   pymodm
   Flask
   ```
 * You can now install the requirements inside your virtual environment by running `pip install -r requirements.txt`
 
## pymodm example
We will step through a pymodm example in class, but below is the sample code: 
```
from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590")

class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()

u = User('user1@email.com', last_name='Ross', first_name='Bob')
u.save()
```

 
 

