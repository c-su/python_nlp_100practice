# -*- coding:utf-8 -*-

# 014 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# 解答
# head -n 4 hightemp.txt (先頭から4行)

def head_file(fileName, n):
    f = open(fileName, 'r')

    for i in range(n):
        line = f.readline()
        print(line)


if __name__ == '__main__':
    n = int(raw_input())

    head_file('hightemp.txt', n)