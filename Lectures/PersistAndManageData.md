# Persist and Manage Data
* When developing software systems, it's common that we may need to persist data between software executions or encode data to be passed between software programs.
* Consider a collection of users. 
  * How do we find a single User to determine their permission level? 
  * How should this data be stored?
  * What happens when there's concurrent access by different programs?

| name          | department | permission_level |
|---------------|------------|------------------|
| Bob Smith, MD | Neurology  | ADMIN            |
| Tom Smith, MD | Urology    | GUEST            |
|      ...      |    ...     |       ...        |




## Databases
* Centralized persistent storage for applications that have certain consistency guarantees and can be accessed by multiple programs concurrently and efficiently.
* Databases are __software programs__ that expose an interface to other programs for inserting and querying data 
* Different types of databases (NoSQL, SQL, distributed databases, in memory databases)
* MySQL, postgres, redis, mongodb
* Tables
* Universally Unique Identifiers (UUIDs)
  * Unique labels for rows in a database 
  * v4 UUIDs look like this: `17947c2a-c6b7-4ce7-91ac-7f3af231cf89`
  * UUIDs can be generated at any time and be guaranteed to be a universally unique identifier to refer to some piece of data. This is useful when adding new entries to a database as you will not have any collisions where you'll generate two UUIDs that are the same.
* Sample queries to databases
* Sample inserts into databases
* Indicies and lookup tables to make queries more efficient
* [MimicIII database](https://mimic.physionet.org/) of over 40,000 critical care patients (includes billing, lab tests, orders, demographics, notes, and other information) 
