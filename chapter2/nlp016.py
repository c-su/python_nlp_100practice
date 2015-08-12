# -*- coding:utf-8 -*-

# 016 ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230888/

# 解答
# split -l 10 hightemp.txt out

def split_file(fileName, n):
    f = open(fileName, 'r')

    result = []
    for line in f:
        result.append(line)

    countFile = 0
    minLine = -1
    while len(result) > minLine:
        out = open('out' + str(countFile) + '.txt', 'a')

        for i in range(n):
            minLine += 1

            if len(result) == minLine:
                out.close()
                return

            out.write(result[minLine])

        countFile += 1
        out.close()

if __name__ == '__main__':
    n = int(raw_input())

    split_file('hightemp.txt', n)
