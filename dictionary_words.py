import random
import sys

word_list = []

# Open the file and add the words from the file to the word list seperatly
with open("/usr/share/dict/words","r") as f:
    for line in f.readlines():
        word_list.extend(line.split())


def generate_the_word():
    """ This will pick a random word from the file and return the word """
    random_word = random.choice(word_list)
    return random_word

# This will put those range of words together and print it on the console
print(" ".join([word_list[random.randrange(0, len(word_list))] for i in range(4)]))

# TO do
    #Need to accept an argument from the user
    #show the number words words based on how many words the user wants to see




"""
Links I Looked at:
https://stackoverflow.com/questions/49144723/python-creating-a-random-sentence-generator-from-dictionary
https://gist.github.com/bergantine/2390284
https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
https://stackoverflow.com/questions/36706734/reading-words-from-a-file-and-putting-into-list
https://www.google.com/search?q=random+shuffle+list+python&oq=random+shu&aqs=chrome.1.0l3j69i57j0l2.7221j0j7&sourceid=chrome&ie=UTF-8
"""





# def generate_the_word(infile):
#     random_line = random.choice(open(infile).read().split('\n'))
#     return random_line
#
# def main():
#     infile = "/usr/share/dict/words"
#     print(generate_the_word(infile))
#
# main()
