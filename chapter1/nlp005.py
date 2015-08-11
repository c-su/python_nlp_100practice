# -*- coding:utf-8 -*-

# 005 n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# 参考資料
# N-gram
# http://gihyo.jp/dev/serial/01/make-findspot/0005
#
# コード
# http://yu-write.blogspot.jp/2013/11/python-n-gram.html
# http://blog.livedoor.jp/yawamen/archives/51513695.html

def nlp005():
    str = 'I am an NLPer'
    word_bigram(str)
    answer_word_bigram(str)
    char_bigram(str)


def word_bigram(sequence):
    sequence = sequence.split()

    results = []
    n = 2

    for i in xrange(len(sequence) - n + 1):
        results.append(sequence[i:i + n])

    print(results)

def char_bigram(sequence):
    sequence = "".join(sequence.split())
    n = 2
    print [sequence[k:k + n] for k in range(len(sequence) - n + 1)]

def answer_word_bigram(sequence):
    sequence = sequence.split()
    n = 2
    print [sequence[k:k+n] for k in range(len(sequence) - n + 1)]


if __name__ == '__main__':
    nlp005()