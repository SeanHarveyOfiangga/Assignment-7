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

sentence = input('Please type in the sentence here: ').upper()
vowel = "AEIOU"
space = " "
consonant = "BCDFGJKLMNPQSTVXZHRWY"

def vowel_counter(sentence, vowel):
    vcount = 0
    for c in sentence:
        for d in vowel:
            if c == d:
                vcount = vcount + 1
    return vcount

def word_counter(sentence, space):
    wordcount = 1
    for c in sentence:
        for d in space:
            if c == d:
                wordcount = wordcount + 1
    return wordcount

def consonant_counter(sentence, consonant):
    ccount = 0
    for c in sentence:
        for d in consonant:
            if c == d:
                ccount = ccount + 1
    return ccount

word_count = word_counter(sentence, space)
vowel_count = vowel_counter(sentence, vowel)
consonant_count = consonant_counter(sentence, consonant)

print(consonant_count)