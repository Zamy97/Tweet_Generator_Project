import random
from random import shuffle

random_words = open("/usr/share/dict/words").read().split()
shuffle(random_words[:9])
print(random_words)














# import random
#
# def generate_the_word(infile):
#     random_line = random.choice(open(infile).read().split('\n'))
#     return random_line
#
# def main():
#     infile = "/usr/share/dict/words"
#     print(generate_the_word(infile))
#
# main()
