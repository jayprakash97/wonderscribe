import streamlit as st

import streamlit as st
from PIL import Image
import requests
import json
import base64
import re
from io import BytesIO
from PIL import Image
import requests
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

st.set_page_config(page_title="Contact", page_icon="👩‍🏫", layout="wide")

# Custom CSS to apply the background gradient and create a box
page_bg = """
<style>
/* Apply background gradient to the main container */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #8c52ff, #5ce1e6);
    background-attachment: fixed;
}

/* Optional: Adjust text color and other styles */
[data-testid="stAppViewContainer"] .stMarkdown {
    color: white;  /* Adjust text color for contrast */
}

/* Style for the content box */
.custom-box {
    background-color: #eaf1ff; /* Light background color for the box */
    border-radius: 10px; /* Rounded corners */
    padding: 20px; /* Spacing inside the box */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for a raised effect */
    color: black; /* Text color inside the box */
    margin-top: 20px; /* Space above the box */
}

/* Position the logo in the top-left corner */
img[alt="WonderScribeLogo"] {
    position: absolute;
    top: 40px;
    left: 40px;
    width: 150px; /* Adjust width if needed */
    z-index: 10;
}

/* Add padding to avoid overlap with the content */
[data-testid="stAppViewContainer"] {
    padding-top: 80px; /* Add padding to avoid logo overlapping */
}
</style>
"""
# Apply the custom CSS
st.markdown(page_bg, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Style for the sidebar content */
    [data-testid="stSidebarContent"] {
        background-color: #7dd8ff; /*#7dd8ff; Sidebar background color */
        
    }
    /* Set color for all text inside the sidebar */
    [data-testid="stSidebar"] * {
        color: #8c52ff !important;  /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("pages/images/WonderScribeLogo.png", width=150)

st.title("Contact with WonderScribe Team")

with st.form("form_key"):
    Department = st.selectbox("Department", options=["Sales", "Human Resources", "Information Technology", "Public Relation", "Complaince", "Marketing", "Data Engineering", "Data Science", "Data Analytics"])
    Full_name = st.text_input("Enter your full name. (First Name, Middle Name, Last Name)")
    Company = st.text_input("Enter your Company Name")
    Country = st.text_input("Enter your Country Name")
    State = st.text_input("Enter your State or Province Name")
    email = st.text_input("Enter your email address")
    phone = st.text_input("Enter your phone# (country code, city code, and local phone number)")
    question = st.text_area("Question or Comments")
    submit_btn = st.form_submit_button("Submit")

