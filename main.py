# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

st.title('MBTI별 오늘의 운세')

content = st.text_input('자신의 MBTI를 넣어주세요 ')

if st.button('오늘의 운세보기'):
    with st.spinner('운세 보는 중...'):
        result = llm.predict(content + "의 오늘의 운세를 봐 줘")
        st.write(result)
