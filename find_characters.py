word_list = ['hello','world','my','name','is','Anna']
char = 'y'
new_list = []

for word in word_list:
    if char in word:
        new_list.append(word)
print new_list