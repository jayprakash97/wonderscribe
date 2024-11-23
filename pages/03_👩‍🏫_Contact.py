import streamlit as st

st.set_page_config(page_title="Contact", page_icon="👩‍🏫", layout="wide")

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
    color: white;  /* Default text color for readability */
}}

/* Add a semi-transparent box for content */
.custom-box {{
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
    border-radius: 10px; /* Rounded corners */
    padding: 20px; /* Space inside the box */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow effect */
    color: black; /* Text color inside the content box */
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

/* Adjust text color for readability */
[data-testid="stAppViewContainer"] .stMarkdown {{
    color: white;
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# WonderScribe logo
st.image("pages/images/WonderScribeLogo.png", width=150)

# Page title
st.title("Contact the WonderScribe Team")

# Contact form inside a semi-transparent content box
st.markdown(
    """
    <div class="custom-box">
        <h2>Contact Us</h2>
        <p>
            We are here to help! Please fill out the form below, and a member of our team will get back to you shortly.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Form section
with st.form("form_key"):
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)  # Start custom box for form
    Department = st.selectbox(
        "Department",
        options=[
            "Sales", "Human Resources", "Information Technology",
            "Public Relations", "Compliance", "Marketing",
            "Data Engineering", "Data Science", "Data Analytics",
        ],
    )
    Full_name = st.text_input("Enter your full name (First Name, Middle Name, Last Name)")
    Company = st.text_input("Enter your Company Name")
    Country = st.text_input("Enter your Country Name")
    State = st.text_input("Enter your State or Province Name")
    email = st.text_input("Enter your email address")
    phone = st.text_input("Enter yo
