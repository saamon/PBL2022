#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import sqlite3
import csv
import subprocess

st.title("誰でもビジネスマン")
list_number = 0
list_data_before = []
list_data_aftar = []
sentence = ""

def main():
    ### DataBaseから読み込み ###
    get_data = DataBaseAccess()
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

# データベースを使用します
def DataBaseAccess():
    # dbを作成し、接続（すでに存在する場合は接続のみ）
    conn = sqlite3.connect("gojiteisei.db")
    cur = conn.cursor()
    create_test = "CREATE TABLE IF NOT EXISTS test (beforeword TEXT, aftarword TEXT)"
    cur.execute(create_test)
    # load csv
    open_csv = open("businessbunsyo.csv", encoding="utf-8")
    read_csv = csv.reader(open_csv)
    # csvデータをexecutemany()でINSERTする
    # next_row = next(read_csv)
    rows = []
    for row in read_csv:
        rows.append(row)

    cur.executemany("INSERT INTO test (beforeword, aftarword) VALUES (?, ?)", rows)
    # テーブルの変更内容保存
    conn.commit()
    # close csv
    open_csv.close()
    # testテーブルの確認
    select_before = "SELECT beforeword FROM test"
    cur = conn.cursor()
    cur.execute(select_before)
    for i in cur:
        list_data_before.append(str(i[0]))
    # list_data_before

    select_aftar = "SELECT  aftarword FROM test"
    cur = conn.cursor()
    cur.execute(select_aftar)
    for i in cur:
        list_data_aftar.append(str(i[0]))
    # list_data_aftar

    # end db
    conn.close

    return list_data_before, list_data_aftar

def TextConvert(list_data_before, list_data_aftar, list_number, sentence):
    ### ここから先は未実装 ###
    ### ら抜き言葉のチェックはできても修正ができない(使用しているパッケージの仕様上) ###

    ### sentence save to txt file ###
    f = open(R'C:\Users\jouza\textlint-demo\sentence.txt', 'w', encoding='utf-8')
    f.write(sentence)
    f.close()
    ### ら抜き言葉 ###
    ### 今現在、チェックのみ修正なし ###
    # subprocess.run(["npx", "textlint", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)
    # subprocess.Popen(["npx", "textlint", "--fix", R"C:\Users\jouza\textlint-demo\sentence.txt", R"C:\Users\jouza\textlint-demo\.textlintrc"], shell=True)

    ### text convert ###
    ### セルデータの個数分カウンタを回して ###
    ### セルリストの変換前が含まれてて　かつ　変換後が含まれていなければ　置換　 ###
    for count_list in range(list_number+1):
        if list_data_aftar[count_list] not in sentence and list_data_before[count_list] in sentence:
            sentence = sentence.replace(list_data_before[count_list], list_data_aftar[count_list])
    return sentence

if __name__ == '__main__':
    main()