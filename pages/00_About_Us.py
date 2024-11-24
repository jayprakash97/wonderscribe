import streamlit as st

# Set page configuration
st.set_page_config(page_title="About WonderScribe", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"


# CSS for gradient and background image
background_css = f"""
<style>
/* Apply the background image to the main app container */
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;  /* Ensure it covers the full viewport */
    background-position: center;  /* Center the image */
    background-repeat: no-repeat;  /* Do not repeat the image */
    background-attachment: fixed;  /* Keep the background fixed during scrolling */
}}

/* Add a semi-transparent box for content */
.custom-box {{
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
    border-radius: 10px; /* Rounded corners */
    padding: 20px; /* Space inside the box */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    color: black; /* Text color */
    margin-top: 20px; /* Space above the box */
}}

/* Sidebar customization */
#[data-testid="stSidebar"] {{
    #background-color: #7dd8ff; /* Light blue */
    #border-right: 2px solid #bfa989; /* Border on the right */
}}

[data-testid="stSidebar"] * {{
    color: #8c52ff; /* Purple text for sidebar */
}}

/* Adjust text color for readability on the gradient */
[data-testid="stAppViewContainer"] .stMarkdown {{
    color: white;
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# Display the WonderScribe logo
st.image("pages/images/Updated_WonderS_logo.png", width=300)

# Page title
st.title("Welcome to WonderScribe")

# Content with semi-transparent box
st.markdown(
    """
    <style>
        .custom-box {
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
            font-family: Arial, sans-serif;
            color: #333; /* Dark gray text color for readability */
            line-height: 1.6; /* Improved text spacing for readability */
        }
    </style>

    <div class="custom-box">
        <h1>Welcome to WonderScribe, where stories come to life!</h1>
        <p>We are a passionate team of innovators on a mission to empower young imaginations through the magic of storytelling. At WonderScribe, we believe that every child has a story to tell, and our platform makes it possible for children to become the authors, illustrators, and narrators of their own adventures. Using cutting-edge generative AI, we create a unique, interactive storytelling experience that brings together text, images, and audio to craft personalized, immersive tales. With WonderScribe, kids and parents can co-create stories that reflect their dreams, personalities, and cultures, fostering creativity, literacy, and self-expression in a fun and engaging way.

We aim to make storytelling:

Interactive: Children don’t just read stories—they create them.
Inclusive: Our platform celebrates diverse narratives and cultures, ensuring every child feels represented.
Accessible: Designed for children everywhere, regardless of their background or language.
Join us on this exciting journey as we reimagine the world of storytelling, one personalized tale at a time. Let WonderScribe inspire your child’s imagination and unlock the power of their creativity!</p>
    """,
    unsafe_allow_html=True,
)
