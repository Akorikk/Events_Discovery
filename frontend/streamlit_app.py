import streamlit as st
import requests


st.title("Heilbronn Event Discovery")


API_URL = "http://127.0.0.1:8000/events"


events = requests.get(API_URL).json()


for event in events:

    st.subheader(event["title"])

    st.write("📅 Date:", event["date"])

    st.write("📍 Location:", event["location"])

    st.write("🎭 Category:", event["description"])

    st.write("🔗 Source:", event["source_url"])

    st.markdown("---")