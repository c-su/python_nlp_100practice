# -*- coding:utf-8 -*-

# 006 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

# 参考資料
# set関連資料
# http://python.civic-apps.com/set/

def nlp006():
    str1 = 'paraparaparadise'
    str2 = 'paragraph'

    X = set(char_bigram(str1))
    Y = set(char_bigram(str2))

    print(X)
    print(Y)
    print(X.union(Y))
    print(X.difference(Y))
    print(X.intersection(Y))

def char_bigram(sequence):
    sequence = "".join(sequence.split())
    n = 2
    return [sequence[k:k + n] for k in range(len(sequence) - n + 1)]

if __name__ == '__main__':
    nlp006()