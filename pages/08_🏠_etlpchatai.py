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
            # Read the binary data and encode to base64
            encoded_string = base64.b64encode(image_file.read())
        
            #convert bytes to string for easier handling
            return encoded_string.decode('utf-8')
        
    except exception as e:
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
def fetch_and_decode_images(payload, captions, _force_refresh=False):
    if _force_refresh:
        st.cache_data.clear()
    AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
    headers = {"Content-Type": "application/json"}
    decoded_images = []
    
    for index, caption in enumerate(captions):
        if index == 0:
            payload2 = {
                "payload": payload, 
                "api_Path": "getImage",
                "storyPrompt": caption,
                "previousPrompt": ''
            }
        else:
            payload2 = {
                "payload": payload, 
                "api_Path": "getImage",
                "storyPrompt": caption,
                "previousPrompt": captions[index - 1]     
            }
            
        json_data = payload2            
        response = requests.post(AWS_API_URL, headers=headers, json=json_data)
        
        if response.status_code == 200:
            data = response.json()

            # st.write('line 196')
            if data["image_data_decode1"] == "INVALID_PROMPT":
                invalid_image = "pages/images/pic_next_page.png"
                decoded_images.append(encode_image_to_base64(invalid_image))
                # st.write('line 200')
            else:
                # st.write('line 202')
                decoded_images.append(data["image_data_decode1"])
    return decoded_images

# Main app
def main():

    st.markdown("<h1 style='text-align: center; color: #5481c4;'>Welcome to ETLP Chat</h1>", unsafe_allow_html=True)
    # st.title("📖 Welcome to WonderScribe!")
    # st.write("Craft personalized stories that bring adventure to life.")
    
    if 'cache_cleared' not in st.session_state:
        st.session_state.cache_cleared = False

    #=================
    # Set the page configuration with a wide layout for a book-like feel
    # Add custom CSS for the storybook theme
    
    st.markdown("""
    <style>
        /* Overall background styling */
        # body {
        #     #background-color: #f5f0e1;
        #     font-family: 'Merriweather', serif;
        #     #color: #4e342e;
        #     [data-testid="stAppViewContainer"] {
        #     background: linear-gradient(135deg,#8c52ff, #5ce1e6);
        #     background-attachment: fixed;
        #     # background-color: #7dd8ff;  /* #c0dc8f Light gray-green #d2e7ae; Purple=#8c52ff, #5f20eb*/
        # }

 
        # /* Sidebar styling to resemble a table of contents */
        # .css-1d391kg {
        #     #background-color: #e8e0d2 !important;
        #     background-color: #7dd8ff; /*#7dd8ff; Sidebar background color */
        #     #background-color: #7dd8ff !important;
        #     border-right: 2px solid #bfa989;
        # }
 
        /* Sidebar Title */
        .css-1544g2n {
            color: #4e342e !important;
            font-size: 1.5em;
            font-family: 'Merriweather', serif;
            font-weight: bold;
        }
 
        /* Menu buttons in the sidebar */
        .css-1vbd788 {
            background-color: #d4c1a7;
            border-radius: 10px;
            border: 2px solid #bfa989;
            padding: 10px;
            font-size: 1.2em;
            color: #4e342e !important;
            margin-bottom: 15px;
        }
 
        .css-1vbd788:hover {
            background-color: #e0d3b8;
            color: #4e342e !important;
        }
 
        /* Main content area - text background with borders */
        .storybook-text {
            background-color: #faf3e7;
            padding: 30px;
            border-radius: 15px;
            border: 3px solid #bfa989;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
            font-family: 'Merriweather', serif;
            font-size: 18px;
            line-height: 1.6;
            text-align: justify;
        }
 
        /* Image styling */
        .storybook-image {
            border-radius: 15px;
            border: 3px solid #bfa989;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
            max-width: 100%;
            height: auto;
        }
 
        /* Styling for the page navigation buttons */
        .stButton > button {
            background-color: #d4c1a7;
            color: #4e342e;
            border: 2px solid #bfa989;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 1.2em;
        }
 
        .stButton > button:hover {
            background-color: #e0d3b8;
            color: #4e342e;
        }
    </style>
    """, unsafe_allow_html=True)

    if 'validation_errors' not in st.session_state:
        st.session_state.validation_errors = []

    #=================
    # st.write('line 308')
    with st.form("form_key"):
        st.write("Craft personalized stories that bring adventure to life and ignite imagination and creativity.")
        story_theme = st.text_input("Please provide a detailed description of the topic that will be used to create your story. It should be at least 10 characters long and have more than two words.?", placeholder="Enter brief idea of a story. 'Example - Friendship between two girls' ")
        audio_value = st.audio_input("What is story theme")
        moral_lesson = st.text_input("What moral lesson would you like your story to focus on?", placeholder="Enter a moral lesson from this story. 'Example - build trust and support each other' ")
        audience = st.selectbox("Who will be the target audience for your story?", ["Children", "toddler", "Young Adult", "Adult", "Senior"])
        story_setting = st.selectbox("What will the story's setting be to shape its tone and character interactions?", options=["Magical Kingdoms", "Underwater Kingdoms", "Pirate Ships", "Fairy Tale Lands", "Forests and Jungles", "Modern Cities","Mountains and Caves", "Haunted Houses", "Imaginary Worlds", "Theme Parks or Circuses", "Extraterrestrial/Space"])
        story_type = st.selectbox("Story Type", options=["Fantasy", "Fairy Tales", "Mythology", "Bedtime stories", "Adventure", "Mystery", "Love", "Horror"])
        story_lang = st.selectbox("What language would you like your story to be written in?", options=["English", "Spanish", "French", "German", "Mandarin", "Hindi", "Urdu", "Arabic", "Italian", "Vietnamese","Tagalog", "Tamil", "Bengali"])
        character_type = st.selectbox("What will be the 'Character Type Genre' in your story?",options=["Human-Centric Stories", "Animal-Centric Stories", "Plant-Based Stories", " Object-Centric Stories","Non-Living Entity Stories"])
        main_character = st.text_input("What will be the name of the main Character in your story?", placeholder="Who will be the star in your story?")
        gender = st.selectbox("What gender will the main character in your story be?", ["Female", "Male", "Non Binary", "Don't want to share"])
        age = st.text_input("How old will the main character be in your story?", placeholder="Please enter the age of main character in numbers.")
        height = st.selectbox("What will be the height and build of the main character in your story", options=["tall and fit", "tall and slim", "tall and muscular", "short and slim", "short and muscular", "normal", "average build", "stocky"])
        hair_color = st.selectbox("What will be the hair color of the main character in your story", options= ["black","brown", "blonde", "golden","red","gray", "white"])
        eye_color = st.selectbox("What color will the main character's eyes be?", options=["brown", "blue", "green", "hazel", "gray", "amber"]) 
        story_length = st.selectbox("Story Length (in words)", options=["300", "400", "500","700", "1500","2000"])
       
        submit_btn = st.form_submit_button("submit")

        # outfit = st.text_input("outfit of the main character", placeholder="outfit of the star of your story?")
        # ethnicity = st.text_input("ethnicity of the main character", placeholder="Ethnicity of the star of your story?")
 

        # ============

    try:
        if submit_btn:
            # Clear previous validation errors
            st.session_state.validation_errors = []
        
            # Validate main character
            if not main_character or len(main_character.strip()) < 2:
                st.session_state.validation_errors.append("Main character name must be at least two characters long")
            elif not main_character.replace(" ", "").isalpha():
                st.session_state.validation_errors.append("Main character name should only contain letters")

            # Validate story theme
            if not story_theme or len(story_theme.strip()) < 10:
                st.session_state.validation_errors.append("Story theme must be at least 10 characters long.")
            elif len(story_theme.split()) < 2:
                st.session_state.validation_errors.append("Story theme should contain at least two words.")

            # Validate moral lesson
            if not moral_lesson or len(moral_lesson.strip()) < 10:
                st.session_state.validation_errors.append("Moral lesson must be at least 10 characters long.")
            elif len(moral_lesson.split()) < 2:
                st.session_state.validation_errors.append("Moral lesson should contain at least two words.")

            # Display all validation errors if any
    
            if st.session_state.validation_errors:
                error_message = "Please fix the following errors:\n" + "\n".join(f".{error}" for error in st.session_state.validation_errors)
                st.error(error_message)
                st.stop() # Stop further execution if there are validation errors

            # if no validation errors, proceed with form submission
            st.session_state.submit_btn = True
            
        menu_options = ["About", "Storybook"]
        st.session_state.current_page = "Storybook"
        # st.write('line 361')

        if submit_btn:
            st.cache_data.clear()
            st.session_state.cache_cleared = True
            st.success("Cache has been cleared! Refresh the page to fetch new data.")
            st.session_state.submit_btn = True
            st.session_state.page_index = 0
            # st.write('line 369')
            
        if st.session_state.submit_btn and st.session_state.current_page == "Storybook":
            # Create payload
            payload = {
                "character_type": character_type,
                "age": age,
                "height": height,
                "hair_color": hair_color,
                "eye_color": eye_color,
                "audience": audience,
                "story_type": story_type,
                "main_character": main_character,
                "story_theme": story_theme,
                "moral_lesson": moral_lesson,
                "setting": story_setting,
                "word_count": story_length,
                "story_lang": story_lang,
                "api_Path": "getStory"
                }

            # Fetch data
            story_texts, captions, storyfiles = fetch_story_data(payload)
            # st.write('line 389')
            decoded_images = fetch_and_decode_images(payload, captions)

            # ========
            # character_prompt = f""" {character_type} character_type {main_character} whoes gender is {gender}, age is {age}, height is {height}, hair color is {hair_color}, eye color is {eye_color}"""
            # #story_text = [story_text + character_prompt for story_text in story_texts]
            # st.write('character_prompt', character_prompt)
            # caption_with_character_feature = [caption_with_character_feature + character_prompt for caption_with_character_apprearance in captions]
            # st.write("caption_with_character_feature", {caption_with_character_feature})
            # #decoded_images = fetch_and_decode_images(story_text)
            # # decoded_images = fetch_and_decode_images(captions)
         
            # ==========

            audioStoryFiles = []
            for storyFile in storyfiles:
                # st.write('line 395')
                output = s3client.generate_presigned_url('get_object',
                                                    Params={'Bucket': 'wonderstorytexttoaudiofile',
                                                            'Key': storyFile},
                                                    ExpiresIn=3600)
                audioStoryFiles.append(output)
                
                # Reset the cache_cleared flag. Don't clear the cache
            st.session_state.cache_cleared = False
            expected_parts = 7
            story_pages = []
            total_pages = min(len(story_texts), len(decoded_images), len(captions), len(audioStoryFiles))

            if total_pages < expected_parts:
                st.error(f"Oops! Only {total_pages} out of {expected_parts} story parts received. Please try again or modify your input.")
                print("Incomplete story data:", {
                    "story_texts": len(story_texts),
                    "decoded_images": len(decoded_images),
                    "captions": len(captions),
                    "audio_files": len(audioStoryFiles)
                })

            for i in range(total_pages):
                story_pages.append({
                    "text": story_texts[i],
                    "image": decoded_images[i],
                    "caption": captions[i],
                    "audio": audioStoryFiles[i]
                })

            # if total_pages < expected_parts:
            #     st.info(f"Showing {total_pages} story pages out of the expected 7.")
 
            # story_pages = [
            #     {
            #         "text": story_texts[0],
            #         #"image": "img1.png",
            #         "image": decoded_images[0],
            #         "caption": captions[0],
            #         "audio": audioStoryFiles[0]
            #     },
            #     {
            #         "text": story_texts[1],
            #         #"image": "img2.png",
            #         "image": decoded_images[1],
            #         "caption": captions[1],
            #         "audio": audioStoryFiles[1]
            #     },
            #     {
            #         "text": story_texts[2],
            #         #"image": "img3.png",
            #         "image": decoded_images[2],
            #         "caption": captions[2],
            #         "audio": audioStoryFiles[2]
            #     },
            #     {
            #         "text": story_texts[3],
            #         #"image": "img4.png",
            #         "image": decoded_images[3],
            #         "caption": captions[3],
            #         "audio": audioStoryFiles[3]
            #     },
            #     {
            #         "text": story_texts[4],
            #         #"image": "img4.png",
            #         "image": decoded_images[4],
            #         "caption": captions[4],
            #         "audio": audioStoryFiles[4]
            #     },
            #     {
            #         "text": story_texts[5],
            #         #"image": "img4.png",
            #         "image": decoded_images[5],
            #         "caption": captions[5],
            #         "audio": audioStoryFiles[5]
            #     },
            #     {
            #         "text": story_texts[6],
            #     #     #"image": "img4.png",
            #         "image": decoded_images[6],
            #         "caption": captions[6],
            #         "audio": audioStoryFiles[6]
            #     }
            # ]
            
            st.write('line 457')
            #st.markdown(story_pages[0]["image"])
            # Initialize session state for the current story page index
            if 'page_index' not in st.session_state:
                st.session_state.page_index = 0
                
            # st.write('line 463')
            # Functions for navigating between pages
            def next_page():
                if st.session_state.page_index < len(story_pages) - 1:
                    st.session_state.page_index += 1
                    st.session_state.submit_btn = True
 
            def prev_page():
                if st.session_state.page_index > 0:
                    st.session_state.page_index -= 1
                    st.session_state.submit_btn = True
 
            # Get the current page's content
            current_page = story_pages[st.session_state.page_index]
 
            st.title("📖 My Storybook")
            image = image_decode(current_page["image"])
            # st.write('line 479')
            col1, col2 = st.columns(2)
 
            with col1:
                #st.markdown(f'<div class="storybook-text">{current_page["text"]}</div>', unsafe_allow_html=True)
                #st.markdown(f'<div class="storybook-text" style="height: {image.height}px;"><p>{current_page["text"]}</p></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="storybook-text"><p>{current_page["text"]}</p></div>', unsafe_allow_html=True)
                st.audio(current_page["audio"], format='audio/mp3')
            with col2:
                # Use custom HTML and CSS for image with the desired style
                #st.markdown(f'<img src="{current_page["image"]}" alt="{current_page["caption"]}" class="storybook-image">', unsafe_allow_html=True)
                st.image(image, caption=current_page["caption"], use_container_width=True)
 
            # Create Previous and Next buttons for navigation
            col1, col2, col3 = st.columns([1, 2, 1])

            st.write("Page No: ", st.session_state.page_index + 1, " out of 7")
            with col1:
                if st.session_state.page_index > 0:
                    st.button("Previous", on_click=prev_page)
                    st.session_state.submit_btn = True
 
            with col3:
                if st.session_state.page_index < len(story_pages) - 1:
                    st.button("Next", on_click=next_page)
                    st.session_state.submit_btn = True
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if "submit_btn" not in st.session_state:
        st.session_state.submit_btn = False
    main()
