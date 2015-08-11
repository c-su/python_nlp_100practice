# -*- coding:utf-8 -*-

# 009 Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading
# : the phenomenal power of the human mind."）を与え，その実行結果を確認せよ．

# 参考資料
# http://stackoverflow.com/questions/2668312/shuffle-string-in-python
# http://python.civic-apps.com/string-split-join/

from collections import Counter
import random

def typoglycemia(str):

    list = str.split()

    result = []
    for item in list:
        if len(item) > 4:
            tmp = item[1:-1]
            s = ''.join(random.sample(tmp, len(tmp)))
            result.append(item[0] + s + item[-1])
        else:
            result.append(item)

    print ' '.join(result)


if __name__ == '__main__':
    typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
