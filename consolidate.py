dict_file = open('spanishDictionary.txt', 'r')
translated = set()
new_dict = open('newDict.txt', 'w')

for line in dict_file:
	span = line.split()[0]
	translated.add(span)

new_words = open('newWords.txt', 'r')
for line in new_words: 
	if line.strip() not in translated: 
		new_dict.write(line.strip() + '\n')



