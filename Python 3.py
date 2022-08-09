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


"""