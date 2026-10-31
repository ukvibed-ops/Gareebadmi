import streamlit as st

st.title("5 Min Video Maker")

topic = st.text_input("Topic likho")

min = st.slider("Minute", 1, 5, 5)

if st.button("Video Banao"):
    st.success("Video Ready!")
    st.write(topic)
    st.balloons()
