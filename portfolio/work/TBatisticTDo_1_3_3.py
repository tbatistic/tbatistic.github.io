from __future__ import print_function #Use Python 3.40 printing
  
def age_limit_output(age):
    '''Steo 6a if-else example'''
    AGE_LIMIT = 13 #Convention = Use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print('Minimum age is', AGE_LIMIT)

def report_grade(percent):
    '''Step 6b if-else'''
    PERCENT_LIMIT = 80
    if percent < PERCENT_LIMIT:
        print(percent, 'does not indicate mastery.')
    else:
        print(percent, 'indicates mastery.')
        
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
    #should check len(letter)==1
    
def letter_in_word(letter):
    word = ("bandBANDBand")
    if letter in word:
        print("YES")
    else:
        print("NO")
        
def hint(color, secret):
    if color in secret:
        print('The color', color, 'IS in the sequence.')
    else:
        print('The color', color, 'IS NOT in the sequence.')
