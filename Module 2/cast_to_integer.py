"""
Program: cast_to_integer.py
Author: Dylan Thomas
Last date modified: 09/06/2020



The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 
"""

userNum = input("Input anything: ")


print ()

print ("Integer: ")
print (int(float(userNum)))
print ()


#It seems that a string can't be changed into an integer or a float since it
# is not a number of any kind so it results in an error

# Input   Expected Output  Actual Output
#    3           3                3
#   8.8          8                8
#   -20         -20              -20
#   -1.5        -1                -1
#'somestr'      error           error        
