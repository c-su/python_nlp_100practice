# -*- coding:utf-8 -*-

# 011 タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# 参考資料
# http://itpro.nikkeibp.co.jp/article/COLUMN/20131007/509542/

# 解答
# expand hightemp.txt > hightemp-space.txt

def replace_tab_to_space(fileName):
    f = open(fileName, 'r')
    wf = open('result.txt', 'w')

    for line in f:
        str = line.replace('\t', ' ')
        wf.write(str)

    f.close()
    wf.close()

if __name__ == '__main__':
    replace_tab_to_space('hightemp.txt')
