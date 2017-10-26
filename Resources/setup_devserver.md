# Configure Virtual Machine
To configure your virtual machine, you must first install conda and then setup your conda virtual environment to run your application. 

To install conda on your development machine, first `ssh` into your machine and then run the following commands. As the installer runs, select yes for the prompts and use the default install location.
```sh
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh # Fetch this file from the internet to your machine
chmod +x Miniconda3-latest-Linux-x86_64.sh # Allow this file to be executable
./Miniconda3-latest-Linux-x86_64.sh # Execute this shell script
source ~/.bashrc # Re-source bashrc to pull in latest config
```

After everything has run, you should then be able to run `which conda` successfully. 

When running your flask application you should use the following command:

```sh
FLASK_APP=test.py flask run --host 0.0.0.0
```

Setting the `host` to 0.0.0.0 tells flask to run the server locally but to allow external connections (from outside your remote machine) to make requests to your development server.

You should now be able to make requests to your server from anywhere on the internet at port 5000. For example, you should be able to hit a url like `http://vcm-1866.vm.duke.edu:5000/` except with your VM name instead of mine. 
