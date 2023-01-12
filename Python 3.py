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
from subprocess import STD_ERROR_HANDLE
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

By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number
For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9)

If we use a third input, we can create a list that “skips” numbers
For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number

"""

#example
# Your code below: 

#modified number_list so the range contains numbers starting at 0 up to but not including 9
number_list = range(9)\
#created range called zero_to_seven with numbers 0 through 7 
zero_to_seven = range(8)

print(list(zero_to_seven))
print(list(number_list))

# example
my_range2 = range(2, 9, 2)
print(list(my_range2))

# outputs
# [2, 4, 6, 8]



#length| len()

"""

Often, we’ll need to find the number of items in a list, usually called its length

When we apply len() to a list, we get the number of elements in that list
example
my_list = [1, 2, 3, 4, 5]
 
print(len(my_list))

outputs
5
"""

#example
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below:
long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

#outputs
#18
#30


#slicing 
"""

often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing

we have a list of letters:

letters = ["a", "b", "c", "d", "e", "f", "g"]


Suppose we want to select from "b" through "f"
letters[start:end]

start is the index of the first element that we want to include in our selection. 
In this case, we want to start at "b", which has index 1

end is the index of one more than the last index that we want to include. 
The last element we want is "f", which has index 5, so end needs to be 6

sliced_list = letters[1:6]
print(sliced_list)
"""

#example

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

#selects first two element of the list
beginning = suitcase[0:2]
#select middle two items
middle = suitcase[2:4]
# Your code below: 
print(beginning)
print(middle)

#output
#['shirt', 'shirt']
#['pants', 'pants']

"""
slicing pt. 2

slicing syntax in python is very flexible

if want to select the first n elements of a list, could use the following code
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
fruits[:n]

The following code would start slicing from index 0 and up to index 3
fruits[:3]

We can do something similar when we want to slice the last n elements in a list
fruits[-n:]


Negative indices can also accomplish taking all but n last elements of a list.
fruits[:-n]

print(fruits[:-1])
Would output:

['apple', 'cherry', 'pineapple', 'orange']

"""

#example
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
#only contain last two elements
last_two_elements = suitcase[-2:]
print(last_two_elements)
#slice last three elements
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


#count | .count()
"""

count is a function that counts the occurrences of an item in a list
example

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i)

counts the number of times "i" appears in the list

.count() returns a value, we can assign it to a variable to use it


can even use .count() to count element appearances in a two-dimensional list

example
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

If we wanted to know how often the sublist [100, 200] appears:

num_pairs = number_collection.count([100, 200])
print(num_pairs)

outputs
2


"""

#example
#determine how many students voted for "Jake" and save it to the variable "jake_votes"
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)


#sort| sort.()
#sort| sorted()

"""
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order
example

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

names.sort()
print(names)
output
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

.sort() also provides us the option to go in reverse
names.sort(reverse=True)
print(names)
output
['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

.sort() method does not return any value and thus does not need to be assigned to a variable


sorted()

sorted() is different from .sort()

it comes BEFORE a list, instead of after as all built-in functions do
it generates a new list rather than modifying the one that already exits

sorted_names = sorted(names)
print(sorted_names)

output
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

names isn't changed, the sort is in a new variable
"""

#practice code
"""

Make Some Pizzas
1.
To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"

Stuck? Get a hint
2.
To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:

2
6
1
3
2
7
2

Stuck? Get a hint
3.
Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.


Stuck? Get a hint
4.
Find the length of the toppings list and store it in a variable called num_pizzas.


Stuck? Get a hint
5.
Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.


Stuck? Get a hint
6.
Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.

Price	Topping
2	"pepperoni"
6	"pineapple"
1	"cheese"
3	"sausage"
2	"olives"
7	"anchovies"
2	"mushrooms"

For this new list make sure the prices come before the topping name like so:

[price, topping_name]
Note: You do not need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.


Stuck? Get a hint
7.
Print pizza_and_prices.

Does it look the way you expect?


Stuck? Get a hint
Sorting and Slicing Pizzas
8.
Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).


Stuck? Get a hint
9.
Store the first element of pizza_and_prices in a variable called cheapest_pizza.


Stuck? Get a hint
10.
A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.


Stuck? Get a hint
11.
It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.


Stuck? Get a hint
12.
Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

[2.5, "peppers"]
Add the new peppers pizza topping to our list pizza_and_prices.

Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!


Stuck? Get a hint
13.
Three mice walk into the store. They do not have much money (they are mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.


Stuck? Get a hint
14.
Great job! The mice are very pleased and will be leaving you a 5-star review.

Print the three_cheapest list.



"""
# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "achovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices =[[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5, "peppers"])

three_cheapest = pizza_and_prices[0:3]
print(pizza_and_prices)
print(three_cheapest)


#tuples

"""

tuple is a data structure in python that allows us to store multiple pieces of data inside of it
tuple is similar to list
tuple is inmutable (cannot be changed)


"""

my_info = ('Marisa', 27, 'Programmer')
# ^ tuple will have this stored forever and cannot be changed

name, age, occupation = my_info
#this will store the info into a separate variable = unpacking a variable
"""
unpacking a tuple ^^^
"""

#one element tuple
one_element_tuple = (4)
print(one_element_tuple)
#this will print out the element 4

#if want to created element tuple, have to type (4,)

#what's a situation a tuple might come in handy?  python provides data structure, store data that have to be grouped together, but they're not similar to each other
#the order matters when creating an associated variable


#project

"""
Prices and Cuts:
1.Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, leTs sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

2.Loop through the prices list and add each price to the variable total_price.


3.After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.


4.Print the value of average_price so the output looks like:

Average Haircut Price: <average_price>


5.That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

6.print new_prices.

Revenue:
7.Carly really wants to make sure that Carlys Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.

8.Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!


9.Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.



10.After your loop, print the value of total_revenue, so the output looks like:

Total Revenue: <total_revenue>
11.Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.

12.Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.


Hint
Syntax you can use for your list comprehension might look like:

new_list = [old_list[i] for i in range(len(old_list)) if different_list[i] < 0]
This makes a new list of every entry in old_list for which the index i satisfies the condition different_list[i] < 0.

13.Print cuts_under_30.


"""
#EXAMPLE CODE
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price = total_price + price

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)
#THIS NEXT PART IS CHALLENGING FOR ME
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i] + total_revenue
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)
"""
combining lists: Zip Function
zip()
allows us to quickly combine associated data sets without needy to rely on multi-dimensional lists

example

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]


names_and_heights = zip(names, heights)
but if to examine the list

print(names_and_heights)
Would output:

<zip object at 0x7f1631e86b48>
the zip object contains the LOCATION of this variable in computer's memory
can convert object into a useable list by using list()

converted_list = list(names_and_heights)
print(converted_list)

Outputs:

[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

2 things to notice:
1. Our data set has been converted from a zip memory object to an actual list (denoted by [ ])
2. Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list)


"""

#example code

"""
Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.

Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.

Print list_of_names_and_dogs_names.

"""
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

#code here
names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)





#LOOPS

"""
 In a loop, we perform a process of iteration (repeating tasks).
Python implements two types of iteration

1. Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.

2. Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).
"""

#for loop

"""
In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length

for <temporary variable> in <collection>:
  <action>

    1. A for keyword indicates the start of a for loop.
    2. A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
    3. An in keyword separates the temporary variable from the collection used for iteration.
    4. A <collection> to loop over. In our examples, we will be using a list.
    5. An <action> to do anything on each iteration of the loop.

example:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
for ingredient in ingredients:
  print(ingredient)

    1. ingredient is the <temporary variable>.
    2. ingredients is our <collection>.
    3. print(ingredient) was the <action> performed on every iteration using the temporary variable of ingredient.


TEMPORARY VARIABLES:
A temporary variable name is arbitrary and does not need to be defined beforehand

these two examples do the same thing as the example above
for i in ingredients:
  print(i)

for item in ingredients:
 print(item)

Programming best practices suggest we make our temporary variables as descriptive as possible. 
Since each iteration (step) of our loop is accessing an ingredient it makes more sense to call our temporary variable ingredient rather than i or item

INDENTATION:
Everything at the same level of indentation after the for loop declaration is included in the loop body and is run on every iteration of the loop

ELEGANT LOOPS:
Python loves to help us write elegant code so it allows us to write simple for loops in one-line
    for ingredient in ingredients: print(ingredient)
One-line for loops are useful for simple programs. 
It is not recommended you write one-line loops for any loop that has to perform multiple complex actions on each iteration
"""

#example
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)


#   FOR LOOPS: USING RANGE
"""
Often we will not be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times

    For example, if we wanted to print out a "Learning Loops!" message six times using a for loop, we would follow this structure:

    for <temporary variable> in <list of length 6>:
        print("Learning Loops!")

    Notice that we need to iterate through a list with a length of six, but we do not necessarily care what is inside of the list.

To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range().

We can then use the range directly in our for loops as the collection to perform a six-step iteration:

for temp in range(6):
  print("Learning Loops!")

Would output:

    Learning Loops!
    Learning Loops!
    Learning Loops!
    Learning Loops!
    Learning Loops!
    Learning Loops!

    Something to note is we are not using temp anywhere inside of the loop body. 
    If we are curious about which loop iteration (step) we are on, we can use temp to track it. 
    Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

  Output:
  Loop is on iteration number 1
    Loop is on iteration number 2
    Loop is on iteration number 3
    Loop is on iteration number 4
    Loop is on iteration number 5
    Loop is on iteration number 6
"""

#example
"""
Use the range() function in a for loop to print() out the provided promise variable five times.
"""

promise = "I will finish the python loops module!"

#my code 
for every in range(5):
  print(promise)


#WHILE LOOPS
"""
  Another type of loop is called a while loop and is a form of indefinite iteration.

A while loop performs a set of instructions as long as a given condition is true

structure
    while <conditional statement>:
        action>

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1


    1. count is initially defined with the value of 0. 
    The conditional statement in the while loop is count <= 3, 
    which is true at the initial iteration of the loop, 
    so the loop body executes.

    2. Inside the loop body, count is printed and then incremented by 1.

    3. When the first iteration of the loop has finished, 
    Python returns to the top of the loop and checks the conditional again. 
    After the first iteration, count would be equal to 1 so the conditional still evaluates to True and so the loop continues.

    4. This continues until the count variable becomes 4. 
    At that point, when the conditional is tested it will no longer be True and the loop will stop.
The output would be:

    0
    1
    2
    3

INDENTATION:
Notice that in our example the code under the loop declaration is indented. 
Similar to a for loop, everything at the same level of indentation after the while loop declaration is run on every iteration of the loop while the condition is true.

ELEGANT LOOPS:
Python allows us to write elegant one-line while loops
    count = 0
    while count <= 3: print(count); count += 1
Here we separate each statement with a ; to denote a separate line of code.
"""

#To quickly comment out the code, use your cursor or mouse to highlight all the code and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.

#example
"""
Let us write a while loop that counts down from 10 to 0(inclusive). 
Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".

1. Create a variable named countdown and set the value to 10.
2. Define a while loop that will run while our countdown variable is greater than or equal to zero.

On each iteration:

    We should print() the value of the countdown variable.
    We should decrease the value of the countdown variable by 1
    Make sure to only print the value of countdown.
Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.

"""
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")


#output should be
"""
    10
    9
    8
    7
    6
    5
    4
    2
    1
    We have liftoff!
"""

#WHILE LOOPS: LISTS
"""
we can use while loops to iterate through a list as well

# Length will be 5 in this case
length = len(ingredients)

# Index starts at zero
index = 0

We still need an additional variable that will be used to compare against our length.
while index < length:

On the first iteration, we will be comparing the equivalent of 0 < 5 which will evaluate to True, and start the execution of our loop body.
# The first iteration will print ingredients[0]
print(ingredients[index])

# Increment index to access the next element in ingredients
# Each iteration gets closer to making the conditional no longer true
index += 1



length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1
"""

"""
We are going to write a while loop to iterate over the provided list python_topics.

First, we will need a variable to represent the length of the list. This will help us know how many times our while loop needs to iterate.

Create a variable length and set its value to be the length of the list of python_topics.

2.Next, we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.

Create a variable called index and initialize the value to be 0.

3.Let us now build our loop. We want our loop to iterate over the list of python_topics and on each iteration print "I am learning about <element from python_topics>". 
For this loop we will need the following components:

    A condition for our while loop
    A statement in the loop body to print from our condition
    A statement in the loop body to increment our index forward.
    The end result should output:

        I am learning about variables
        I am learning about control flow
        I am learning about loops
        I am learning about modules
        I am learning about classes

"""
#example code
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0

while index < length:
  print("I am learning about " + str(python_topics[index]))
  index +=1


#INFINITE LOOPS
"""
A loop that never terminates is called an infinite loop
 If you accidentally stumble into an infinite loop while developing on your own machine, you can end the loop by using control + c to terminate the program.

A program that hits an infinite loop often becomes completely unusable. The best course of action is to avoid writing an infinite loop.
"""

#LOOP CONTROL: BREAK
"""
to prevent a loop to continue running
you can stop iteration from inside the loop by using break loop control statement
When the program hits a break statement it immediately terminates a loop


Example:
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
 
print("End of search!")
"""

#example
"""
1.You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.

Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.

Use the <temporary variable> name of dog_breed in your loop declaration.

2.Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"


3.Add a break statement when your loop has found dog_breed_I_want so that the rest of the list does not need to be checked once we have found our breed
"""

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

#LOOP CONTROL: CONTINUE
"""
What if we only want to skip the current iteration of the loop
Let us take this list of integers as our example:

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
What if we want to print out all of the numbers in a list, but only if they are positive integers. We can use another common loop control statement called continue.

for i in big_number_list:
  if i <= 0:
    continue
  print(i)
This would produce the output:

1
2
4
5
2
We can use another common loop control statement called continue

    1. Similar to when we were using the break control statement, our continue control statement is usually paired with some form of a conditional (if/elif/else).
    2. When our loop first encountered an element (-1) that met the conditions of the if statement, it checked the code inside the block and saw the continue. 
    When the loop then encounters a continue statement it immediately skips the current iteration and moves onto the next element in the list (4).
    3. The output of the list only printed positive integers in the list 
    because every time our loop entered the if statement and saw the continue statement 
    it simply moved to the next iteration of the list and thus never reached the print statement.

"""

#example code
"""
1.
Your computer is the doorman at a bar in a country where the drinking age is 21.

Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.

"""

#my code
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i <= 20:
    continue
  print(i)


#NESTED LOOPS
"""
Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.

example

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
Using a for or while loop can be useful here to get each team:

for team in project_teams:
  print(team)
Would output:

["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]
But what if we wanted to print each individual student? In this case we would actually need to nest our loops to be able loop through each sub-list

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)


"""


"""
1.We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

2.Loop through the sales_data list using the following guidelines:

For our temporary variable of the for loop, call it location.
print() out each location list.

3.Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

By the end, you should have the sum of every number in the sales_data nested list.


Hint: We want one loop inside of another:

for location in sales_data:
  # Some Action
  for <temporary variable> in location
    # Some Action
4. Print out the value of scoops_sold outside of the nested loop.

"""

#example code
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for ice_cream in location:
    scoops_sold = ice_cream + scoops_sold
print(scoops_sold)


#LISTS COMPREHENSIONS: INTRODUCTION
"""
In this exercise, we are going to examine another way we can write elegant loops in our programs using list comprehensions.

We could accomplish this using a for loop and a new list called doubled:

numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

Here is our same problem but now written as a list comprehension:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


Let us break down our example in a more general way:

new_list = [<expression> for <element> in <collection>]

In our doubled example, our list comprehension:

    1. Takes an element in the list numbers
    2. Assigns that element to a variable called num (our <element>)
    3. Applies the <expression> on the element stored in num and adds the result to a new list called doubled
    4. Repeats steps 1-3 for every other element in the numbers list (our <collection>)
"""

#example code
"""
1.We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.

2.Print scaled_grades.
"""
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]
print(scaled_grades)


#LIST COMPREHENSIONS: CONDITIONALS
"""
for example
Suppose we wanted to double only our negative numbers from our previous numbers list
We will start by using a for loop and a list only_negative_doubled:

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

Now, here is what our code would look like using a list comprehension:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)


In our negative_doubled example, our list comprehension:

    1. Takes an element in the list numbers.
    2. Assigns that element to a variable called num.
    3. Checks if the condition num < 0 is met by the element stored in num. If so, it goes to step 4, otherwise it skips it and goes to the next element in the list.
    4. Applies the expression num * 2 on the element stored in num and adds the result to a new list called negative_doubled
    5. Repeats steps 1-3 (and sometimes 4) for each remaining element in the numbers list.

We can also use If-Else conditions directly in our comprehensions

example: 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

This is a bit different than our previous comprehension since the conditional if num < 0 else num * 3 comes after the expression num * 2 but before our for keyword


"""

# EXAMPLE CODE
"""
1.
We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.

Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.

2.
Print can_ride_coaster.
"""
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)


"""
1.
Create a list called single_digits that consists of the numbers 0-9 (inclusive).

Checkpoint 2 Passed

Hint
You can use the list() function with range(n) to make a list from 0 through n-1. The command:

print(list(range(5)))
yields:

[0, 1, 2, 3, 4]
2.
Create a for loop that goes through single_digits and prints out each one.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Before the loop, create a list called squares. Assign it to be an empty list to begin with.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

Checkpoint 5 Passed

Hint
You can square a number by either using:

number_to_square**2
(which takes it to the second power), or using:

number_to_square*number_to_square
which multiplies it by itself.

To append an element to a list, you can use the .append() method:

my_list.append(number_to_add)
5.
After the for loop, print out squares.

Checkpoint 6 Passed

Stuck? Get a hint
6.
Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

Checkpoint 7 Passed

Stuck? Get a hint
7.
Print cubes.

Good job!

"""
#example code
single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
print(squares)
  
cubes = [item**3 for item in single_digits]
print(cubes)




#INTRODUCTIONS TO FUNCTIONS
"""
In programming, as we start to write bigger and more complex programs, 
one thing we will start to notice is we will often have to repeat the same set of steps in many different places in our program.



example
Let us imagine we were building an application to help people plan trips! When using a trip planning application we can say a simple procedure could look like this:
function: navigation_steps()

 1. Establish your origin and destination
 2. Calculate the distance/route
 3. Return the best route to the user

Functions are a convenient way to group our code into reusable blocks.
A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again.

DEFINING A FUNCTION
def function_name():


  1. The def keyword indicates the beginning of a function (also known as a function header). 
  The function header is followed by a name in snake_case format that describes the task the function performs. 
  It Is best practice to give your functions a descriptive yet concise name.

  2. Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). 
  In this example function, we have no parameters.

  3. A colon : to mark the end of the function header.

  4. Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

  5. Notice we have indented our # function tasks go here comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.
"""

#EXAMPLE CODE
#defined a function and it's rules within the function
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:| this will run the function and execute the statements within the body
directions_to_timesSq()

"""

 In order for us to make our function a bit more dynamic, we are going to use the concept of function parameters
 Function parameters allow our function to accept data as an input value. We list the parameters a function takes as input between the parentheses of a function ( ).

EXAMPLE
def my_function(single_parameter)
  # some code

In the context of our trip_welcome() function, it would look like this:

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

The parameter is the name defined in the parenthesis of the function and can be used in the function body.
A function definition in Python

The argument is the data that is passed in when we call the function and assigned to the parameter name.
"""

#EXAMPLE CODE
# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Central Park")

#MULTIPLE PARAMETERS
"""
a single parameter is useful but functions let us use as many parameters as we want
We can write a function that takes in more than one parameter by using commas

example
def my_function(parameter1, parameter2, parameter3):
  # Some code

When we call our function, we will need to provide arguments for each of the parameters we assigned in our function definition.

# Calling my_function
my_function(argument1, argument2)

EXAMPLE
1.Our travel application users want to calculate the total expenses they may have to incur on a trip.

Write a function called calculate_expenses that will have four parameters (in exact order):

plane_ticket_price
car_rental_rate
hotel_rate
trip_time
Each of these parameters will account for a different expense that our users will incur.

Note: Like before, if we run this function now, we will get an error since there are no statements in the body.

2.Within the body of the function, let us start to make some calculations for our expenses. First, let us calculate the total price for a car rental.

Create new variable called car_rental_total that is the product of car_rental_rate and trip_time.


3.Next, we want to apply the same logic but for our hotel_rate.

Create new variable called hotel_total that is the product of hotel_rate and trip_time.

We also have a coupon to give our users some cashback for their hotel visit so subtract 10 from that total in the same statement. Woohoo, coupons! 💵

4.Lastly, let us print a nice message for our users to see the total. Use print to output the sum of car_rental_total, hotel_total and plane_ticket_price.

5.Call your function with the following argument values for the parameters listed:

plane_ticket_price : 200
car_rental_rate : 100
hotel_rate : 100
trip_time: 5

"""

#EXAMPLE CODE
# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)



#TYPES OF ARGUMENTS
"""
3 different types of arguments we can give a function

1. Positional arguments: arguments that can be called by their position in the function definition.
Their assignments depend on their positions in the function call.

2. Keyword arguments: arguments that can be called by their name.
Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call
Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)


3. Default arguments: arguments that are given default values.
We can provide a default value to an argument by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our calculate_taxi_price function will always have a default value of 10:

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)
 
# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)


EXAMPLE
1.Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.


2.First, we want to introduce the trip to users. Use print() in our function to output Here is what your trip will look like!.


3.In our function definition let us provide an itinerary that will describe the destinations our user will visit in order. Print a statement that follows this form:

First, we will stop in <first_destination>, then <second_destination>, and lastly <final_destination>
An example call to our function using positional arguments:

trip_planner("London", "India", "New Zealand")
Should output:

Here is what your trip will look like!
First, we will stop in London, then India, and lastly New Zealand
To test out your function, call trip_planner() with the following values for the parameters:

first_destination: "France"

second_destination: "Germany"

final_destination: "Denmark"


4.Call the function trip_planner() again with the following values for the parameters:

first_destination: "Denmark"

second_destination: "France"

final_destination: "Germany"

Note the difference in your output depending on the position of your arguments.


5.Call the function trip_planner() again using keyword arguments in this exact order:

first_destination: "Iceland"

final_destination: "Germany"

second_destination: "India"


6.Lastly, go ahead and call the function trip_planner() using only two positional arguments to see the default argument in action:

first_destination: "Brooklyn"

second_destination: "Queens"
"""

#EXAMPLE CODE
# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

trip_planner("Brooklyn", "Queens")

#BUILT-IN FUNCTIONS VS USER DEFINED FUNCTIONS
"""
2 distinct categories for functions in Python

User Defined Functions - functions written by users

Built-in functions - funcitons that come built into Python for us to use.

examples of built-in functions:

print()
str()
len()
help(): output the definition
max(): take the max amount
min(): takes the min amount
round(): rounds number, followed by an argument on how many decimal places we want to round it

  example
  The round() built-in function takes in two arguments. The first argument is the number we want to round, followed by an argument on how many decimal places we want to round it.

    Here is an example:

    rounded_zero = round(10.54, 0)
    rounded_one = round(10.54, 1)
 
    print(rounded_zero)
    print(rounded_one)
"""

#VARIABLE ACCESS
"""
where exactly do we have access to our variables?

only where it is defined. if a variable is only defined within a function, it can only be accessed within the function. not outside of it
We call the part of a program where destination can be accessed its "scope"

If a variable lives outside of any function it can be accessed anywhere in the file
"""

#RETURNS
"""
Functions can also return a value to the program so that this value can be modified or used late

Saving our values returned from a function allows us to reuse the value (in the form of a variable) throughout the rest of the program.

When there is a result from a function that is stored in a variable, it is called a returned function value


EXAMPLE
1.Our travel application is getting really popular. Some of our users have posted on social media that it would be useful if our application could help them track their budget during trips. We want to help them track their starting budget and let them know how much they have left after an expense.

We have provided some starting code to get started. Take a second to understand the code and then click Run and take a look at the output.

2.Let Us create a new function called deduct_expense() that will take two parameters.

The first parameter will be budget and the second parameter will be expense. Our function will be taking in a budget value as well as the expense we want to subtract.

We will want our function to return the budget minus the expense our travelers are incurring.

3.Looks like the most common expense our travelers are incurring is a t-shirt purchase.

Let Us create a variable called shirt_expense and for now, we will give it a set value of 9 (We are not accounting for currency changes at the moment). Make sure this is defined outside of the functions in your script.


4.Now that we have an expense to subtract, create a new variable called new_budget_after_shirt and set it to be the function call of deduct_expense().

Pass our current_budget variable as the first argument and the shirt_expense variable as the second argument.


5.Lastly, we want our users to see the remaining budget.

Call the provided print_remaining_budget() function, passing in new_budget_after_shirt as the only argument.

6.Great Job! This is the biggest program with functions we have built so far! Take a second to review your code and click Run one last time when you are ready to move on.
"""
#EXAMPLE CODE
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


#MUTLIPLE RETURNS
"""
Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma

example

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
 
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned function values by assigning them to variables when we call the function:

monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)

EXAMPLE

1.Our users liked the previous functionality that we added to our travel application, but recently we have had an influx of users planning trips in Italy. We want to create a small function to output the top places to visit in Italy. Another member of our team already started on the implementation of this feature but it is still missing a few key details.

Take a second to review the code and click Run when you are ready to move on. For now, there will be no output.

2.We want to be able to return the three most popular destinations from our function top_tourist_locations_italy().

Add a line in the function top_tourist_locations_italy() that will return the values of first, second, third in that exact order.

3.
In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names after we call our function.

Set the return of the function top_tourist_locations_italy() to be equal to three new variables called most_popular1, most_popular2, and most_popular3 in that exact order.

4.Use three print() statements to output the value of most_popular1, most_popular2, and most_popular3.
"""

#EXAMPLE CODE
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#EXAMPLE CODE| REVIEW
"""
1. Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

First, like in our previous exercises, we want to make sure to welcome our users to the application.

Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

Welcome to tripplanner v1.0 <Name Here>
Where <Name Here> represents the parameter variable of name we defined.

Call trip_planner_welcome(), passing your name as an argument.


2.Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our users trip.

An example call for this function will look like this:

estimated_time_rounded(2.5)
Where 2 represents 2 hours and .5 represents 30 minutes.

Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
Return rounded_time.
After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.

3.Next, we are going to generate messages for a users planned trip.

Create a function called destination_setup() that will have four parameters in this exact order:

origin
destination
estimated_time
mode_of_transport
Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Dont worry we will do that in the next step.


4.Next, we are going to write four print() statements in our function. The output on this function call should look like this:

Your trip starts off in <origin>
And you are traveling to <destination>
You will be traveling by <mode_of_transport>
It will take approximately <estimated_time> hours
Each of these print() statements use a different parameter from our function destination_setup().

Note: The estimated_time parameter will come in the form of an integer. Make sure to use str() to convert the parameter in your print statement.

After the function definition, call destination_setup() with the following arguments:

origin and destination should be string values representing the places you will travel from and to
Use the estimate you created earlier for estimated_time
If you will be traveling by a mode other than Car, be sure to overwrite the default value of mode_of_transport



5.Great job! 👏

We have successfully finished our first version of the trip builder application. Go ahead and try passing different values into your functions!


"""
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Marisa")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(4.56)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("LAX", "Germany", estimate, "Plane")


#EXAMPLE CODE/ PROJECT
"""
Turn up the Temperature
1.Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.

It should then return c_temp.

The equation you should use is:

Temp (C) = (Temp (F) - 32) * 5/9


2.Lets test your function with a value of 100 Fahrenheit.

Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.


3.Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

It should then return f_temp.

The equation you should use is:

Temp (F) = Temp (C) * (9/5) + 32

4.Lets test your function with a value of 0 Celsius.

Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.


Use the Force
5.Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

6.Test get_force by calling it with the variables train_mass and train_acceleration.

Save the result to a variable called train_force and print it out.

7.Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.

8.Define a function called get_energy that takes in mass and c.

c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

get_energy should return mass multiplied by c squared.

9.Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.


10.Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.

Do the Work
11.Define a final function called get_work that takes in mass, acceleration, and distance.

Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.


Hint
To call get_force, use mass and acceleration as inputs. Do this inside the get_work function.

12.Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.

13.Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance.


Hint
Remember to cast train_work and train_distance to strings using str() before concatenating.

The GE train does 22680000 Joules of work over 100, by the way.

"""

#PROJECT CODE
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp - 32 * 5/9)
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration, distance):
  get_force = mass * acceleration
  return get_force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")


#REGGIE'S LINEAR REGRESSION
"""
this project will combine lists, loops, and syntax to help a mad scientist perform some calculations on his data

"""

#Articles on Codeacademy Notes

def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False

"""
In this solution, we test the two bounds connected with an and boolean operator. 
This means that the code nested in the if statement will only execute if both of the conditions are true. 
We also do not include the else statement here. Since our if statement will return True and exit the function if the condition is true, 
the last line will only be reached if the condition was false.
"""

#elif and numerous if statements

def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

"""
above was codeacademy's solution
below is my solution.
both works
"""
def movie_review(rating):
  if (rating <= 5):
    return "Avoid at all costs!"
  elif (rating < 9):
    return "This one was fun."
  else:
    return "Outstanding!"

#elif and if function example
def max_num(num1, num2, num3):
  if (num1 > num2 and num1 > num3):
    return num1
  elif(num2 > num1 and num2 > num3):
    return num2
  elif(num3 > num1 and num3 > num2):
    return num3
  else:
    return ("It's a tie!")

"""
this is my code and solution code
In this code, we use a series of if, elif, and else statements. 
We test the first parameter against the other two parameters and return the value if it is greater than the other two. 
We have two more tests to check if the second parameter is greater than the other two, then if the third parameter is greater than the other two. 
In the case where none of the parameters were greater than both of the other parameters, 
then we know that there must have been a tie and the final return statement is reached.
"""

#Append list

def append_size(lst):
  lst.append(len(lst))
  return lst
"""
appends lst with the length of list aka adds the number of how many items are in list, to the end of the list
"""

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

"""
The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
"""

#length of list

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

"""
The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
"""

#count item in list
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False
"""
The function should return True if item appears in the list more than n times. The function should return False otherwise.
"""

#sorting lists in a function
def combine_sort(lst1, lst2):
  unsorted = (lst1 + lst2)
  sortedList = sorted(unsorted)
  return sortedList

"""
The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""

#range

def every_three_nums(start):
  return list(range(start, 101, 3))
"""
The function should return a list of every third number between start and 100 (inclusive). 
For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
If start is greater than 100, the function should return an empty list.
"""

#remove list in middle of list

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

"""
The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
"""

#counting items in list
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

"""
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
Return either item1 or item2 depending on which item appears more often in lst.
"""

#double index

def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

"""
did not get this one whatsoever

Our next function will double a value at a given position. We will provide a list and an index to double. 
This will create a new list by replacing the value at the index provided with double the original value. 
If the index is invalid then we should return the original list. Here is what we need to do:

  Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
  Test if the index is invalid. If its invalid then return the original list
  If the list is valid then get all values up to the index and store it as a new list
  Append the value at the index times 2 to the new list
  Add the rest of the list from the index onto the new list
  Return the new list

Create a function named double_index that has two parameters: a list named lst and a single number named index.
The function should return a new list where all elements are the same as in lst except for the element at index. 
The element at index should be double the value of the element at index of the original lst.
If index is not a valid index, the function should return the original list.
"""

#find middle element in list

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

"""
there is no way i can figure this out, i need to review this a bit more

instructions:
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. 
If there are an even number of elements, the function should return the average of the middle two elements.

Hint
Remember to use modulus % to determine if a number is divisible by 2. 
If len(lst) % 2 == 0 then the number is even. If we divide the length of the list by 2 we can get the middle element index. 
We then need to convert that value into an integer and access element at that index. 
This will look something like: lst[int(len(lst)/2)].


  solution explanation:
  We used modulus to determine if the list had an even or odd number of elements. 
  After determining this, for an odd number of elements, we calculate the middle index and return the middle element from the list. 
  For an even number of elements, we calculate the index of the element close to the middle and the other element close to the middle 
  (by subtracting 1 from the middle calculation). We get the values at those indices and calculate the average.

  Note that the math to find the middle index is a bit tricky. 
  In some cases, when we divide by 2, we would get a double. 
  For example, if our list had 3 items in it, then 3/2 would give us 1.5. 
  The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. 
  In total, this is int(len(lst)/2).
"""


# Divisible By Ten

"""


Lets start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. 
This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. 
Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. 
These are the steps we need to complete this:

Define the function to accept one input parameter called nums
Initialize a counter to 0
Loop through every number in nums
Within the loop, if any of the numbers are divisible by 10, increment our counter
Return the final counter value



Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.

Hint
Create a counter that starts at 0. Inside the loop, whenever you find a number divisible by ten, add 1 to that counter.
x is divisible by ten if x % 10 == 0 is True.


"""


#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count



#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))



#Greetings

"""
You are invited to a social gathering, but you are tired of greeting everyone there. 
Luckily we can create a function to accomplish this task for us. 
In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. 
This will require a few steps:

  Define the function to accept a list of strings as a single parameter called names
  Create a new list of strings
  Loop through each name in names
  Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
  Afterwards, return the new list of strings

  Create a function named add_greetings() which takes a list of strings named names as a parameter.

  In the function, create an empty list that will contain each greeting. 
  Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

  Return the new list containing the greetings.

Hint
Use + to concatenate 'Hello, ' with every name in names. Don't forget to add the comma and the space to the greeting!

"""

def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#my solution was pretty close considering I haven't coded in a couple of weeks

def add_greetings(names):
  names([])
  for name in names:
    names.append("Hello, " + name)

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))



#Delete starting even numbers

"""
Lets try a tricky challenge involving removing elements from a list. 
This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements.
 It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. 
 To do this, we will need the following steps:

    Define our function to accept a single input parameter lst which is a list of numbers
    Loop through every number in the list if there are still numbers in the list and if we havent hit an odd number yet
    Within the loop, if the first number in the list is even, then remove the first number of the list
    Once we hit an odd number or we run out of numbers, return the modified list


Write a function called delete_starting_evens() that has a parameter named lst.
The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
Make sure your function works even if every element in the list is even!

Hint
  Use a while loop to check two things. 
  First, check if the list has at least one element, using len(lst). 
  Second, check to see if the first element is odd using mod (%). 
  If both of those are True, slice off the first element of the list using lst = lst[1:].


After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. 
We provide two conditions for the while loop to continue. 
We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. 
If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. 
Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.

"""
#given solution

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#my solution

def delete_starting_evens(lst):
  new_list = []
  for element % 2 == 0 in lst:
    new_list.remove(0)
  return delete_starting_evens(lst)

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


#Odd Indices

"""
This next function will give us the values from a list at every odd index. 
We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. 
Here are the steps needed:

  Define the function header to accept one input which will be our list of numbers
  Create a new list which will hold our values to return
  Iterate through every odd index until the end of the list
  Within the loop, get the element at the current odd index and append it to our new list
  Return the list of elements which we got from the odd indices.

Create a function named odd_indices() that has one parameter named lst.
The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

Hint
There are a few ways to do this. range(1, len(lst), 2) will create a list of the indices you're interested in. So you could loop through that list like this:
for index in range(1, len(lst), 2):
  new_list.append(lst[index])
 

In our solution, we iterate through a range of values. 
The function range(1, len(lst), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. 
This causes the loop to iterate through every odd number until the last index of our list of numbers. 
Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

Another way to do this would be to iterate through all indices and use an if statement to see if the index youre currently looking at is odd.
"""

#my solution without the help
def odd_indices(lst):
  new_list = []
  lst.append([])
  return new_list


#my solution with help
#Write your function here
def odd_indices(lst):
  new_list = []
  for index in range (1, len(lst), 2):
    new_list.append(lst[index])
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Here is this solution:

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst



#Exponents

"""
In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

Define the function to accept two lists of numbers, bases and powers
Create a new list that will contain our answers
Create a loop that iterates through every base in bases
Within that loop, create another loop that iterates through every power in power
Within that nested loop, append the result of the current base raised to the current power.
After all iterations of both loops are complete, return the list of answers


Coding question
Create a function named exponents() that takes two lists as parameters named bases and powers. 
Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first.
Then two to the second. Then two to the third, and so on.

Hint
Use nested for loops. The outer for loop should loop through all of the bases and the inner for loop should loop through all of the powers.
Remember a ** b is a to the power of b

"""

#my code before solution

#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in exponents:
    bases ** powers
  for power in powers:
      
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


#solution
#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))



#1. Larger Sum

"""
We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. 
We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

Define the function to accept two input parameters: lst1 and lst2
Create two variables to record the two sums
Loop through the first list and add up all of the numbers
Loop through the second list and add up all of the numbers
Compare the first and second sum and return the list with the greater sum



Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

Hint
Create variables named sum1 and sum2 and set them to be 0. 
Loop through each list separately and add to the appropriate variable. 
After looping through each list, compare the two sums in an if statement and return the correct list.
"""

#my code: key word is "loop", i forgot my "for" loop (i knewn i needed to do it, but wasn't sure how to do it)

#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum(lst1)
  sum2 = 0
  sum(lst2)
  if sum1 > sum2 :
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#solution code

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2


#2. over 900

"""
We are constructing a device that is able to measure the power level of our coding abilities and according to the device, 
it will be impossible for our power levels to be over 9000. Because of this, 
as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. 
Once this happens, we should stop adding the numbers and return the value where we stopped. 
In order to do this, we will need the following steps:

Define the function to accept a list of numbers
Create a variable to keep track of our sum
Iterate through every element in our list of numbers
Within the loop, add the current number we are looking at to our sum
Still within the loop, check if the sum is greater than 9000. If it is, end the loop
Return the value of the sum when we ended our loop



Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. 
When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, 
the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

Hint
Create a variable named sum that begins at 0. 
Loop through all of the elements of lst and use a break when the sum is greater than 9000.
 Return sum after the loop.
"""

#my code

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if sum > 9000:
      break
  return sum 
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#I GOT IT ON FIRST TRY!

#solution code

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum



#Max Num
"""

Here is a more traditional coding problem for you. 
This function will be used to find the maximum number in a list of numbers. 
This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. 
Here is what we need to do:

Define the function to accept a list of numbers called nums
Set our default maximum value to be the first element in the list
Loop through every number in the list of numbers
Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
Return the maximum number


Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums

Hint
Create a variable called maximum to track the max number, and have it start as the first element in the list. 
Loop through all of the numbers in the list, and if a number is ever greater than the current max number, the max number should be re-set to that number.
"""

#my code.. i was a little confused and distracted while doing this.  got close!

#Write your function here
def max_num(nums):
  maximum = [0]
  for number in max_num:
    if number > max_num[0]:
      maximum = number

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum



# Same Values

"""
In this challenge, we need to find the indices in two equally sized lists where the numbers match. 
We will be iterating through both of them at the same time and comparing the values, 
if the numbers are equal, then we record the index. 
These are the steps we need to accomplish this:

Define our function to accept two lists of numbers
Create a new list to store our matching indices
Loop through each index to the end of either of our lists
Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
Return our list of indices


Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
Hint
Loop through all of the indices of each list using for index in range(len(lst1)) and compare lst1[index] to lst2[index]. 
Append index to a new list if those two items are equal.
"""

#my code | it did something, but not entirely correctly. brought up the correct numbers [0, 0, 2, 3] but it was supposed to look like [0, 2, 3]: need to ger rid of 0 in new_list at top
#Write your function here
def same_values(lst1, lst2):
  new_list = [0]
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_list.append([index])
  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#solution code, very close
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

# 5. reversed list

"""
For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. 
There are a few different ways to approach this, 
but we are going to try a method that iterates through each of the values in one direction for the first list 
and compares them against the values starting from the other direction in the second list. 
Here is what you need to do:

Define a function that has two input parameters for our lists
Loop through every index in one of the lists from beginning to end
Within the loop, compare the element in the first list at the current index against the element at the second lists last index minus the current index. 
If there was a mismatch, then the lists arent reversed and we can return False
If the loop ended successfully, then we know the lists are reversed and we can return True.

Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

Hint
Let's say the lists are of size 5. You want to compare lst1[0] with lst2[4], lst1[1] with lst2[3] and so on.
Loop through the numbers created by range(len(lst1)) using a variable named index

Compare lst1[index] to lst2[len(lst2) - 1 - index]. 
If those two items are not equal, return False. 
If you loop through the entire list and you never return False, 
that means that every item was equal, 
and you should return True.

"""

#my code with help from hint
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] == lst2[len(lst2) - 1 - index]:
      return True
    else:
      return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))



#solution code | looks exactly the same as my code, but != instead of ==.  Has to be != i suppose

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

"""
In this code, we iterate through each of the indices for the entire length of either of the lists 
(since we assume the lengths are equal) and we perform a comparison on each of the elements. 
We get the element at the current index from our first list with lst1[index] 
and we test it against the last index of the second list minus the current index len(lst2) - 1 – index.

That math is a little complicated — it helps to look at a concrete example. 
If we are given a list of 5 elements, the valid indices are 0 to 4. 
Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. 
Now in order to get the inverse of the position we are at in the first list, 
we subtract the index we are at from the end of the second list. 
So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. 
On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. 
If we made it to the end without a mismatch then we can return True since the second list is the reverse of the first. 
You could also try simplifying this code by using the python function reversed() or other methods that you will learn later on such as ‘slicing’.

"""



#FUNCTIONS PYTHON CHALLENGES

#1. tenth power
"""
Let’s create some functions which can help us solve math problems! 
For this first function, we are going to take the tenth power of a number. 
In order to do this we need to do three things:

Set up the function header for tenth_power which accepts one parameter
Take the tenth power of the input value
Return the result


Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power.

Hint
Remember to use def when defining the function. 
To take the power of a value, you can use the power operator **. 
For example, two to the power of five would look like: 2 ** 5.
"""

#my code : easy peasy
# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


#solution code
def tenth_power(num):
  return num ** 10


#2. square root
"""

Another useful function for solving math problems is the square root function. 
We can create this using similar steps from the last problem. 
The code will look very similar. 
We need to:

Set up the function header for square_root which accepts one parameter
Take the square root of the input value
Return the result

Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num.

Hint
Remember to use def when defining the function. 
To take the square root of a value, you can use the power operator **. 
The square root of a number is the same as taking the ½ power of the number. 
For example, the square root of 6 would look like: 6 ** 0.5.

"""

#my code

def square_root(num):
  return num ** 0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


#solution code
def square_root(num):
  return num ** 0.5



# 3. win percentage

"""
Next, we will create a function which calculates the percentage of games won. 
In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. 
For this function, there will be two input parameters, the number of wins and the number of losses. 
We also need to make sure that we return the result as a percentage (in the range of 0 to 100). 
In order to create this method we need the following steps:

Define the function header with two parameters, wins and losses
Calculate the total number of games using the number of wins and losses
Get the ratio of winning using the number of wins out of the total number of games.
Convert the ratio to a percentage
Return the percentage


Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers.

Hint
In order to calculate the ratio of wins out of total games we can use wins / (wins + losses) where wins + losses is equal to the total number of games.
To convert that value to a percentage, multiply it by 100.

"""

#my code
# Write your win_percentage function here:
def win_percentage(wins, losses):
  total = ((wins/ (wins + losses) * 100)
    return total
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


#solution code
def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100


"""
review previous code and solution

First, we defined our function with two parameters, one for games won and one for games lost. 
Next, we calculated the total number of games using the number of wins + losses. 
After that, we use calculate the ratio of wins out of the total number of games by dividing wins by our total_games variable. 
Since this gives us a ratio and we want it in percentage form, we multiply the answer by 100 and return it.
"""


#### STRINGS!

"""


Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator() that takes two inputs, first_name and last_name, 
and then concatenates the last three letters of each and returns them as a string.

Test your function on the provided first_name and last_name and save it to the variable temp_password.



"""

#code/my code + solution code
##given
first_name = "Reiko"
last_name = "Matsuki"

##created 
def password_generator(first_name, last_name):
  employee = first_name[2:] + last_name[4:]
  return employee

temp_password = password_generator(first_name, last_name)
print(temp_password)


#NEGATIVE Indices

"""
Negative Indices
In the previous exercise, we used len() to get a slice of characters at the end of a string.

There’s a much easier way to do this — we can use negative indices! Negative indices count backward from the end of the string, so string_name[-1] is the last character of the string, string_name[-2] is the second last character of the string, etc.

Here are some examples:

favorite_fruit = 'blueberry'
print(favorite_fruit[-1])
# => 'y'
 
print(favorite_fruit[-2])
# => 'r'
 
print(favorite_fruit[-3:])
# => 'rry'

"""

#Example
"""
Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.
"""

##given
#company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"


company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

#my code
second_to_last = (company_motto[-2])
final_word = (company_motto[-4:])



"""
Strings are Immutable
So far in this lesson, we’ve been selecting characters from strings, slicing strings, and concatenating strings. 
Each time we perform one of these operations we are creating an entirely new string.

This is because strings are immutable. 
This means that we cannot change a string once it is created. 
We can use it to create other strings, but we cannot change the string itself.

This property, generally, is known as mutability. 
Data types that are mutable can be changed, and data types, like strings, that are immutable cannot be changed.


"""


"""
The most recent hire at Copeland’s Corporate Company is a fellow named Rob Daily. 
Unfortunately, Human Resources seem to have made a bit of a typo and sent over the wrong first_name.

Try changing the first character of first_name by running

first_name[0] = "R"


Oh right! Strings are immutable, so we can’t change an individual character. Okay that’s no problem—we can still fix this!

Delete the code you just wrote for step 1.

Then, concatenate the string "R" with a slice of first_name that includes everything but the first character, 
"B", and save it to a new string fixed_first_name.
"""

##given
first_name = "Bob"
last_name = "Daily"


#my code

fixed_first_name = "R" + first_name[-2:]

print(fixed_first_name)


"""
Escape Characters
Occasionally when working with strings, 
you’ll find that you want to include characters that already have a special meaning in python. 
For example let’s say I create the string

 favorite_fruit_conversation = "He said, "blueberries are my favorite!""
We’ll have accidentally ended the string before we wanted to by including the " character. 
The way we can do this is by introducing escape characters. 
By adding a backslash in front of the special character we want to escape, \", we can include it in a string.

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""


"""

"""
When Rob Daily (remember him? From the last exercise?) set up his account he set his password to be

theycallme"crazy"91
His password was causing some errors in the system because of the " marks. 
Rewrite his password using escape characters and save it to the variable password.


"""

#given code

password = "theycallme"crazy"91"

#my code
password = "theycallme\"crazy\"91"

print(password)


"""
Iterating through Strings
Now you know enough about strings that we can start doing the really fun stuff!

Because strings are lists, that means we can iterate through a string using for or while loops. 
This opens up a whole range of possibilities of ways we can manipulate and analyze strings. 
Let’s take a look at an example.

def print_each_letter(word):
  for letter in word:
    print(letter)
This code will iterate through each letter in a given word and will print it to the terminal.

favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'
Let’s try a couple of problems where we need to iterate through a string.


"""


"""
.
Let’s replicate a function you are already familiar with, len().

Write a new function called get_length() 
that takes a string as an input and returns the number of characters in that string. 
Do this by iterating through the string, don’t cheat and use len()!
"""

#my code

def get_length("supercalifragilistic expialidocious"):
  counter = 0
  for number in get_length:
    counter += 1
print(get_length)

#solution code
def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

  #my code after solution
  
def get_length(supercalifragilisticexpialidocious):
  counter = 0
  for number in supercalifragilisticexpialidocious:
    counter += 1
  return counter