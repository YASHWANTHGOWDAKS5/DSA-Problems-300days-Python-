#Day_8
#Getting the first unique element in a string
#using collections library
from collections import Counter

def uniquestring(s: str)->int:
    freq=Counter(s)
    for i, char in enumerate(s):
        if freq[char]==1:
            return i
s='helloworld'
print(uniquestring(s))