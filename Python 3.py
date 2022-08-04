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