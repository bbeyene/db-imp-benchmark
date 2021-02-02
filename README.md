# db-imp-benchmark

MySQL implementation and benchmarking

## Introduction

Hello from Bruh and Michael. We are computer science students at Portland State University. This repository contains our CS 4/585 Database Implementation Project.

For the project, we will implement a relational database system. The system will then be put through a grinder. Testing how the system performs with datasets of various sizes. And testing how the system performs when we tweak its settings.

## Data Generation

## System

The system we have chosen is MySQL. MySQL has been around for 25+ years and has been crowned as the world's most popular DBMS (source)

So it is imperative that two CS students near graduation should gain intimate knowledge of such ubiquitious system.

## Demonstration

## Lessons Learned

### Mike's String Struggle

In developing the data generation script, we had some issues creating the strings (by we I mean I -- Michael).

Earlier versions of the script used the string format of the early Wisconsin Benchmark. If I had read just a few more pages of the document, I would have realized the string format was updated in a later version of the Benchmark.

I ended up wracking my brain trying to figure out how to implement the $ + 25 x's + $ + 24 x's + $ algorithm. I spent too many hours staring at nested while loops. Losing track of several variables and perhaps 2% of my sanity (I'm being dramatic).

Luckily I met with Bruh the next day. He pointed up the updated string format - $$$$$$$ + 45 x's. In a fraction of the time troubleshooting my previous code, I sucessfully implemented the updated string aglorithm for stringu1 and stringu2. string4 was trivial.

Long story short: read the whole document before you program!
