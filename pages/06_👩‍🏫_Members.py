import streamlit as st
import base64

# Paths to the logos
logo = "pages/images/Updated_WonderS_logo.png"
#st.image("pages/images/Updated_WonderS_logo.png", width= 300)

###########################
# Add LOGO
###########################


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
                padding-top: 150px;
                background-position: 10px 10px;
                background-size: {width};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call the add_logo function with the path to your local image
add_logo(logo, "300px")

st.markdown(
    """
    <style>
    /* Style for the sidebar content */
    [data-testid="stSidebarContent"] {
        #background-color: #7dd8ff; /*#7dd8ff; Sidebar background color */
        
    }
    /* Set color for all text inside the sidebar */
    [data-testid="stSidebar"] * {
        color: #8c52ff !important;  /* Text color */
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

# Customizing the title with HTML/CSS to make it larger and green
st.markdown(
    "<h1 style='color: #5f20eb;font-size: 60px;'>About Us</h1>", unsafe_allow_html=True
)


# Define group members
members = [
    {
        "name": "Jay Prakash",
        "role": "Product Management, GenAI, AWS architecure",
        "bio": "Jay is the technical backbone of WonderScribe, leading the development of the platform’s robust AWS architecture. With expertise in cloud-based solutions and Generative AI, Jay ensures the platform's seamless integration of services like API Gateway, Lambda, and Bedrock. His focus on scalability and efficiency has been instrumental in building a secure and reliable foundation for WonderScribe's innovative storytelling capabilities.",
        "image": "pages/images/Jay_Profile_pic.jpg",
        "email": "jprakash@berkeley.edu",
    },
    {
        "name": "Jailynne Estevez",
        "role": "Program Management, UI/UX Design, Presentation Development",
        "bio": "Jailynne brings creativity and precision to WonderScribe, playing a key role in crafting a user-friendly and engaging platform for children and parents. She has helped design an intuitive interface that ensures a seamless storytelling experience while also leading the development of presentations, scripts, and pitches to effectively showcase the project’s value. Jailynne’s efforts extend beyond design and communication, as she actively collaborates with the team to bridge technical development with user needs. Her dedication to WonderScribe’s mission has been pivotal in creating a platform that fosters creativity, learning, and imagination for all.",
        "image": "pages/images/jailynne.png",
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
        "role": "ML, Data & Analytics, UI/UX Design, Model Development",
        "bio": "Natsnet’s dual focus on data exploration and design brings WonderScribe’s creative vision to life. She leads exploratory data analysis, ensuring the platform leverages child-friendly and culturally diverse datasets. Additionally, her contributions to user interface design make WonderScribe an intuitive and engaging platform for children and parents alike. Her ability to merge data insights with user-centric design is a key driver of the project’s success.",
        "image": "pages/images/Natsnet Demoz.jfif",
        "email": "ndemoz@berkeley.edu",
    },
    {
        "name": "Wilford Bradford",
        "role": "SME, Model Development",
        "bio": "Wil lends his expertise as a subject matter expert to refine WonderScribe’s storytelling framework. His work focuses on aligning the platform’s AI capabilities with user expectations, ensuring every story element resonates with children and their imaginations. Wil also collaborates on model development, emphasizing inclusivity and quality across WonderScribe’s texts and images.",
        "image": "pages/images/WilfordBradford.jfif",
        "email": "wbradford@berkeley.edu",
    },
]

# Set up the About Us section
st.write("")

# Iterate over each group member and display their details
for member in members:
    # Create a two-column layout: image on the left, bio/role on the right
    col1, col2 = st.columns([1, 2])  # Adjust column width as needed

    with col1:
        st.image(member["image"], width=150)  # Display member's image

    with col2:
        st.subheader(member["name"])
        st.write(f"**Role:** {member['role']}")
        st.write(f"**Bio:** {member['bio']}")
        st.write(f"**Email Address:** {member['email']}")

    st.write("---")  # Add a horizontal divider between members
