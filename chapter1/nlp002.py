# -*- coding:utf-8 -*-

# 002 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def nlp002():
    str1 = u'パトカー'
    str2 = u'タクシー'
    joinStr = ''

    for i in range(len(str1)):
        joinStr += str1[i] + str2[i]

    print(joinStr)

def answer_nlp002():
    str1 = u'パトカー'
    str2 = u'タクシー'
    joinStr = ''

    # 複数のシーケンスに同時アクセス可能になる zip 関数
    for char1, char2 in zip(str1, str2):
        joinStr += char1 + char2

    print(joinStr)

def answer2_nlp002():
    # ループ毎の連結はメモリ消費大
    # リスト作ってからjoinが良し
    str1 = u'パトカー'
    str2 = u'タクシー'
    print(''.join([char1 + char2 for char1, char2 in zip(str1, str2)]))

if __name__ == '__main__':
    nlp002()
    answer_nlp002()
    answer2_nlp002()

















