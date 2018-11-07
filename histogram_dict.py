import sys
import collections

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
    print("   {:<20s} / {} occuers 5 times in the file.".format(word, search_counts[word]))
