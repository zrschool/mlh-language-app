# coding: utf8
zh_dict = {'过海':5, "看你":3}

def split_zh_words(sentence, zh_dict):
    sentence.replace(" ","") #remove whitespace
    if sentence == '':
        return []
    #Start at the first char, and see if it combines with the second char to make a word.
    #if so, test the first 3 chars, and if not, add that word to the list, and move on
    word = sentence[0:3]
    wordlen = 1
    #check if the first two characters are a word
    while len(sentence) >= wordlen*3+3 and (word + sentence[wordlen*3:wordlen*3+3]) in zh_dict:
        word += sentence[wordlen*3:wordlen*3+3]
        wordlen += 1
    #recursion: builds a list of the first word built so far
    print word
    return [word] + split_zh_words(sentence[3*wordlen:],zh_dict)

print split_zh_words('过海看你', zh_dict)
