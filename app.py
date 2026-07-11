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
    telescope_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop"
    st.image(telescope_url, use_column_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E3A8A; font-weight: 900; margin-bottom: 0;'>🌌 ASTROPHYSICS & COSMOLOGY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B7280; font-size: 1.2em; font-style: italic; margin-top: 5px;'>Icciitii Uumama Hawwaa, Sochii Urjiilee fi Bal'ina Daangaa Hin Qabne</p>", unsafe_allow_html=True)
    st.write("---")
    
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
    
    st.markdown("<p style='text-align: center; font-weight: bold; color: #4B5563; margin-bottom: 5px;'>👤 QORATAA KANNAA</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        suuraa_url = "https://raw.githubusercontent.com/kitesanegasa2012-arch/kitesa-Astro/main/qixxeessaa.jpg"
        try:
            st.image(suuraa_url, use_column_width=True, caption="Barsiisaa Qixxeessaa")
        except:
            st.warning("⚠️ Suuraan 'qixxeessaa.jpg' URL kee irratti argamuu hin dandeenye.")

    st.write("---")
    st.info("👉 Appilikeeshinii kana gadi fageenyaan dubbisuuf, gara bitaa skriinii keessanii irratti bakka **'Filannoo Qabiyyee'** jedhu tuquun boqonnaalee barbaaddan filadhaa!")

# 1. GALATAA
elif menu == "Galataa (Acknowledgement)":
    st.header("🙏 Galataa ")
    
    st.markdown("### 🛐 Uumaa Koo Waaqayyoon")
    st.write(
        "Jalqabaa fi xumura hojii koo kan ta'e, Sammuu koo naaf banee saayinsii hawwaa "
        "gadi fagoo kana keessa lixee akkan qoradhuuf humna, beekumsaa fi obsa naaf kenne, "
        "Waaqayyo Uumaa kootiif galanni guddaan, fi dhuma hin qabne haa ta'u. "
    )
     
    st.markdown("### 🔬 Gorsaa Koo ")
    st.write(
        "Appilikeeshinii Kana kalaquuf jalqabaa irraa eegale hanga dhumaatti "
        "ogummaa saayinsawaa, gorsa, qajeelcha fi deeggarsa walirraa hin cinne naaf kennaa kan turan "
        "ammas na waliin kan jiran Barsiisaa koo, Gorsaa koo fi Yuunvarsiitii Wallagaatti Barsiisaa astroonoomii "
        "fi gargaara piroosofeeraa kan ta'an **Dr. Darajjee Wakgaarii Amantee** guddaan galateeffadha."
    )
     
    st.markdown("### 🏡 Maatii Koo")
    st.write(
        "Duraan dursee, Maatiikoo, dhalachuu koo irraa eegalanii nama ta'uu kootiif na guddisuun, na barsiisuun "
        "bu'uura cimaa kan naaf kuusan, **Haadha koo** deessuu koo fi dandeessuu koo kan taatee **Aadde Mulee Baqqalaa** "
        "fi **Abbaa koo** Lafa kana irratti utubaa jireenya kootiii kan ta'aani Waan hundaan na bira dhaabbachaa jiran "
        "Barsiisaa **Nagaasaa Fayisaa** tiif obbolaankoo **Qixxaattuu Nagaasaa, Darajjee Nagaasaa, Lalisaa Nagaasaa, "
        "Eebbisaa Nagaasaa Fi Eebbisee Nagaasaa** kallattii hundaan deggersa obbolummaa naaf taasisaa hundaaf galannikoo haa ta'uuf "
        "har'a kanaan na geessan; lafee dugdaa fi ifa jireenya kooti!"
    )
     
    st.write(
        "Halkanii fi guyyaa osoo hin jedhiin, yeroo ani qo'annoo fi qorannoon rarra'ee jiru kanneen obsaan "
        "na eegaa turan, jaalala, onnee fi humna itti fufiinsaa kan naaf ta'an jaalatamtuu haadha manaa koo "
        "**Barsiistuu Araaree Taaddasaa** fi ijoollee koo, abdiwwan koo **Hiikaa** fi **Latii**-f galanni ani qabu "
        "ibsa jechaa olitti. Isin hundi keessanuu miidhagina fi utubaa jireenya kooti!"
    )

# 2. WAA'EE QORATAA (PROFILE)
elif menu == "Waa'ee Qorataa (Profile)":
    st.header("👤 Waa'ee Qorataa fi Piroofaayilii")
    st.write(
        "**Barsiisaa Qixxeessaa Nagaasaa Fayisaa** qorataa fi barsiisaa Fiiziksii fi Astroofiiziksii yoo ta'an, "
        "Yuunvarsiitii Wallagaa (Wallaga University) keessatti digrii lammaffaa (MSc) isaanii fiiziksii urjiilee fi hawwaa "
        "irratti xumuratanii jiru. Qo'annoon isaanii inni guddaan **Urjiilee Niiwutiroonii Naanna'an (Rotating Neutron Stars)** "
        "irratti kan xiyyeeffate dha."
    )
    st.markdown("""
    - **Maqaa:** Qixxeessaa Nagaasaa Fayisaa
    - **Barnoota:** MSc in Astrophysics (Wallaga University)
    - **Hojii:** Barsiisaa Fiiziksii & Qorataa Saayinsii Hawwaa
    - **Xiyyeeffannoo Qo'annoo:** Pulsars, Rotating Neutron Stars, Gravitational Waves, and Stellar Evolution.
    """)
    st.info("💡 Barsiisaa Qixxeessaan barsiisaa fi qorataa fiiziksii dhaloota boruuf ifa ta'an dha.")

# 3. SEENSA KITAABAA & HIIKA
elif menu == "Seensa Kitaabaa & Hiika":
    st.header("🌌 Seensa Kitaabaa fi Hiika Saayinsii Hawwaa")
    st.write(
        "**Astroonoomiin (Astronomy)** saayinsii waa'ee qaamolee hawwaa kan akka urjiilee, pilaaneetota, "
        "komeetota, fi gaalaaksilee qo'atu dha. Inni uumama qaamolee kanaa, fiiziksii isaanii, keemistrii fi "
        "sochii isaanii koonkireetii ta'e xiin-sammuu fi saayinsii maateemaatikaatiin addaan baasee qorata."
    )
    st.write(
        "**Hawwaan (Universe/Duniyaan)** immoo walitti qabaa waan jiru hunda tii—hanni meetaa, anniisaa (energy), "
        "yeroo (time), fi iddoo (space) hammata. Fiiziksiin fi Keemistriin bu'uura guddaa ta'anii seera uumamaa "
        "hawaa kana keessatti akkamitti akka urjiileen dhalatan, dhoo'an, fi uumaman nu hubachiisu."
    )

# 4. KAAYYOO FI MUL'ATA
elif menu == "Kaayyoo fi Mul'ata":
    st.header("🎯 Kaayyoo fi Mul'ata (Objectives & Vision)")
    st.markdown("### 📌 Kaayyoo (Objectives)")
    st.write(
        "1. Hubannoo saayinsii hawwaa fi astroofiiziksii afaan keenya, Afaan Oromootiin, hawaasa biraan gahuu.\n"
        "2. Qo'annoo gadi fagoo *Rotating Neutron Stars* fi seera *Radiative energy loss* irratti gochuun saayinsii addunyaaf gumaachuu.\n"
        "3. Barattoota gara fiiziksii fi astroomoomiitti akka dhufan kakaasuu."
    )
    st.markdown("### 👁️ Mul'ata (Vision)")
    st.write(
        "Oromiyaa fi Itoophiyaa keessatti wiirtuu qo'annoo saayinsii hawwaa kan addunyaa waliin hiriiru uumuuf "
        "bu'uura beekumsaa fi teeknoolojii ta'uu."
    )

# 5. BOQONNAA 1: SIRNA PILAANEETOTAA
elif menu == "Boqonnaa 1: Sirna Pilaaneetotaa":
    st.header("🪐 Boqonnaa 1: Sirna Pilaaneetotaa (Planetary Systems)")
    st.subheader("☀️ Uumama Sirna Aduu (Nebular Hypothesis)")
    st.write(
        "Akka yaada *Nebular Hypothesis* jedhamutti, sirni aduu keenya duumessa gaasii fi dhukkee guddaa "
        "(*solar nebula*) waggaa biiliyana 4.6 dura of irratti kuffe irraa uumame. Giddu galeessi isaa aduu "
        "yoo uumu, naannoo isaa immoo pilaaneetota uumee."
    )
    st.subheader("🪨 Pilaaneetota Dhagaa (Terrestrial Planets)")
    st.write("Pilaaneetonni aduutti dhiyoo jiran fi jabaa ta'an kunniin:")
    st.markdown("""
    * **Mercury (Meerkurii):** Pilaaneetii aduutti dhiyoo fi ishee xiqqoo dha.
    * **Venus (Benuus):** Pilaaneetii baay'ee ho'ituu fi duumessa abiddaa qabdu.
    * **Earth (Dachee):** Iddoo jireenya lubbuu qabdu tokkichaa.
    * **Mars (Maarsii):** Pilaaneetii diimtuu iron oxide-iin badhaate.
    """)

# 6. BOQONNAA 2: FIIZIKSII URJIILEE
elif menu == "Boqonnaa 2: Fiiziksii Urjiilee":
    st.header("⭐ Boqonnaa 2: Fiiziksii Urjiilee (Stellar Physics & Evolution)")
    st.write(
        "Urjiileen kan dhalatan duumessa interstellar gaasii keessatti uumama **Protostars** jedhamuun. "
        "Ho'i fi dhiibbaan giddu-galeessaa yoo dabalu, dhoohiinsa **Nuclear Fusion** (wal-itti makama hayidiroojiinii "
        "gara heeliyeemitti) eegala. Kuni madda ifa fi ho'a urjiiti."
    )
    st.subheader("📊 Hertzsprung-Russell (H-R) Diagram")
    st.write(
        "H-R Diagram-iin urjiilee *Luminosity* (ifinna) fi *Effective Temperature* (ho'a) isaanii irratti "
        "hirkachuun addaan baasa. Urjiileen jireenya isaanii keessaa baay'ee naannoo **Main Sequence** irratti dabarsu."
    )

# 7. BOQONNAA 3: COMPACT OBJECTS SADAN
elif menu == "Boqonnaa 3: Compact Objects Sadan":
    st.header("🕳️ Boqonnaa 3: Compact Objects Sadan (The Three Compact Objects)")
    st.write(
        "Urjiileen yeroo du'an bifa sadiin hafnaan isaanii uumama: "
    )
    st.markdown("""
    1. **White Dwarfs (Urjii Addaaxxiqqoo):** Urjiilee hamma aduu qaban kan dhumarratti *Electron Degeneracy Pressure*-iin utubamanii hafan.
    2. **Neutron Stars (Urjiilee Niiwutiroonii):** Urjiilee guguddaa dhoohiinsa *Supernova* kuffan irraa uumaman. Madda dhiibbaa niiwutirooniitiin dhaabatu.
    3. **Black Holes (Qullaawwan Gurraacha):** Humni kalattii gravity waan hundumaa dabalatee ifas yoo liqimsu, daangaan isaa *Event Horizon* jedhama.
    """)

# 8. H-R DIAGRAM DATA VISUALIZATION
elif menu == "H-R Diagram":
    st.header("📊 Hertzsprung-Russell (H-R) Diagram Deep Dive")
    st.write(
        "H-R Diagram-iin meeshaa fiiziksii urjiilee keessatti baay'ee barbaachisaa ta'e dha. "
        "Gadi fageenyaan yoo ilaallu, ho'i fi ifinni urjiilee akkamitti akka jijjiiramu agarsiisa."
    )
    st.markdown("""
    - **Axis-X:** Effective Temperature ($T_{eff}$ in Kelvin) - Gara bitaatti ho'aa, gara mirgaatti qorraa deema.
    - **Axis-Y:** Luminosity ($L/L_{\odot}$) - Gara irratti ifinna guddaa agarsiisa.
    """)
    st.image("https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=800&auto=format&fit=crop", caption="Urjiilee Hawwaa keessaa")

# 9. P-PDOT DIAGRAM (NEUTRON STARS)
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("🔄 P-Pdot Diagram & Rotating Neutron Stars")
    st.write(
        "Diagram-iin **P-Pdot (Period vs. Period derivative)** urjiilee niiwutiroonii (Pulsars) "
        "umrii isaanii fi hamma maagneetiksii isaanii addaan baasuuf gargaara."
    )
    st.subheader("🌌 Radiative Energy Loss ($f^6$ Relation)")
    st.write(
        "Urjiin niiwutiroonii tokko yeroo naanna'u anniisaa isaa bifa electromagnetic radiation fi gravitational waves-tiin "
        "of irraa gadi dhiisa. Anniisaa gadi dhiifamu kun sochii naannanna frequency ($f$) wajjin firooma addaa qaba:"
    )
    st.latex(r"\dot{E} \propto f^6")
    st.write(
        "Kuni firooma *model-agnostic tool* ta'ee saayinsii astroofiiziksii keessatti evolutionary characteristics "
        "urjiilee niiwutiroonii qorachuuf gargaaru dha."
    )
