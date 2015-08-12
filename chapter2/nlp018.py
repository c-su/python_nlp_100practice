# -*- coding:utf-8 -*-

# 018 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230887/

# 解答
# sort -k 3 hightemp.txt > hightemp_sorted.txt

def reverse_file(fileName):
    f = open(fileName, 'r')

    result = []
    for line in f:
        result.append(line.split("\t"))

    sorted_list = sorted(result, key=lambda temp: result[2], reverse=False)

    for item_list in sorted_list:
        for item in item_list:
            print item + '\t',
        print

if __name__ == '__main__':
    reverse_file('hightemp.txt')
