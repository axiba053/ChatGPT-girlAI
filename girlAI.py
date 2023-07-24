import streamlit as st
from streamlit_chat import message
from PIL import Image
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

icon = Image.open('AIgirl.png')
st.set_page_config(page_title='AI女友', layout='wide', page_icon=icon)
st.header("AI女友👧")

OPENAI_API =st.text_input("API-KEY", type="password")#'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'

def generate_response(input_text):
    chat = ChatOpenAI(openai_api_key=OPENAI_API,temperature=0.5)
    return chat(input_text)

# initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="我希望你充当一个温柔女友，为我提供不同场景下的甜言蜜语。"
                              "请根据提供的状态生成一句适当的甜言蜜语，体现你的关心和温柔。"
                              "不需要提供背景解释，只需提供根据场景生成的甜言蜜语语录。")
    ]
# sidebar with user input
with st.sidebar:
    image = Image.open("AIgirl.png")
    st.image(image, caption="", width=150)
    st.markdown("---")
    st.markdown("# 简介")
    st.markdown("输入ChatGPT的API，即可免费、免注册、免魔法，直接使用！")
    st.markdown("大家好，这里是:blue[《三强的小屋》]！")
    st.markdown("欢迎在:green[B站]或者:green[微信视频号]关注，了解更多精彩内容!")
    image = Image.open("shipinhao.jpg")
    st.image(image, caption="", width=200)
user_input = st.text_input("请在这里输入: ",key="user_input")
# handle user input
if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Thinking..."):
        # response = chat(st.session_state.messages)
        response=generate_response(st.session_state.messages)
    st.session_state.messages.append(
        AIMessage(content=response.content))
# display message history
messages = st.session_state.get('messages', [])
for i, msg in enumerate(messages[1:]):
    if i % 2 == 0:
        message(msg.content, is_user=True, key=str(i) + '_user')
    else:
        message(msg.content, is_user=False, key=str(i) + '_ai')

