#practice practice practice

#def a function is_even that will take number x as input
#if x is even, then return True
#otherwise, return False

def is_even(x):
  if x % 2 == 0 :
    return True
  else:
    return False

#def a function is_int that takes a number x as an input
#return True if the number is an integer and False otherwise
#is_int(7.0) = True
#is_int(7.5) = False
#is_int(-1) = True

#my code
def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False
#my code also works

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print (is_int(10.0)) #True
print (is_int(10.5)) #False
print (is_int(-2)) #True

#digit_sum
#summing the digits of a number
#write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits

#  // => floor division
#  % => modulo (remainder)

#           CHALLENGE METHOD
#floor division will reduce the number by one digit if we divide by 10
# 123 // 10 => 12

#modulo will give us the last digit if our divisor is 1o
# 123 % 10 => 3

#now set up a loop to carry out the cycles until we reduce the number down to zero

#           INITIAL METHOD

#used this to convert integer to a string with str(), iterate over it, and turn the substrings back into integers with int() to do the addition.
def digit_sum(n):
  total = 0
  for x in str(n):
    total += int(x)
  return total

print (digit_sum(48652))

#factorial
#factorial(4) = 4 * 3 * 2 * 1
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print (factorial(5))