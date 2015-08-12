# -*- coding:utf-8 -*-

# 019 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230738/
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230887/
# http://python.rdy.jp/wiki.cgi?page=japaneseCharset
# http://qiita.com/hatchinee/items/a904c1f8d732a4686c9d

# 解答
# cut -c 1 hightemp.txt > hightemp_first.txt

from collections import Counter

def calc_freqence_char_in_file(fileName):
    f = open(fileName, 'r')

    result = []
    for item in f:
        result.append(item.split('\t')[0])

    count_words = Counter(result)

    for word, cnt in count_words.most_common():
        print word


if __name__ == '__main__' :
    calc_freqence_char_in_file('hightemp.txt')
