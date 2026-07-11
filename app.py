import streamlit as st
import numpy as np
import plotly.graph_objects as go
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
    st.markdown("<p style='text-align: center; font-weight: bold; color: #4B5563; margin-bottom: 5px;'>👤 SUURA QOPHEESSAA</p>", unsafe_allow_html=True)
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
        "**Barsiistuu Araaree Taaddasaa ** fi ijoollee koo , abdiwwan koo kan ta'an **Hiikaa** fi **Latii**-f galanni ani qabu "
        "ibsa jechaa olitti. Isin hundi keessanuu miidhagina fi utubaa jireenya kooti!"
    )
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
    st.header("📖 Seensa Appilikeeshinii fi Hiika")
    st.write(
        "Baga gara Appilikeeshinii Saayinsii Hawwaa fi Astroofiiziksii (Astrophysics & Cosmology) "
        "kan barsiisaa fi qorataa Qixxeessaa Nagaasaatiin qophaa'etti nagaan dhuftan! "
        "Appilikeeshiniin kun icciitiiwwan hawwaa gadi fagoo, ballina uumamaa dhuma hin qabne, fi "
        "sochiiwwan urjiilee seera fiiziksii fi herregaatiin gadi fageenyaan kan xiinxalu dha. "
        "Keessattuu, qorannoo saayinsawaa mataduree *'The study of Evolutionary characteristics of rotating neutron star'* "
        "jedhu irratti xiyyeeffachuun, jijjiirama 'angular momentum', dhiibbaa 'braking index', fi dhabama anniisaa "
        "raadiyaashinii ($f^6$) urjiilee neutron star irratti uumamu hubachuuf riqicha guddaa dha."
    )
    st.write(
        "Kun uummata keenyaaf, keessattuu barattootaa fi qorattoota afaan kootiin saayinsii hawwaa argachuu "
        "barbaadaniif ifa guddaa kan guraaruu fi hubannoo gadi fagoo kan kennu dha."
    )
    st.write("---")
    st.subheader("🔭 Hiika Saayinsii Hawwaa fi Astroofiiziksii")
    st.write(
        "**Astroofiiziksiin (Astrophysics):** Damee saayinsii astroonoomii ta'ee, seera fiiziksii fi keemistrii "
        "fayyadamuudhaan geeddaramiinsa, amaloota fizikaalaa, dhalachuu fi du'uu wantoota hawaa keessatti argamanii—kanneen akka "
        "urjiilee, pilaaneetotaa, neebulaawwanii, fi gaalaaksotaa kan qoratu dha. Appilikeeshiniin kunis hiika saayinsawaa "
        "kanneen gama koodiifi diagramootaan gadi fageenyaan isiniif ibsa."
    )
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
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("🌌 Rotating Neutron Star & Radiative Energy Loss")
    st.write(
        "Kutaan kun qorannoo kee isa *'The study of Evolutionary characteristics of rotating neutron star'* "
        "jedhu kallattiidhaan kan ibsu dha. Frequency urjii sanaa ($f$) yoo dabalu, "
        "anniisaan raadiyaashiniidhaan dhabamu seera $f^6$ kanaan ariitiidhaan dabalataa deema."
    )
    
    st.write("---")
    
    # --- INPUTS (SLIDERS) ---
    col1, col2 = st.columns(2)
    with col1:
        f = st.slider("Rotation Frequency (f in Hz):", min_value=10, max_value=1000, value=300, step=10)
    with col2:
        I_inertia = st.slider("Moment of Inertia ($I$ in $10^{45}\text{ g}\cdot\text{cm}^2$):", min_value=0.5, max_value=3.0, value=1.0, step=0.1)
    
    # --- MATH & CALCULATION ($E_{dot} \propto f^6$) ---
    # Equation simple simulation model
    f_range = np.linspace(10, 1000, 100)
    # E_dot proportional to I * f^6
    E_dot_range = (I_inertia * 1e45) * (f_range ** 6) * 1e-15  # Scaled for visual graph
    E_dot_current = (I_inertia * 1e45) * (f ** 6) * 1e-15
    
    # --- PLOTLY CHART ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=f_range, y=E_dot_range, mode='lines', name='f^6 Scaling', line=dict(color='#3B82F6', width=3)))
    fig.add_trace(go.Scatter(x=[f], y=[E_dot_current], mode='markers+text', name='Urjii Filatame', 
                             marker=dict(color='#D97706', size=14, symbol='star'),
                             text=[f"{f} Hz"], textposition="top left"))
    
    fig.update_layout(
        title="Frequency vs Radiative Energy Loss",
        xaxis_title="Rotation Frequency (f in Hz)",
        yaxis_title="Energy Loss Rate (Arbitrary Scale)",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_column_width=True)
    
    # --- INTERACTIVE NOTE ---
    st.success(f"💡 Kiilomeetira ariitii {f} Hz kanaan, urjiin neutron star sun anniisaa hammana guraaraa jirti!")
# 9. P-PDOT DIAGRAM
elif menu == "P-Pdot Diagram (Neutron Stars)":
    st.header("⏱️ P-Pdot Diagram & Rotating Neutron Stars")
    st.write("**P-Pdot Diagram**-iin marsaa naanna'uu urjii Neutron Star ($P$) fi ariitii ittiin naanna'uu gadi bu'u ($\dot{P}$) walitti hidhuun gosa Pulsar-oota addaan baasa.")
    st.info("💡 Anniisaan dhangala'u (Radiative energy loss relation) formulaa kanaan ibsama:")
    st.latex(r"\dot{E} \propto f^6")
