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

## Configure SSH keys for faster login
When you use SSH to login to your virtual machine (VM) in the cloud, you currently have to provide the password for the `vcm` user. You can use SSH keys, which rely on concepts of public-private key encrpytion to eliminate the login step, as the VM can verify that you are who you say you are through this mechanism. The high-level idea here is as follows: public and private keys are generated in pairs -- each public key has a corresponding private key. As you might imagine the public key can be shared widely and the private key should be kept private. Any holder of your public key can cryptographically verify if a message is sent from a party holding the corresponding private key without being modified (and only _you_ should have the private key). In this way if you login to your VM and add your public key in a special place, your VM can verify that it is indeed _you_ who is trying to login over ssh because it can verify a signed message (by your private key) that your computer sends to the VM.

Steps to set this up:
1. Print out and _copy_ your public key (should have been generated already if you set up SSH with github already):
   ```sh
   cat ~/.ssh/id_rsa.pub
   ```
2. Now login _as usual_ to your virtual machine
3. You will now paste your public key from step 1 into the `~/.ssh/authorized_keys` file. Type `vim ~/.ssh/authorized_keys` and paste your public key into the file. This is the file that holds the public keys of all machines/users who should be able to `ssh` into this machine.
4. Logout of the virtual machine, and try to ssh back into it again. You should notice it logs you in automatically without prompting you for a password!
