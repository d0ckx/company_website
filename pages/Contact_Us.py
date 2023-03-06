
import streamlit as st
import pandas
from send_mail import send_mail

df = pandas.read_csv("topics.csv")
item_list = [row['topic'] for index, row in df.iterrows()]

with st.form("contact_form"):
    sender_mail = st.text_input("Your email address")
    sender_topic = st.selectbox("What topic do you want to discuss?",
                                options=item_list)
    sender_message = st.text_area("Message")
    message = f"""\
Subject: New email from {sender_mail}


From: {sender_mail}
Topic: {sender_topic}
{sender_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_mail(message)
        st.info("Your message was sent successfully!")