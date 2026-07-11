import streamlit as st

# Maqaa Appii fi Waamicha Jalqabaa
st.set_page_config(page_title="Kitesa Astro", page_icon="🌌", layout="centered")

# --- MENU SIDEBAR (Tartiiba Sirreeffame) ---
menu = st.sidebar.selectbox(
    "Filannoo Qabiyyee:",
    [
        "Fuula Jalqabaa (Cover Page)", 
        "Seensa Kitaabaa & Hiika", 
        "Kaayyoo fi Mul'ata",
        "Baafata & Qabiyyee Kitaabichaa", 
        "H-R Diagram", 
        "P-Pdot Diagram (Neutron Stars)", 
        "Waa'ee Qorataa (Profile)",
        "Galata Addaa"
    ]
)

# 0. FUULA JALQABAA (COVER PAGE) - Design Haaraa (Halluu fi Border Bareedaa)
if menu == "Fuula Jalqabaa (Cover Page)":
    # Suuraa Teeleskooppii Hawaa onlaayinii irraa fida
    telescope_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop"
    st.image(telescope_url, use_column_width=True)
    
    # Mataduree Guddicha
    st.markdown("<h1 style='text-align: center; color: #0F172A; font-family: sans-serif; font-weight: 800; margin-bottom: 0;'>🌌 ASTROPHYSICS & COSMOLOGY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 1.2em; font-style: italic; margin-top: 5px;'>Icciitii Uumama Hawwaa, Sochii Urjiilee fi Bal'ina Daangaa Hin Qabne</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Card Border bareedaa qabu (Maqaa Kee fi Unka Qorannoo)
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

# 1. SEENSA KITAABAA & HIIKA
elif menu == "Seensa Kitaabaa & Hiika":
    st.header("📖 Seensa Kitaaba Saayinsii Hawwaa")
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
    st.subheader("🔭 Hiika Saayinsii Hawwaa fi Astroonoomii")
    st.write("**Astroonoomiin** saayinsii uumamaa wantoota qilleensa lafaatiin alatti (hawaa keessatti) argaman hunda qoratudha. Argama, geeddaramiinsa, amaloota fizikaalaa fi amala wantoota hawaa—kanneen akka pilaaneetotaa, urjiilee, gaalaaksotaa fi neebulaawwanii qorachuuf herrega, fiziksii fi keemistrii fayyadama.")

# 2. KAAYYOO FI MUL'ATA
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

# 3. BAAFATA FI QABIYYEE KITAABICHAA
elif menu == "Baafata & Qabiyyee Kitaabichaa":
    st.header("📖 Tarreefi Baafata Qabiyyee Kitaabichaa")
    st.write("Kitaabni kun gadi fageenyaan yaada bu'uuraa irraa kaasee hanga sakatta'iinsa saayinsii ammayyaatti boqonnaalee armaan gadiitti qoodama:")
    
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
    
    st.markdown("### 📘 Boqonnaa 4: Fiiziksii Urjiilee Neeutroonii Naanna'anii")
    st.write("**4.1 Pulsar Observations:** Rurrukuttaan rediyoo (radio pulses) akkamitti lafatti dhiyaata.")
    st.write("**4.2 P-Pdot Diagram:** Marsaa naanna'uu fi gadi bu'iinsa ariitii naanna'uu pulsar-ootaa.")

# 4. H-R DIAGRAM
elif menu == "H-R Diagram":
    st.header("📊 Hertzsprung-Russell (H-R) Diagram")
    st.write("**H-R Diagram**-iin wal-itti dhufeenya ho'a urjiilee (Effective Temperature) fi ifa isaanii (Luminosity) agarsiisa. Urjiileen baay'een sarara qajeelaa 'Main Sequence' jedhamu irratti argamu.")
    st.latex(r"L = 4\pi R^2 \sigma T^4")

# 5. P-PDOT DIAGRAM
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("⏱️ P-Pdot Diagram & Rotating Neutron Stars")
    st.write("**P-Pdot Diagram**-iin marsaa naanna'uu urjii Neutron Star ($P$) fi ariitii ittiin naanna'uu gadi bu'u ($\dot{P}$) walitti hidhuun gosa Pulsar-oota addaan baasuuf gargaara.")
    st.info("💡 Anniisaan dhangala'u (Radiative energy loss relation) formulaa kanaan ibsama:")
    st.latex(r"\dot{E} \propto f^6")

# 6. WAA'EE QORATAA (PROFILE)
elif menu == "Waa'ee Qorataa (Profile)":
    st.header("👤 Profile Qopheessaa / Qorataa")
    
    # Suuraa kee isa GitHub irratti ol-feete onlaayiniitti fida
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

# 7. GALATA ADDAA
elif menu == "Galata Addaa":
    st.header("🙏 Kutaa Galataa")
    st.write("---")
    st.markdown("### **Galata Addaa Fi Guddinaa**")
    st.write(
        "Kallattiidhaan kitaaba kanaafi hojii qorannoo koo dhimma saayinsii hawwaa xumuruu keessatti, "
        "gorsa, ogummaa saayinsawaa, fi deeggarsa walirraa hin cinne qajeelfama naaf kennaa kan turan "
        "**Dr. Darajjee Wakgaarii** Yuunivarsiitii Wallaggaatti Barsiisaa Astroonoomii fi gorsaa koo kan ta'an, "
        "galanni koo guutuu fi guddaadha. Gorsi keessan onnee qorannoo koo ti."
    )
    st.markdown("#### 🔬 Mataduree Qorannoo MSc:")
    st.info("📊 *'The study of Evolutionary characteristics of rotating neutron star'*")
