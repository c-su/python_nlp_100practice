# -*- coding:utf-8 -*-

# 008 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#    ・英小文字ならば(219 - 文字コード)の文字に置換
#    ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# 参考資料
# コード変換，文字変換
# http://python.civic-apps.com/char-ord/

def nlp008():
    result = cipher('This is a pen.')

    print(result)
    print(cipher(result))

def cipher(str):
    result = ''
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            result += chr(219 - ord(str[i]))
        else:
            result += str[i]
    return result

if __name__ == '__main__':
    nlp008()