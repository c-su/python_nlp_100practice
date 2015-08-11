# -*- coding:utf-8 -*-

# 000 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

def nlp000():
    str = 'stressed'

    list = []

    for char in str:
        # 指定した要素番号に挿入，元からのはずれる
        list.insert(0, char)

    print("".join(list))

def answer_nlp000():
    str = "stressed"
    # 3つめはステップ数
    # 指定するとステップ毎にとなる
    print(str[::-1])

if __name__ == '__main__':
    nlp000()
    answerNLP000()