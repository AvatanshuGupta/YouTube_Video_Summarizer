import streamlit as st
from src.responses import GettingResponse
from src.youtube_api import api
st.title("YouTube Video Summarizer and Analyzer")
link=st.text_input("Enter YouTube Video Link : ")
if link:
    api=api()
    transcript=api.fetch_transcript(link)
    thumbnail=api.fetch_thumbnail(link)
    st.image(thumbnail)

if st.button("Get Summary"):
    res=GettingResponse()
    response=res.get_response(transcript)
    st.text(response)
