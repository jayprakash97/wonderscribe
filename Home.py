import streamlit as st

st.set_page_config(page_title="WonderScribe", page_icon="📖", layout="wide")

st.image("pages/images/Updated_WonderS_logo.png", width= 300)

#*****

# List of image paths (URLs or local paths)
background_images = [
    "pages/images/WonderScribe_bk1_page_1.jpg",
    "pages/images/WonderScribe_bk2_page_1.jpg",
    "pages/images/WonderScribe_bk_blue_page_1.jpg"
]

# Function to select an image (simple selection, or cycle based on user choice)
def get_background_image(index):
    return background_images[index % len(background_images)]

# Set the background image (example uses the first image)
selected_image = get_background_image(0)

# Custom CSS for transparent background with the selected image
background_css = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("{selected_image}");
    background-size: cover;  /* Cover the entire viewport */
    background-position: center;  
    background-repeat: no-repeat;
    background-attachment: fixed;  /* Keeps background fixed during scroll */
}}
[data-testid="stAppViewContainer"] {{
    background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent black overlay */
}}
</style>
"""

# Apply the background CSS
st.markdown(background_css, unsafe_allow_html=True)

# Streamlit content
st.title("Transparent Background with Images")
st.write("This Streamlit app demonstrates setting a PDF-extracted image as a transparent background.")
st.write("You can cycle through images or set them programmatically.")

# Dropdown to select background image
image_index = st.selectbox(
    "Choose a background image:",
    options=list(range(len(background_images))),
    format_func=lambda x: f"Background {x + 1}"
)

# Update the background image dynamically
selected_image = get_background_image(image_index)
background_css_dynamic = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("{selected_image}");
    background-size: cover;
    background-position: center;  
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(background_css_dynamic, unsafe_allow_html=True)

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
        background: linear-gradient(135deg, #8c52ff, #5ce1e6);
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

