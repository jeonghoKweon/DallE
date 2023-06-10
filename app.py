import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form") : 
    User_input = st.text_input("prompt")
    size = st.selectbox("size", ["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("submit")

if submit and User_input:
    gpt_prompt = [{
        "role" : "system",
        "content" : "Imagine the detail appeareance of the input. \
                    response it shortly around 20 words"
    }]

    gpt_prompt.append({
        "role" : "user",
        "content" : User_input
    })

    with st.spinner("waiting for ChatGPT..."):

        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = gpt_prompt
            )
        
        prompt = gpt_response["choices"][0]["message"]["content"]
        st.write(prompt)

    with st.spinner("waiting for Dalle..."):
        dalle_response = openai.Image.create(
            prompt = prompt,
            size = size
        )

        st.image(dalle_response["data"][0]["url"])

