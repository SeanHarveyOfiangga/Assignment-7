#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

#intro
def intro():
    print ('\n\033[47m\033[30m**Hello, welcome to word, vowel, and consonant counter**\n\033[0m')
intro()

#user input
sentence = input('\033[92mPlease type in the sentence here: \033[0m').upper()

#variables needed
vowel = "AEIOU"
space = " "
consonant = "BCDFGJKLMNPQSTVXZHRWY"

#vowel counter function
def vowel_counter(sentence, vowel):
    vcount = 0
    for c in sentence:
        for d in vowel:
            if c == d:
                vcount = vcount + 1
    return vcount

#word counter function
def word_counter(sentence, space):
    wordcount = 1
    for c in sentence:
        for d in space:
            if c == d:
                wordcount = wordcount + 1
    return wordcount

#consonant counter function
def consonant_counter(sentence, consonant):
    ccount = 0
    for c in sentence:
        for d in consonant:
            if c == d:
                ccount = ccount + 1
    return ccount

#calls for functions and stored into variables
word_count = word_counter(sentence, space)
vowel_count = vowel_counter(sentence, vowel)
consonant_count = consonant_counter(sentence, consonant)

#overall program output
def output():
    print (f"\nYou entered: {sentence}\n Word(s): {word_count}\n Vowel(s): {vowel_count}\n Consonant(s): {consonant_count}")
    print("\nThank you for using this program!")
output()

#program completed