# -*- coding:utf-8 -*-

# 003 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

def nlp003():
    str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print(str.split())

    word_count = []
    for item in str.split(' '):
        word_count.append(len(item))

    print(word_count)

if __name__ == '__main__':
    nlp003()