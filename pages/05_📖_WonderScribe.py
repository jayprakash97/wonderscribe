

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
#background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"
#background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk2_page_1.jpg"
# CSS for setting the background
background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    filter: opacity(0.8);
    background-color: rgba(255, 255, 255, 0.8);
}}
</style>
"""

# Sidebar CSS
sidebar_css = """
<style>
[data-testid="stSidebar"] {
    #background-color: #7dd8ff;
    border-right: 2px solid #bfa989;
}

[data-testid="stSidebar"] h1 {
    color: #4e342e;
    font-size: 1.5em;
    font-family: 'Merriweather', serif;
    font-weight: bold;
}

[data-testid="stSidebar"] button {
    background-color: #d4c1a7;
    border-radius: 10px;
    border: 2px solid #bfa989;
    padding: 10px;
    font-size: 1.2em;
    color: #4e342e;
    margin-bottom: 15px;
}

[data-testid="stSidebar"] button:hover {
    background-color: #e0d3b8;
    color: #4e342e;
}
</style>
"""

# Apply CSS
st.markdown(background_css, unsafe_allow_html=True)
st.markdown(sidebar_css, unsafe_allow_html=True)

# S3 Client setup
s3client = boto3.client("s3")

# Decode base64 image
def image_decode(image_data_decode):
    image_data = base64.b64decode(image_data_decode)
    return Image.open(BytesIO(image_data))

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
        payload = {
            "api_Path": "getImage",
            "storyPrompt": caption,
            "previousPrompt": captions[index - 1] if index > 0 else "",
        }
        response = requests.post(AWS_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            decoded_images.append(data["image_data_decode1"])
    return decoded_images

# Main app
def main():
    st.title("📖 Welcome to WonderScribe!")
    st.write("Craft personalized stories that bring adventure to life.")

    with st.form("form_key"):
        gender = st.selectbox("Your Gender", ["Male", "Female", "Non Binary", "Don't want to share"])
        main_character = st.text_input("Main Character Name", placeholder="Enter the name of the main character")
        audience = st.selectbox("Audience", ["Children", "Young Adult", "Adult", "Senior"])
        story_setting = st.selectbox(
            "Story Setting", 
            ["Magical Kingdoms", "Underwater Kingdoms", "Pirate Ships", "Imaginary Worlds", "Other"]
        )
        story_type = st.selectbox("Story Type", ["Fantasy", "Fairy Tales", "Adventure", "Mystery", "Love"])
        story_theme = st.text_input("Story Theme", placeholder="Enter the theme of your story")
        moral_lesson = st.text_input("Moral Lesson", placeholder="Enter a moral lesson")
        story_length = st.selectbox("Story Length (words)", ["300", "400", "500"])
        story_lang = st.selectbox(
            "Story Language", 
            ["English", "Spanish", "French", "German", "Mandarin"]
        )

        submit_btn = st.form_submit_button("Generate Story")

    if submit_btn:
        # Validate inputs
        errors = []
        if not main_character or len(main_character) < 2:
            errors.append("Main character name must be at least 2 characters.")
        if not story_theme or len(story_theme) < 10:
            errors.append("Story theme must be at least 10 characters.")
        if errors:
            for error in errors:
                st.error(error)
            st.stop()

        # Create payload
        payload = {
            "api_Path": "getStory",
            "audience": audience,
            "story_type": story_type,
            "main_character": main_character,
            "story_theme": story_theme,
            "moral_lesson": moral_lesson,
            "setting": story_setting,
            "word_count": story_length,
            "story_lang": story_lang,
        }

        # Fetch data
        story_texts, captions, storyfiles = fetch_story_data(payload)
        decoded_images = fetch_and_decode_images(captions)

        # Display story
        for idx, text in enumerate(story_texts):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"### Page {idx + 1}")
                st.markdown(f"<div>{text}</div>", unsafe_allow_html=True)
            with col2:
                st.image(image_decode(decoded_images[idx]), use_column_width=True)

if __name__ == "__main__":
    main()
