import streamlit as st
import base64
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Members - WonderScribe", page_icon="📖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

# CSS for background image, sidebar customization, and custom box
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
                background-size: contain;
                background-repeat: no-repeat;
                background-position: top center;
                height: 250px;
                padding-top: 20px;
                margin-bottom: 20px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the top of the sidebar
add_logo_to_sidebar_top("pages/images/Updated_WonderS_logo.png", width="250px")

# Content wrapped in a div with class "custom-box"
st.markdown(
    """
    <div class="custom-box" style="width: 80%; max-width: 800px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
    <p style="font-size:18px;"> Meet <b style="color:Green;">Empowered Technology Leaders(ETL)</b> who foster supportive and collaborative environments within J&J organizations. 
These ETL leaders are trained to:

<p style="font-size:16px;"> 1. Enhance their technical and leadership skills through comprehensive learning content
<p style="font-size:16px;"> 2. Amplify their leadership brand
<p style="font-size:16px;"> 3. Broaden their network and gain insights from their cohort, fostering a supportive sense of belonging.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Function to process and resize images to 1:1 ratio
def process_image(image_path, size=(800, 800)):
    img = Image.open(image_path)
    # Crop image to square
    min_dimension = min(img.size)
    cropped_img = img.crop((
        (img.width - min_dimension) // 2,
        (img.height - min_dimension) // 2,
        (img.width + min_dimension) // 2,
        (img.height + min_dimension) // 2,
    ))
    # Resize to the specified size
    resized_img = cropped_img.resize(size)
    return resized_img

# Page Title
st.markdown(
    "<h1 style='color: #5481c4; text-align: center;'>Our Team</h1>",
    unsafe_allow_html=True,
)

# Define group members
members = [
    {
        "name": "Jay Prakash",
        "role": "AI Product XFT Leader and GenAI Solutions Architect, Data & Insights",
        # "bio": "Jay Prakash is a visionary leader at WonderScribe, combining expertise in product management and Generative AI solutions to drive the platform's innovative capabilities. He architects and optimizes WonderScribe’s AWS infrastructure, seamlessly integrating technologies such as API Gateway, Lambda, and Bedrock to deliver exceptional storytelling experiences. With a strong focus on scalability, security, and efficiency, Jay ensures the platform’s foundation supports its mission to inspire creativity and enhance digital literacy. His technical acumen and strategic insights play a pivotal role in shaping WonderScribe’s success.",
        "bio": "Jay Prakash is a seasoned technical leader in developing and implementing solutions within pharma to improve patient care and drive business growth. He is also passionate about leveraging AI and GenAI to help the business grow, improve patient care, and create new innovations. Currently, Jay is part of Johnson & Johnson’s Data Science & Insights team for 4.5 year, where he leads end-to-end data management, advanced analytics, and data science initiatives supporting Commercial Business, Market Analysis, Patient Support Services, and more. He also serves as the primary contact for delivering integrated data analytics & reporting across Commercial, and Government pharmaceutical contracting operations across all Therapeutic Areas.",
        "image": "pages/images/Jay_Headshots2.jpg",
        "email": "jprakas5@its.jnj.com" # "jprakash@berkeley.edu", 
    },
    {
        "name": "Komathi SunilKumar",
        "role": "Senior Tech Product Manager - JJIT",
        "bio": "Komathi is a highly motivated IT professional with over 17+ years of experience in IT specializing in AWS RDS engines, AWS Redshift, AWS BigData Platforms & AWS ECO Systems, Microsoft SQL Server, Talend Big Data Studio, MS BI SSIS, PowerShell, Python, Unix, Perl, Informix, C#, ASP.NET, PowerBuilder, Oracle, MySQL, PostgreSQL with wide experience in Analysis, Design, Implementation and testing of business requirements and also having desire to learn and work in a close-knit high performing team.",
        "image": "pages/images/komathi_sunil2.jpg",
        "email": "ksunilku@ITS.JNJ.com",
    }
    # {
    #     "name": "Jude Francis",
    #     "role": "Product Director, Data & Insights",
    #     # "bio": "Mian is the visionary behind WonderScribe, originally conceiving the idea to revolutionize storytelling through the power of Generative AI. Mian is one of the machine learning engineers for WonderScribe, driving the integration of cutting-edge generative AI models. From fine-tuning the RAG framework to deploying advanced text and image generation models, Mian’s work ensures that WonderScribe delivers creative, engaging, and contextually relevant stories. His passion for AI innovation and storytelling shines through in every technical detail.",
    #     # "image": "pages/images/MianHaseeb.jpg",
    #     "email": "mianh1@berkeley.edu",
    # },
    # {
    #     "name": "Sriram  Hariharan",
    #     "role": "Sr. Product Manager, Data & Insights ",
    #     # "bio": "Jailynne brings creativity and precision to WonderScribe, playing a key role in crafting a user-friendly and engaging platform for children and parents. She has helped design an intuitive interface that ensures a seamless storytelling experience while also leading the development of presentations, scripts, and pitches to effectively showcase the project’s value. Jailynne’s efforts extend beyond design and communication, as she actively collaborates with the team to bridge technical development with user needs. Her dedication to WonderScribe’s mission has been pivotal in creating a platform that fosters creativity, learning, and imagination for all.",
    #     # "image": "pages/images/JEN.jpeg",
    #     "email": "jestevez@berkeley.edu",
    # },
    # {
    #     "name": "Jude Francis",
    #     "role": "Product Director, Data & Insights",
    #     # "bio": "Mian is the visionary behind WonderScribe, originally conceiving the idea to revolutionize storytelling through the power of Generative AI. Mian is one of the machine learning engineers for WonderScribe, driving the integration of cutting-edge generative AI models. From fine-tuning the RAG framework to deploying advanced text and image generation models, Mian’s work ensures that WonderScribe delivers creative, engaging, and contextually relevant stories. His passion for AI innovation and storytelling shines through in every technical detail.",
    #     # "image": "pages/images/MianHaseeb.jpg",
    #     "email": "mianh1@berkeley.edu",
    # },
]

# Display team members with processed images
for member in members:
    col1, col2 = st.columns([1, 3])  # Adjust column width for better layout
    with col1:
        processed_image = process_image(member["image"])
        st.image(processed_image, use_container_width=True)
    with col2:
        st.markdown(f"### {member['name']}")
        st.markdown(f"**Role:** {member['role']}")
        st.markdown(f"**Bio:** {member['bio']}")
        st.markdown(f"**Email:** [{member['email']}](mailto:{member['email']})")
    st.write("---")
