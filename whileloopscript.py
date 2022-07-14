#while loop is similar to an if statement
#while loop will continue to execute as long as the condition is true

#it executes whil that thing is true

count = 0

if count < 5:
  print ("Hello, I am an if statement and count is"), count

while count <= 9:
  print ("Hello, I am a while and count is"), count
  count += 1

#the while loop above will print out the statement until the count goes to number 10, and then it will completely stop looping

#Loop condition
# condition is the expression that decides whether the loop is going to continue being exececuted or not
# 5 steps
    #loop_condition variable is set to True
    #the while loop checks to see if loop_condition is True.  It is, so the loop is entered
    #the print statement is executed
    #the variable loop_condition is set to False
    #The while loop again checks to see if loop_condition is True. 

#create while loop that counts 1-10 inclusive, inside loop, print num squared num **2, and increment num
num = 1

while num <= 10:  # Fill in the condition
  print (num**2)
  num += 1

#loop condition so user will be prompted for a choice over and over again while choice does not equal "y" or "n"
choice = (raw_input('Enjoying the course? (y/n)'))

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
  choice = (raw_input("Sorry, I didn't catch that. Enter again: "))

#infinite loop is a loop that never exists. few reasons why
#     the loop condition cannot possibly be false (e.g., while 1 != 2)
#     the logic of the loop prevents the loop condition from becoming false

#break
  # the break is a one-line statement that means "exit the current loop"
  # first create a while with a condition that is always true. 
  #using an if statement, you define the stopping condition.  inside the if, you write berak, meaning "exit the loop"

count = 0

while True:
  print (count)
  count += 1
  if count >= 10:
    break

#the above code will continue until if condition occurs

#while/else is similar to if/else, but the difference:
  # the else block will exectue anytime the loop condition is evaluated to False.
    #means that it will execute if the loop is never entered of it the loop exits normally
    #if loop exits as the result of a break, the else will not be executed

from logging import StringTemplateStyle
import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")

  #the example above generates 3 numbers, and will loop until 3 rounds.
  #unless if the generated number is 5, then it'll break


  #while/else practice
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!/ develop code based off of given instructions
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print ("You win!")
    break
  guesses_left -= 1
else:
  print ("You lose.")

#alternative way is "for" loop
print "Counting..."

for i in range(20):
  print (i)


#create for loop that prompts user for a hobby 3x
#save the result of each prompt in a hobby variable
#append each one to hobbies
#print hobbies after your for loop
#make sure to answer the prompts in the terminal when testing code

#for loop should use range(3). should use the raw_input*() function to get info from the user and hobbies.append(hobby) to add the hobby to the list

hobbies = []

# Add your code below!
for num in range(3):
  hobby = raw_input("Your hobbies: ")
  hobbies.append(hobby)
  print (hobbies)

#for strings
#using a for loop, you can print out each individual character in a string 
thing = "spam!"

for c in thing:
  print (c)

word = "eggs!"

# Your code here!
for l in word:
  print (l)

#string manipulation is useful in for loops to modify some content in a string
#the "," character after print statement mean that the next print statement keeps printing on the same line
# filter the "A" and "a" from string: "A bird in the hand..."

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print ("X"),
  else:
    print (char),




#Don't delete this print statement!
print

#for loop is most useful and most common when going through  a list 
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print (num)

# Add your loop below!
for num in numbers:
  print (num**2)

#looping over a dictionary
#utilize the key to get the value when looping over a dictionary
#example

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print ("This dictionary has the value 10!")
#first, create a dictionary with strings as the keys and numbers as the values
#then, iterate through the dictionary, each time storing the key in "key"
#next, check if the key's value is equal to 10
#if so, print "this dictionary has the value of 10!"

#print the key, followed by a space, followed by the value associated with that key.
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print (key, d[key])

#weakness of using for-each style, is you don't know the index of the thing you're looking at.
#sometimes it's useful to know how far into the list you are
#enumerate helps
#works by supplying a corresponding index to each element in the list that you pass it
#each time you go through the loop, index will be 1 greater, and item will be the next item in the sequence
#similar to using a normal "for" loop with a list, except this gives us an easy way to count how many items we've seen so far

#example code
#havethe user see things listed starting from index 1
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
  #i added "+ 1" to the code

#multiple lists; it's common to need to iterate over 2 lists at once
#zip function comes in handy
#zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list
#zip can handle 3 or more lists as well

#compare each pair of elements and print out the larger of the two
#use max function to compare the two lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  print (max(a, b))

#just like with while, for loops may have an "else" associated with them
#the else statement is executed after the "for", but only if the "for" ends normally - that is, not with a "break"
#this example given code will "break" when it hits 'tomato', so the "else" block won't be executed

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A'), f
else:
  print ('A fine selection of fruits!')

#the "else" block won't run this case, since "break" executes when it hits 'tomato'

#last exercise "create your own"
hobbies = ['fly fishing', 'hiking', 'crafting', 'strength training', 'asmr', 'Netflix']

print 'My hobbies include...'
for h in hobbies:
  if h == 'Netflix':
    print ('Netflix is not a hobby!')
    break
else:
  print (hobbies)

  