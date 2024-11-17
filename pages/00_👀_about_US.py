import streamlit as st

# col1, col2  = st.columns(2, vertical_alignment="center")
# # col1, col2 = st.columns(2, horizontal_alignment="left")
# with col1:
#     st.image("pages/WS_Logo.png", width=150)
# with col2:
#     st.write("")

# Test Background color
 background: #ff0099; 
 background: -webkit-linear-gradient(to right, #ff0099, #493240); 
 background: linear-gradient(to right, #ff0099, #493240);"

st.markdown("""
<style>
body {
  background: #ff0099; 
  background: -webkit-linear-gradient(to right, #ff0099, #493240); 
  background: linear-gradient(to right, #ff0099, #493240); 
}
</style>
    """, unsafe_allow_html=True)
 # +++++++
                              
st.image("pages/images/WonderScribeLogo.png", width=150)
st.title(" Welcome to WonderScribe")
st.write(
"""
We are a passionate team of authors, educators, and creatives on a mission to ignite young readers' imaginations
everywhere. We believe in the power of stories to transport children to magical words, introduce them to 
fascinating characters, and inspire endless possibilities.

At WonderScribe, we use cutting-edge technology, including AI and advanced language models, to create a unique
storytelling experience. Our platform allows kids to become co-authors of their adventures, customizing tales
to reflect their dreams, personalities, and imaginations.

We aim to make reading fun, interactive, and accessible to all children, no matter where they are. Through our
innovative platform, we hope to foster a love of reading, spark creativity, and encourage every child to believe 
in the magic of their own stories

Join us on this exciting journey and watch your child's imagination soar!
""")
