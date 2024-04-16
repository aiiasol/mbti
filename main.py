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






# Advertisement iframe
advertisement_iframe = """
<iframe src="https://ads-partners.coupang.com/widgets.html?id=769781&template=carousel&trackingCode=AF7086871&subId=&width=680&height=140&tsource=" width="100%" height="140" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
"""

st.markdown(advertisement_iframe, unsafe_allow_html=True)
