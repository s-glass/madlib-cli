# Lab - Class 03
## Project: madlib-cli

Author: Sarah Glass for Python 401

Collaborated with Dan Quinn, Logan Reece, and Anthony Sinitsa on the code.

## Overview

Build a command line tool that will perform the following:

* Print a welcome message to the user, explaining the Madlib process and command line interactions.
* Read a template Madlib file (Example), and parse that file into usable parts.
* Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
* With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
* After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
* Write the completed text (Example)to a new file on your file system (in the repo).

## Links and Resources

* Lots of TA and peer help.
* Google searches (no links to direct code) and references to previous Labs

## Setup
No .env requirements; gitignore invludes venv.

## How to initialize/run your application

* python3 madlib.py
* python3 test_madlib.py

## How to use your library
The only library brought in was Regex

## Tests
All acceptance testing run through test_series.py file and pytest following TDD.