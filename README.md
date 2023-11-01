# Fall 2023 CPSC 335.02/CPSC 335.09 Project 1: Implementing Algorithm

## Group Members:

- Student 1
  Name: Justin Sohn
  Student Email: sohnjustin@csu.fullerton.edu

- Student 2:
  Name: Hao Doan Anh Vo  
  Student Email: vodoananhhao@csu.fullerton.edu

- Student 3:
  Name: Anthony Seng
  Student Email: aseng6825@csu.fullerton.edu

## How to run the Program

This program will be ran in Python3 and will need to do the following to get the program to run.

1.  Mac

    - brew install python

2.  Linux

    - sudo apt-get install python3

3.  Windows

    - You must install python through the offical website: https://www.python.org/downloads/windows/

After installing python onto your machine, in order to run the program, find where the directory of the program is and perform the following command.

- python3 project1_starter.py

# Instructions

## Abstract

Develop a pseudocode for an algorithm; analyze your pseudocode mathematically; implement the algorithm in Python or C++; test your implementation; and describe your results.

### The Problem

Matching Group Schedules The group schedule matching takes two or more arrays as input. The arrays represent slots that are already booked and login/logout time of group members. It outputs an array containing intervals of time when all members are available for a meeting for a minimum duration expected.

## The group schedule matching takes following inputs:

1. Busy_Schedule: A list of list that represent the persons existing schedule (they can’t plan any
   other engagement during these hours)
2. Working_period: Daily working periods of group members. (login,logout)
3. Duration of the meeting

It outputs a list of list containing intervals of time when all members are available for a meeting for the minimum duration of the meeting required.

## Direction

Assume there are two persons in your class project group. You want to schedule a meeting with another group member. The members decide to provide you with (a) a schedule of their daily activities, containing times of planned engagements. They are not available during these periods. (b) the earliest and latest times at which they are available for meetings daily. Your schedule and availability are provided too.

Write an algorithm that takes in your schedule, your daily availability (earliest time, latest time) and that of your group member (or members), and the duration of the meeting you want to schedule. Time is given and should be returned in military format. For example: 9:30, 22:21. The given times(output) should be sorted in ascending order.Inputs are also in sorted order.

An algorithm for solving this problem involves combing the two sub-arrays into an array containing of a set unavailability, with consideration of the daily active periods.

# Sample input

- person1_busy_Schedule =[ [’12:00’, ’13:00’], [’16:00’, ’18:00’]]
- person1_work_hours = [‘9:00’, ’19:00’]
- person2_busy_Schedule = [[‘9:00’, ’10:30’], [’12:20’, ’14:30’], [’14:30’, ’15:00’], [’16:00’, ’17:00’]]
- person2_work_hours = [‘9:00’, ’18: 30’]
- duration_of_meeting =30

# Sample output

- [[’10:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]

# Implementation

## Have following files

1. Project1_starter.py or project1_starter.cpp that defines functions for the algorithm
   described above. You will need to develop and write the functions. Describe how to run your
   program in the ReadMe file
2. Input.txt containing the sample input files. Use these sample files to run your program to see
   whether your algorithm implementations are working correctly. Have a new line character
   separating the sample test cases (10)
3. Output.txt – load the sample test case result to output.txt

## To Do

1. Create a Readme file and include your name(s) and email address(es). The Readme file
   should also contain instructions on how to run your program.
2. Study the sample input and output above. Write your own complete and clear code for an
   algorithm to solve this problem.
3. Analyze your code for the algorithm mathematically and prove its efficiency class.
4. Implement your algorithm using either Python or C++.
5. Run your code using different data inputs

## Finally, produce a brief written project report in PDF format. Your report should include the following:

1. Your names, CSUF email address(es), and an indication that the submission is for project 1.
2. A screenshot showing the output of your code for a minimum of 10 test cases defined by
   yourself.
3. Link to your github repo. Keep it private until due date. Make it public after due date(No
   code commits allowed post due date, any code change after due date will not be considered
   for grading)
4. A brief proof argument for the time complexity of your algorithm, including step-counts

## Mathematical Analysis (Our Analysis)

Just looking at schedule algorithm, our step counts is nlogn + 38n + 16. To prove this efficiency class, we are 
using proving efficiency class by using limits. T(n) is nlogn + 38n + 16 and F(n) is nlogn. lim (nlogn + 38n + 16)/nlogn
turns into 1 + lim 38/logn + lim 16/nlogn. This means that L = 1 since both lim 38/logn and lim 16/nlogn are 0.
Since L=1 and L is a non-negative constant therefore nlogn + 38n + 16 ∈ O(nlogn). We think that we can do better by creating 
our own sort function instead of relying on python built in sort function which is a mergesort algorithm which has a 
efficiency class of O(nlogn). Another way to do it better is to not use the replace() function and have the input have no brackets so it
makes it easier to convert it into datetime object. No, the complexity class won't change regardless of the increase in n. 
![image](https://github.com/NotSohn/CPSC-335-Project-1/assets/98761137/c0c6384c-0efa-4e2f-8127-50cf6f01a2e6)


## Grading Rubric

The suggested grading rubric is below.

1. Algorithm design and implementation = 50 points, divided as follows:
   - Clear and complete code = 20 points
   - Complete and clear README.md file = 3 points
   - Successful compilation = 15 points
   - Produces accurate result = 12 points
2. Analysis = 50 points, divided as follows
   - Mathematical analysis and proof, including step count =22
   - Report document presentation = 20 points
   - Screenshot = 5 points
   - Comments on possible improvements = 3

## Ensure your submissions are your own works. Your submissions will be checked for similarities using a software.

# Submitting your code

Submit your project as a zip folder with following format <Team_member_name1_member_2_member_3>.zip to the Project 1 link on Canvas. It allows for multiple submissions. Include following files in the zip folder:

    1. Readme
    2. Input.txt
    3. Project1_starter.py or project1_starter.cpp
    4. Output.txt

# Deadline

The project deadline is October 2,2023 11:59 pm on Canvas. Penalty for late submission is as stated in the syllabus. Projects submitted more than 48 hours after the deadline will not be accepted.
