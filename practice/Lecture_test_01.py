words = 'one two three'.split()
for i in range(len(words)):
    words[i] = words[i].title()
text = ', '.join(words)
print(text)


