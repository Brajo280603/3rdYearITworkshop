import re

def clean_string(s):
    return ''.join(sorted(re.sub(r'\W+', '', s).lower()))

def are_anagrams(s1, s2):
    return clean_string(s1) == clean_string(s2)

s1 = input("Enter first word: ")
s2 = input("Enter second word: ")

if(are_anagrams(s1, s2)):
    print("Both words are anagrams")  
else:
    print("Both words are not anagrams")
