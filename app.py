import streamlit as st

# Maqaa Appii fi Waamicha Jalqabaa
st.set_page_config(page_title="Kitesa Astro", page_icon="🌌", layout="centered")

# ==========================================
# 🔍 KUTAA BARBAACHAA (SEARCH BAR FUNCTION)
# ==========================================
database = {
    "galata": "Galataa Acknowledgement Uumaa Koo Waaqayyoon Dr. Darajjee Wakgaarii Amantee Aadde Mulee Baqqalaa Nagaasaa Fayisaa Qixxaattuu Darajjee Lalisaa Eebbisaa Eebbisee Araaree Hiikaa Latii",
    "qorataa": "Waa'ee Qorataa Profile Barsiisaa Qixxeessaa Nagaasaa Fayisaa MSc Astrophysics Wallaga University rotating neutron star",
    "seensa": "Seensa Kitaabaa Hiika Saayinsii Hawwaa Universo Duniyaan Astroonoomiin fiziksii keemistrii",
    "kaayyoo": "Kaayyoo fi Mul'ata Objectives Vision Afaan Oromootiin Rotating Neutron Stars",
    "boqonnaa1": "Boqonnaa 1 Sirna Pilaaneetotaa Planetary Systems Uumama Sirna Aduu Nebular Hypothesis Pilaaneetota Dhagaa Mercury Venus Earth Mars",
    "boqonnaa2": "Boqonnaa 2 Fiiziksii Urjiilee Stellar Physics & Evolution Protostars Nuclear Fusion Hertzsprung-Russell H-R Diagram",
    "boqonnaa3": "Boqonnaa 3 Compact Objects Sadan White Dwarfs Electron Degeneracy Neutron Stars Supernova Black Holes Event Horizon",
    "hr_diagram": "Hertzsprung-Russell H-R Diagram Luminosity Effective Temperature Main Sequence",
    "ppdot_diagram": "P-Pdot Diagram Neutron Stars Rotating Neutron Stars Pulsar f^6 Radiative energy loss"
}

st.sidebar.markdown("### 🔍 Barbaacha (Search)")
search_query = st.sidebar.text_input("Jecha barbaaddan asitti barreessaa:", "")

menu_options = [
    "Fuula Jalqabaa (Cover Page)", 
    "Galataa (Acknowledgement)", 
    "Waa'ee Qorataa (Profile)",
    "Seensa Kitaabaa & Hiika", 
    "Kaayyoo fi Mul'ata",
    "Boqonnaa 1: Sirna Pilaaneetotaa", 
    "Boqonnaa 2: Fiiziksii Urjiilee",
    "Boqonnaa 3: Compact Objects Sadan",
    "H-R Diagram", 
    "P-Pdot Diagram (Neutron Stars)"
]

current_menu = "Fuula Jalqabaa (Cover Page)"

if search_query:
    q = search_query.lower()
    if any(word in database["galata"].lower() for word in q.split()):
        current_menu = "Galataa (Acknowledgement)"
    elif any(word in database["qorataa"].lower() for word in q.split()):
        current_menu = "Waa'ee Qorataa (Profile)"
    elif any(word in database["seensa"].lower() for word in q.split()):
        current_menu = "Seensa Kitaabaa & Hiika"
    elif any(word in database["kaayyoo"].lower() for word in q.split()):
        current_menu = "Kaayyoo fi Mul'ata"
    elif any(word in database["boqonnaa1"].lower() for word in q.split()):
        current_menu = "Boqonnaa 1: Sirna Pilaaneetotaa"
    elif any(word in database["boqonnaa2"].lower() for word in q.split()):
        current_menu = "Boqonnaa 2: Fiiziksii Urjiilee"
    elif any(word in database["boqonnaa3"].lower() for word in q.split()):
        current_menu = "Boqonnaa 3: Compact Objects Sadan"
    elif any(word in database["hr_diagram"].lower() for word in q.split()):
        current_menu = "H-R Diagram"
    elif any(word in database["ppdot_diagram"].lower() for word in q.split()):
        current_menu = "P-Pdot Diagram (Neutron Stars)"
    
    st.sidebar.success(f"🔍 '{search_query}' kanaan argameera!")

menu = st.sidebar.selectbox("Filannoo Qabiyyee:", menu_options, index=menu_options.index(current_menu))


# ==========================================
# 📂 QABIYYEEWWAN APPILIKESHINICHAA
# ==========================================

# 0. FUULA JALQABAA (COVER PAGE)
if menu == "Fuula Jalqabaa (Cover Page)":
    # Fakkii duubaa (Background telescope)
    telescope_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop"
    st.image(telescope_url, use_column_width=True)
    
    # Mataduree Guutuu
    st.markdown("<h1 style='text-align: center; color: #1E3A8A; font-weight: 900; margin-bottom: 0;'>🌌 ASTROPHYSICS & COSMOLOGY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B7280; font-size: 1.2em; font-style: italic; margin-top: 5px;'>Icciitii Uumama Hawwaa, Sochii Urjiilee fi Bal'ina Daangaa Hin Qabne</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Boorderoo Bareedaa (Card Layout) Maqaa kee fi Wallaga University hammate
    st.markdown("""
    <div style='background-color: #F8FAFC; padding: 25px; border-radius: 16px; border: 3px double #3B82F6; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); text-align: center;'>
        <h2 style='color: #D97706; font-size: 2em; font-weight: 800; margin-bottom: 5px;'>BARSIISAA QIXXEESSAA NAGAASAA FAYISAA</h2>
        <p style='font-size: 1.2em; color: #059669; font-weight: bold; margin-bottom: 15px;'>🚀 MSc Graduate / Researcher in Astrophysics</p>
        <div style='background-color: #EFF6FF; padding: 12px; border-radius: 8px; border-left: 5px solid #3B82F6;'>
            <p style='color: #1E40AF; font-size: 1.1em; margin: 0; font-weight: 600;'>🏫 WALLAGA UNIVERSITY</p>
            <p style='font-style: italic; color: #1E293B; font-size: 1em; margin-top: 5px;'><strong>Thesis:</strong> \"The study of Evolutionary characteristics of rotating neutron star\"</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    # Suuraa kee (Size 2x2) gidduutti fi boorderoo waliin
    st.markdown("<p style='text-align: center; font-weight: bold; color: #4B5563; margin-bottom: 5px;'>👤 QORATAA KANNAA</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2: # Gidduutti akka bahuuf col2 fayyadamna
        suuraa_url = "https://raw.githubusercontent.com/kitesanegasa2012-arch/kitesa-Astro/main/qixxeessaa.jpg"
        try:
            # Kaameeraa size 2x2 gochuuf width=200 madaalawaa dha
            st.image(suuraa_url, use_column_width=True, caption="Barsiisaa Qixxeessaa")
        except:
            st.warning("⚠️ Suuraan 'qixxeessaa.jpg' URL kee irratti argamuu hin dandeenye.")

    st.write("---")
    st.info("👉 Appilikeeshinii kana gadi fageenyaan dubbisuuf, gara bitaa skriinii keessanii irratti bakka **'Filannoo Qabiyyee'** jedhu tuquun boqonnaalee barbaaddan filadhaa!")

# 1. GALATAA
elif menu == "Galataa (Acknowledgement)":
    st.header("🙏 Galataa ")
     
    # 1. Waaqayyoon Galateeffachuu
    st.markdown("### 🛐 Uumaa Koo Waaqayyoon")
    st.write(
        "Jalqabaa fi xumura hojii koo kan ta'e, Sammuu koo naaf banee  saayinsii hawwaa "
        "gadi fagoo kana keessa lixee akkan qoradhuuf humna, beekumsaa fi obsa naaf kenne, "
        "Waaqayyo Uumaa kootiif galanni guddaan,  fi dhuma hin qabne haa ta'u. "
    )
     
    # 2. Gorsaa Keetiif (Dr. Darajjee)
    st.markdown("### 🔬 Gorsaa Koo ")
    st.write(
        " Appilikeeshinii Kana kalaquuf jalqabaa irraa eegale hanga dhumaatti "
        "ogummaa saayinsawaa, gorsa ,qajeelcha fi deeggarsa walirraa hin cinne naaf kennaa kan turn ammas na waliin kan jiran Barsiisaa koo,Gorsaakoo fi Yuunvarsiitii Wallagaatti Barsiisaa astroonoomii fi gargaara piroosofeeraa kan ta'an "
        "**Dr. Darajjee Wakgaarii Amantee**  guddaan galateeffadha. "
    )
     
    # 3. Maatii Keetiif (Warra Koo, Araaree, Hiikaa fi Latii)
    st.markdown("### 🏡 Maatii Koo")
     
    # Warra Keetiif (Haadha fi Abbaa)
    st.write(
        "Duraan dursee, Maatiikoo, dhalachuu koo irraa eegalanii nama ta'uu kootiif na guddisuun,na barsiisuun "
        "bu'uura cimaa kan naaf kuusan, **Haadha koo** deessuu koo fi dandeessuu koo kan taatee **Aadde Mulee Baqqalaa** fi **Abbaa koo**  Lafa kana irratti utubaa "
        "jireenya kootiii kan ta'aani Waan hundaan na bira dhaabbachaa jiran Barsiisaa **Nagaasaa Fayisaa** tiif obbolaankoo **Qixxaattuu Nagaasaa,Darajjee Nagaasa,Lalisaa Nagaasa,Eebbisaa Nagaasaa Fi EEbbisee Nagaasaa** kallattii hundaan deggersa obbolummaa naaf taasisaa hundaaf galannikoo haa ta'uuf "
        "har'a kanaan na geessan; lafee dugdaa fi ifa jireenya kooti!"
    )
     
    # Haadha Manaa fi Ijoolleedhaaf
    st.write(
        "Halkanii fi guyyaa osoo hin jedhiin, yeroo ani qo'annoo fi qorannoon rarra'ee jiru kanneen obsaan "
        "na eegaa turan, jaalala, onnee fi humna itti fufiinsaa kan naaf ta'an jaalatamtuu haadha manaa koo "
        "**Barsiistuu Araaree Taaddasaa ** fi ijoollee koo ,  **Hiikaa** fi **Latii**-f galanni ani qabu "
        "ibsa jechaa olitti. Isin hundi keessanuu miidhagina fi utubaa jireenya kooti!"
    )
