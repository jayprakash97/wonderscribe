import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Members - WonderScribe", page_icon="📖", layout="wide")

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
#[data-testid="stSidebar"] {{
    #background-color: #7dd8ff; /* Light blue */
    #border-right: 2px solid #bfa989; /* Border on the right */
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

# Paths to the logos
logo = "pages/images/Updated_WonderS_logo.png"

# Function to add the logo to the sidebar
def add_logo(logo, width):
    # Read the image and convert it to Base64
    with open(logo, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    # Inject CSS with Base64-encoded image into the sidebar
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{data}");
                background-repeat: no-repeat;
                padding-top: 250px;
                background-position: 10px 10px;
                background-size: {width};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo
add_logo(logo, "250px")

# Page Title
st.markdown(
    "<h1 style='color: #5f20eb; text-align: center;'>Our Team</h1>",
    unsafe_allow_html=True,
)

# Define group members
members = [
    {
        "name": "Jay Prakash",
        "role": "Product Management, GenAI, AWS Architecture",
        "bio": "Jay is the technical backbone of WonderScribe, leading the development of the platform’s robust AWS architecture. With expertise in cloud-based solutions and Generative AI, Jay ensures the platform's seamless integration of services like API Gateway, Lambda, and Bedrock. His focus on scalability and efficiency has been instrumental in building a secure and reliable foundation for WonderScribe's innovative storytelling capabilities.",
        "image": "pages/images/Jay_Profile_pic.jpg",
        "email": "jprakash@berkeley.edu",
    },
    {
        "name": "Jailynne Estevez",
        "role": "Program Management, UI/UX Design, Presentation Development",
        "bio": "Jailynne brings creativity and precision to WonderScribe, playing a key role in crafting a user-friendly and engaging platform for children and parents. She has helped design an intuitive interface that ensures a seamless storytelling experience while also leading the development of presentations, scripts, and pitches to effectively showcase the project’s value.",
        "image": "pages/images/jailynne.png",
        "email": "jestevez@berkeley.edu",
    },
    {
        "name": "Mian Haseeb",
        "role": "ML Engineering, GenAI",
        "bio": "Mian is the visionary behind WonderScribe, originally conceiving the idea to revolutionize storytelling through the power of Generative AI. He leads the integration of cutting-edge generative AI models, fine-tuning the RAG framework to deploy advanced text and image generation models.",
        "image": "pages/images/MianHaseeb.jfif",
        "email": "mhaseeb@berkeley.edu",
    },
    {
        "name": "Natsnet Demoz",
        "role": "ML, Data & Analytics, UI/UX Design, Model Development",
        "bio": "Natsnet’s dual focus on data exploration and design brings WonderScribe’s creative vision to life. She leads exploratory data analysis, ensuring the platform leverages child-friendly and culturally diverse datasets.",
        "image": "pages/images/Natsnet Demoz.jfif",
        "email": "ndemoz@berkeley.edu",
    },
    {
        "name": "Wilford Bradford",
        "role": "SME, Model Development",
        "bio": "Wil lends his expertise as a subject matter expert to refine WonderScribe’s storytelling framework. His work focuses on aligning the platform’s AI capabilities with user expectations, ensuring every story element resonates with children and their imaginations.",
        "image": "pages/images/WilfordBradford.jfif",
        "email": "wbradford@berkeley.edu",
    },
]

# Display team members
for member in members:
    st.markdown(
        f"""
        <div class="custom-box">
            <div style="display: flex; align-items: center;">
                <img src="{member['image']}" alt="{member['name']}" style="width: 150px; border-radius: 10px; margin-right: 20px;" />
                <div>
                    <h3 style="margin: 0;">{member['name']}</h3>
                    <p><strong>Role:</strong> {member['role']}</p>
                    <p><strong>Bio:</strong> {member['bio']}</p>
                    <p><strong>Email:</strong> <a href="mailto:{member['email']}" style="color: #5f20eb;">{member['email']}</a></p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("---")
