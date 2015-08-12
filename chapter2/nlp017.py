# -*- coding:utf-8 -*-

# 017 １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230887/
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230918/

# 解答
# sort col1.txt > col1_sorted.txt
# uniq col1_sorted.txt > col1_uniq.txt


def uniq_file(fileName):
    f = open(fileName, 'r')

    result = []
    for line in f:
        result.append(line.split("\t")[0])

    uniq_list = set(result)

    for item in uniq_list:
        print(item)

if __name__ == '__main__':
    uniq_file('hightemp.txt')
