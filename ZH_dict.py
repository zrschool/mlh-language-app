import collections

Entry = collections.namedtuple('Entry', ('pinyin', 'translation'))

class ZH_Dict:
    """holds the Chinese-Pinyin-English dictionary"""

    def __init__(self, file):
        self.zh_dict = self.load_zh_dict(file)
    
    #parses a line of the dictionary into (simplified, traditional, pinyin, translation)
    def _parse_entry(self, line) -> 'tuple':
        #example line
        #彩畫 彩画 [cai3 hua4] /color painting/
        parse = line.split('[')
        zh_chars = parse[0].split(' ')
        py_trn = parse[1].split(']')

        simp, trad = zh_chars[0], zh_chars[1]
        pinyin, transl = py_trn[0], py_trn[1].strip().strip('/')
    
        return (simp, trad, pinyin, transl)
    
    #reads the chinese dictionary, maps chinese chars to pinyin and definition
    def load_zh_dict(self, file) -> 'dict':
        zh_dict = {} #Chinese to pinyin and definition
        cedict = open(file, 'r')

        for line in cedict:
            info = self._parse_entry(line)

            zh_dict[info[0]] = Entry(info[2], info[3]) #stores pinyin and English translation
            zh_dict[info[1]] = Entry(info[2], info[3]) #again for traditional (TW) characters
        return zh_dict

    def pinyin(self, word):
        return self.zh_dict[word].pinyin

    def english(self, word):
        return self.zh_dict[word].translation

    def __contains__(self, key):
        return key in self.zh_dict
