# PPHA 30535
# Spring 2021
# Homework 1

# SUNENA GUPTA
# SUNENAG

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.


#making a list of objects:
q1_list = [7, "apple", 43, "basketball", 732, "Chicago" ]

#creating a list which contains the index position and the object at that particular position:
a=list(enumerate(q1_list))
print(a)

#printing the required statement:
for i,j in a:
    print('The value at position', i, 'is', j)
    
    
     


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

#importing required library:
import re

#defining a new function to determine whether a phrase is a palindrome: 
#The function removes all punctuation, spaces and converts all letters to lower case. 
#It then converts the resultant object, 'b', to a list, separating all letters
#Next, we reverse the order of the list.
#If the forwards version is the same as backwards, the function returns True.
# True implies that the expression is a palindrome
def palindrome(a):
    b = re.sub(r'[^a-zA-Z]', '', a).lower()
    c=list(b)
    d=c[::-1]
    return c==d

#testing out the required words and phrases:
palindrome("radar")
palindrome("A man, a plan, a canal, Panama!")
palindrome("Apple")
palindrome("This isn't a palindrome")




# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')

#using the while function to make a conditions:
#If the vegetable entered by user is not in the list, available_vegetables, then the program 
#continues asking for a input until a vegetable from the list available_vegetables is entered. 
#If the vegetable entered by user is in the available_vegetables list, the program prints the 
#required statement with the vegetable of choice. 
while choice not in available_vegetables:
    choice = input('Please pick a vegetable I have available: ')
else:
    print('The user can have', choice)


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

#making a list of strings, including variation in capitalization and starting alphabet:
lst=["applE", "BanAnA", "Car", "DiAmonD", "AlpHAbet"]

#creating an empty list to insert the strings that satisfy the requirements:
q4_list=[]

#Going through each term in the original list 'lst'.
#Converting each string to lower case. 
#Converting each string to its own list, separating the letters.
#Checking if the first letter (index position 0) is 'a' or 'b'. 
#If it is, the string is appended to the new list q4_list.
 
for i in lst:
    a=i.lower()
    b=list(a)
    if b[0]=="a" or b[0]=="b":
        q4_list.append(a)
        
print(q4_list)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]


q5=[i * 2 for i in start_list[::-1]]
    
print(q5)
    


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']


q6_dict = dict(zip(short_names, long_names))
print(q6_dict)

