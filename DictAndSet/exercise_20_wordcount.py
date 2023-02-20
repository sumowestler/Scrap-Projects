word_count = {}

text = "Later in the course, you'll see how to use the collections Counter class."

for letter in sorted(text.casefold()):
    if letter not in word_count and str(letter).isalpha():
        word_count.setdefault(str(letter), 1)
    elif letter in word_count:
        word_count[str(letter)] += 1
for character, count in word_count.items():
    print(character, count, sep=":")
