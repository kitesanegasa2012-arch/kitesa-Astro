import streamlit as st
import streamlit.components.v1 as components
import os
import base64
import re
from PIL import Image

# Page layout setup
st.set_page_config(page_title="Astiroonoomii Dashboard", layout="wide")

# ==========================================
# TOOFTAA SUURAA AUTOMATIC FUDHACHU (BASE64)
# ==========================================
def suuraa_base64_godhi(daandii_suuraa):
    """Suuraa fooldeera keessa jiru dubbisee koodii HTML simatu uuma"""
    if os.path.exists(daandii_suuraa):
        with open(daandii_suuraa, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

def html_suuraa_guuti(html_koodii):
    """HTML keessaa src='maqaa.jpg' ykn src='Kitesa Astro/maqaa.jpg' 
    kan jedhan hunda ofumaan koodii suuraatiin bakka buusa."""
    # src="..." keessaa maqaa faayilii adda baasa
    pattern = r'src=["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp))["\']'
    maqaalee_suuraa = re.findall(pattern, html_koodii, re.IGNORECASE)
    
    for daandii_suuraa in maqaalee_suuraa:
        # Maqaa faayilii qofa adda baasuu (Fkn: 'Kitesa Astro/qixxeessaa.jpg' yoo ta'e 'qixxeessaa.jpg' godha)
        maqaa_faayilii = os.path.basename(daandii_suuraa)
        
        # Kallattiin fooldeeri keessa yoo jiraate dubbisa
        b64_str = suuraa_base64_godhi(maqaa_faayilii)
        
        # Yoo achitti argamuu dide, fooldeera 'Kitesa Astro' keessaa barbaada
        if not b64_str and os.path.exists("Kitesa Astro"):
            b64_str = suuraa_base64_godhi(os.path.join("Kitesa Astro", maqaa_faayilii))
            
        if b64_str:
            ext = maqaa_faayilii.split('.')[-1].lower()
            ext = 'jpeg' if ext == 'jpg' else ext
            base64_src = f"data:image/{ext};base64,{b64_str}"
            # HTML keessatti src saniin bakka buusa
            html_koodii = html_koodii.replace(daandii_suuraa, base64_src)
            
    return html_koodii

# ==========================================
# SIDEBAR - QIXXEESSAA NAGAASAA
# ==========================================
# Daandii suuraalee mirkaneessuu (kallattiin ykn fooldeera jala)
path_qixxeessaa = "qixxeessaa.jpg" if os.path.exists("qixxeessaa.jpg") else "Kitesa Astro/qixxeessaa.jpg"
path_telescope = "telescope.jpg" if os.path.exists("telescope.jpg") else "Kitesa Astro/telescope.jpg"

with st.sidebar:
    st.title("Suura Barreessaa")
    
    # Suuraa kee
    if os.path.exists(path_qixxeessaa):
        image = Image.open(path_qixxeessaa)
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
    
    # Suuraa Teleskooppii
    if os.path.exists(path_telescope):
        st.image(path_telescope, caption="Astrophysics Research", use_container_width=True)
    
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
    if os.path.exists(path_telescope):
        cover_image = Image.open(path_telescope)
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
    file_path = "astiroonoomii.html" if os.path.exists("astiroonoomii.html") else "Kitesa Astro/astiroonoomii.html"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        # Suuraaleen HTML keessa jiran hunda automatic koodiitti jijjiiri
        html_code = html_suuraa_guuti(html_code)
        
        # HTML agarsiisuu
        components.html(html_code, height=2000, scrolling=True)
    else:
        st.error(f"Faayiliin '{file_path}' hin argamne.")
