import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5, max_tokens=500, streaming=False)

def get_llm_response(user_input: str, expert_type: str) -> str:
    if expert_type == "旅行":
        system_prompt = "あなたは旅行の専門家です。旅行に関する質問に親切かつ的確に答えてください。"
    elif expert_type == "健康":
        system_prompt = "あなたは健康の専門家です。健康や医療に関する質問に親切かつ的確に答えてください。"
    else:
        system_prompt = "You are a helpful assistant."
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input),
    ]
    result = llm(messages)
    return result.content

st.title("LLMチャットアプリ")

st.write("""
このアプリは、OpenAIの大規模言語モデル（LLM）を活用したチャットアプリです。  
下記の手順でご利用いただけます。

1. 「専門家の種類を選択してください」で「旅行」または「健康」を選択してください。
2. 「質問を入力してください」の欄に質問内容を入力してください。
3. 「送信」ボタンを押すと、選択した専門家になりきったAIが回答します。
""")

expert_type = st.radio(
    "専門家の種類を選択してください：",
    ("旅行", "健康")
)

user_input = st.text_input("質問を入力してください:")

if st.button("送信") and user_input:
    response = get_llm_response(user_input, expert_type)
    st.write("回答:")
    st.success(response)