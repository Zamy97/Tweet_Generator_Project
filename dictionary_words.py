import random
import sys

word_list = []

with open("random_words.text","r") as f:
    for line in f.readlines():
        word_list.extend(line.split())

def generate_the_word():
    random_word = random.choice(word_list)
    return random_word

print(word_list)
print(generate_the_word())
print(" ".join([word_list[random.randrange(0, len(word_list))] for i in range(5)]))






# def generate_the_word(infile):
#     random_line = random.choice(open(infile).read().split('\n'))
#     return random_line
#
# def main():
#     infile = "/usr/share/dict/words"
#     print(generate_the_word(infile))
#
# main()
