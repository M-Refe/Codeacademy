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