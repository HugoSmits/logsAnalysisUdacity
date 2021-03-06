# My Logs Analysis

## Description

#### The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

#### The following source code will answer the next 3 questions:

- ##### What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
- ##### Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
- ##### On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

## Index
1. [Bio and File info](#bio-and-file-info)
2. [Version](#version)
3. [Setting up for this project](#setting-up-for-this-project)
4. [Requisites](#requisites)
5. [Download the data](#download-the-data)
6. [How to connect and access the database](#how-to-connect-and-access-the-database)
7. [Running Code](#running-code)
8. [Guidelines](#guidelines)
8. [Code solution example](#code-solution-example)
9. [Output solution example](#output-solution-example)
10. [Views created](#views-created)
11. [Execute selects in psql with views](#execute-selects-in-psql-with-views)
12. [Contribuition](#contribuition)
13. [Licensing info](#licensing-info)
14. [WebBio](#webbio)

## Bio and File info

- ##### Author: Hugo Smits
- ##### Date of creation : 12/11/2018
- ##### Last modified : 14/11/2018

## Version

##### Current version of the repository is version 1.1 .

## Setting up for this project
##### To do the exercises in this project, you will need access to a Linux machine you can log into with SSH. One option is to install a Linux-based virtual machine on your own computer.

### Your Linux machine (Local VM option)
##### If you prefer to work on your own computer instead of a commercial service, you can run a Linux virtual machine (VM) on top of your regular operating system.

### You will need to install two pieces of software:

- ##### VirtualBox, which you can get from this [download page](https://www.virtualbox.org/wiki/Downloads).
- ##### Vagrant, which you can get from this [download page](https://www.vagrantup.com/downloads.html).

##### You will also need a Unix-style terminal program. On Mac or Linux systems, you can use the built-in Terminal. On Windows, I recommend Git Bash, which is installed with the Git version control software.

##### Once you have VirtualBox and Vagrant installed, open a terminal and run the following commands:
```
mkdir networking
cd networking
vagrant init ubuntu/trusty64
vagrant up
```
##### This will create a new directory for this project and begin downloading a Linux image into this directory. It may take a long time to download, depending on your Internet connection.

##### When it is complete, you can log into the Linux instance with ```vagrant ssh```. You are now ready to continue with the project.

##### If you log out of the Linux instance or close the terminal, the next time you want to use it you only need to run ```cd networking``` and ```vagrant ssh```.

## Requisites

##### Views must be created in vagrant/psql environment before the selects can run be run!

## Download the data

##### Next, download the data [here](https://github.com/HugoSmits/logsAnalysisUdacity). You can fork the repository and clone it to your local git repository. The file needed is called newsdata.sql the rest are personal answers to the project. Put this file into the vagrant directory, which is shared with your virtual machine.

##### Within the repository you can find the file called Vagrantfile which will help you set up your vagrant environment with the right configurations. BEWARE: config.vm.box_download_insecure is set to TRUE. Doesn't verify ssl certificates. Line can be removed or altered at said file. Setup can't be guaranteed if done so.

##### To load the data, cd into the vagrant directory and follow the command show in "How to connect and access the database. 


## How to connect and access the database
#### connecting for the first time 
```
psql -d news -f newsdata.sql.
```
#### following connections don't need the f flag with the database.
```
psql -d news
```
##### Here's what this command does:
##### psql — the PostgreSQL command line program:

- ##### -d news — connect to the database named news which has been set up for you
- ##### -f newsdata.sql — run the SQL statements in the file newsdata.sql

##### Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Running Code
##### If you are using python 2.x.x use the following line to execute the python code:
```
python logsAnalysis.py
```

##### If you are using python 3.x.x use the following line to execute the python code:
```
python3 logsAnalysis.py
```

## Guidelines

##### The following source code is written according to [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/).
```
autopep8 --in-place -a --max-line-length 79 logsAnalysis.py
```

## Code solution example

##### An example of the code used to generate a correct output can be found in **_logsAnalysis.py_**

## Output solution example

##### An example of the output generated by the source code can be found in **_Output.txt_**

## Execute selects in psql

- ##### Ex1: select articles.title , count(articles.author) as subtotal from articles , log where log.path LIKE concat('%' , articles.slug) group by articles.author , articles.title , articles.slug order by 2 DESC; 
- ##### Ex2: select authors.name , count(author) as subTotal from authors , articles , log where (log.path LIKE concat('%' , articles.slug)) and (articles.author = authors.id) group by 1 order by 2 DESC;
- ##### Ex3: select date_trunc('day', time) as day , ((count(\*) filter (where status != '200 OK') / cast(count(\*) as float)) \*100 ) as errorpercentage from log group by 1 having ((count(\*) filter (where status != '200 OK') / cast(count(\*) as float)) \*100 ) > 1;

## Contribuition

##### To contribuite to this project the person must follow the guidelines mentioned in **Usage** and send a written email to the moderator of the source code hugo.smits1995@gmail.com 

## Licensing info

##### The following project uses the [MIT license](https://opensource.org/licenses/MIT)

## WebBio

- ##### Full Stack Web Developer Nanodegree Udacity Lesson 2 From Ping to HTTP -  "Setting up for this course"
- ##### Full Stack Web Developer Nanodegree Udacity Lesson 3 Project Logs Analysis -  "Prepare the software and data"
- ##### https://www.postgresql.org/docs/9.6/app-psql.html
- ##### http://www.postgresqltutorial.com/postgresql-python/
- ##### https://www.tutorialspoint.com/postgresql
- ##### https://www.hacksparrow.com/python-split-string-method-and-examples.html
- ##### https://stackoverflow.com/questions/22412258/get-the-first-element-of-each-tuple-in-a-list-in-python
- ##### https://www.postgresql.org/message-id/271d057bf6acfee775e7c47fe899cc9e%40biglumber.com
- ##### https://www.w3schools.com/sql/sql_like.asp
- ##### https://popsql.io/learn-sql/postgresql/how-to-group-by-time-in-postgresql/
- ##### https://stackoverflow.com/questions/1400078/is-it-possible-to-specify-condition-in-count/1400115
- ##### https://dba.stackexchange.com/questions/112796/postgres-count-with-different-condition-on-the-same-query
- ##### https://stackoverflow.com/questions/1780242/postgres-math-expression-calculcated-for-each-row-in-table
- ##### http://www.postgresqltutorial.com/postgresql-having/
- ##### https://www.postgresql.org/docs/9.6/functions-formatting.html
- ##### http://www.postgresqltutorial.com/postgresql-round/