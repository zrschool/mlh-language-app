import collections
from ZH_dict import ZH_Dict
import random

dict_file = 'txt/cedict_ts.u8'
pinyin_file = 'txt/all_pinyin.txt'

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

#returns a set of all words in a file
def word_set(filename) -> 'set':
    all_words = set()
    for line in open(filename):
        for word in line.split():
            all_words.add(word)
    return all_words

#returns an item that is a valid chinese word, AKA not punctuation from a list
def rand_zh(words:"list") -> "string":
    word = words[random.randint(0, len(words)-1)]
    while word not in zh_dict:
        word = words[random.randint(0, len(words)-1)]
    return word

#generates a number of possible choices for the pinyin, one of which is correct
def gen_choices(word:"string", count:"int", zh_dict:"ZH_Dict", pinyin_set:"set") -> "list":
    assert count >= 1
    choices = [zh_dict.pinyin(word)] #begin with the correct answer
    while len(choices) < count:
        answer = random.sample(pinyin_set, len(word)) #a random combination of pinyin
        for i in range(len(answer)): #append tones
            answer[i] += str(random.randint(1,4))
        choices.append(" ".join(answer))
    return choices

#from a list of chinese words, takes a word and generates a question
#returns a tuple in the form (chinese chars, correct pinyin, list of possible answers)
def gen_question(wordlist, answer_count, zh_dict, pinyin_set) -> "tuple":
    word = rand_zh(words)
    py = zh_dict.pinyin(word)
    choices = gen_choices(word, answer_count, zh_dict, pinyin_set)
    
    return (word, py, choices)

print("Loading dictionary...")
zh_dict = ZH_Dict(dict_file)
print("Dictionary Loaded.")
words = split_zh_words("贸易是自願的貨品或服務交換。貿易也被稱為商業。", zh_dict)
print(words)

pinyin_set = word_set(pinyin_file)

#generates a word and some incorrect choices for the multiple choice
print (gen_question(words, 3, zh_dict, pinyin_set))
    
    
    
    
    
