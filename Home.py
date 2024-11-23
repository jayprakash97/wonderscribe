import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="WonderScribe", page_icon="📖", layout="wide")

# Display the logo
st.image("pages/images/Updated_WonderS_logo.png", width=300)

# Background image URL (ensure this is the raw link from GitHub)
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk2_page_1.jpg"

# CSS for setting the background image
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
</style>
"""

# Apply the CSS
st.markdown(background_css, unsafe_allow_html=True)
# CSS for the transparent background image
background_css = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("{background_image_url}");
    background-size: cover;  /* Cover the full viewport */
    background-position: center;  
    background-repeat: no-repeat;
    background-attachment: fixed;  /* Keep the background fixed during scroll */
    filter: opacity(0.5);  /* Adjust transparency (0.0 is fully transparent, 1.0 is fully visible) */
}}
[data-testid="stAppViewContainer"] {{
    background-color: rgba(255, 255, 255, 0.8);  /* Add a light overlay (adjust rgba values as needed) */
}}
</style>
"""

# Apply the CSS
st.markdown(background_css, unsafe_allow_html=True)

# Page Title
st.title("Welcome to WonderScribe")

# Introduction Text
st.write(
    """
    At WonderScribe, we use cutting-edge technology, including AI and advanced language models, 
    to create a unique storytelling experience. Our platform allows kids to become co-authors 
    of their adventures, customizing tales to reflect their dreams, personalities, and imaginations.

    We aim to make reading fun, interactive, and accessible to all children, no matter where they are. 
    Through our innovative platform, we hope to foster a love of reading, spark creativity, and encourage 
    every child to believe in the magic of their own stories.

    Join us on this exciting journey and watch your child's imagination soar!
    """
)

# Additional CSS for styling (optional improvements)
st.markdown(
    """
    <style>
    /* Sidebar Styling */
    [data-testid="stSidebarContent"] {
        #background-color: #7dd8ff;  /* Light blue */
    }
    [data-testid="stSidebar"] * {
        color: #b3ccff !important;  /* Light text color */
    }

    /* Default font and text styling */
    p, li, span {
        color: #4b7170;  /* Dark green-gray */
        font-size: 18px;  /* Default font size */
    }

    /* Background Gradient Styling */
    .stApp {
        background: linear-gradient(135deg, #8c52ff, #5ce1e6);  /* Purple to blue gradient */
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
