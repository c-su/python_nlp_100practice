# -*- coding:utf-8 -*-

# 010 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20060228/230994/

# 解答
# wc -l hightemp.txt

def count_file_line(fileName):
    count = 0

    f = open(fileName, 'r')
    for line in f:
        count += 1

    print count

    f.close()

if __name__ == '__main__':
    count_file_line('hightemp.txt')