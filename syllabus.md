# Medical Software Design Syllabus

## Instructors
Dr. Mark Palmeri, M.D., Ph.D.  
<mark.palmeri@duke.edu>  
Office Hours: https://calendly.com/mark-palmeri

Suyash Kumar, Uber Software Engineer, Web Guru, Deep Learning Master  
<suyash.kumar@duke.edu>  
Office Hours: Friday after class (266 Hudson Hall Annex)

## Teaching Assistants
Arjun Desai  
<arjun.desai@duke.edu>  
Office Hours: Monday 11:30-12:30 (Teer Basement)

Nisarg Shah  
<nisarg.shah@duke.edu>  
Office Hours: Wednesday 14:00-15:00 (Teer Basement)

## Lecture
Wed/Fri 11:45--13:00  
216 Hudson Hall

All lecture content will be outlined in [Lectures](Lectures/).

## Course Overview
Software plays a critical role in almost all medical devices, spanning device
control, feedback and algorithmic processing.  This course focuses on software
design skills that are ubiquitous in the medical device industry, including
software version control, unit testing, fault tolerance, continuous integration
testing and documentation.  Experience will be gained in Python and JavaScript
(and potentially other languages).

The course will be structured around a project to build an Internet-connected
medical device that measures and processes a biosignal, sends it to a web
server, and makes those data accessible to a web client / mobile application.
This project will be broken into several smaller projects to develop software
design fundamentals.  All project-related work will be done in groups of 3
students.

## Prerequisites
Basic familiarity with programming concepts (e.g., variables, loops,
conditional statements).

## Course Objectives
* Define software specifications and constraints
* Agile project management
* Device programming fundamentals
  + Review of data types
  + Python (v3.6): numpy, scipy, pandas, scikit
  + Virtual environments & dependency management (`pip`, `requirements.txt`)
  + Data management (variables, references, pointers, ASCII/Unicode/binary data)
  + Regular expressions (regex)
  + Use of a programming IDE
  + Debugging (`pudb`)
* Backend Software Development in the Cloud
  + Databases (MySQL, MongoDB)
  + HTTP & RESTful APIs
  + Leverage scalable compute infrastructure in the cloud via Remote Procedure Calls (RPCs)
  + Call web services from Matlab \& Python
  + Design & Implementation of a biomedical web service (Python Flask)
  + Docker and dependency management intro
  + SSL and Encryption
  + Internet of Things (IoT) and cloud connected biomedical device design
  + Sockets and streaming data over networks
* Software version control (`git`, GitHub)
* Documentation
  + Docstrings
  + Markdown
  + Sphinx
  + [ReadTheDocs](https://readthedocs.org)
* Testing
  + Unit testing
  + Functional / System testing
  + Continuous integration (Travis CI)
* Fault tolerance (raising exceptions)
* Logging
* Resource profiling (`cProfile`)

## Attendance
Lecture attendance and participation is important because you will be working
in small groups most of the semester.  Participation in these in-class
activities will count for 15\% of your class grade.  It is very understandable
that students will have to miss class for job interviews, personal reasons,
illness, etc.  Absences will be considered \emph{excused} if they are
communicated to Dr. Palmeri and Mr. Kumar at least 48 hours in advance (subject
to instructor discretion as an excused absence) or, for illness, through
submission of a [Short Term Illness Form
(STIF)](http://www.pratt.duke.edu/undergrad/policies/3531) **before** class.
Unexcused absences will count against the participation component of your class
grade.

## Textbooks & References
There are no required textbooks for this class.  A variety of online resources
will be referenced throughout the semester.  A few great resources for an overview
of Python: 
* [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
* [Intermediate Python](http://book.pythontips.com/en/latest/index.html)

## Project Details
Project details will be discussed in lecture throughout the semester.

## Grading
The course GitHub repository will host all [Assignments](Assignments/).
Due dates--including those that change--will be announced in lecture and by
Sakai announcements that will be emailed to the
class.  

The following grading scheme is subject to change as the semester progresses:
<table>
<tr>
<td>Participation</td>
<td>15%</td>
</tr>
<tr>
<td>Midterm project deliverables</td>
<td>55%</td>
</tr>
<td>Final project</td>
<td>30%</td>
</tr>
</table>

## Class Schedule
The course schedule is very likely to change depending on progress throughout
the semester.  The updated [schedule](schedule.md) will always be available in
the GitHub course repository.  

## Distributed Version Control Software (git)
Software management is a ubiquitous tool in any engineering project, and this
task becomes increasingly difficult during group development. Version control
software has many benefits and uses in software development, including
preservation of versions during the development process, the ability for
multiple contributors and reviewers on a project, the ability to tag
*Releases* of code, and the ability to branch code into different functional
branches.  We will be using [GitHub](https://github.com) to centrally host our
git repositories.  Specifically, we will be creating student teams in the [Duke
BME Design](https://github.com/Duke-BME-Design) group.  Some guidelines
for using your git repositories:

* *All* software additions, modifications, bug-fixes, etc. need to be done in
  your repository.
* The *Issues* feature of your repository should be used as a "to do" list of
  software-related items, including feature enhancements, and bugs that are
  discovered.
* There are several repository management models that we will review in class,
  including branch-development models that need to be used throughout the
  semester.
* Instructors and teaching assistants will only review code that is committed
  to your repository (no emailed code!).
* All of the commits associated with your repository are logged with your name
  and a timestamp, and these cannot be modified.  Use descriptive commit
  messages so that your group members, instructors, and teaching assistants can
  figure out what you have done!!  You should not need to email group members
  when you have performed a commit; your commit message(s) should speak for
  themselves.
* Code milestones should be properly tagged.
* Write software testing routines early in the development process so that
  anyone in your group or an outsider reviewing your code can be convinced that
  it is working as intended.
* Modular, modular, modular.
* Document!
* Make commits small and logical; do them often!

We will review working with git repositories in lecture, and feedback on your
software repository will be provided on a regular basis.

## Online Slack Channels
We have online help through the [Duke Co-Lab
Slack](https://dukecolab.slack.edu/) team.  We have started two specifics
channels for this class: `#git` and `#python`.  Please add yourselves to these
channels to get help from your instructors, your TAs and the Duke community!

## Duke Community Standard & Academic Honor
Engineering is inherently a collaborative field, and in this class, you are
encouraged to work collaboratively on your projects.  The work that you submit
must be the product of your and your group's effort and understanding.  All
resources developed by another person or company, and used in your project,
must be properly recognized.

All students are expected to adhere to all principles of the [Duke Community
Standard](http://www.integrity.duke.edu/standard.html).  Violations of the Duke
Community Standard will be referred immediately to the Office of Student
Conduct.  Please do not hesitate to talk with your instructors about any
situations involving academic honor, especially if it is ambiguous what should
be done.
