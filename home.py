import streamlit as st

st.title("# 誰でもビジネスマン :sunglasses:")

# Webページの紹介を書く
st.write("このWebアプリは、GPT-3を用いて、あなたの経歴をもとに、ビジネス文章の作成をお手伝いします。")

# 3種類の機能についての説明を箇条書きで書く
st.markdown("### 3種類の機能")
st.markdown("- AIを用いて経歴からビジネス文章を作成 (1)")
st.markdown("- ビジネス文章の誤字訂正 (2)")
st.markdown("- テンプレートのビジネス文章を呼び出す (3)")

## 利用イメージを書く
st.markdown("### 利用イメージ")
st.markdown("- 志望動機、ガクチカ、自己PRの文章を作成できます")
st.markdown("- 自分の作成した文章の誤字訂正をできます")
st.markdown("- 就活に用いるテンプレートの文章を呼び出すことができます")

# 使い方を書く
st.markdown("### 使い方")
st.markdown("1. あなたの応募したい職種を入力してください")
st.markdown("2. あなたの簡単な経歴を入力してください")
st.markdown("3. 出力したい文章の雰囲気を選択してください")


# streamlit run home.pyで実行