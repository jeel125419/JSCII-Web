import streamlit as st
from JSCII import Encode, Decode

st.title("JSCII Encoder/Decoder")

mode = st.selectbox(
    "Choose Mode",
    ["Encode", "Decode"]
)

if mode == "Encode":
    user_text = st.text_area("Enter text")
    if st.button("Encode"):
        result = Encode(user_text)
        st.code(result)

if mode == "Decode":
    encoded_input = st.text_area("Enter JSCII code")
    if st.button("Decode"):
        text, yours = Decode(encoded_input)

        if yours:
            st.code(text)
        else:
            st.write("Invalid JSCII code")