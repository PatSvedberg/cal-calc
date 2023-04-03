# CalCalc - Calorie Calculator. Project 3 by Patric Svedberg

# Introduction
Project milestone 3 for Code Institute Full-stack development program: Python Terminal.
CalCalc runs in the Code Institute mock terminal on Heroku. The main goal is to calculate the calories burned after an activity.

# User Experience - UX
## User Stories:
* ### User Goals:
    * The user should be able to understand the program without prior experience with it
    * The screen should not be unnecessarily cluttered with text.

* ### Creator Goals:
    * I want to create a program that can be used with as few inputs as possible
    * The worksheet should be easy to understand and read.

# Design

## Flowchart - TO BE ADDED
Flowchart picutre
# Features
## Start
### Setting up the profile
When the program starts the user will be asked to enter a username. Then a worksheet will be created named after the username inside the connected Google Sheet. Next the user will be asked to enter their current weight. This will be used to calculate the calories burned later.

## Activity
### Picking and activity
Now the profile is set and the user will be asked to pick and activity. Right now there is only two activities. But more can easily be added. You enter (1) to pick jogging (2) to pick swimming.

### Enter time
After picking the activity, the user will be asked to enter for how long they did that activity.

## The calculation
### The equation
The equation i used to calculate how many calories was burned:<br>
Calories burned = (time * MET * weight) / 200<br><br>
<b>MET</b> (Metabolic Equivalent of Task) is a measure of the intensity of physical activity. It is defined as the ratio of the rate at which a person expends energy during an activity, to the rate at which they expend energy while at rest. The value of different activities varies slightly. For this program I used:

* 7 for Jogging
* 10 for Swimming
