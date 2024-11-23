import streamlit as st

# Set page configuration
st.set_page_config(page_title="About WonderScribe", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk1_page_1.jpg"

# CSS for gradient and background image
background_css = f"""
<style>
/* Apply a gradient background overlaid with the background image */
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(135deg, rgba(140, 82, 255, 0.8), rgba(92, 225, 230, 0.8)), 
                      url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    padding: 20px; /* Add padding to the container */
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
[data-testid="stSidebar"] {{
    background-color: #7dd8ff; /* Light blue */
    border-right: 2px solid #bfa989; /* Border on the right */
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
    <div class="custom-box">
        <p>We are a passionate team of authors, educators, and creatives on a mission to ignite young readers' imaginations
        everywhere. We believe in the power of stories to transport children to magical worlds, introduce them to 
        fascinating characters, and inspire endless possibilities.</p>
        
       <p>At WonderScribe, we use cutting-edge technology, including AI and advanced language models, to create a unique
        storytelling experience. Our platform allows kids to become co-authors of their adventures, customizing tales
        to reflect their dreams, personalities, and imaginations.</p>
        
        <p>We aim to make reading fun, interactive, and accessible to all children, no matter where they are. Through our
        innovative platform, we hope to foster a love of reading, spark creativity, and encourage every child to believe 
        in the magic of their own stories.</p>
        
        <p>Join us on this exciting journey and watch your child's imagination soar!</p>
    </div>
    """,
    unsafe_allow_html=True,
)
