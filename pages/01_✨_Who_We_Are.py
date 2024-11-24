import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="About WonderScribe", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

# CSS for background image and semi-transparent box
background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
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
    background-color: #f0f4ff; /* blue */
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

# Page title
st.markdown(
    "<h1 style='color: #5481c4; text-align: center; font-size: 3em;'>WonderScribe, where stories come to life!</h1>",
    unsafe_allow_html=True,
)

# Content wrapped in a div with class "custom-box"
st.markdown(
    """
    <div class="custom-box">
        <p>We are a passionate team of innovators on a mission to empower young imaginations through the magic of storytelling. At WonderScribe, we believe that every child has a story to tell, and our platform makes it possible for children to become the authors, illustrators, and narrators of their own adventures. Using cutting-edge generative AI, we create a unique, interactive storytelling experience that brings together text, images, and audio to craft personalized, immersive tales. With WonderScribe, kids and parents can co-create stories that reflect their dreams, personalities, and cultures, fostering creativity, literacy, and self-expression in a fun and engaging way.</p>
        <h3>We aim to make storytelling:</h3>
        <ul>
            <li><strong>Interactive:</strong> Children don’t just read stories—they create them.</li>
            <li><strong>Inclusive:</strong> Our platform celebrates diverse narratives and cultures, ensuring every child feels represented.</li>
            <li><strong>Accessible:</strong> Designed for children everywhere, regardless of their background or language.</li>
        </ul> 
        <p>Join us on this exciting journey as we reimagine the world of storytelling, one personalized tale at a time. Let WonderScribe inspire your child’s imagination and unlock the power of their creativity!</p>
    </div>
    """,
    unsafe_allow_html=True,
)
