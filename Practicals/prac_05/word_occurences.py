text = input(str('Text: '))
text_list = text.split()
word_list = {}
output = []
max_length = 0
for word in text_list:
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1
for word in word_list:
    output.append([word, word_list[word]])
    if len(word) > max_length:
        max_length = len(word)
output.sort()
for word in output:
    print('{:<{}} : {}'.format(word[0], max_length, word[1]))

