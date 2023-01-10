import os
import openai
from dotenv import load_dotenv  # この行を追加
import streamlit as st

st.title("自己PRジェネレーター")

with st.form("my_form"):
    # 応募する職種を入力するテキストボックスを作成
    job_type = st.text_input("応募する職種を入力してください")

    # 経験を簡単に入力するテキストボックスを作成
    experience = st.text_area("経験を簡単に入力してください")

    # ユーザーが出力する文章の雰囲気を選択できるセレクトボックスを作成
    # 雰囲気はtemperatureで調整する
    mood = ["大胆", "丁寧", "カジュアル"]
    selected_mood = st.selectbox("出力する文章の雰囲気を選択してください", mood)

    # ボタンを作成
    submit_button = st.form_submit_button("Generate")

    if submit_button:
        # .envファイルを読み込む
        load_dotenv()
        # .envファイルからAPIキーを取得
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # GPT-3に渡すパラメータを設定
        prompt = f"応募する職種: {job_type}\n経験: {experience}\n雰囲気: {selected_mood}+自己PR文を生成してください\n\n自己PR文:\n"
        if selected_mood == "大胆":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            # 文章を出力する
            st.write(response["choices"][0]["text"])
        # もし、丁寧と選択されたらtemperatureを0.1に設定
        elif selected_mood == "丁寧":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.1,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            # 文章を出力
            st.write(response["choices"][0]["text"])
        # もし、カジュアルと選択されたらtemperatureを0.3に設定
        else:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.3,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            # 文章を出力
            st.write(response["choices"][0]["text"])
# このコードを実行するには、以下のコマンドを実行してください。

# streamlit run TextGeneration/self_appeal.py（ファイル名）で実行
