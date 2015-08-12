# -*- coding:utf-8 -*-

# 013 col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20131209/523511/

# 解答
# paste col1.txt col2.txt

def merge_files(fileName1, fileName2):
    f1 = open(fileName1, 'r')
    f2 = open(fileName2, 'r')
    f3 = open('result.txt', 'w')

    for line1, line2 in zip(f1, f2):
        f3.write(line1.replace('\n', ' ') + line2)

if __name__ == '__main__':
    merge_files('col1.txt', 'col2.txt')