'''
A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
Input Format
The first line contains two space-separated integers describing the respective values of  (the number of words in the magazine) and  (the number of words in the ransom note).
The second line contains  space-separated strings denoting the words present in the magazine.
The third line contains  space-separated strings denoting the words present in the ransom note.

Print "Yes" if the magazine can create an untracable replica of the ransom note
Otherwise, print No

I used this problem along with some popular solutions to learn about "Counter"
in Python.
'''
from collections import Counter

def ransom_note(magazine, ransom):
    # Counters give a collection of hashable objects from an input. 
    # i.e. in this case it will give us the number of instances of a word
    # from the input.
    # We calculate ransom first because it will have a smaller size comapred
    # to the magazine. The magazine should contail everything in ransom, so
    # the final result should be 0 if this is accurate.
    return(Counter(ransom) - Counter(magazine)) == {}

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
