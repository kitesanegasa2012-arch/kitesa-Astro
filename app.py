import streamlit as st

# Maqaa Appii fi Waamicha Jalqabaa
st.set_page_config(page_title="Kitesa Astro", page_icon="🌌", layout="centered")

st.title("🌌 Kitesa Astro")
st.markdown("### ASTIRONOOMII(SAAYINSII HAWWAA)")
st.write("---")

# Menu Appii keetii (Sidebar)
menu = st.sidebar.selectbox(
    "Filannoo Qabiyyee:",
    ["Hiika Saayinsii Hawwaa", "H-R Diagram", "P-Pdot Diagram (Neutron Stars)", "Baafata & Qabiyyee Kitaabichaa", "Galata fi Waraqa Qorannoo", "Waa'ee Qopheessaa"]
)
# 0. FUULA JALQABAA (COVER PAGE)
if menu == "Fuula Jalqabaa (Cover Page)":
    # Suuraa Teeleskooppii Hawaa bareedaa onlaayinii irraa fida
    telescope_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop"
    st.image(telescope_url, use_column_width=True)
    
    # Mataduree Guddicha
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🌌 ASTROPHYSICS & COSMOLOGY</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4B5563;'>Icciitii Uumama Hawwaa, Sochii Urjiilee fi Bal'ina Daangaa Hin Qabne</h3>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Maqaa Kee fi Unka Qorannoo Kee
    st.markdown("""
    <div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #1E3A8A; text-align: center;'>
        <p style='font-size: 1.2em; margin-bottom: 5px;'><strong>Qopheessaa:</strong></p>
        <h2 style='margin-top: 0; color: #111827;'>Barsiisaa Qixxeessaa Nagaasaa Fayisaa</h2>
        <p style='font-size: 1.1em; color: #374151;'>MSc Candidate in Astrophysics | Wallaga University</p>
        <p style='font-style: italic; color: #6B7280; font-size: 0.95em;'>"The study of Evolutionary characteristics of rotating neutron star"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.info("👉 Appilikeeshinii kana gadi fageenyaan dubbisuuf, gara bitaa skriinii keessanii irratti bakka **'Filannoo Qabiyyee'** jedhu tuquun boqonnaalee barbaaddan filadhaa!")
# 1. Hiika Saayinsii Hawwaa
if menu == "Hiika Saayinsii Hawwaa":
    st.header("🔭 Hiika Saayinsii Hawwaa fi Astroonoomii")
    st.write("**Astroonoomiin** saayinsii uumamaa wantoota qilleensa lafaatiin alatti (hawaa keessatti) argaman hunda qoratudha. Argama, geeddaramiinsa, amaloota fizikaalaa fi amala wantoota hawaa—kanneen akka pilaaneetotaa, urjiilee, gaalaaksotaa fi neebulaawwanii qorachuuf herrega, fiziksii fi keemistrii fayyadama..")

# 2. H-R Diagram
elif menu == "H-R Diagram":
    st.header("📊 Hertzsprung-Russell (H-R) Diagram")
    st.write("**H-R Diagram**-iin wal-itti dhufeenya ho'a urjiilee (Effective Temperature) fi ifa isaanii (Luminosity) agarsiisa. Urjiileen baay'een sarara qajeelaa 'Main Sequence' jedhamu irratti argamu.")
    st.latex(r"L = 4\pi R^2 \sigma T^4")

# 3. P-Pdot Diagram
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("⏱️ P-Pdot Diagram & Rotating Neutron Stars")
    st.write("**P-Pdot Diagram**-iin marsaa naanna'uu urjii Neutron Star ($P$) fi ariitii ittiin naanna'uu gadi bu'u ($\dot{P}$) walitti hidhuun gosa Pulsar-oota addaan baasuuf gargaara.")
    st.info("💡 Anniisaan dhangala'u (Radiative energy loss relation) formulaa kanaan ibsama:")
    st.latex(r"\dot{E} \propto f^6")

# 4. BAAFATA FI QABIYYEE KITAABICHAA
elif menu == "Baafata & Qabiyyee Kitaabichaa":
    st.header("📖 Seensafi Baafata Qabiyyee Kitaaba Saayinsii Hawwaa")
    st.write("---")
    
    st.subheader("SEENSA KITAABAA")
    st.write(
        "Duniyaan ykn hawwaan (Universe) amala guutummaatti adda ta'e, ballina dhuma hin qabne, "
        "fi icciitiiwwan heedduu qorannoodhaan bira hin gahamne of keessaa qaba. Ilmi namaa tanuma uumamaa "
        "jalqabeefi lafa kana irra qubatee kaasee, ija isaa gara gubbaatti ol deebisee waa'ee urjiilee, "
        "addeessaa, aduufi wantoota fageenya hamiitiin ala jiran xiinxaluun halkaniifi guyyaa sammuu isaa rarraasaa "
        "tureera. Saayinsiin hawwaafi fiiziksiin hawwaa (Astronomy and Astrophysics) icciitiiwwan fageenya fagoo "
        "sanatti uumamanii dhoohan, kanneen akka dhalachuufi du'uu urjiilee, guunguma dhabama duudaa (black holes), "
        "fi sochii galaaksiiwwanii seera fiiziksiifi herregaa fayyadamanii saayinsii kallattiidhaan ibsa itti kennani dha."
    )
    
    st.write("---")
    st.subheader("TARTEEFI BAAFATA QABIYYEE KITAABICHAA")
    st.markdown("### 📘 Boqonnaa 1: Sirna Pilaaneetotaa (Planetary Systems)")
    st.write("**1.1 Uumama Sirna Aduu:** Nebular Hypothesis fi akkamitti aduun dhalattee naannoo isiitti pilaaneetonni uumaman.")
    st.write("**1.2 Pilaaneetota Dhagaa:** Amaloota Mercury, Venus, Earth, fi Mars.")
    
    st.markdown("### 📘 Boqonnaa 2: Fiiziksii Urjiilee (Stellar Physics & Evolution)")
    st.write("**2.1 Protostars:** Urjiileen haaraa dhalachaa jiran fi Nuclear Fusion.")
    st.write("**2.2 Hertzsprung-Russell (H-R) Diagram:** Wal-itti dhufeenya Luminosity fi Temperature.")

    st.markdown("### 📘 Boqonnaa 3: Compact Objects Sadan (The Three Compact Objects)")
    st.write("**3.1 White Dwarfs:** Electron Degeneracy Pressure.")
    st.write("**3.2 Neutron Stars:** Supernova, Neutron Degeneracy Pressure.")
    st.write("**3.3 Black Holes:** Event Horizon fi Singularity.")

# 5. KUTAA GALATAA
elif menu == "Galata fi Waraqa Qorannoo":
    st.header("🙏 Kutaa Galataa")
    st.write("---")
    st.markdown("### **Galata Addaa Fi Guddinaa**")
    st.write(
        "Kallattiidhaan kitaaba kanaafi hojii qorannoo koo dhimma saayinsii hawwaa xumuruu keessatti, "
        "gorsa, ogummaa saayinsawaa, fi deeggarsa  walirraa hin cinne qajeelfama naaf kennaa kan turan "
        "**Dr. Darajjee Wakgaarii** Yuunversitii wallaggaatti B/saa astronoomii fi gorsaakoo   kan ta'an galanni koo "
        "guddaadha."
    )
    st.markdown("#### 🔬 Mataduree Qorannoo MSc:")
    st.info("📊 *'The study of Evolutionary characteristics of rotating neutron star'*")

# 6. Waa'ee Qopheessaa
elif menu == "Waa'ee Qopheessaa":
    st.header("👤 Profile Qopheessaa")
    
    # Suuraa kee isa GitHub irratti ol-feete onlaayiniitti fida
    suuraa_url = "https://raw.githubusercontent.com/kitesanegasa2012-arch/kitesa-Astro/main/qixxeessaa.jpg"
    
    try:
        st.image(suuraa_url, caption="Barsiisaa Qixxeessaa Nagaasaa", width=250)
    except:
        st.warning("⚠️ Suuraan kee onlaayinii irratti argamuu hin dandeenye. Maqaan faayilii keetii 'qixxeessaa.jpg' ta'uu isaa mirkaneessi.")
        
    st.subheader("Maqaan Koo Barsiisaa Qixxeessaa Nagaasaa Fayisaa ti!")
    st.write(
        "Ani Yuunivarsiitii Wallaggaatti barataa digrii lammaffaa (**MSc Astrophysics**) ti. barataa fi qorataa saayinsii hawwaa "
        "yoon ta'u, waraqaan qorannoo koo (*MSc Thesis*) mataduree **'The study of Evolutionary characteristics of rotating neutron star'** "
        "irratti xiyyeeffata."
    )
