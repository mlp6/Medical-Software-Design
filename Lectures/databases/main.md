# Databases and Docker intro

Today we're going to continue talking about databases and how to integrate them into your projects. Databases offer centralized persistent storage with some fantastic garuntees about data consistency, availability, and/or partition tolerance (generally you only get two out of the three, unless you're [Google Spanner](https://cloud.google.com/spanner/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_201438283354-ADGP_Hybrid%20%7C%20AW%20SEM%20%7C%20BKWS%20%7C%20Multi%20~%20Google%20Spanner-KWID_43700021846306996-kwd-343702663564&utm_term=KW_google%20spanner-ST_google%20spanner&gclid=EAIaIQobChMIjdL358Lf2QIVQUOGCh3zAQVtEAAYASAAEgJEQPD_BwE&dclid=CI3U6ujC39kCFQtmwQodrQMLNw)). 

## Docker
To install Docker, follow these instructions [for mac](https://docs.docker.com/docker-for-mac/install/) and [for ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (including ubuntu subsystem) and finally if you really have to, for [windows](https://docs.docker.com/docker-for-windows/install/).

Docker allows us to run programs (with all of their dependencies) in a consistent environment called a __container__. You can think of this container as a "virtual machine" that runs on your computer, like a mini linux computer running inside your own (although it's way more efficient than that). You can push and pull containers that have all of the programs and dependencies already setup to a central place called [DockerHub](https://hub.docker.com/). 

Some common docker commands:
* `docker pull mongo` this pulls down the full mongodb database container from DockerHub
* `docker run mongo` this runs the docker container and the program (mongodb) that comes with it.
* `docker run -it mongo bash` this starts up the mongodb container, and opens up `bash` shell inside the container (kind of like ssh-ing into the container.
* `docker exec -it <container_id> bash` -- "ssh" into a currently running container. 

When we run containers, we can __bind__ container ports to our local machine ports and even bind parts of our filesystem into the container. 

In the future, we'll explore Docker further, and chat about how to create your own containers for your software.

## MongoDB
MongoDB is a non-relational "NoSQL" database that is essentially an object store -- it lets you build structured objects and put them into storage with easy queries for retrieval later. Generally MongoDB is a __schemaless__ database (unlike SQL databases), which means you generally do not have to specify a data structure schema for objects before inserting them into collections. This isn't great for programming because we'd like validation on our data models we're putting into and getting out of the database, so we're going to use `pymodm` to help us interface with MongoDB in that manner. 

Below is the minimal example of a program that connects to a MongoDB database called `bme590` running on `localhost:27017`. To get a database running using `Docker` (which we will introduce in class) simply run 

```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
which will run the `mongo` container, binding the container's `27017` port to your computer's `27017` and binding the current directory's folder `db` to be the place where data is stored inside the container. 
```py
from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590") # connect to database

class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    password = fields.CharField()

u = User('user1@email.com', last_name='Ross', first_name='Bob')
u2 = User('user2@email.com', last_name='Ross', first_name='Rob')

u.save()
u2.save()

for user in User.objects.raw({"first_name":"Rob"}):
        print(user)
	print(user.first_name)
	print(user.last_name)
```

## Mini-project/Assignment
Create a new repository under your github username called `heart_rate_databases_introduction`. Build a web service that exposes the following functionality. You may use any database you are comfortable with or interested in exploring. 

* `POST /api/heart_rate` with
  ```sh
  {
      "user_email": "suyash@suyashkumar.com",
      "user_age": 50, // in years
      "heart_rate": 100
  }
  ```
  which should store this heart rate measurement for the user with that email. Be sure to include the [current time stamp](https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python) in your database. 
* `GET /api/heart_rate/<user_email>` should return all heart rate measurements for that user
* `GET /api/heart_rate/average/<user_email>` should return the user's average heart rate over all measurements
* `POST /api/heart_rate/interval_average` with 
  ```
  {
      "user_email": "",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339" // date string
  }
  ```
  Should calculate and return the average heart rate for the user since the time specified. This should also return an indication of weather this average heart rate is considered [tachycardic](https://en.wikipedia.org/wiki/Tachycardia) for the user's current (latest recorded) age.
  
For this assignment, be sure to write modular code. This means your handler functions for routes should be calling other independent functions in different modules as frequently as possible. All of those other independant functions should be tested. You should also remember to validate user inputs that come from (`request.get_json()`) to ensure the right fields exist in the data and that they are the right type. You can write independant, testable `validate_heart_rate_request(r)` functions. You do not have to test the flask handler functions directly, but all other functions should be tested.  

## MySQL/postgres
An example of a postgres project is [here](../intro_web_services/class_roster_server). For SQL databases, we store data across tables and specify relationships across those tables (as discussed in the previous database lecture). If you use MySQL or Postgres in this class, you will not __have__ to use an ORM or schema manager since SQL databases impose their internal schemas. 


