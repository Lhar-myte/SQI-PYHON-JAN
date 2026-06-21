# Scenario: You want to create a Pig Latin translator.

# Task: Write a program in a file called `pig_latin.py` that takes a string called `text` which is a single valid English
#  word without spaces or special characters and translates the text to Pig Latin. In Pig Latin:

# If a word starts with a single consonant before the first vowel, move the first letter to the end and add "ay" to 
# the end of the word.
# If a word starts with a consonant cluster i.e. more than one consonant before the first vowel, 
# move the consonant cluster to the end and add “ay” to the end of the word.
# If the consonant cluster that starts the word ends with ‘y’, `y` is considered a vowel and therefore remains at the
# beginning with the rest of string, followed by the consonant or consonant cluster and then “ay” at the end of the word.
# If `y` however starts the word, it is considered a consonant and follows the first rule.
# If a word starts with a vowel, add "way" to the end of the word.



def pig_latin(text):
text = "konsonants"
vowels = "aeiou"
consonants = not vowels
for char in text:
    if text.startswith(vowels):
