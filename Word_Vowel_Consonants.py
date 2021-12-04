#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

def intro():
    print ('\nHello, welcome to word, vowel, and consonant counter\n')
intro()

def word():
    word = input('Please type in the sentence here: ')
    print(word)

word()