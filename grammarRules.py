import sys, re

def reorder_noun1_of_noun2(line): 
    reordered = []
    reordered.insert(0, line[len(line)-1])
    i = len(line)-2
    prev_of = (-1, -1)
    while i >= 0: 
        if i > 0: 
            prev = line[i-1]
            curr = line[i]
            next = line[i+1]
            if curr[0] == 'of' and is_noun_not_proper(prev) and is_noun_not_proper(next): 
                if prev_of[0] == -1: # no ofs in a row
                    reordered = reordered[1:]
                    reordered.insert(0, prev)
                    reordered.insert(0, next)
                    prev_of = (0, 1)
                else: 
                    reordered.insert(prev_of[1]+1, prev)
                    prev_of = (0, prev_of[1]+1)
                i -= 1

            else: 
                reordered.insert(0, curr)
                prev_of = (-1, -1)
        else: 
            reordered.insert(0, line[i])
        i -= 1
    return reordered

def remove_be_before_verbs(line): 
    reordered = []
    index = 0
    while index < len(line): 
        curr = line[index]
        #print 'curr = ', curr
        if curr[0] == 'be' and index != len(line)-1: 
            next = line[index+1]
            if is_verb(next) is False: 
                reordered.append(curr)
        else: 
            reordered.append(curr)
        index += 1
    return reordered

def is_noun_not_proper(tup): 
    if tup[1] == 'NN' or tup[1] == 'NNS': 
        return True
    return False

def is_noun(tup): 
    if tup[1] == 'NN' or tup[1] == 'NNS' or tup[1] == 'NNP' or tup[1] == 'NNPS': 
        return True
    return False

def swap_nouns_adjectives(line): 
    reordered = line
    for i in range(1, len(reordered)): 
        curr = reordered[i]
        prev = reordered[i-1]
        if is_adjective(curr) and is_noun(prev): 
            reordered[i-1] = curr
            reordered[i] = prev
    return reordered


def is_verb(tup): 
    if tup[1] == 'VB' or tup[1] == 'VBD' or tup[1] == 'VBG' or tup[1] == 'VBN' or tup[1] == 'VBP' or tup[1] == 'VBZ': 
        return True
    return False

def is_adjective(tup): 
    return tup[1] == 'JJ'

def is_adverb(tup): 
    return tup[1] == 'RB'

def is_proper_noun(tup): 
    if tup[1] == 'NNP' or tup[1] == 'NNPS': 
        return True
    return False

def reorder_in_and_adverbs(line): 
    reordered = line
    in_index = -1
    adverbs_present = False
    in_list = []
    adverb_list = []
    i = 0
    while i < len(line):
        curr = line[i]
        if curr[0] == 'in': 
            in_index = i
            in_list.append(curr)

        else: 
            if is_adverb(curr): 
                adverb_list.append(curr)
                adverbs_present = True
            else: 
                if in_index != -1 and adverbs_present is False: 
                    in_list.append(curr)
                if adverbs_present is True and in_index != -1: 
                    adverbs_present = False
                    before = line[0:in_index]
                    after_index = in_index + len(in_list) + len(adverb_list)
                    after = line[after_index:]
                    line = before + adverb_list + in_list + after
                    adverb_list = []
                    in_list = []
                    in_index = -1

        i += 1

    return line

def remove_a_before_proper_nouns(line): 
    reordered = []
    index = 1
    reordered.append(line[0])
    while index < len(line)-1: 
        curr = line[index]
        prev = line[index-1]
        next = line[index+1]
        if curr[0] == 'at': 
            if is_proper_noun(next) is False:# or is_verb(prev) is False: 
                # commented out is_verb(prev) because the POS tag for prev is often wrong
                reordered.append(curr)
        else: 
            reordered.append(curr)
        index += 1

    reordered.append(line[len(line)-1])
    return reordered

def remove_article_before_proper_noun(line): 
    reordered = []
    index = 0
    while index < len(line): 
        curr = line[index]
        #print 'curr = ', curr
        if curr[1] == 'DT' and index != len(line)-1: 
            next = line[index+1]
            if is_proper_noun(next) is False: 
                reordered.append(curr)
        else: 
            reordered.append(curr)
        index += 1
    return reordered

def swap_verbs_personal_pronouns(line): 
    reordered = line
    for i in range(1, len(reordered)): 
        curr = reordered[i]
        prev = reordered[i-1]
        if is_verb(curr) and prev[1] == 'PRP': 
            reordered[i-1] = curr
            reordered[i] = prev
    return reordered

def fix_a_an(line): 
    reordered = line
    for i in range(0, len(reordered)): 
        curr = reordered[i]
        if curr[0] == 'a' and i < len(reordered)-1:
            next = reordered[i+1]
            if is_vowel(next[0][0]): 
                reordered[i] = ('an', 'DT')
        if curr[0] == 'an' and i < len(reordered)-1: 
            next = reordered[i+1]
            if is_vowel(next[0][0]) is False:
                reordered[i] = ('a', 'DT')
    return reordered

def is_vowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': 
        return True
    return False

def remove_consecutive_same_words(line): 
    prev_word = ''
    reordered = []
    reordered.append(line[0])
    for i in range(1, len(line)): 
        curr = line[i]
        prev = line[i-1]
        if curr[0] != prev[0]: 
            reordered.append(curr)
    return reordered

def switch_adverbs_and_verbs(line):
    reordered = []
    i = 0
    while i < len(line)-1:
        currTuple = line[i]
        currWord = currTuple[0]
        if is_verb(currTuple):
            nextTuple = line[i+1]
            nextWord = nextTuple[0]
            if is_adverb(nextTuple):
                print currWord + ' ' + nextWord
                reordered.append(nextTuple)
                reordered.append(currTuple)
                i += 1
            else: 
                reordered.append(currTuple)
        else:
            reordered.append(line[i])
        i += 1
    reordered.append(line[len(line)-1])
    return reordered


def switch_reflexive_verbs(line):
    reordered = []
    i = 0
    while i < len(line):
        currTuple = line[i]
        currWord = currTuple[0]
        if currTuple[1] == 'PRP':
            nextTuple = line[i+1]
            nextWord = nextTuple[0]
            if is_verb(nextTuple):
                print currWord + ' ' + nextWord
                reordered.append(nextTuple)
                reordered.append(currTuple)
                i += 1
        else:
            reordered.append(line[i])
        i += 1
    return reordered

def is_adverb(tup):
    currWordPOS = tup[1]
    if currWordPOS == 'RB' or currWordPOS == 'RBR' or currWordPOS == 'RBS':
        return True
    return False


