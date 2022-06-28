#Create three dictionaries: lloyd, alice, and tyler
#Give each dictionary the keys "name", "homework", "quizzes", and "tests"
#Have the “name” key be the name of the student (that is, lloyd‘s name should be "Lloyd") and the other keys should be an empty list (We’ll fill in these lists soon!)

lloyd = {
  "name": "Lloyd", 
  "homework": [], 
  "quizzes": [], 
  "tests": []}

alice = {
  "name": "Alice", 
  "homework": [], 
  "quizzes": [], 
  "tests": []}

tyler = {
  "name": "Tyler", 
  "homework": [], 
  "quizzes": [], 
  "tests": []}

 #Now fill out your lloyd dictionary with the appropriate scores. To save you some time, we’ve filled out the rest for you
 #Homework: 90.0, 97.0, 75.0, 92.0
 #Quizzes: 88.0, 40.0, 94.0
 #Test Scores: 75.0, 90.0
 #Make sure to include the decimal points so your grades are stored as floats! This will be important later.

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
#Below your code, create a list called students that contains lloyd, alice, and tyler.
students = [lloyd, alice, tyler]
#for each student in your students list, print out that student's data as follows: print student's name, print student's homework, print student's quizzes, print student's tests
for student in students:
  print (student["name"])
  print (student["homework"])
  print (student["quizzes"])
  print (student["tests"])

#Write a function average that takes a list of numbers and returns the average
#   Define a function called average that has one argument, numbers.
#   Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
#   Like the example above, use float() to convert total and store the result in total.
#   Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
#   Return that result
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

#compute a student's average using weighted averages
#Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average
#   Define a function called get_average that takes one argument called student
#   Make a variable homework that stores the average() of student["homework"]
#   Repeat the above step for “quizzes” and “tests”.
#   Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total

#send a letter
#write a get_letter_grade function that takes a number score as input and returns a string with the letter grade that the student should receive
#define a new function called get_letter_grade that has 1 argument called score. expect score to be a number
#inside function, test "score" using a chain of if: / elif: / else: statements
#   If score is 90 or above: return "A"
#   Else if score is 80 or above: return "B"
#   Else if score is 70 or above: return "C"
#   Else if score is 60 or above: return "D"
#   Otherwise: return "F"
# then print the resulting letter grade with "print".  call the get_letter_grade function and pass in get_average(lloyd).
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
print (get_letter_grade(get_average(lloyd)))

#calculate class average
#Define a function called get_class_average that has one argument class_list. You can expect class_list to be a list containing your three students.
#   First, make an empty list called results
#   For each student item in the class_list, calculate get_average(student) and then call results.append() with that result
#   Finally, return the result of calling average() with results.
def get_class_average(class_list):
  results = []
  for student in class_list:
    average_student = get_average(student)
    results.append(average_student)
  return average(results)

#check on numerical grade of class total
#   create list "students" and fill with 3 students: alice, lloyd, and tyler
#   find average grade of the class. print numerical grade to terminal
#   determin the letter grade for the class's average and print to terminal
students = [alice, lloyd, tyler]
print (get_class_average(students))
# in the code for get_letter_grade, the alphabetical letter already prints out before the numerical number.  it works because the print function is already called on in a previous function therefore, no need to retype the print alphabetical letter grade
