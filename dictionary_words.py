import random

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

def main():
    infile = "/usr/share/dict/words"
    print(generate_the_word(infile))

main()
