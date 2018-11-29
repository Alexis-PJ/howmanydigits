"""
find the number of digits in a given integer
"""

num = int(input("Enter the number :")) # Enter the number using keyboard

div = 1 # start with the power of 10 in the iteger division
while num// 10**div != 0: # check the condithion: is the quotient of the
                          # integer divison num divided by 10 to the power of div
                          # not equal to zero?
                          # if yes execute the loop body
    div = div + 1

print("the number :", num, "has",div ,"digits")
                          # the massage
