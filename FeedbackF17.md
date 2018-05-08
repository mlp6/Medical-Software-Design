# Fall 2017 Feedback
Random emails, class announcements, etc. that were accumulated from running the fall version of the course w/ Suyash.  Consolidating here to integrate into the curriculum this semester and not have them sit idle in my email archive.
## Raising exceptions (from Arjun)
The URL below does a good overview of basic practices to remember when raising
errors in python. While raising errors hasn't been emphasized much yet, it is
important to know how to handle and respond to cases that you do not expect.
https://stackoverflow.com/questions/2525845/proper-way-in-python-to-raise-errors-while-setting-variables
Take these practices with a grain of salt- each programmer/group/team has a
different implementation of notifying when something has happened, but the
framework is the same- catch that there is an error in the program, show that
there is an error to the user, try to fix the error or break out of program (in
real clients, the latter is a huge red flag)

## Ignoring IDE-generated files
Several groups are hitting an issue with conflicts of files in their
repositories that should not actually be committed.  One such example is the
directory .idea/ that is created by PyCharm.  That directory contains local
configuration files for your PyCharm environment, but that can quickly cause
problems when different developers use different settings.  You can manually
not add the `.idea/*` files to your commit queues, but if you would like git to
ignore that entire directory, then you can create a .gitignore file in the root
directory of your repository that containts a line: .idea git will ignore any
of the contents of .gitignore when displaying file status, etc.  You can
forcibly override the file ignores if you had to at some point.  If you have
already commited and pushed .idea/ to GitHub, you can remove the directory from
git--but keep it locally--by using git rm --cached .idea/ from the root-level
of your repository.  Other good things to include in your .gitignore file
includes `__pycache__` (cached files that can conflict when run on different
OSs) and `*.pyc` files that are bytecompiled intermediates that can also
conflict on different systems.


Assignment - install postman (https://www.getpostman.com/) - consider using
python to act as the client?  Some folks got confused of what postman was doing
and why it couldn’t be done with python...

https://docs.google.com/presentation/d/1sCWA78KixOqvwXuSoF2QAtZ8LAMRAxv0pU8B-9kVDd8/edit#slide=id.p

## Feedback from Pablo mid-semester
Due to the group project approach to solving assignments, I feel like I have
missed out on some important topics that either Julia or Emelina have done for
the group. Specifically, I happened to not be in charge of Travis or creating
the .yml file and the environment. They did a good job with that, but I have
little to no understanding of how they did it, so I wouldn’t be able to do it
myself and that’s a little frustrating.  I would guess the same happened to
them regarding Sphinx, as I was the one who worked on it.

## Screen / Tmux
Some instructions regarding screen if you haven't already looked it up: To
install screen on your VM run `sudo apt-get install screen`. To create a new
screen run `screen -S <screen_name>`. Inside this new screen you can run your
server. Then go ahead and detach your server screen by pressing ctrl-a and then
d right after. You can then log out of your VM without killing your server. To
re-attach your screen, log back into your VM and then run `screen -r
<screen_name`.

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

## Pymodm
I had a few questions referring to why we were using the pymodm example during
class rather than pymongo. I looked up pymodm and it seems that pymodm is some
sort of ORM, but I am not quite sure what that means exactly. I am just curious
what use pymodm is and how it helps us interact with the mongodb.  An advantage
of using pymodm is that it forces you to create "models" that define your
database schema upfront. There's validation that is then done to ensure your
code isn't inserting random data structures into the database. ORMs are
packages that map (in this case, Python) objects ("models") to database
entities. The advantages being you can deal with native representations of data
and then use the ORM to get/put those entries into a database. In this case,
creating a model object includes/enforces schema validation, which will lead to
less bugs. 


## VM Docker Install
Avoid install Docker directly on Win 10; look into using linux subsystem or VM.

I know some folks have been running into some Docker installation issues on
their VM. I was able to get a working setup by following the below steps (let
me know if they don't work for you):
1. Install Docker https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-convenience-script
2. Setup Docker without sudo: sudo usermod -aG docker vcm
3. Install docker-compose: https://docs.docker.com/compose/install/
4. clone repo and run docker-compose up

## CORS
Also, as many of you start to make RESTful API calls from your web frontend to
your web service, you may run into CORS issues when making the request. CORS is
a set of rules that modern browsers follow to restrict whether or not a web
application is allowed to make calls to a particular server. At a high level,
most API servers are configured to tell browsers that anyone can make API calls
to them. To configure this, you will need to set up Flask-Cors in your Flask
web application. As you can see in the example, this entails adding just two
lines into your Flask application :).

## REACT Stuff
Also I am planning on running a frontend introduction session with ReactJS
tomorrow immediately after class. React is a industry standard framework (built
at Facebook) to build web and native applications. Please let me know if you're
planning to stick around after class for this session. I expect it to take
1.5ish hours. Like I mentioned last class, if you can't make it but are
interested, please let me know.  If you're coming PLEASE DO THE FOLLOWING
BEFORE THE SESSION IF POSSIBLE:
1. Install Node.js (which comes with NPM): https://nodejs.org/en/
2. Install create-react-app scaffolding tool by running: "npm install -g create-react-app"
3. Set up a sample project for the session. Go ahead and run: "create-react-app react-learning" which will go ahead and create a scaffold react web application in a new folder called "react-learning" in your current working directory.
4. Go ahead and install create-react-native-app by running: "npm install -g create-react-native-app"
5. Go ahead and create a sample native project by running "create-react-native-app react-native-learning" 
6. If you'd like to preview your app on your phone, please install the Expo client on your mobile phone: https://expo.io/

Here is the introduction to React video recorded from the session I did last
Thursday: https://www.youtube.com/watch?time_continue=362&v=T3K4Wjz_jAQ. This
geared to be a ground up explanation of React, and by the end of it you'll be
making a RESTful API request and displaying the result in a browser (and you'll
build a nifty counter too). The skills learned here translate directly towards
React Native, which can be used to build iOS and Android applications.

Also if you're making a multi-view (or page) application, check out react
router: https://github.com/ReactTraining/react-router

You may also consider making several "tabs" which may be a little easier:
http://www.material-ui.com/#/components/tabs

With the tabs, you'd have a variable in state that holds onto which tab is
current visible or "selected" and you can change this programatically (for
example when the upload completes, you can switch the user to the results tab
by calling setState)

Before deploying any frontend React code, you'll want to remove
registerServiceWorker() from index.js, otherwise Chrome will throw security
errors that you haven't deployed your application using SSL (https). All that
command does is do some caching and other things to make your page load faster,
which isn't a huge deal right now.

## SSH Raspberry Pi
1. The IP address on the pi changes periodically. So this means that you will have to check the ip address before you can ssh into it
2. I currently have the devices registered under my name. If you want, I can unregister the pi from my account and you can reregister it on your account, where you might be able to see a stable ip address after SSHing into the pi a few times.
3. if you choose to register it on your account, send me your MAC address - WIFI and ETH (label which one is which) - which you can find on the back of your pi. I will send you an email when I unregister the pi from my account so you can register it.
4. When you re-register the device, you can register it with WIFI and ETH to be able to use the pi either via wifi or ethernet.
5. To reregister the device, go to https://dukereg.duke.edu/

## RFCs
Don't worry too much about the Alerting section -- do be sure to talk about how you will handle errors in the Architecture section, though
For security considerations -- don't worry too much about the prompts given (you likely will not have service secrets) but please do try to be creative and throw something you might think would be a security worry in that section :). 
You may see mention of "protobufs" do not worry about those -- please just list out your RESTful API endpoints and their expected inputs/outputs in the endpoints section at minimum. 
Again, I wanted to remind folks that this is the first pass of the RFC and that it's a "living document" so will be expected to improve once you get feedback, which I would like to get to you ASAP. It should also be retroactivly updated as you work on your project if your design or architecture changes.

## Deep Learning
I also wanted to follow up on the introduction to deep learning lecture from Thursday. Attached here are the slides from Ouwen's lecture. He has updated the Docker container with a new notebook called "MINST Notes" that walks through a great MINST training and classification example for those interested. As mentioned in class, we want to get you exposed to deep learning but the focus of the final project will be on the good software design practices you have been learning all semester in this class (as opposed to building the most accurate deep learning models), so we will be walking folks through much of the deep learning components. I highly encourage you to look through the high quality materials Ouwen has put together, as getting exposure to deep learning is more and more important as industry shifts towards machine learning. If you would like to reach out to Ouwen, you can contact him at ouwen.huang@duke.edu. 
Better way to utilize the R Pi earlier in the semester?

## Feedback from Joseph Cobb
Overall appraisal of the course: This class is awesome! I really valued all of the technical skills that were covered. The throwing us in the deep-end approach is fun and a great way to learn (when grades aren’t stressing people out). I loved this class.
 
*Biggest negative:* The lack of organization was a bang-your-head-on-the-wall experience at times. I know this was only the second offering of the course and the largest role Suyash has had to date so I understand why, but the biggest room for improvement is organization! Even a better way to organize resources when students want to find them would be a huge help.
 
*Biggest positive:* The instructors! Both of you are very enthusiastic and engaging. After my internship over the summer (w/ Capital One), this class did feel like a work-place environment and that was cool.
 
*Honesty-time:* It just came to mind that some class times could have been used better. For example, I didn’t love the deep dive into machine learning. That felt like too much too fast with not enough follow up. I loved the exposure and idea, but quality of exposure could be increased and quantity decreased in some ways.
 
*An idea:* Because there is such a myriad of topics available to teach, a comprehensive list at the beginning of the semester and polling the class interest may allow the class to be unique each semester and maximize the expertise you both have to offer.
 
I think we should start final projects earlier! I also wouldn’t mind rotating groups (as long as the assignments were short and for the purpose of coding best practices).

## Feedback from Daniel Wu
I  just wanted to let y'all know how much for I had in BME590 this semester. I thought that the class was extremely well instructed and helpful in me developing good software techniques and practices. I look forward to one day working with you guys again. MHappy Holidays!
