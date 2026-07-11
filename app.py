import streamlit as st

# Maqaa Appii fi Waamicha Jalqabaa
st.set_page_config(page_title="Kitesa Astro", page_icon="🌌", layout="centered")

# ==========================================
# 🔍 KUTAA BARBAACHAA (SEARCH FUNCTION)
# ==========================================
# Qabiyyee appii keetii hunda as jalatti kuusna, search bar-ichi as keessaa barbaada
database = {
    "cover": "Astrophysics & Cosmology Icciitii Uumama Hawwaa, Sochii Urjiilee Barsiisaa Qixxeessaa Nagaasaa Fayisaa Wallaga University Thesis Rotating neutron star",
    "galata": "Kutaa Galataa Addaa Dr. Darajjee Wakgaarii Yuunivarsiitii Wallaggaatti Barsiisaa Astroonoomii gorsaa koo",
    "qorataa": "Profile Qopheessaa Qorataa Barsiisaa Qixxeessaa Nagaasaa Fayisaa MSc Astrophysics Wallaga University rotating neutron star",
    "seensa": "Seensa Kitaaba Saayinsii Hawwaa Universo Duniyaan Astroonoomiin saayinsii uumamaa herrega fiziksii fi keemistrii",
    "kaayyoo": "Kaayyoo fi Mul'ata Objectives Vision Afaan Oromootiin dhiyeessuu Rotating Neutron Stars",
    "boqonnaa1": "Boqonnaa 1 Sirna Pilaaneetotaa Planetary Systems Uumama Sirna Aduu Nebular Hypothesis Pilaaneetota Dhagaa Mercury Venus Earth Mars",
    "boqonnaa2": "Boqonnaa 2 Fiiziksii Urjiilee Stellar Physics & Evolution Protostars Nuclear Fusion Hertzsprung-Russell H-R Diagram Luminosity Temperature",
    "boqonnaa3": "Boqonnaa 3 Compact Objects Sadan White Dwarfs Electron Degeneracy Pressure Neutron Stars Supernova Neutron Degeneracy Pressure Black Holes Event Horizon Singularity",
    "hr_diagram": "Hertzsprung-Russell H-R Diagram Luminosity Effective Temperature Main Sequence L = 4pi R^2 sigma T^4",
    "ppdot_diagram": "P-Pdot Diagram Neutron Stars Rotating Neutron Stars Pulsar E = f^6 Radiative energy loss"
}

st.sidebar.markdown("### 🔍 Barbaacha (Search)")
search_query = st.sidebar.text_input("Jecha barbaaddan asitti barreessaa:", "")

# Tartiiba menu sidebar
menu_options = [
    "Fuula Jalqabaa (Cover Page)", 
    "Kutaa Galataa",
    "Waa'ee Qorataa (Profile)",
    "Seensa Kitaabaa & Hiika", 
    "Kaayyoo fi Mul'ata",
    "Boqonnaa 1: Sirna Pilaaneetotaa", 
    "Boqonnaa 2: Fiiziksii Urjiilee",
    "Boqonnaa 3: Compact Objects Sadan",
    "H-R Diagram", 
    "P-Pdot Diagram (Neutron Stars)"
]

# Yoo namni tokko search bar fayyadame, menu ofumaan jijjiirama
current_menu = "Fuula Jalqabaa (Cover Page)"

if search_query:
    q = search_query.lower()
    if any(word in database["galata"].lower() for word in q.split()):
        current_menu = "Kutaa Galataa"
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

# Menu dhumarratti saagma
menu = st.sidebar.selectbox("Filannoo Qabiyyee:", menu_options, index=menu_options.index(current_menu))


# ==========================================
# 📂 QABIYYEEWWAN APPILIKESHINICHAA
# ==========================================

# 0. FUULA JALQABAA (COVER PAGE)
if menu == "Fuula Jalqabaa (Cover Page)":
    telescope_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop"
    st.image(telescope_url, use_column_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #0F172A; font-family: sans-serif; font-weight: 800; margin-bottom: 0;'>🌌 ASTROPHYSICS & COSMOLOGY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 1.2em; font-style: italic; margin-top: 5px;'>Icciitii Uumama Hawwaa, Sochii Urjiilee fi Bal'ina Daangaa Hin Qabne</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Card Border bareedaa qabu
    st.markdown("""
    <div style='background-color: #FAFCDA; padding: 25px; border-radius: 12px; border: 2px solid #0EA5E9; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); text-align: center;'>
        <p style='font-size: 1.1em; color: #0284C7; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px;'>MSc RESEARCH FRAMEWORK</p>
        <h2 style='margin-top: 0; color: #0F172A; font-size: 1.8em; font-weight: 700;'>Barsiisaa Qixxeessaa Nagaasaa Fayisaa</h2>
        <p style='font-size: 1.1em; color: #334155; margin-bottom: 15px;'>MSc Candidate in Astrophysics | Wallaga University</p>
        <div style='background-color: #FFFFFF; padding: 10px; border-radius: 8px; border-left: 4px solid #F59E0B;'>
            <p style='font-style: italic; color: #475569; font-size: 1em; margin: 0;'><strong>Thesis Title:</strong> "The study of Evolutionary characteristics of rotating neutron star"</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("👉 Appilikeeshinii kana gadi fageenyaan dubbisuuf, gara bitaa skriinii keessanii irratti bakka **'Filannoo Qabiyyee'** jedhu tuquun boqonnaalee barbaaddan filadhaa!")

# 1. KUTAA GALATAA
elif menu == "Kutaa Galataa":
    st.header("🙏 Kutaa Galataa Addaa")
    st.write(
        "Kallattiidhaan kitaaba kanaafi hojii qorannoo koo dhimma saayinsii hawwaa xumuruu keessatti, "
        "gorsa, ogummaa saayinsawaa, fi deeggarsa walirraa hin cinne qajeelfama naaf kennaa kan turan "
        "**Dr. Darajjee Wakgaarii** Yuunivarsiitii Wallaggaatti Barsiisaa Astroonoomii fi gorsaa koo kan ta'an, "
        "galanni koo guutuu fi guddaadha. Gorsi keessan onnee qorannoo koo ti."
    )
    st.markdown("#### 🔬 Mataduree Qorannoo MSc:")
    st.info("📊 *'The study of Evolutionary characteristics of rotating neutron star'*")

# 2. WAA'EE QORATAA (PROFILE)
elif menu == "Waa'ee Qorataa (Profile)":
    st.header("👤 Profile Qopheessaa / Qorataa")
    suuraa_url = "https://raw.githubusercontent.com/kitesanegasa2012-arch/kitesa-Astro/main/qixxeessaa.jpg"
    try:
        st.image(suuraa_url, caption="Barsiisaa Qixxeessaa Nagaasaa", width=250)
    except:
        st.warning("⚠️ Suuraan kee onlaayinii irratti argamuu hin dandeenye. Maqaan faayilii keetii 'qixxeessaa.jpg' ta'uu isaa mirkaneessi.")
        
    st.subheader("Maqaan Koo Barsiisaa Qixxeessaa Nagaasaa Fayisaa ti!")
    st.write(
        "Ani Yuunivarsiitii Wallaggaatti barataa digrii lammaffaa (**MSc Astrophysics**) ti. Barataa fi qorataa saayinsii hawwaa "
        "yoon ta'u, waraqaan qorannoo koo (*MSc Thesis*) mataduree **'The study of Evolutionary characteristics of rotating neutron star'** "
        "irratti xiyyeeffata."
    )

# 3. SEENSA KITAABAA & HIIKA
elif menu == "Seensa Kitaabaa & Hiika":
    st.header("📖 Seensa Kitaaba Saayinsii Hawwaa")
    st.write(
        "Duniyaan ykn hawwaan (Universe) amala guutummaatti adda ta'e, ballina dhuma hin qabne, "
        "fi icciitiiwwan heedduu qorannoodhaan bira hin gahamne of keessaa qaba. Ilmi namaa tanuma uumamaa "
        "jalqabeefi lafa kana irra guudunfamee kaasee, ija isaa gara gubbaatti ol deebisee waa'ee urjiilee, "
        "addeessaa, aduufi wantoota fageenya hamiitiin ala jiran xiinxaluun halkaniifi guyyaa sammuu isaa rarraasaa "
        "tureera. Saayinsiin hawwaafi fiiziksiin hawwaa (Astronomy and Astrophysics) icciitiiwwan fageenya fagoo "
        "sanatti uumamanii dhoohan, kanneen akka dhalachuufi du'uu urjiilee, guunguma dhabama duudaa (black holes), "
        "fi sochii galaaksiiwwanii seera fiiziksiifi herregaa fayyadamanii saayinsii kallattiidhaan ibsa itti kennani dha."
    )
    st.write("---")
    st.subheader("🔭 Hiika Saayinsii Hawwaa fi Astroonoomii")
    st.write("**Astroonoomiin** saayinsii uumamaa wantoota qilleensa lafaatiin alatti (hawaa keessatti) argaman hunda qoratudha. Argama, geeddaramiinsa, amaloota fizikaalaa fi amala wantoota hawaa—kanneen akka pilaaneetotaa, urjiilee, gaalaaksotaa fi neebulaawwanii qorachuuf herrega, fiziksii fi keemistrii fayyadama.")

# 4. KAAYYOO FI MUL'ATA
elif menu == "Kaayyoo fi Mul'ata":
    st.header("🎯 Kaayyoo fi Mul'ata Appilikeeshinichaa")
    st.subheader("📌 Kaayyoo (Objectives)")
    st.write(
        "1. Barattoota, barsiistota fi jaallattoota saayinsii hawwaatiif odeeffannoo fi qorannoowwan "
        "Astrofiiziksii ammayyaa bifa salphaa ta'een Afaan Oromootiin dhiyeessuu.\n"
        "2. Icciitii urjiilee fi qorannoo olaanaa (kan akka Rotating Neutron Stars) gara hawaasaatti gadi buusuu.\n"
        "3. Dhaloota haaraa dhimma kanaan qorannoo gochuuf fedhii qabaniif bu'uura guutuu ta'uu."
    )
    st.subheader("👁️ Mul'ata (Vision)")
    st.write(
        "Saayinsii hawwaafi fiiziksii ammayyaa afaan keenyaan bal'isanii sadarkaa qorannoo addunyaatti "
        "cesisuu fi ogeessota afaan kanaan damee koflee hawaa keessatti sakatta'an horachuu."
    )

# 5. BOQONNAA 1
elif menu == "Boqonnaa 1: Sirna Pilaaneetotaa":
    st.header("📘 Boqonnaa 1: Sirna Pilaaneetotaa (Planetary Systems)")
    st.write("---")
    st.markdown("### **1.1 Uumama Sirna Aduu**")
    st.write("Nebular Hypothesis fi akkamitti aduun dhalattee naannoo isiitti pilaaneetonni uumaman dhiyeessa.")
    st.markdown("### **1.2 Pilaaneetota Dhagaa**")
    st.write("Amaloota gadi fageenyaa kanneen akka Mercury, Venus, Earth, fi Mars.")

# 6. BOQONNAA 2
elif menu == "Boqonnaa 2: Fiiziksii Urjiilee":
    st.header("📘 Boqonnaa 2: Fiiziksii Urjiilee (Stellar Physics & Evolution)")
    st.write("---")
    st.markdown("### **2.1 Protostars**")
    st.write("Urjiileen haaraa dhalachaa jiran fi Nuclear Fusion keessatti amala agarsiifamu.")
    st.markdown("### **2.2 Hertzsprung-Russell (H-R) Diagram**")
    st.write("Wal-itti dhufeenya Luminosity fi Temperature urjiilee gidduu jiru ibsa.")

# 7. BOQONNAA 3
elif menu == "Boqonnaa 3: Compact Objects Sadan":
    st.header("📘 Boqonnaa 3: Compact Objects Sadan (The Three Compact Objects)")
    st.write("---")
    st.write("**3.1 White Dwarfs:** Electron Degeneracy Pressure.\n\n"
             "**3.2 Neutron Stars:** Supernova, Neutron Degeneracy Pressure.\n\n"
             "**3.3 Black Holes:** Event Horizon fi Singularity.")

# 8. H-R DIAGRAM
elif menu == "H-R Diagram":
    st.header("📊 Hertzsprung-Russell (H-R) Diagram")
    st.write("**H-R Diagram**-iin wal-itti dhufeenya ho'a urjiilee (Effective Temperature) fi ifa isaanii (Luminosity) agarsiisa.")
    st.latex(r"L = 4\pi R^2 \sigma T^4")

# 9. P-PDOT DIAGRAM
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("⏱️ P-Pdot Diagram & Rotating Neutron Stars")
    st.write("**P-Pdot Diagram**-iin marsaa naanna'uu urjii Neutron Star ($P$) fi ariitii ittiin naanna'uu gadi bu'u ($\dot{P}$) walitti hidhuun gosa Pulsar-oota addaan baasa.")
    st.info("💡 Anniisaan dhangala'u (Radiative energy loss relation) formulaa kanaan ibsama:")
    st.latex(r"\dot{E} \propto f^6")
