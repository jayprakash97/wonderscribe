import streamlit as st

st.set_page_config(page_title="WonderScribe", page_icon="📖", layout="wide")

st.image("pages/images/Updated_WonderS_logo.png", width= 300)

#*****

import streamlit as st

# Title with custom CSS
original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Streamlit CSS Styling✨</h1>'
st.markdown(original_title, unsafe_allow_html=True)

# Set the background image (Replace with your GitHub raw URL or a hosted URL)
background_image_url = "https://raw.githubusercontent.com/your-username/repo-name/branch-name/path/to/WonderScribe_bk2_page_1.jpg"

# CSS for setting the background image
background_image = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("{background_image_url}");
    background-size: 100vw 100vh;  /* Cover the entire viewport */
    background-position: center;  
    background-repeat: no-repeat;
}}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# Transparent input field styling
input_style = """
<style>
input[type="text"] {{
    background-color: transparent;
    color: #a19eae;  /* Text color inside the input box */
    font-size: 16px;
    border: none;
    border-bottom: 1px solid #a19eae;  /* Underline for the input box */
}}
div[data-baseweb="base-input"] {{
    background-color: transparent !important;
}}
</style>
"""

# Apply the input style
st.markdown(input_style, unsafe_allow_html=True)

# Input field
st.text_input("", placeholder="Streamlit CSS Input Example")

# Add additional content
st.write("This Streamlit app demonstrates a transparent input field and a background image.")



#*****

st.title("Welcome to WonderScribe")
st.write(
"""
At WonderScribe, we use cutting-edge technology, including AI and advanced language models, to create a unique
storytelling experience. Our platform allows kids to become co-authors of their adventures, customizing tales
to reflect their dreams, personalities, and imaginations.

We aim to make reading fun, interactive, and accessible to all children, no matter where they are. Through our
innovative platform, we hope to foster a love of reading, spark creativity, and encourage every child to believe 
in the magic of their own stories

Join us on this exciting journey and watch your child's imagination soar!
""")
#st.sidebar.title("📚 Table of Contents")


st.markdown(
    """
    <style>
    /* Style for the sidebar content */
    [data-testid="stSidebarContent"] {
        #background-color: #7dd8ff; /*#7dd8ff; Sidebar background color */
        
    }
    # color #8c52ff
    /* Set color for all text inside the sidebar */
    [data-testid="stSidebar"] * {
        color: #b3ccff !important;  /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Change the background color
st.markdown(
    """
    <style>
    .stApp {
        [data-testid="stAppViewContainer"] {
        #background: linear-gradient(135deg, #8c52ff, #5ce1e6);
        background-attachment: fixed;
        # background-color: #7dd8ff;  /* #c0dc8f Light gray-green #d2e7ae; Purple=#8c52ff, #5f20eb*/
    }
    .custom-label{
        # color: #5f20eb, #8c52ft;   /* old color #3b8bc2; #5ce1e6*/
        color: #8C52FF;
        font-size: 18px;  /* Set the font size for text input, number input, and text area */
        padding: 10px;    /* Optional: adjust padding for better appearance */
    }
    p, li, span{
        color: #4b7170;
        font-size: 18px;  /* Set default font size */
        /* font-weight: bold;   Make the text bold */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

