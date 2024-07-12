import os
os.environ['DISPLAY'] = ':0'

import streamlit as st
from pywhatkit import sendwhatmsg_instantly as sendwhatmsg
import pandas as pd
from datetime import date, datetime
import time

def send_messages(data):
    if 'Date' not in data.columns:
        data['Date'] = None
    if 'Time' not in data.columns:
        data['Time'] = None
    if 'Status' not in data.columns:
        data['Status'] = None

    today = date.today()
    today = today.strftime('%d %b %Y')

    for index, row in data.iterrows():
        if pd.isnull(row['Status']):
            message = f"""
Dear Customer,
🎉 End of Season Sale Alert! 🎉

Step up your style game with our exclusive Buy 1 Get 1 Free offer on selected footwear! 👠👡👢
Hurry, don't miss out on this fabulous deal!
Visit SOLES Commercial Street 
Shop now and double your fashion fun! 💃 

SOLES, Commercial Street
            """
        
            phone_no = "+91" + str(row['Phone number'])

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            sendwhatmsg(phone_no, message, tab_close=True, wait_time=10)

            print(message)
            print("---------------------------------------------------")

            data.at[index, 'Status'] = 'Done'
            data.at[index, 'Date'] = today
            data.at[index, 'Time'] = current_time

            time.sleep(1)

    st.success("All messages sent successfully!")
    return data

st.title("Bulk WhatsApp Message")

data = st.file_uploader("CSV file")
if data is not None:
    data = pd.read_csv(data)
    st.write(data)

button = st.button("Send", type="primary")
if button:
    send_messages(data)
    st.write("Updated Records")
    st.write(data)
