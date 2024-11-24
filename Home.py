import streamlit as st
import base64

# Set up the page configuration
st.set_page_config(page_title="WonderScribe", page_icon="📖", layout="wide")

# Background image URL
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
st.markdown(background_css, unsafe_allow_html=True)

# Function to add the logo to the sidebar
def add_logo_to_sidebar(logo_path, width="250px"):
    with open(logo_path, "rb") as f:
        encoded_logo = base64.b64encode(f.read()).decode("utf-8")
    st.sidebar.markdown(
        f"""
        <style>
            [data-testid="stSidebar"]::before {{
                content: '';
                display: block;
                background-image: url("data:image/png;base64,{encoded_logo}");
                background-size: {width}; /* Adjust the size of the logo */
                background-repeat: no-repeat;
                background-position: top center; /* Center the logo at the top */
                height: 200px; /* Adjust height to fit the logo */
                padding-top: 20px;
                margin-bottom: 20px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the sidebar
add_logo_to_sidebar("pages/images/Updated_WonderS_logo.png", width="200px")


# Page Title
st.markdown(
    "<h1 style='text-align: center; color: #5481c4;'>Welcome to WonderScribe</h1>",
    unsafe_allow_html=True,
)


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
