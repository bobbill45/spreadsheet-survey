import streamlit as st
import pandas as pd
import os 
import qrcode
from io import BytesIO

survey_url = "https://spreadsheet-survey-mx8thvk5lpz6r3aqkepmzk.streamlit.app"

#Generate QR code

qr = qrcode.QRCode(box_size=14, border=7)
qr.add_data(survey_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

buffer = BytesIO()
img.save(buffer, format="PNG")
buffer.seek(0)

st.title("Business spreadsheet cleaning survey")
st.image(buffer, caption="Scan me please")
st.write("---")

q1 = st.radio("What type of spreadsheet do you work with the most?", ["Customers", "Inventory","Vendors","Timecards", "Sale reports", "others"])
q2 = st.radio("How often do you receive messy or inconsistent speadsheets?", ["Daily", "Weekly", "monthly", "Rarely", "Constantly"])
q3 = st.radio("What are the problems do you see the most often?", ["Duplicates", "Wrong unit messurement","Missspellings", "Missing columns", "Wrong formats","Hidden Security theats"])
q4 = st.radio("What system do you import data into?", ["Quickbooks", "Xero", "POS systems", "Customer software","Not sure"])
q5 = st.radio("Would you use this tool that cleans and secures your spreadsheets automatically?", ["Yes", "Maybe", "Only if cheap", "No"])

    


if st.button("Submit"):
    data = {
        "Spreadsheet Type" : [q1],
        "Messy Frequency" : [q2],
        "Problems" : [", ".join(q3)],
        "Import system" : [q4],
        "Interest" : [q5]
    }
    
    df = pd.DataFrame(data)
    
    if os.path.exists("responses.csv"):
        df.to_csv("responses.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("responses.csv", index=False)
    
    st.success("Thank you for the feedback!! Your answers has been saved.") 
    
