import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="Asad Pro AI", layout="centered")

# 2. Simple Password Protection (کوئی فائل نہیں، کوئی پیچیدگی نہیں)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 Login to Pro AI")
    password = st.text_input("Enter Password", type="password")
    if st.button("Unlock"):
        if password == "12345":  # آپ یہاں اپنا کوئی بھی پاسورڈ رکھ سکتے ہیں
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Wrong Password!")
else:
    # 3. Gemini Pro AI Chat
    st.title("🤖 Live Gemini AI")
    
    # یہاں اپنی API Key ڈالیں (صرف ایک بار)
    api_key = "AQ.Ab8RN6J6yT3ZmKpblIm8xRtOTNuDGZ9nRRzoqGGot8oE10Eg4g" # اپنی اصلی API Key یہاں پیسٹ کریں
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Link den, main HTML bana deta hoon..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(f"Create professional eBay HTML for: {prompt}")
            # st.code میں خود بخود 'Copy' بٹن آتا ہے
            st.code(response.text, language='html')
            st.session_state.messages.append({"role": "assistant", "content": response.text})
