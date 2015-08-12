# -*- coding:utf-8 -*-

# 012 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230738/

# 解答
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt

def write_col(fileName):
    f = open(fileName, 'r')
    col1f = open('col1.txt', 'w')
    col2f = open('col2.txt', 'w')

    for line in f:
        col1f.write(line.split('\t')[0] + '\n')
        col2f.write(line.split('\t')[1] + '\n')

if __name__ == '__main__':
    write_col('hightemp.txt')
