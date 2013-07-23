import re

def main(): 
    spanishFile = open('SpanishText.txt', 'r')
    translated = open('translated.txt', 'w')
    dictionary = dict()
    dictFile = open('spanishDictionary.txt', 'r')

    for line in dictFile.readlines(): 
        print line
        words = line.split()
        span = words[0]
        eng = ''
        for i in range(1, len(words)): 
            eng += words[i] + ' '
        eng = eng.strip()
        dictionary[span] = eng

    for line in spanishFile.readlines(): 
        for word in line.split(): 
            w = word.lower()
            w = re.sub('[.?!",]', '', w)
            print w
            translated.write(dictionary[w] + ' ')
        translated.write('\n')

if __name__ == "__main__":
    main()



