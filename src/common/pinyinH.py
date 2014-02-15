#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self, dict_file=''):
        self.word_dict = {}
        if dict_file == "":
            dict_file = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "word.data"
            )
        self.dict_file = dict_file

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)

            word = self.word_dict.get(key, char).split()[0][:-1].lower()
            if not word:
                word = self.word_dict.get(key, char).split()[0]
            result.append(word)

        return result

    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)


class PinyinH:
    ins = None

    @staticmethod
    def loads(words):
        if PinyinH.ins is None:
            PinyinH.ins = PinYin()
            PinyinH.ins.load_word()
        return "".join(PinyinH.ins.hanzi2pinyin(string=words))

if __name__ == "__main__":
    string = u"钓鱼岛是中国的111aaa"
    print(PinyinH.loads(string))
