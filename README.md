# PythonStarter

# Question 1 (5 points):
## Purpose: To practice working with 2D arrays.
## Degree of Diculty: Easy.
Nurse Joy is in charge of training new nurses for a new Pokémon Center in Saskatoon city. As part of the
training, she gave her students a multipe-choice quiz.
She wants to produce a summary of student performance for all questions where fewer than 55% of the
trainee nurses got the questions right.
Write a Python program to accomplish this task.
## Using Numpy Arrays
Although in principle this question could be solved using lists only, our goal is to gain practice working
with arrays. Therefore, you must convert the quiz data to an array and perform all calculations using array
operations.
Before you start anything, make sure you have imported the ♥✉♠♣② module. This module is NOT standard,
so if you are working on your own machine, you may need to install it rst.
## Quiz Data
A starter le is provided for you that contains the quiz data as a list-of-lists. The data is organized such that
each sublist represents the quiz result for a single student. Each sublist is the same length and contains
multiple integers, indicating the student’s score on each question on the quiz. A value of 1 means the
student got the question right and 0 means the student got the question wrong.
The program you hand in should compute the result for the q✉✐③❘❡s✉❧ts list, but two other very small lists
are provided to help you perform simple testing. For example, t❡st✷ represents a quiz with just 4 questions
that was written by 5 students, where all 5 students got the second question right.
Program Behaviour
Your program should:
(a) Create a 2D array from the list of lists for a quiz. Your program should work no matter how many
students there are, or how many questions in the quiz.
(b) For each question, calculate the percentage of students who answered incorrectly
• If fewer than 55% answered correctly, print the information (performance and question number)
for that question to the console
Take advantage of the power of arrays to do this! In particular, you can slice a 2D array across multiple
dimensions; think about how this might be useful.
Sample Run
✞
☎
P♦♦r❧② ❞♦♥❡ q✉❡st✐♦♥s ✿
❖♥❧② ✹✵ ♣❡r❝❡♥t ♦❢ st✉❞❡♥ts s♦❧✈❡❞ q✉❡st✐♦♥ ✶
❖♥❧② ✹✺ ♣❡r❝❡♥t ♦❢ st✉❞❡♥ts s♦❧✈❡❞ q✉❡st✐♦♥ ✷
❖♥❧② ✺✵ ♣❡r❝❡♥t ♦❢ st✉❞❡♥ts s♦❧✈❡❞ q✉❡st✐♦♥ ✼
✝
✆

## What to Hand In
(a) A document entitled ❛✼q✶✳♣② containing your nished program, as described above.
Evaluation
• 1 mark for creating a 2D array
• 3 marks for calculating the student performance for each question
• 1 mark for correct console output
• -1 mark if the student did not include their name, NSID, student number and instructor’s name at the
top of the submitted le.
P


Question 2 (12 points):
Purpose: To practice simple le I/O and numpy array operations
Degree of Diculty: Moderate.
In Canada, the federal government is made up of a number of seats. The seats are divided among the
provinces; for example, Saskatchewan has 14 seats, while Ontario has 121.
For this question, you will write a program using population data from the Canadian census to determine
which provinces are over- or under- reprented in the federal government based on their populations.
Using Numpy Arrays
The main purpose of this question is to practice data manipulation using numpy arrays. Therefore, for full
marks, you must perform all of the signicant calculations by using numpy array operations.
You will need all three of: array arithmetic, array relations, and logical array indexing. The only place where
you will use loops in your program is at the very beginning (for reading from le) and at the very end (for
printing the results).
Task Breakdown
The steps below will help you break down this process into manageable pieces.
Before you start anything, make sure you have imported the ♥✉♠♣② module. This module is NOT standard,
so if you are working on your own machine, you may need to install it rst.
Load the Data into Arrays
Download the le
♣r♦✈✐♥❝✐❛❧❴s❡❛ts✳t①t from the course Moodle. The le looks like this:
✞
☎
◆✉♥❛✈✉t ✱✸✺✵✵✵ ✱✶
❆❧❜❡rt❛ ✱✹✵✻✼✵✵✵ ✱✸✹
❙❛s❦❛t❝❤❡✇❛♥ ✱✶✵✾✽✵✵✵ ✱✶✹
❨✉❦♦♥ ✱✸✺✵✵✵ ✱✶
✳✳✳
✝
✆

Each line consists of a province or territory’s name, its population (rounded to the nearest thousand) and
its number of seats in the government, all separated by commas.
Write code to open this le and read this data into three separate lists (one for the names, one for the
populations, and one for the seats). Then, convert each list to a numpy array using the ✳❛rr❛②✭✮ method
from ♥✉♠♣②. Make sure to maintain the order so that the lists line up by position (i.e. ◆✉♥❛✈✉t is rst in the
array of names, and its matching population and seats are the rst items in their respective arrays).
Test these arrays before you move on! You will use them to perform all the following array calculations.
## Predicted Seats
Using array operations on the loaded data, create an array that contains, for each province, the expected
number of seats that each province WOULD have if its seats were exactly proportional to its population.
Round these values to the nearest integer (you can use numpy’s ✳❛r♦✉♥❞✭✮ method).
Hint: As part of this calculation, you’ll probably need Canada’s total population, and the total number of
seats. Think about how you can get these using the data you already have using numpy’s ✳s✉♠✭✮ method.


