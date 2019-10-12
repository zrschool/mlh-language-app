import collections
from ZH_dict import ZH_Dict

filename = 'cedict_ts.u8'

#Split a Chinese sentences into its words and punctuation
def split_zh_words(sentence, zh_dict) -> 'list':
    sentence.replace(" ","") #remove whitespace
    if sentence == '':
        return []
    #Start at the first char, and see if it combines with the second char to make a word.
    #if so, test the first 3 chars, and if not, add that word to the list, and move on
    word = sentence[0]
    wordlen = 1
    #check if the first two characters are a word
    while len(sentence) > wordlen+1 and word + sentence[wordlen] in zh_dict:
        word += sentence[wordlen]
        wordlen += 1
    #recursion: builds a list of the first word built so far
    return [word] + split_zh_words(sentence[wordlen:],zh_dict)

#print("Loading dictionary...")
#zh_dict = ZH_Dict(filename)
#print("Dictionary Loaded.")
#print (split_zh_words("他不會說英文，德文就更加不用說了。", zh_dict))
    
    
    
