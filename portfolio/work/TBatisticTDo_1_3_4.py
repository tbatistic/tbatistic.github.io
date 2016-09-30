from __future__ import print_function # must be first in file 
import random

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = False
        print('potato bug in food_id()')
    if food_id('taco') != 'NOT Starchy, NOT Fruit':
        works = False
        print('taco bug in food_id()')
 
    if works:
        print('food_id passed all tests')
    return works
    
#Determine in user input is even or odd
def f(n):
    if int(n) == n:
	    if n % 2 == 0:
                if n % 3 == 0:
	            print ("n is a multiple of 6")
                else:
                    print ("n is even")
            else:
                print ("n is odd")
    else:
            print ("n is not an integer")

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
        
def quiz_decimal():
    low = float(raw_input("Insert low value: "))
    high = float(raw_input("Insert high value: "))
    if low > high:
        print ("Please enter valid values")
        quiz_decimal()
    print ("Type a number between", low, "and", high, ":")
    between = float(raw_input("")) 
    if high > between > low:
        print ("Good!", low)
    elif low > between:
        print ("No,", between, "is less than", low)
    elif between > high:
        print ("No,", between, "is greater than", high)

quiz_decimal()