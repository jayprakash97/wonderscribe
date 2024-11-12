import streamlit as st
import base64

# Paths to the logos
logo = "./images/logo4.png"

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
add_logo(logo, "200px")

st.markdown(
    """
    <style>
    /* Style for the sidebar content */
    [data-testid="stSidebarContent"] {
        background-color: white; /*#bac9b9; Sidebar background color */
    }
    /* Set color for all text inside the sidebar */
    [data-testid="stSidebar"] * {
        color: #3b8bc2 !important;  /* Text color */
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
        background-color: #d2e7ae;  /* #c0dc8f Light gray-green */
    }
    .custom-label{
        color: #3b8bc2;
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
    "<h1 style='color: #4b7170;font-size: 60px;'>About Us</h1>", unsafe_allow_html=True
)


# Define group members
members = [
    {
        "name": "Victor Brew",
        "role": "EDA, Model Development",
        "bio": "bio...",
        "image": "./images/victor.png",
        "email": "vbrew@berkeley.edu",
    },
    {
        "name": "Nat Buisson",
        "role": "Project Management, UI/UX",
        "bio": "bio...",
        "image": "./images/nat.jpeg",
        "email": "nbuisson@berkeley.edu",
    },
    {
        "name": "Alex Hubbard",
        "role": "SME, Model Development",
        "bio": "bio...",
        "image": "./images/alex.png",
        "email": "alex.hubbard@berkeley.edu",
    },
    {
        "name": "Elias Tavarez",
        "role": "ML Engineering, GenAI",
        "bio": "bio...",
        "image": "./images/elias.png",
        "email": "etav@berkeley.edu",
    },
    {
        "name": "Ruiyu Zhou",
        "role": "EDA, Model Development",
        "bio": "bio...",
        "image": "./images/ruiyu.jpeg",
        "email": "rzhou9@berkeley.edu",
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
