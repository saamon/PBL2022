import os
import openai
from dotenv import load_dotenv  # この行を追加

import streamlit as st
st.title('GPT-3 Demo')

# promptを入力するテキストボックスを作成
prompt = st.text_area('prompt')

# ボタンを作成
if st.button('Generate'):
    # .envファイルを読み込む
    load_dotenv()
    # .envファイルからAPIキーを取得
    openai.api_key = os.getenv('OPENAI_API_KEY')
    # GPT-3に渡すパラメータを設定
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # GPT-3の出力を表示
    st.write(response['choices'][0]['text'])

    # streamlit run test.py（ファイル名）で実行
    # Templete_outputのブランチ