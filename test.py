import os
import openai
from dotenv import load_dotenv  # この行を追加

load_dotenv()  # この行を追加（環境変数を読み込む）

openai.api_key = os.getenv("OPENAI_API_KEY")  # この行を追加

# 単語から文章を生成する
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="ゼミ 遅刻 謝罪",
    temperature=0.5,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 結果を表示する
print(response["choices"][0]["text"])

# 結果
# ご迷惑をおかけして申し訳ございません。予定より遅れて参加できなかったことをお詫び申し上げます。今後は時間厳守して参加できるよう努力します。