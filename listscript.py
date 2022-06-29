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

