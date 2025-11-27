
import streamlit as st
from datetime import datetime
import google.genai as genai

client = genai.Client(api_key="AIzaSyBk1pQOyGOvbLnqhtQBGTvt-4W1MVBW_sU")


st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("Gemini Chatbot")
st.write("Welcome!.......")
user_message = st.text_input("Your Message", placeholder="Say something...")


if user_message:

    
    bot_response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_message
    )


    st.subheader("Bot Response:")
    st.write(bot_response.text)

 
    st.caption(f"Replied on: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")