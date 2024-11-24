import streamlit as st
import base64

st.set_page_config(page_title="Contact", page_icon="👩‍🏫", layout="wide")

# Background image URL (ensure this is the raw link from GitHub)
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

# CSS for setting the background image
background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Custom CSS for increasing font size in form labels */
label {{
    font-size: 35px; /* Increase font size for form labels */
    font-weight: bold; /* Optional: make labels bold */
    color: #333; /* Optional: set label text color */
}}
</style>
"""

# Apply the CSS
st.markdown(background_css, unsafe_allow_html=True)

# Function to add a logo to the sidebar
def add_logo_to_sidebar(logo_path, width="250px"):
    # Read and encode the image in Base64
    with open(logo_path, "rb") as f:
        encoded_logo = base64.b64encode(f.read()).decode("utf-8")
    # Add the encoded logo as CSS in the sidebar
    st.sidebar.markdown(
        f"""
        <style>
            [data-testid="stSidebar"] {{
                background-image: url("data:image/png;base64,{encoded_logo}");
                background-size: {width};
                background-repeat: no-repeat;
                background-position: top center;
                padding-top: 100px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the sidebar
add_logo_to_sidebar("pages/images/Updated_WonderS_logo.png")

# Title for the page
st.markdown(
    "<h1 style='color: #5481c4; text-align: center; font-size: 3em;'>Contact the WonderScribe Team</h1>",
    unsafe_allow_html=True,
)

# Contact form
with st.form("form_key"):
    Full_name = st.text_input("Full Name (First Name, Last Name)")
    Company = st.text_input("Company Name")
    Country = st.text_input("Country Name")
    State = st.text_input("State or Province Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number (country code, city code, and local phone number)")
    question = st.text_area("Question or Comments")
    submit_btn = st.form_submit_button("Submit")
