import streamlit as st
from PIL import Image
import requests
import json
import base64
from io import BytesIO
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Set the page configuration
st.set_page_config(page_title="Interactive Storybook", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

# CSS for background image and semi-transparent box (No Gradient)
background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: #f0f4ff; /* Solid fallback color */
}}

.custom-box {{
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
    color: #5481c4;
    line-height: 1.6;
}}
.custom-box h3 {{
    text-align: center;
    margin-top: 20px;
}}
.custom-box ul {{
    padding-left: 20px;
}}

/* Sidebar customization */
[data-testid="stSidebar"] {{
    background-color: #f0f4ff; /* Light blue solid color */
    color: #5481c4; /* Match the main page color */
    font-family: Arial, sans-serif;
    font-size: 18px; /* Adjust font size */
}}
[data-testid="stSidebar"] * {{
    color: #5481c4; /* Sidebar text color */
}}
[data-testid="stSidebar"] .stMarkdown {{
    text-align: center; /* Center text inside sidebar */
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# Function to add the logo to the top of the sidebar
def add_logo_to_sidebar_top(logo_path, width="250px"):
    with open(logo_path, "rb") as f:
        encoded_logo = base64.b64encode(f.read()).decode("utf-8")
    st.sidebar.markdown(
        f"""
        <style>
            [data-testid="stSidebar"]::before {{
                content: '';
                display: block;
                background-image: url("data:image/png;base64,{encoded_logo}");
                background-size: contain; /* Ensure the logo scales proportionally */
                background-repeat: no-repeat;
                background-position: top center;
                height: 250px; /* Increase height to fit the full logo */
                padding-top: 20px; /* Add space above the logo */
                margin-bottom: 20px; /* Add space below the logo */
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the top of the sidebar
add_logo_to_sidebar_top("pages/images/Updated_WonderS_logo.png", width="250px")

# ============

# S3 Client setup
s3client = boto3.client("s3")

# Decode base64 image
def image_decode(image_data_decode):
    image_data = base64.b64decode(image_data_decode)
    return Image.open(BytesIO(image_data))

def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string.decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None
        

# Fetch story data
@st.cache_data
def fetch_story_data(payload, _force_refresh=False):
    if _force_refresh:
        st.cache_data.clear()
    AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
    headers = {"Content-Type": "application/json"}

    response = requests.post(AWS_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["story_texts"], data["captions"], data["storyfiles"]
    return [], [], []

# Fetch and decode images
@st.cache_data
def fetch_and_decode_images(captions, _force_refresh=False):
    if _force_refresh:
        st.cache_data.clear()
    AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
    headers = {"Content-Type": "application/json"}
    decoded_images = []
    
    for index, caption in enumerate(captions):
        if index == 0:
            payload2 = {
                "api_Path": "getImage",
                "storyPrompt": caption,
                "previousPrompt": ''
            }
        else:
            payload2 = {
                "api_Path": "getImage",
                "storyPrompt": caption,
                "previousPrompt": captions[index - 1]
            }
            
        response = requests.post(AWS_API_URL, headers=headers, json=payload2)
        
        if response.status_code == 200:
            data = response.json()
            if data["image_data_decode1"] == "INVALID_PROMPT":
                invalid_image = "pages/images/invalid_img.jpg"
                decoded_images.append(encoded_image_to_base64(invalid_image))
            else:
                decoded_images.append(data["image_data_decode1"])
    return decoded_images

# Main app
def main():
    st.markdown("<h1 style='text-align: center; color: #5481c4;'>Welcome to WonderScribe</h1>", unsafe_allow_html=True)

    # Story form
    with st.form("form_key"):
        st.write("Craft personalized stories that bring adventure to life.")
        gender = st.selectbox("Your Gender", ["Male", "Female", "Non Binary", "Don't want to share"])
        main_character = st.text_input("Main Character Name", placeholder="Enter the name of the main character")
        audience = st.selectbox("Audience", ["Children", "Young Adult", "Adult", "Senior"])
        story_setting = st.selectbox("Story Setting", options=["Magical Kingdoms", "Underwater Kingdoms", "Pirate Ships", "Exotic locations", "Imaginary Worlds", "Digital words", "Other"])
        story_type = st.selectbox("Story Type", options=["Fantasy", "Fairy Tales", "Mythology", "Bedtime stories", "Adventure", "Mystery", "Love", "Horror"])
        story_theme = st.text_input("What would be the topic of the story?", placeholder="Enter brief idea of a story")
        moral_lesson = st.text_input("What would be the moral of this story?", placeholder="Enter a moral lesson from this story")
        story_length = st.selectbox("Story Length (in words)", options=["300", "400", "500","700"])
        story_lang = st.selectbox("Story Language", options=["English", "Spanish", "French", "German", "Mandarin", "Hindi", "Urdu", "Arabic", "Italian", "Vietnamese","Tagalog"])

        submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        st.write("Processing your story...")
        # Continue with story generation logic

if __name__ == "__main__":
    main()
