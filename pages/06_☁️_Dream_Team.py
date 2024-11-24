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
    color: gray;
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
    "<h1 style='color: #5481c4; text-align: center;'>Our Team</h1>",
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
        "bio": "Jailynne brings creativity and precision to WonderScribe, playing a key role in crafting a user-friendly and engaging platform for children and parents. She has helped design an intuitive interface that ensures a seamless storytelling experience while also leading the development of presentations, scripts, and pitches to effectively showcase the project’s value. Jailynne’s efforts extend beyond design and communication, as she actively collaborates with the team to bridge technical development with user needs. Her dedication to WonderScribe’s mission has been pivotal in creating a platform that fosters creativity, learning, and imagination for all.",
        "image": "pages/images/JEN.jpeg",
        "email": "jestevez@berkeley.edu",
    },
    {
        "name": "Mian Haseeb",
        "role": "ML Engineering, GenAI",
        "bio": "Mian is the visionary behind WonderScribe, originally conceiving the idea to revolutionize storytelling through the power of Generative AI. Mian is one of the machine learning engineers for WonderScribe, driving the integration of cutting-edge generative AI models. From fine-tuning the RAG framework to deploying advanced text and image generation models, Mian’s work ensures that WonderScribe delivers creative, engaging, and contextually relevant stories. His passion for AI innovation and storytelling shines through in every technical detail.",
        "image": "pages/images/MianHaseeb.jfif",
        "email": "mhaseeb@berkeley.edu",
    },
    {
        "name": "Natsnet Demoz",
        "role": "Data & Analytics, UI/UX Design, Model Development",
        "bio": "Natsnet’s dual focus on data exploration and design brings WonderScribe’s creative vision to life. She leads exploratory data analysis, ensuring the platform leverages child-friendly and culturally diverse datasets. Additionally, her contributions to user interface design make WonderScribe an intuitive and engaging platform for children and parents alike. Her ability to merge data insights with user-centric design is a key driver of the project’s success.",
        "image": "pages/images/Natsnet Demoz.jfif",
        "email": "ndemoz@berkeley.edu",
    },
    {
        "name": "Wilford Bradford",
        "role": "SME, Model Development",
        "bio": "Wil lends his expertise as a subject matter expert to refine WonderScribe’s storytelling framework. His work focuses on aligning the platform’s AI capabilities with user expectations, ensuring every story element resonates with children and their imaginations. Wil also collaborates on model development, emphasizing inclusivity and quality across WonderScribe’s texts and images",
        "image": "pages/images/WilfordBradford.jfif",
        "email": "wbradford@berkeley.edu",
    },
]

# Display team members
for member in members:
    col1, col2 = st.columns([1, 3])  # Adjust column width for better layout
    with col1:
        # Use st.image for displaying local images without captions
        st.image(member["image"], use_column_width=True)  # Removed the caption argument
    with col2:
        st.markdown(f"### {member['name']}")
        st.markdown(f"**Role:** {member['role']}")
        st.markdown(f"**Bio:** {member['bio']}")
        st.markdown(f"**Email:** [{member['email']}](mailto:{member['email']})")
    st.write("---")

