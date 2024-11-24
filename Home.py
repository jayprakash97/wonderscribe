import streamlit as st
import base64

# Set up the page configuration
st.set_page_config(page_title="WonderScribe", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk2_page_1.jpg"

# CSS for setting the background image
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

# Center and middle align the title and introduction text
st.markdown(
    """
    <style>
    .center-content {
        display: flex;
        flex-direction: column;
        justify-content: center; /* Vertically center */
        align-items: center;    /* Horizontally center */
        height: 90vh;           /* Full viewport height (adjust as needed) */
        text-align: center;     /* Center-align text */
    }
    .center-content h1 {
        color: #5481c4;         /* Customize title color */
        font-size: 3em;         /* Adjust font size */
        margin-bottom: 20px;    /* Space below the title */
    }
    .center-content p {
        color: #4b7170;         /* Customize paragraph color */
        font-size: 1.25em;      /* Adjust font size */
        line-height: 1.6;       /* Improve line spacing */
    }
    </style>
    <div class="center-content">
        <h1>Welcome to WonderScribe</h1>
        <p>
            At WonderScribe, we use cutting-edge technology, including AI and advanced language models, 
            to create a unique storytelling experience. Our platform allows kids to become co-authors 
            of their adventures, customizing tales to reflect their dreams, personalities, and imaginations.
        </p>
        <p>
            We aim to make reading fun, interactive, and accessible to all children, no matter where they are. 
            Through our innovative platform, we hope to foster a love of reading, spark creativity, and encourage 
            every child to believe in the magic of their own stories.
        </p>
        <p>
            Join us on this exciting journey and watch your child's imagination soar!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
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
