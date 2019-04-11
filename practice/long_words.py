text = "This is a sentence"
words = text.split()
print(words)
long_words = [word for word in words if len(word) > 3]
print(long_words)
