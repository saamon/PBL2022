#!/usr/bin/env python
# -*- coding: shift_jis -*-
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import subprocess

st.title("誰でもビジネスマン")
list_number = 0
list_data_before = []
list_data_aftar = []
sentence = ""

def main():
    ### SpradSheetsから読み込み ###
    get_data = DataLoad()
    list_data_before = get_data[0]
    list_data_aftar = get_data[1]

    ### セルデータの個数を取得 ###
    list_number = list_data_before.index(list_data_before[-1])

    ### text input ###
    sentence = st.text_area(label='文章入力欄', value='ここに変換したい文章を入れてください')

    ### 文章修正 ###
    sentence = TextConvert(list_data_before, list_data_aftar, list_number, sentence)

    ### text output ###
    st.write('出力欄\n\n', sentence)

def DataLoad():
    # お決まりの文句
    # 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    # ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
    credentials = Credentials.from_service_account_file(
        R"C:\Users\jouza\Downloads\macro-mender-370900-a3fd26f71ed1.json", scopes=scope)
    # OAuth2の資格情報を使用してGoogle APIにログイン。
    gc = gspread.authorize(credentials)
    # スプレッドシートIDを変数に格納する。
    SPREADSHEET_KEY = '1bI2obwUhSoJsm66YVTR481jYgOAFi7z5vVyvlr0hgUI'
    # スプレッドシート（ブック）を開く
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    # シートの一覧を取得する。（リスト形式）
    worksheets = workbook.worksheets()
    print(worksheets)
    # シートを開く
    worksheet = workbook.worksheet('シート1')

    ### セルデータ読み込み ###
    list_data_before = worksheet.col_values(2)
    list_data_aftar = worksheet.col_values(3)

    ### セルの先頭を削除 ###
    list_data_before.pop(0)
    list_data_aftar.pop(0)

    return list_data_before, list_data_aftar

def TextConvert(list_data_before, list_data_aftar, list_number, sentence):
    ### ここから先は未実装 ###
    ### ら抜き言葉のチェックはできても修正ができない(使用しているパッケージの仕様上) ###

    ### sentence save to txt file ###
    f = open(R'C:\Users\jouza\textlint-demo\sentence.txt', 'w')
    f.write(sentence)
    f.close()
    ### ら抜き言葉 ###
    ### 今現在、チェックのみ修正なし ###
    subprocess.run(["npx", "textlint", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)
    subprocess.Popen(["npx", "textlint", "--fix", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)

    ### text convert ###
    ### セルデータの個数分カウンタを回して ###
    ### セルリストの変換前が含まれてて　かつ　変換後が含まれていなければ　置換　 ###
    for count_list in range(list_number+1):
        if list_data_aftar[count_list] not in sentence and list_data_before[count_list] in sentence:
            sentence = sentence.replace(list_data_before[count_list], list_data_aftar[count_list])
    return sentence

if __name__ == '__main__':
    main()