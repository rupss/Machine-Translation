Class: CS124 (From Languages to Information), Winter 2013
Teammate: Jujhaar Singh

Translates SpanishText.txt from Spanish to English, using the definitions in spanishDictionary.txt (1 to 1 relationship).
The challenge was to implement a set of grammar rules that would improve the direct word-for-word translation. 

Usage: 

Step 1) python translate.py -- writes the file "translated.txt" that replaces each word in SpanishText.txt with its corresponding English word from spanishDictionary.txt. We put together the dictionary by hand, putting the first translation only. 

Step 2) python tag.py -- reads from translated.txt and uses the grammar rules from grammarRules.py to reorder the translated text. The final translated text is put into reordered.txt. 

Other Files: 
 
- SpanishText.txt: contains the Spanish text to translate
- spanishDictionary.txt: contains the Spanish dictionary
- translated.txt: generated after running translate.py
- PA7Report-MachineTranslation.pdf: our final report
