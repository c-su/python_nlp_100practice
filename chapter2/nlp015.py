# -*- coding:utf-8 -*-

# 015 末尾からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

# 解答
# tail -n 4 hightemp.txt (末尾から4行)

def tail_file(fileName, n):
    f = open(fileName, 'r')

    result = []
    for line in f:
        result.append(line)

    for i in range(1, n + 1):
        str = result[len(result) - i]
        print(str)

if __name__ == '__main__':
    n = int(raw_input())

    tail_file('hightemp.txt', n)
