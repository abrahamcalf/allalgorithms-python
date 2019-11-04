'''
Counting valleys deals with strings. One has to count the number of valleys and Hills in the given string and return the position of traveller at end w.r.t the start point. 
'U' is treated as 'the traveller came across a hill' and 'D' denotes that he came across a valley.

Input is guranteed as a string with 'U', and 'D' with an integer having the value of length of input string.

Output should be a single integer that denotes the number of valleys traveller walked through during his hike.

Example : 
Input = 8
        UDDDUDUU

Output = 1
'''

import sys
n = int(input())
s = input()

m = 0
v = 0

for i in s:
    if i == 'U':
        m += 1
        if m == 0:
            v += 1
    else:
        m -= 1
print(v)
         
