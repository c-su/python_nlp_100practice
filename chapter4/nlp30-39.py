# coding: utf-8

import sys
import matplotlib.pyplot as plt
from matplotlib import font_manager

def nlp30():
    textfile = open('./neko.txt.mecab')

    # 問題30
    words = []
    for line in textfile:
        line = line.rstrip()
        line = line.replace('\t', ',')

        if line == 'EOS':
            continue

        word = line.split(',')
        surface = word[0] # 表層形
        base = word[7] # 基本形
        pos = word[1] # 品詞
        pos1 = word[2] #品詞細分類1

        words.append({
            'surface': surface,
            'base': base,
            'pos': pos,
            'pos1': pos1
        })

    return words

def nlp31(words):
    for word in words:
        if word['pos'] == '動詞':
            print(word['surface'])

def nlp32(words):
    for word in words:
        if word['pos'] == '動詞':
            print(word['base'])

def nlp33(words):
    for word in words:
        if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
            print(word['surface'])

def nlp34(words):
    for i in range(len(words)):

        if i - 1 < 0 and i + 1 >= len(words):
            continue

        if words[i - 1]['pos'] == '名詞' and \
        words[i]['surface'] == 'の' and \
        words[i + 1]['pos'] == '名詞':
            print(words[i - 1]['surface'] + words[i]['surface'] + words[i + 1]['surface'])

def nlp35(words):

    max_num = 2
    now_num = 0
    res = ''
    for i in range(len(words)):

        if i + 1 >= len(words):
            continue

        if words[i]['pos'] == '名詞' and words[i + 1]['pos'] == '名詞':
            text = words[i]['surface']
            now_num = 1

            for j in range(i + 1, len(words)):
                if not words[j]['pos'] == '名詞':
                    if now_num > max_num:
                        max_num = now_num
                        res = text
                    break
                now_num += 1
                text += words[j]['surface']

    print(res)

def nlp36(words):
    # 語彙頻度
    freq = {}
    for word in words:
        if not word['base'] in freq:
            freq[word['base']] = 1
        else:
            freq[word['base']] += 1

    for word in sorted(freq, key=freq.get, reverse=True):
        print(word + '\t' + str(freq[word]))

def nlp37(words):
    # 語彙頻度
    freq = {}
    for word in words:
        if word['pos'] == '動詞':
            if not word['base'] in freq:
                freq[word['base']] = 1
            else:
                freq[word['base']] += 1

    # 上位10語の抽出
    count = 1
    x = []
    y = []
    label = []
    for word in sorted(freq, key=freq.get, reverse=True):
        if count > 10:
            break

        x.append(count)
        y.append(freq[word])
        label.append(unicode(word, 'utf-8'))
        count += 1

        print(word + '\t' + str(freq[word]))

    # グラフ描画
    # http://yubais.net/doc/matplotlib/bar.html
    fontprop = font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

    plt.legend(fp=fontprop)
    plt.bar(x, y, align='center')
    plt.xticks(x, label)
    plt.show()

def nlp38(words):
    # 語彙頻度
    freq = {}
    for word in words:
        if word['pos'] == '動詞':
            if not word['base'] in freq:
                freq[word['base']] = 1
            else:
                freq[word['base']] += 1

    count = 1
    x = []
    for word in sorted(freq, key=freq.get, reverse=True):
        if count > 100:
            break

        x.append(freq[word])
        count += 1

        print(word + '\t' + str(freq[word]))


    plt.hist(x, bins=50)
    plt.xlabel(u'出現頻度')
    plt.ylabel(u'種類数')
    plt.show()

def nlp39(words):
    # Zipfの法則：https://ja.wikipedia.org/wiki/%E3%82%B8%E3%83%83%E3%83%97%E3%81%AE%E6%B3%95%E5%89%87

    # 語彙頻度
    freq = {}
    for word in words:
        if word['pos'] == '動詞':
            if not word['base'] in freq:
                freq[word['base']] = 1
            else:
                freq[word['base']] += 1

    count = 1
    x = []
    y = []
    for word in sorted(freq, key=freq.get, reverse=True):
        x.append(count)
        y.append(freq[word])
        count += 1

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(x, y, 'o')
    plt.show()

def main():
    words = nlp30()

    # nlp31(words) # 問題31
    # nlp32(words) # 問題32
    # nlp33(words) # 問題33
    # nlp34(words) # 問題34
    # nlp35(words) # 問題35
    # nlp36(words) # 問題36
    # nlp37(words) # 問題37
    # nlp38(words) # 問題38
    nlp39(words) # 問題39



if __name__ == '__main__':
    main()
