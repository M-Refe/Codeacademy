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

#is_prime function
#a prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
#my code that semi works
def is_prime(x):
  for n in range(2, x-1):
    if x % n:
      return False
    else: 
      return True
print (is_prime(5))  #it returned False - so it works, but it's resulting error because 0 is coming out as none

def is_prime(x):
  if x < 2:
    return False
  else:
    for n in range(2, x-1):
      if x % n == 0:
        return False
    return True
print (is_prime(9))

# reverse
#i honestly don't get this part without using Pro
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print (reverse("Hello World"))

#anti_vowel
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print (anti_vowel("hello book"))

#scrabble_score
#my code
#define scrabble_score that takes the a string "word" as input and returns the equivalent scrabble score for that word
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = ""
  word = word.lower()
  total = 0
  for word in score:
    print (score[word])
    total = total + score[word]
    return total
print (scrabble_score("pie"))

#solution
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print (scrabble_score("pizza"))

#censor
#write function called "censor", that takes two strings, 'text' and 'word' as input. It should return the 'text' with the 'word' you chose replaced with asterisks.
#i've literally don't understand this part of the course. I've not learned any of this. and none is in my notes
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print (censor("this hack is wack hack", "hack"))
#it took the word "hack" and replaced it with ***


#define a function called count that has 2 arguments "sequence" and "item"
#return the number of times the item occurs in the list
#for example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list)
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  
print (count([1, 2, 1, 1], 1))

#purify 
#define a function called purify that takes a list of numbers, removes all odd numbers in the list, and "returns" the result. 
#do not directly modify the list you are given as input; instead return a new list with only the even numbers

#used the community forums to help me with this: GOT IT THOOOOO YAAAAAAAYYYY
def purify(lst):
  new = list(lst)
  for x in lst:
    if x % 2 == 0:
      x = x
    else:
      new.remove(x)
  return new

print (purify([8, 5, 9, 4, 6, 7, 3, 2]))

#product
#define a function called product that takes a list of integers as input and returns the product of all of the elements in the list
#solution code
def product(list):
  total = 1
  for num in list:
    total = total * num
  return total

print (product([4, 5, 5]))

#remove_duplicates
