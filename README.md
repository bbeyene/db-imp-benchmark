# db-imp-benchmark

MySQL implementation and benchmarking

## Introduction

Hello from Bruh and Michael. We are computer science students at Portland State University. This repository contains our CS 4/585 Database Implementation Project.

For the project, we will implement a relational database system. The system will then be put through a grinder. Testing how the system performs with datasets of various sizes. And testing how the system performs when we tweak its settings.

## System

The system we have chosen is MySQL.

MySQL has been around for 25+ years and has been crowned as the world's most popular DBMS. [source](https://community.idera.com/database-tools/blog/b/community_blog/posts/why-is-mysql-so-popular#:~:text=MySQL%20has%20emerged%20as%20the,such%20as%20MongoDB%20and%20PostgreSQL.)

So it would be an utmost priority for two CS students, near graduation, to gain intimate knowledge and experience with such ubiquitious system.

To host the database, we went the cloud route. Additionally, using a virtual machine would grant us that sweet sweet extra credit. As a result, our database lives in Google Cloud Console.

## Data Generation

say something here

## Demonstration

say something here

## Lessons Learned

### Mike's String Struggle

In developing the data generation script, we had some issues creating the strings (by we I mean I -- Michael).

Earlier versions of the script used the string format of the early Wisconsin Benchmark. If I had read just a few more pages of the document, I would have realized the string format was updated in a later version of the Benchmark.

I ended up wracking my brain trying to figure out how to implement the algorithm to generate the string pattern. I spent too many hours staring at nested while loops. Losing track of several variables and perhaps 2% of my sanity (I'm being dramatic).

Luckily I met with Bruh the next day. He pointed out the updated string format - (7 letters [A-Z] followed by 45 x's) and generation pattern.

In a fraction of the time troubleshooting my previous code, I sucessfully implemented the updated string aglorithm for stringu1 and stringu2. string4 was trivial.

Long story short: read the whole document before you program!
