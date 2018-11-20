# Head Impact Exposure (HIE) Sensor Multi-Unit Downloading, Logging and Storage Management Tool

**Client:** Jason Luck, PhD (Injury Biomechanics Laboratory)  
**Contact information:** jfl1@duke.edu and 919-660-5152 (ofc)

**Final Project DUE:** Thursday, Dec 13, 2018 05:00PM EST                                                                                   

## Background
Mild traumatic brain injury (mTBI) or "concussive" injuries are a major
societal issue and are associated with activities such as sports, motor vehicle
crashes, and falls. Sports-related concussions in children and adolescents
(5-18 years) account for between 30-60% of all pediatric concussions. There
currently exists no available technology to provide accurate measurement of
head impacts in concussive or sub-concussive environments. Furthermore,
challenges exist in objectively diagnosing mTBI and quantifying the
physiological implications of cumulative sub-concussive insults. Currently, Dr.
Luck is leading a prospective study in the Raleigh-Durham community where youth
athletes are instrumented with the DASHR: a novel, noninvasive sensor that uses
industry-standard earpieces (e.g. hearing aids) in the bony canal to quantify
head impact exposure. In association with head exposure data measured by the
DASHR the research team is also completing both novel and traditional on- and
off-field injury assessments to assist with quantifying the symptomology of
participants from concussive and cumulative sub-concussive insults to the
pediatric brain.

## Client Need
Client requires a hardware and software solution that accepts multiple HIE
sensors simultaneously to accommodate downloading of HIE data from the devices
to a central storage unit.  Currently the client utilizes a Manhattan® MondoHub
multi-unit USB hub that can accommodate 20+ units.  The hub is currently used
to charge multiple devices simultaneously.  For downloading the client
currently connects individual HIE sensors to a computer and manually copies and
pastes the data from the HIE sensor to the computer.  The data is stored in
sequentially numbered binary files (e.g., `L0.bin`, `L1.bin`, `L2.bin`) located
in sequentially numbered folders (e.g., `0`, `100`, `200`, etc.) in a `FAT32`
file system.  The storage media in the HIE sensor is a standard SD card (e.g.,
SanDisk Ultra microSD 8/16 GB) and when connected to a computer shows up as a
removable storage device.  Currently, if one were to connect two or more HIE
sensors to the hub and then connect the hub to a computer multiple removable
storage devices would appear.  If one were to look into each of these “drives”
they would find folders and files that looked exactly the same with no
identification between the PIN and data.  Each HIE device has a MAC address
associated with it and this address is associated with a specific PIN. 

## Functional Specifications
Client requests the following software toolkit (GUI) [Python] that client
utilizes to facilitate all aspects of downloading, logging and storage
management.
* Download data (binary files) from multiple devices simultaneously (using a
  hub that may or may not be the Manhattan® MondoHub discussed earlier)
* Store downloaded data in folders associated with specific HIE device (each
  device will be associated with a unique PIN number)
* Store data by the date HIE data was acquired – two options:
  + User defined via GUI prior to download
  + Using real-time clock data associated with HIE device
* Provide ability for client to download variable number of devices:
  + User can select to download all devices simultaneously
  + User can select to download individual device from multi-port hub
  + User can select to download some number of devices greater than one from
    multi-port hub
* Software will provide post-download log report.  Report will include the
  following:
  + Number of files downloaded, folders created, PIN numbers associated with
    the downloaded data
  + Stand-alone log reporting.  Client may use software to check what data has
    been downloaded for a given PIN, range of PINs, date, and range of dates
    (dates corresponding to when data was collected on the field, not
    downloaded).
* Software provides flexibility to interface with a database (i.e. SQL) and
  NTFS file system.  All data is associated with a unique PIN and these data
  include the HIE sensor data that is the focus of the current document but
  also includes additional assessment and background data.  

## Deliverables
* A detailed `README` describing the final performance and state of your
  project.
* Recorded video demo of your image processor in action.
* All project code (in the form of a tagged GitHub repository named
  `bme590final`)
* Link to deployed web service 

## Grading
**You should approach this final project as an opportunity to show a potential
future employer an example of your software development skills.**

It is expected that your team will follow proper professional software
development and design conventions taught in this class, including:
* Git Repository
  + Issues/Milestones
  + Commits are discrete, logical changesets
  + Feature-branch workflow
* Software best practices
  + Modularity of software code
  + Handling and raising exceptions
  + Language convention and style (PEP8)
  + Sphinx documentation for all modules/functions
* Testing and CI
  + Unit test coverage of all functions (except Flask handler)
  + Travis CI passing build
* Cloud-based Web Service
  + RESTful API Design 
  + Validation Logic 
  + Returning proper error codes
  + Robust deployment on virtual machine 
* Proper use of a database 
* User interface functionality
* Demo of the final working project
* Robust README
