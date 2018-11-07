import collections
from collections import Counter

# Finds the number of repeted words in the file
def find_most_common_words(textfile):
    """ Return the most common words in a text file. """
    textfile = open("source_text.text")
    text = textfile.read().lower()
    textfile.close()
    words = collections.Counter(text.split()) # how often each word appears
    return dict(words.most_common())

word_frequency = find_most_common_words("source_text.text")
print(word_frequency)

count = {}

# Prints out how many times the unique words are in the file
def unique_words(find_most_common_words):
    print ("The number of unique words in the file is: " + str(len(set(w.lower() for w in open("source_text.text").read().split()))))
    # for w in open("source_text.text").read().split():
    #     if w in count:
    #         count[w] += 1
    #     else:
    #         count[w] = 1
    # for word,times in word_frequency.items():
    #     print(word,times)

unique_words("any")


# next few lines asks the user which word they want to look up in the file_name# It'll show them how many times that word has been repeted in the file
# file_name = input("What file would you like to open? ")
with open("source_text.text", "r") as f:
    words = f.read().split()
# Search for words in the splitted file
search_words = input("What word do you want to find? ").split(',')
search_words = [word.strip().lower() for word in search_words]
#print(search_words)
search_counts = dict.fromkeys(search_words, 0)

print ('\n... analyzing ... hold on ...')
for word in words:
    word = word.rstrip(",.").lower()
    if word in search_counts:
        search_counts[word] += 1

# print ('\nFrequency of word usage within', file_name + ":")
for word in search_words:
    print("   {:<20s} / {} occuers in the file.".format(word, search_counts[word]))



"""
Links I have Looked at:

https://stackoverflow.com/questions/41011521/count-frequency-of-word-in-text-file-in-python
https://stackoverflow.com/questions/9919604/efficiently-calculate-word-frequency-in-a-string
https://stackoverflow.com/questions/21873511/python-word-frequency-count-program
https://docs.python.org/3.7/library/collections.html
https://codereview.stackexchange.com/questions/176862/most-common-words-in-a-text-file-of-about-1-1-million-words
https://stackoverflow.com/questions/914382/how-can-i-count-unique-terms-in-a-plaintext-file-case-insensitively/930185#930185
https://stackoverflow.com/questions/21852066/counting-word-frequency-and-making-a-dictionary-from-it
https://github.com/woodward4422/tweet-generator/blob/master/histogram_list.py
https://stackoverflow.com/questions/43272360/python-word-frequency-in-a-file
https://stackoverflow.com/questions/47843707/count-frequency-of-item-in-a-list-of-tuples

"""
