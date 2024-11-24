import streamlit as st

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
    color: #333;
    line-height: 1.6;
}}
.custom-box h3 {{
    text-align: center;
    margin-top: 20px;
}}
.custom-box ul {{
    padding-left: 20px;
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# Display logo
st.image("pages/images/Updated_WonderS_logo.png", width=300)

# Page title
st.title("WonderScribe, where stories come to life!")

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
