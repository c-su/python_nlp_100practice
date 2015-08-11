# -*- coding:utf-8 -*-

# 004 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def nlp004():
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = str.split()
    one_word_number = [0, 4, 5, 6, 7, 8, 14, 15, 18]

    dict = {}
    for i in range(len(words)):
        if i in one_word_number:
            dict[words[i][:1]] = i + 1
        else:
            dict[words[i][:2]] = i + 1

    print dict

def answer_nlp004():
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    str = str.replace(".", "")
    words = str.split()
    words_index = {}

    # enumerate を使用することで，インデックス付きループができる
    for i, word in enumerate(words):
        n = i + 1
        if n in [0, 5, 6, 7, 8, 14, 15, 19]:
            words_index[word[:1]] = n
        else:
            words_index[word[:2]] = n

    print(words_index)

if __name__ == '__main__':
    nlp004()
    answer_nlp004()
