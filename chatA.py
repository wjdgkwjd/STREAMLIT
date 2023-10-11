import openai
import streamlit as st

openai.api_key = "5hsnInhTX3SCdRWIHtj1T3BlbkFJHChJcJnyW4OMbZcrg8Zl"

st.title('제돌이 챗')
#prompt = input("user: ")
with st.form("form"):
    user_input = st.text_input("user: ")
    submit = st.form_submit_button("Submit")
if submit and user_input:
    prompt = [{"role": "user","contact": user_input}]
    with st.spinner("Waiting for ChatGPT..."):
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )
    prompt = response["choices"][0]["message"]["content"]
    st.write(prompt)

#spinner 모양 바꾸기
#채팅창 두 줄로 만들기