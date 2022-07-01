#On line 3, multiply the second element of the n list by 5
#Overwrite the second element with that result.
#Make sure to print the list when you are done!

n = [1, 3, 5]
# Do your multiplication here
m = n[1] * 5
n[1] = m
#given underneath
print (n)

#append
#Append the number 4 to the end of the list n.

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print (n)

#remove elements from list

#will remove item at index from list, and return it to you
n.pop(1)
n = [1, 3, 5]
print (n)

#will remove the actual item "1" from the list, as opposed to index 1.
n.remove(1)
print (n)

#will delete item at index 1, won't return it
del(n[1])
print (n)

#Define a function called add_function that has 2 parameters x and y and adds them together
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
  return x + y
print (add_function(m, n))

#Write a function called string_function that takes in a string argument (s) and then returns that argument concatenated with the word 'world'. Don’t add a space before world!
n = "Hello"
# Your function here!
def string_function(s):
  return s + "world"
print (string_function(n))

#using a list as an argument in a function is the same as using just a number or a string
def list_function(x):
  return x
n = [3, 5, 7]
print (list_function(n))

#Change line 2 so that list_function returns only the item stored in index one of x, rather than the entire x list.
def list_function(x):
  return x[1]
#changed return x to return x[1]
n = [3, 5, 7]
print (list_function(n))

#change list_function to 
#   to add 3 to the item at index 1 of the list
#   store the result back into index 1
#   return list
#original section
def list_function(x):
  return x[1]

n = [3, 5, 7]
print (list_function(n))
#my final code/ with solution
def list_function(x):
  x[1] = x[1] + 3
  return x
n = [3, 5, 7]
print (list_function(n))

#define function called list_extender, that has one parameter lst
#   inside the function, append the number 9 to lst
#   return modified list
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst
print (list_extender(n))

#   modifying each element in a list in a function
#   Create a function called double_list that takes a single argument x (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.
n = [3, 5, 7]
#inserted definition and indented for loop to create this function. changed all from n to x in for loop
def double_list(x):
  x * 2
  for i in range(0, len(x)):
    x[i] = x[i] * 2
# Don't forget to return your new list!
  return x
print (double_list(n))

# Passing a range into a function
# learning about range() and it's uses
# range(stop), range(start, stop), range(start, stop, step), the start and stop are replaced with numbers... / integers

#replace the ____ with a range() that returns a list containing [0, 1, 2].
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print( my_function(range(0, 3))) #range(0, 3) was my input
# Add your range between the parentheses! ^

#iterating over a list in a function
# method 1, for item in list:
for item in list:
    print(item)
# method 2, iterate through indexes:
for i in range(len(list)):
    print(list[i])

#example
    #create a function that returns the sum of a list of numbers
        #On line 3, define a function called total that accepts one argument called numbers. It will be a list.
        #Inside the function, create a variable called result and set it to zero.
        #Using one of the two methods above, iterate through the numbers list. For each number, add it to result.
        #Finally, return result.
    #helpful tips showed me: If you chose to write your loop with the range() method, 
    # you’ll need to access your list items with the current number in your range. 
    # In the code below, i holds the value of the current range value for our loop 
    # and we use that to access an index in our list.
        #for i in range(len(some_list)):
            #print i  |||# This will print a number, starting at 0, going up to the list length
             #result += some_list[i]  |||# Access the current value in our list
n = [3, 5, 7]

def total(numbers):
  result = 0
  for n in range(len(numbers)):
    print (n)
    result += numbers[n]
  return result
#i wrote the entire function with range, only given was the list n = [3, 5, 7]

#using strings in lists in functions
    #create a function that concatenates strings, define join_strings, accepts argument words.
    #inside function, create variable result = "", empty string.
    #iterate through words list and concatenate each word to result
    #return the result
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for n in range(len(words)):
    result += words[n]
  return result
#print function was given
print (join_strings(n))

#using two lists as two arguments in a function
#easy, just add the arguments together 
    #define function called join_lists, with 2 arguments, x & y
    #inside function, return the result of concatenating x and y together
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
  result = x + y
  return result

#print function was given
print (join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]

#using a list of lists in a function
    #create funcitn called flatten, takes a single list and concatenates all the sublists that are a part of it into a single list
        #define function called flatten, with 1 argument, lists
        #make new, empty list called results
        #iterate through lists, call looping variable numbers
        #iterate through numbers
        #for each number, .append() to results
        #return results
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

#this one was hard, i wrote
#def flatten(lists):
  #results = []
    #for numbers in lists:
        #for n in numbers:
        #results.append()
    #return results
#very close, i just needed to add "n" into append
print (flatten(n))