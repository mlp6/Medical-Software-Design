# Deployment of Flask Servers, Docker introduction

## Lecture outline
* Review terminology
   * API
   * RESTful APIs
   * 127.0.0.1
   * /hello?
   * GET vs POST
   * Client vs server?
   * Where are RESTful APIs used?
* Review Flask servers
* Was everyone able to complete the Flask mini-project from last class?
* OIT Virtual Machine Configuration
* Deploying flask servers in production using `gunicorn`
* Databases introduction [time permitting]
* Docker introduction [time permitting]


## Deploying Flask Servers in Production
When we run `flask` applications using the `FLASK_APP=server.py flask run` (or `python server.py`) command, we are using Flask's development server to serve requests for our application. The flask development server is useful for debugging and for development but lacks efficiencies and the ability to have process-level load balancing (more on this later) that we might want in production when serving our app to the world. 

### gunicorn deployment

We will be using the `gunicorn` tool to serve our `flask` application logic in production. The `flask` decorators we use to specify our routing and application logic expose a consistent API (called `wsgi`) that allows us to switch out the flask development server with another server like `gunicorn` that will receive HTTP requests and route them efficiently to our application logic (as specified by our routes/decorators). 

An example application that we may want to serve can be found in the [gunicorn_example](gunicorn_example) folder. Go there, activate an environment, and install the requirements (`pip install -r requirements.txt`). This will install the `gunicorn` dependency. 

To run that sample application simply run

```sh
gunicorn --bind 127.0.0.1:5000 main:app
```

The `main:app` comes from the fact that our `flask` application is in the module `main` (`main.py`) and that the top level identifier for the flask application is called `app` (see line 2 of `main.py`). 

#### Public facing deployments
When you `bind` `127.0.0.1` the loopback address, your server will __only__ process requests that originate from your machine. This means that if I want to send a request to your server from my machine, I cannot do so. To allow public computers to send requests to your server, you need to bind the special address `0.0.0.0` as follows:

```sh
gunicorn --bind 0.0.0.0:5000 main:app
```

#### Load balancing
`gunicorn` can spin up multiple "worker" processes that allow for some additional effiencies from asynchronous processing of requests. What this means is that multiple requests can be processed at the same time on the same machine instead of requiring that each request fully complete before processing the next one on the queue. You can specify the number of workers as follows:

```sh
gunicorn --bind 127.0.0.1:5000 --workers 4 main:app
```

## Virtual Machines
Everyone's Duke OIT virtual machine allotment has increased to 2 VMs, so everyone should be able to create and provision a ubuntu VM. Once you provision a ubuntu VM, run the following commands to provision your machine:

```sh
sudo apt-get install python3-pip screen
pip3 install virtualenv
```

You should now be able to pull down python3 projects that use virtualenvs and pip. For example this setup is sufficient for setting up and running the [gunicorn_example](gunicorn_example) server on your VM.

## SSH
To interact with your virtual machine, we can use `ssh` to gain access to a shell/terminal on your remote virtual machine. Windows users should use [mobaxterm](https://mobaxterm.mobatek.net/) to do this process, or you can use `ssh` commands from the built-in Ubuntu subsystem.

A general SSH command looks like:
```sh
ssh <username>@<server ip or hostname>
```

For your VCMs you should always be using the `vcm` username, so your command will look something like:
```sh
ssh vcm@vcm@vcm-3461.vm.duke.edu
```

## Screen
Screen is a linux program that allows you to create multiple terminal sessions (think "tabs") that can be attached and detached. What this means is that you can spin up a "screen" where you are running a program, detach that "screen" and then logout of the VM without the program on that screen being terminated. These are the screen commands:

* `screen -S <new_screen_name>`: creates a new screen with the name <new_screen_name>
* `screen -r <screen_name`> reattaches the screen called <screen_name>
* To detach a screen that is currently active, press `ctrl + a then d`

## Mini-project
* Push your web service from last class to a github repository `flask_getting_started` under your github user
* Clone your repository to your VM
* Deploy it using gunicorn in a `screen`
* Write a client program (`client.py`) using the `requests` library (see the [previous lecture](../intro_web_services/Requests.ipynb)) that calls every API written on your web server and outputs the results to `STDOUT` (your terminal). You should be sending requests to an address that looks something like `vcm-3461.vm.duke.edu:5000`. 
* Commit this client program into your `flask_getting_started` repository (even though it is not needed for the server side of this project).
