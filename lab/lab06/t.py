import sys

def first_inside_quotes(s):
    start = s.find('"')
    end = s.find('"', start+1)

    return s[start+1:end]


str1 = input()
str1 = first_inside_quotes(str1)

print(str1)
