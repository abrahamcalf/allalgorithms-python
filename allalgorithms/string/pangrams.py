# Algorithm to check the string is pangram or not

alpha = "abcdefghijklmnopqrstuvwxyz "

def isPangram(s):
    for i in alpha:
        if i not in s:
            return "not pangram"
    return "pangram"
s = input().lower()
print(isPangram(s))

