import random
import sys

word_list = []

with open("/usr/share/dict/words","r") as f:
    for line in f:
        word_list.extend(line.split())

def generate_the_word():
    random_word = random.choice(word_list)
    return random_word

print(generate_the_word())





# def generate_the_word(infile):
#     random_line = random.choice(open(infile).read().split('\n'))
#     return random_line
#
# def main():
#     infile = "/usr/share/dict/words"
#     print(generate_the_word(infile))
#
# main()
