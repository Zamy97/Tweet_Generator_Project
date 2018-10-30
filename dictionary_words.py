import random

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

def main():
    infile = "random_words.text"
    print(generate_the_word(infile))

main()
