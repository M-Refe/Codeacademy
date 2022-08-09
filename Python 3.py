#Python 3 is free on Codeacademy until 8/9/2022, this is my notes of Python 3 until the free trial is over
#started off with basic simple "Hello World" in the first lesson of the syllabus

#Now  Boolean Expressions
#conditional statement
#difference between  "If it is raining, then bring an umbrella", 
#in python we type it as "If is_raining:  print("bring an umbrella")"

#relational Operations II
#boolean operators (known as logical operators), are conditional statements that require more than one boolean expression to cover.  These operators combine somaller boolean expressions into larger boolean expressions
# 3 boolean operators: and, or, not
# using and, requires both expressions to be True
# using or, requires only 1 component to be True for the statement to be True
# using not, when applied to any boolean expression, it reverses the boolean value.  If there is a True statement, and a not operator is applied, end result of a False statement

    #not statement example in python course
credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >=120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")


#else statements
#else statements allow us to elegantly describe what we want our code to do when certain conditions are not met
#else statements always appear in conjunction with if statements

#elif statements: else if
#example, this is always the example lol
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

#review
"""
Boolean expressions are statements that can be either True or False
A boolean variable is a variable that is set to either True or False.
We can create boolean expressions using relational operators:
==: Equals
!=: Not equals
>: Greater than
>=: Greater than or equal to
<: Less than
<=: Less than or equal to
if statements can be used to create control flow in your code.
else statements can be used to execute code when the conditions of an if statement are not met.
elif statements can be used to build additional checks into your if statements
"""

#example code/ optional code
# #Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.
#Write a space.py program that helps Codey keep track of their target weight by:

#Checks which number planet is equal to.
#t should then compute their weight on the destination planet.
#Here is the table of conversions:
# 
#  #	Planet	Relative Gravity
#1	Venus	0.91
#2	Mars	0.38
#3	Jupiter	2.34
#4	Saturn	1.06
#5	Uranus	0.92
#6	Neptune	1.19

#To compute their weight on the planet they are fighting on, multiply their earth weight and the relative gravity of that planet:

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19
 
print("Your weight:", weight)

#MAGIC 8 BALL PRACTICE

#We’ll be using the following 9 possible answers for our Magic 8-Ball:

#Yes - definitely.
#It is decidedly so.
#Without a doubt.
#Reply hazy, try again.
#Ask again later.
#Better not tell you now.
#My sources say no.
#Outlook not so good.
#Very doubtful.

#The output of the program will have the following format:

#[Name] asks: [Question]
#Magic 8-Ball’s answer: [Answer]

#using .randint() function from random module to generate a random number from a range
"""
if using .randint(), must have "random import" function at the top of the code page



5. Next, we will create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
random.randint(1, 9)

which will generate a random number between 1 (inclusive) and 9 (inclusive).

Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.

Once you are sure this is working as we expected, feel free to comment out this print() statement.


6. Now that we have declared all the variables needed, it is time to implement the core logic of our program!

For this section, we will be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”

12.

If you are up for some more challenges, try implementing the following features to your program.

So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.

13. What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good
As you can see, the formatting of the output can use some improvement when there is no name provided.

We can address this by printing out just the question, such that it looks like the following:

Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good
You can implement this by creating an if/else statement such that:

If the name is an empty string, it will only print the question.
Else, the player name and question are both printed.


14. What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

To ensure that the fabric of reality is safe, we can create an if/else statement where:

If the question is an empty string, print out a message to the user.
Else, print the name and question, with the Magic 8-Ball  answer.




"""

#Final code
import random
name = ""
question = ""
answer = ""

random_number = random.randint(1, 12)

print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "100% f'sho"
elif random_number == 11:
  answer = "Only a little"
elif random_number == 12:
  answer = "*Kermit appears*"  
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("Magic 8-Ball's answer: You didn't ask a question")
else:
  print("Magic 8-Ball's answer: " + answer)



#Sal's Shipping
"""
In this project, you will build a program that will take the weight of a package and determine the cheapest way to ship that package using Sals Shippers.

Sals Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you are not charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00


Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

1.
First things first, define a weight variable and set it equal to any number.


Stuck? Get a hint
2.
Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

Write a comment that says “Ground Shipping”.

Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.


Hint
Your if statement should take a form similar to:

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight [SOME INEQUALITY]:
  # more calculation
elif weight [SOME INEQUALITY]:
  # more calculation
else:
  # last calculation
3.
A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

8.4\ lb \times \$4.00 + \$20.00 = \$53.608.4 lb * $4.00+$20.00=$53.60
Test that your ground shipping function gets the same value.


Stuck? Get a hint
Ground Shipping Premium:
4.
We will also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.


Stuck? Get a hint
5.
Print it out for the user just in case they forgot!


Stuck? Get a hint
Drone Shipping:
6.
Write a comment for this section of the code, “Drone Shipping”.

Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.


Stuck? Get a hint
7.
A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

1.5\ lb \times \$4.50 + \$0.00 = \$6.751.5 lb * $4.50+$0.00=$6.75
Test that your drone shipping function gets the same value.

Solution:
8.
Great job! Now, test everything one more time!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

(See hint for answers)

"""

weight = 41.5

#Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print("Ground Shipping $", cost_ground)
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
  print("Ground Shipping $", cost_ground)
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
  print("Ground Shipping $", cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + 20
  print("Ground Shipping $", cost_ground)

#Premium ground shipping

premium = 125.00

print("Ground Shipping Premium $", premium)


#Drone Shipping

if weight <= 2:
  cost_ground = weight * 4.5 
  print("Drone Shipping $", cost_ground)
elif weight > 2 and weight <= 6:
  cost_ground = weight * 9.0 
  print("Drone Shipping $", cost_ground)
elif weight > 6 and weight <= 10:
  cost_ground = weight * 12.0 
  print("Drone Shipping $", cost_ground)
elif weight > 10:
  cost_ground = weight * 14.25 
  print("Drone Shipping $", cost_ground)





#Errors in Python
"""

Python refers to mistakes within the program as errors (instead of bugs), and will point to a location where an error occurred with a ^ character.

SyntaxError: Error caused by not following the proper structure (syntax) of the language.

This means there is something wrong with the way your program is written — punctuation that does not belong, 
a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

NameError: Errors reported when the interpreter detects a variable that is unknown.

This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined.


TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

This can occur in Python when one attempts to use an operator on something of the incorrect type.


There is also another type of error that does not have error messages that we will cover down the line:

Logic errors: Errors found by the programmer when the program is not doing what it is intending to do.

Remember, Google and Stack Overflow are a programmers BFFs (best friends forever) in situations where an error is giving you a lot of trouble. For some more motivation, check out this blog post.
"""


#Lists
"""
A list begins and ends with square brackets ([ and ]).
Each item (i.e., 67 or 70) is separated by a comma (,)
It is considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.

Lists can contain any data type in Python! For example, this list contains a string, integer, boolean, and float.

Append:
.append(),
adds an element to the end of the list

.remove(),
removes the element in the list


Plus(+):
When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
example:
items_sold_new = items_sold + ["biscuit", "tart"]

output
['cake', 'cookie', 'bread', 'biscuit', 'tart']

variable: items_sold is not changed when using plus because created a new variable for the list

We can only use + with other lists. If we type in this code:
my_list = [1, 2, 3]
my_list + 4

comes with TypeError

Python lists are zero-indexed
This means that the first element in a list has index 0, rather than 1

When accessing elements of a list, you must use an int as the index. 
    If you use a float, you will get an error. 
This can be especially tricky when using division. 
    For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.
    To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. 
    For example, int(5.9) and int(5.0) will both become 5. 
    Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

Accessing List Elements: Negative Index

can use the index -1 to select the last item of a list,
can use -#'s going backwards to access different items off the list
["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
typically it's 0, 1, 2, 3, 4, 5
but in negative index is
-6, -5, -4, -3, -2, -1

2-D lists
    Lists can contain other lists  
    For example
        heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

They are good for representing grids such as games like tic-tac-toe
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]

Accessing 2-D lists

heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]


#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1]

Element	        Index
"Noelle"	heights[0][0]
61	        heights[0][1]
"Ali"	    heights[1][0]
70	        heights[1][1]
"Sam"	    heights[2][0]
67	        heights[2][1]

how to access lists within list using the index

example
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

sams_score = class_name_test[2][1]
ellies_score = class_name_test[-1][-1]


print(ellies_score)
print(sams_score)
print(class_name_test)

Example:
to access multiple parts of the list
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]

change Madison's grade from 7 to 8 using positive indices
incoming_class[2][2] = 8
change Kenny's name to Ken using negative indices
incoming_class[-3][-3] = "Ken"

print(incoming_class)


"""

#Final Example of using 2-D lists and appending/removing
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")

print(preferred_size)


customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

customer_data[2][2] = False

customer_data[1].remove(False)

print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)


#project gradebook

"""

1.
Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"

Stuck? Get a hint
2.
Create a list called grades and fill it with your scores:

98
97
85
88

Stuck? Get a hint
3.
Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

Name	Test Score
"physics"	98
"calculus"	97
"poetry"	85
"history"	88

Assign the value into a variable called gradebook.


Stuck? Get a hint
4.
Print gradebook.

Does it look how you expected it would?


Stuck? Get a hint
Add More Subjects:
5.
Your grade for your computer science class just came in! You got a perfect score, 100!

Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.


Stuck? Get a hint
6.
Your grade for "visual arts" just came in! You got a 93!

Use append to add ["visual arts", 93] to gradebook.


Stuck? Get a hint
Modify The Gradebook:
7.
Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.

Access the index of the grade for your visual arts class and modify it to be 5 points greater.


Stuck? Get a hint
8.
You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.

Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.


Stuck? Get a hint
9.
Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.


Stuck? Get a hint
One Big Gradebook!
10.
You also have your grades from last semester, stored in last_semester_gradebook.

Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.

Print full_gradebook to see our completed list.


"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)


#Working with Lists
"""

will be learning more methods (ones not covered in basic course)

Python List Methods
.count(): A list method to count the number of occurrences of an element in a list | count the number of times that an element appears in a list
.insert(): A list method to insert an element into a specific index of a list | add and remove items from a list using a specific index
.pop(): A list method to remove an element from a specific index or from the end of a list |add and remove items from a list using a specific index
range():  a built-in Python function to create a sequence of integers | create lists with continuous values
len(): A built-in Python function to get the length of a list | get the length of a list
.sort() / sorted(): A method and a built-in funciton to sort a list |sort a list of items


select portions of a list (called slicing)
"""

#Insert| .insert()
"""

The index method takes in two inputs:
1. the index you want to insert into
2. The element you want to insert at the specified index

this method will handle shifting over elements and can be used with negative indices

"""

#example
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")


#Pop| .pop()
"""
Pop method takes an optional single input:
1. The index for the element you want to remove

The method can be called without a specific index. 
Using .pop() without an index will remove whatever the last element of the list is. 
In our case "Clowns 101" gets removed.

.pop() is unique in that it will return the value that was removed. 
If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. 
In this case, we assigned it to removed_element

Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError
"""

#example
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]


# Your code below: 
data_science_topics.pop()
# removes last element
data_science_topics.pop(3)
#removes algorithms
print(data_science_topics)


#range| range()

"""
The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.
 The range() function is unique in that it creates a range object
In order to use this object as a list, we have to first convert it using another built-in function called list()


"""

#example
# Your code below: 

#modified number_list so the range contains numbers starting at 0 up to but not including 9
number_list = range(9)\
#created range called zero_to_seven with numbers 0 through 7 
zero_to_seven = range(8)

print(list(zero_to_seven))
print(list(number_list))