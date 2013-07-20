import nltk
import grammarRules

translatedText = open('translated.txt', 'r')
tagList = []
for line in translatedText:
	currLine = nltk.word_tokenize(line)
	tags = nltk.pos_tag(currLine)
	print tags
	tagList.append(tags)


reordered_file = open('reordered.txt', 'w')
for line in tagList: 
	transformed = line
	
	transformed = grammarRules.reorder_noun1_of_noun2(transformed)
	transformed = grammarRules.remove_be_before_verbs(transformed)
	transformed = grammarRules.swap_nouns_adjectives(transformed)
	transformed = grammarRules.reorder_in_and_adverbs(transformed)
	transformed = grammarRules.remove_a_before_proper_nouns(transformed)
	transformed = grammarRules.remove_article_before_proper_noun(transformed)
	transformed = grammarRules.fix_a_an(transformed)
	transformed = grammarRules.remove_consecutive_same_words(transformed)	
	transformed = grammarRules.switch_adverbs_and_verbs(transformed)
	transformed = grammarRules.switch_reflexive_verbs(transformed)

	for t in transformed: 
		reordered_file.write(t[0] + ' ')
	reordered_file.write('\n')
