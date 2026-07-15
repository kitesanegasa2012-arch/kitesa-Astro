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

    # --- FILANNOO FUULAA (NAVIGATION) ---
    page = st.radio(
        "Gara fuula dambalii deemi:",
        ["🏠 Fuula Jalqabaa", "📊 Astiroonoomii Dashboard"]
    )
    
    st.write("---")
    
    # Suuraa Teleskooppii (Fayyadamii: telescope.jpg jedhii save godhi folder kee keessatti)
    if os.path.exists("telescope.jpg"):
        st.image("telescope.jpg", caption="Astrophysics Research", use_container_width=True)
    
    st.write("---")
    
    # Search Bar
    search_query = st.text_input("🔍 Search documents...", "")
    if search_query:
        st.write(f"Searching for: {search_query}")

# ==========================================
# LOGIC FUULAWWANAA
# ==========================================

# 1. FUULA JALQABAA (COVER PAGE)
if page == "🏠 Fuula Jalqabaa":
    # Slogan kee fi Maqaa kee
    st.markdown(
        "<h1 style='text-align: center; color: #1E90FF; font-family: sans-serif; font-weight: bold;'>"
        "🌌 SAMIIN QE'EE SAAYINSIITI!</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align: center; color: #FFFFFF; font-family: sans-serif;'>"
        "KITESA NEGASA FEYISA</h3>", 
        unsafe_allow_html=True
    )
    st.write("---")
    
    # Suuraa telescope.jpg cover irratti fiduu
    if os.path.exists("telescope.jpg"):
        cover_image = Image.open("telescope.jpg")
        st.image(cover_image, caption="Astrophysics & Space Exploration", use_container_width=True)
    else:
        st.warning(
            "Suuraan 'telescope.jpg' cover page irratti argamuuf folder kee keessa hin jiru. "
            "Maaloo suuraa teleskooppii 'telescope.jpg' maqaa kanaan save gochuu kee mirkaneeffadhu."
        )
        
    st.write("---")
    st.markdown(
        """
        <div style='text-align: center; font-size: 18px; color: #888888;'>
            👋 Baga gara Appilikeeshinii Astiroonoomii fi Astroofiiziksii kootti nagaan dhuftan. <br>
            Gara <b>Astiroonoomii Dashboard</b> cehuuf sidebar (bitaa) irratti filannoo '📊 Astiroonoomii Dashboard' jedhu cuqaasaa.
        </div>
        """, 
        unsafe_allow_html=True
    )

# 2. DASHBOARD (HTML EMBED)
elif page == "📊 Astiroonoomii Dashboard":
    # HTML faayilii dubbisuu fi agarsiisuu
    file_path = "astiroonoomii.html"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        # HTML agarsiisuu
        components.html(html_code, height=2000, scrolling=True)
    else:
        st.error(f"Faayiliin '{file_path}' hin argamne.")
