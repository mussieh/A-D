'''
Created on Feb 8, 2018
Palindrome Permutation Program
@author: Mussie Habtemichael
'''

# Function to strip non-alphabetic characters
# from a string.
def stripChars(givenString):
    strippedString = ''
    letterList = []
    for letter in givenString:
        if letter.isalpha(): letterList.append(letter)
    return strippedString.join(letterList)

# Function that fills a hashtable from the contents of a
# string. The contents of the string are stripped from
# whitespace and other non-alphabetic characters before
# insertion. The keys of the hash table are the letters
# of the string whiie the values are their frequency of occurence
# in the string
def getHashTable(inputString):
    palinTable = {}
    strippedString = stripChars(inputString)
    letter = ''
    for i in strippedString:
        letter = i.lower()
        if palinTable.get(letter) == None:
            palinTable[letter] = 1
        else:
            palinTable[letter] += 1
    return palinTable

# Function that checks if a string is a permutation
# of a palindrome. It uses a hash table of letter frequencies
# to check if a palindrome is possible based on the letter frequencies.
# It returns true only if there is a single odd number letter frequency
def isPalindromePermutation(givenString):
    oddLetterCount = 0
    palinTable = getHashTable(givenString)
    tableValues = palinTable.values()
    for letterCount in tableValues:
        if letterCount % 2 != 0:
            oddLetterCount += 1
        if oddLetterCount > 1:
            return False
    return True

# Function Example Usage         
isPalindromePermutation("A man, a plan, a canal - Panama")