import streamlit as st
import streamlit.components.v1 as components
import os
from PIL import Image

# Page layout setup
st.set_page_config(page_title="Astiroonoomii Dashboard", layout="wide")

# Sidebar - Qixxeessaa Nagaasaa
with st.sidebar:
    st.title("Suura Barreessaa")
    
    # Suuraa kee
    if os.path.exists("qixxeessaa.jpg"):
        image = Image.open("qixxeessaa.jpg")
        st.image(image, caption="Qixxeessaa Nagaasaa", use_container_width=True)
    else:
        st.warning("Suuraan 'qixxeessaa.jpg' hin argamne.")

    st.write("---")
    
    # Suuraa Teleskooppii (Fayyadamii: telescope.jpg jedhii save godhi folder kee keessatti)
    if os.path.exists("telescope.jpg"):
        st.image("telescope.jpg", caption="Astrophysics Research", use_container_width=True)
    
    st.write("---")
    
    # Search Bar
    search_query = st.text_input("🔍 Search documents...", "")
    if search_query:
        st.write(f"Searching for: {search_query}")

# HTML faayilii dubbisuu fi agarsiisuu
file_path = "astiroonoomii.html"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # HTML agarsiisuu
    components.html(html_code, height=2000, scrolling=True)
else:
    st.error(f"Faayiliin '{file_path}' hin argamne.")