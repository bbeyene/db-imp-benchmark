# db-imp-benchmark

MySQL implementation and benchmarking

## Introduction

Hello from Bruh and Michael. We are computer science students at Portland State University. This repository contains our CS 4/587 Database Implementation Project.

For the project, we will implement a schema and benchmark a relational database system. The system will then be put through a grinder. Testing how the system performs with datasets of various sizes. And testing how the system performs when we tweak its settings.

## System

The system we have chosen is MySQL.

MySQL has been around for 25+ years and has been crowned as the world's most popular DBMS. [source](https://community.idera.com/database-tools/blog/b/community_blog/posts/why-is-mysql-so-popular#:~:text=MySQL%20has%20emerged%20as%20the,such%20as%20MongoDB%20and%20PostgreSQL.)

So it would be an utmost priority for two CS students, near graduation, to gain intimate knowledge and experience with such ubiquitious system.

To host the database, we went the cloud route. Additionally, using a virtual machine would grant us that sweet sweet extra credit. As a result, our database lives in Google Cloud Platform.

![GCP MySQL instance](./screenshots/mysql1.PNG)
## Data Generation

How our script creates the tuples ...  

![calling datagen.py](./screenshots/datagen1.PNG)  

The ONEKTUP ...  

![datagen.py output 1](./screenshots/datagen2.PNG)  

The TENKTUP1 and TENKTUP2 ...  
![datagen.py output 2](./screenshots/datagen3.PNG)  
![datagen.py output 3](./screenshots/datagen4.PNG)  
## Demonstration

Calling the create/insert script ...  

![mysqlinsert.py run](./screenshots/insert1.PNG)  

Changing params for each table ...  
![mysqlinsert.py code](./screenshots/insert2.PNG)  


Our tables loaded-in ...  
![GCP MySQL database and tables](./screenshots/mysql2.PNG)  

4 out of 16 of ONEKTUP's columns...  
![GCP MySQL ONEKTUP 1](./screenshots/mysql3.PNG)  
![GCP MySQL ONEKTUP 2](./screenshots/mysql4.PNG)  


## Lessons Learned

### Mike's String Struggle

In developing the data generation script, we had some issues creating the strings (by we I mean I -- Michael).

Earlier versions of the script used the string format of the early Wisconsin Benchmark. If I had read just a few more pages of the document, I would have realized the string format was updated in a later version of the Benchmark.

I ended up wracking my brain trying to figure out how to implement the algorithm to generate the string pattern. I spent too many hours staring at nested while loops. Losing track of several variables and perhaps 2% of my sanity (I'm being dramatic).

Luckily I met with Bruh the next day. He pointed out the updated string format - (7 letters [A-Z] followed by 45 x's) and generation pattern.

In a fraction of the time troubleshooting my previous code, I sucessfully implemented the updated string aglorithm for stringu1 and stringu2. string4 was trivial.

Long story short: read the whole document before you program!
