
with open("source_text.text", "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
