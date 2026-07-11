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

import streamlit as st
# --- 2. QABIYYEE KITAABAA ---
if menu == "Boqonnaa 2: Sirna Pilaaneetotaa":
    st.header("🪐 Boqonnaa 2: Sirna Pilaaneetotaa")
    st.write("Qabiyyeen boqonnaa kanaa asitti dhiyaata...")

elif menu == "Boqonnaa 1: Seensa Astiroonoomii fi Astroofiiziksii":
    st.header("✨ Boqonnaa 1: Seensa Astiroonoomii fi Astroofiiziksii")
    st.write(
        "Uumama keenya keessatti, gaaffileen hunda caalaa nama haasofsiisanii fi sammuu namaa kakaasan "
        "tokko tokko kan ka'an yeroo nuti halkan gara hawwaa (samii) ol ilaallu dha. \"Urjiileen sun maali?\", "
        "\"Uumama hundaa kan uume maali?\", \"Nutis hawwaa kana keessatti bakka akkamii qabna?\" "
        "Gaaffilee kana hundaaf deebii saayinsaawaa kan kennu saayinsii hawwaa (space science) dha."
    )
    st.write(
        "Saayinsiin hawwaa dameewwan guguddoo hedduu kan qabu yoo ta'u, isaan keessaa isaan jalqabaa fi "
        "bu'uuraa kan ta'an **Astiroonoomii** fi **Astroofiiziksii** dha. Boqonnaa kana keessatti saayinsiiwwan "
        "kana maalummaa isaanii, garaagarummaa isaanii fi akkamitti akka qo'ataman bal'inaan ilaalla."
    )

    st.divider()

    st.subheader("🔭 1.1. Maalummaa Astiroonoomii (What is Astronomy?)")
    st.write(
        "Astiroonoomiin saayinsii uumamaa (natural science) isa jalqabaa fi bohaarsaa ta'e dha. Innis "
        "qo'annoo saayinsaawaa qaamolee hawwaa fi raawwiiwwan lafaan ala jiran hunda qo'atu dha. Qo'annoon kun "
        "urjiilee, pilaaneetota, bakkalchaa, addeessa, aduu, qorsaa (comets), astirooyidoota, duumessoota "
        "gaazii (nebulae), gaalaaksiiwwanii fi dhimmoota lafaan ala jiran hunda of keessatti hammata."
    )

    st.markdown("#### 📜 Maqaa fi Hiika Isaa:")
    st.markdown("""
    Jechi **"Astiroonoomii"** jedhu jechoota Afaan Giriikii lama irraa dhufe:
    * **"Astron"** - hiikni isaa "Urjii" (Star) jechu dha.
    * **"Nomos"** - hiikni isaa "Seera" ykn "Bulchiinsa" (Law/Culture) jechu dha.

    Walumaagala, astiroonoomii jechuun **"Seera Urjiilee"** ykn **"Seera Hawwaa Qo'achuu"** jedhamuun hiikama.
    """)

    st.markdown("#### 📂 Dameewwan Astiroonoomii:")
    st.write("Astiroonoomiin haala sadiin qoodamee qo'atama:")
    st.markdown("""
    1. **Astiroonoomii Ilaalchaa (Observational Astronomy):** Kun meeshaalee akka teleskooppii fayyadamuun ifaa fi daataa qaamolee hawwaa irraa dhufu walitti qabuu fi xiinxaluu irratti xiyyeeffata.
    2. **Astiroonoomii Tiyoorii (Theoretical Astronomy):** Kun immoo herrega, koodii kompiitaraa fi moodeloota fiiziksii fayyadamuun amala qaamolee hawwaa ibsuu fi raaguu irratti hojjeta.
    """)

    st.divider()

    st.subheader("⚛️ 1.2. Maalummaa Astroofiiziksii (What is Astrophysics?)")
    st.write(
        "Astroofiiziksiin damee astiroonoomii ta'ee, seera fi herrega fiiziksii fi kemistrii fayyadamuun "
        "uumama, adeemsa, fi amala qaamolee hawwaa qo'ata. Yoo astiroonoomiin \"bakka\" qaamoleen hawwaa jiran "
        "nuti himu, astroofiiziksiin immoo \"maaliif\" fi \"akkamitti\" akka isaan hojjetan seera fiiziksiitiin ibsa."
    )

    st.markdown("#### 📜 Maqaa fi Hiika Isaa:")
    st.markdown("""
    Jechi **"Astroofiiziksii"** jedhu dhufeenyi isaa:
    * **"Astro"** - Urjii ykn Hawwaa.
    * **"Physics"** - Qo'annoo amala maateerii (matter) fi anniisaa (energy).

    Walumaagala, astroofiiziksiin fiiziksii urjiilee fi dhimmoota hawwaa qo'atu dha.
    """)

    st.markdown("#### 🔬 Adeemsa Qo'annoo Astroofiiziksii:")
    st.write("Astroofiiziksiin dhimmoota armaan gadii gadi fageenyaan qorata:")
    st.markdown("""
    * **Uumama fi Du'a Urjiilee:** Urjiin tokko akkamitti uumama? Keessa isheetti anniisaa akkamii uumti? Yeroo duutu maaltu ta'a (fkn, Black Hole ykn Supernova)?
    * **Harkisa Uumamaa (Gravity):** Harkisni uumamaa akkamitti pilaaneetota, urjiilee fi gaalaaksiiwwan tokkoon tokkoo isaanii walitti qabee akka qabu qorata.
    * **Raadiyaashinii (Radiation):** Ifni fi tamsasni anniisaa hawwaa keessa jiru akkamitti akka deemu fi maateerii keessa dabarru qorata.
    """)

    st.divider()

    st.subheader("📊 1.3. Garaagarummaa fi Walitti-dhufeenya Isaanii")
    st.write(
        "Yeroo baay'ee namoonni astiroonoomii fi astroofiiziksii walitti maqsu. Haa ta'u malee, garaagarummaa qabu:"
    )
    st.markdown("""
    | Gidduu-galeessa | Astiroonoomii (Astronomy) | Astroofiiziksii (Astrophysics) |
    | :--- | :--- | :--- |
    | **Xiyyeeffannoo** | Bakka, sochii, qoodama, fi safara qaamolee hawwaa qorata. | Amala, qabiyyee fiiziksaawaa, fi dhimmoota dhiibbaa fi raadiyaashinii qorata. |
    | **Gaaffii Ka'u** | "Urjiin sun eessa jirti? Saffisni ishee meeqa? Maqaan ishee maali?" | "Urjiin sun akkamitti dhukattu? Maaliif ifti? Qabiyyeen ishee maali?" |
    | **Meeshaalee** | Teleskooppiiwwan, kaameeraawwan, fi meeshaalee safaraa. | Seera fiiziksii, qorannoo suulula atomii (nuclear physics), fi moodeloota herregaa. |
    """)

    st.markdown("#### 🤝 Walitti-dhufeenya Isaanii:")
    st.write(
        "Yeroo amma saayinsii ammayyaa keessatti, qo'annoon lamaan kun guutummaatti walitti makamaniiru. "
        "Astronomer ykn Astrophysicist tokko daataa argate qo'achuuf dandeettii lamaan qabaachuu qaba. "
        "Isaanis akka koochoo lamaan shimbiriiti; tokko malee inni biraan deemuu hin danda'u."
    )

    st.divider()

    st.subheader("🌍 1.4. Seenaa fi Ilaalcha Astiroonoomii Addunyaa")
    st.write(
        "Saayinsiin hawwaa kaleessa dhalate miti. Ilmi namaa hundi uumama tana qorachuu fi "
        "kalandarii toffachuuf bara dheeraaf samii ol ilaalaa tureera."
    )
    st.markdown("""
    * **Ilaalcha Durii (Ancient Astronomy):** Giriikonni durii (fkn, Pitolomee) lafti gidduu-galeessa uumamaati, hunduu lafa naanna'a jedhanii amanu turan (**Geocentric Model**). Babilononni fi Chaayinoonnis sochii urjootaa irratti hundaa'anii kalandarii qopheessu turan.
    * **Revolushinii Saayinsii Hawwaa:** Bara gidduu-galeessaa keessa Nikolaas Kooperonikas aduutu gidduu-galeessa, pilaaneetonni immoo aduu naanna'u jedhee mirkaneesse (**Heliocentric Model**). Adeemsa kana Gaaliliyoo Gaalilii teleskooppii uumuun, Yoohaanis Keepiler seerota sochii pilaaneetotaa baasuun, fi Isaaq Niiwuton seera harkisa uumamaa (gravity) kaayun caalaatti gabbisan.
    * **Astiroonoomii Ammayyaa:** Jaarraa 20ffaa fi 21ffaa keessa satalaayitoonni fi teleskooppiiwwan hawwaa (akka Hubble fi James Webb) saayinsii kana sadarkaa hunda caaluun guddisanii jiru.
    """)

    st.divider()

    st.subheader("🦁 1.5. Afrikaa fi Saayinsii Hawwaa")
    st.write(
        "Ardii Afrikaa keessatti beekumsi hawwaa duris akkuma jiru, ammas saayinsii ammayyaan guddinni guddaan galmeessamaa jira."
    )
    st.markdown("""
    * **Beekumsa Durii (Archaeastronomy):** Naannoo **Nabta Playa** (Sudaan fi Gibxii gidduutti) dhagoonni durii dhaha hordofuuf bifa addaan dhabatanii jiran uumamaniiru. Kunis kalandarii addunyaa isa jalqabaa keessaa tokko dha. Saba **Dogon** (Mali) keessa jiran immoo urjii *Sirius B* ishee ijaan hin argamne beekuu isaaniitiin adunyaa dinqisiisaniiru.
    * **Guddina Ammayyaa:** Afrikaa Kibbaa keessatti teleskooppiin adunyaa irratti beekamaa ta'e **SALT** (South African Large Telescope) fi piroojektii teeleskooppii raadiyoo isa guddaa adunyaa **SKA** (Square Kilometre Array) argamu.
    """)

    st.divider()

    st.subheader("🇪🇹 1.6. Astiroonoomii Itoophiyaa")
    st.write(
        "Itoophiyaan saayinsii hawwaa ammayyaatti dhiyeenya kana yoo makamteeyyuu, seenaa durii kanaan walqabatu qabdi."
    )
    st.markdown("""
    * **Ilaalcha Aadaa fi Amantii:** Kalandarri Itoophiyaa durii sochii aduu fi addeessaa irratti hundaa'e. Fakkeenyaaf, *Kitaaba Henok* keessatti maalummaan sochii hawwaa bifa kanaan ibsameera.
    * **Ijaarama Ammayyaa:** Bara 2004 (E.C) keessa Hawaasni Saayinsii Hawwaa Itoophiyaa (ESSS) hundeeffame. Har'a **Riisarchii fi Inistiitiyuutii Saayinsii Hawwaa fi Teeknoolojii (ESSTI)** fi Daawwitii (Teleskooppii) Inxooxoo fayyadamuun qorannoowwan adda addaa gaggeeffamaa jiru. Itoophiyaanis satalaayitii jalqabaa hawwaatti furguggisteetti.
    """)

    st.divider()

    st.subheader("🌳 1.7. Astiroonoomii Aadaa Oromoo (Dhaha Oromoo)")
    st.write(
        "Oromoon saba beekumsa hawwaa saayinsaawaa ta'e afaaniin dhalootaa dhalootatti dabarsaa dhufe dha. "
        "Keessattuu, Oromoon Boranaa sirna dhaha (kalandarii) adunyaa irratti dorgomaa ta'e qaba."
    )
    st.markdown("""
    * **Bu'uura Dhaha Oromoo:** Dhahi Oromoo kalandarii aduu qofa ykn addeessa qofa irratti hundaa'e miti. Inni **Urjii fi Addeessa** wal bira qabuun (Sidereal Calendar) lakkaa'ama. Sirni Gadaa guyyaa itti dhalatu, itti baallii dabarsu fi ayyaana adda addaa kan murteessu dhaha kanaan.
    * **Urjiiwwan Dhahaa:** Oromoon guyyaa lakkaa'uuf urjoota torba (7) guguddoo hordofa. Isaanis:
        1. *Lammii*
        2. *Buusa (Pleiades)*
        3. *Algajima*
        4. *Arba Gadduu*
        5. *Urjii Wallaa*
        6. *Bakkalcha (Venus)*
        7. *Karaa Curree (Milky Way)*
    * **Madaallii Ammayyaa waliin:** Kalandariin ammayyaa aduu irratti hundaa'ee waggaatti guyyaa 365 yoo herregu, dhahi Oromoo immoo sochii urjoota kanaa fi addeessaa madaalee guyyoota fi ji'oota maqaa addaa (Bitsote, Cawaqa, kkf) kenneefii sirritti dhoha.
    """)

    st.divider()

    st.subheader("📐 1.8. Seerota Astiroonoomii Gurguddoo")
    st.write(
        "Qaamoleen hawwaa hundi akka lafatti argamanitti hiriiranii kan socho'an seerota fiiziksii bu'uuraa "
        "armaan gadii kanaan qoratamani dha:"
    )
    st.markdown("""
    * **Seerota Keepiler (Kepler's Laws):** Seerota sadii kan pilaaneetonni akkamitti bifa killee (elliptical orbit) aduu akka naanna'an ibsu dha.
    * **Seera Harkisa Uumamaa Niiwuton (Newton's Law of Universal Gravitation):** Seera humna harkisaa qaamolee hawwaa lama gidduu jiru masaasuu fi ibsu dha.
    """)

import streamlit as st

# --- BOQONNAA 1 ---
if menu == "Boqonnaa 1: Seensa Astiroonoomii fi Astroofiiziksii":
    st.header("✨ Boqonnaa 1: Seensa Astiroonoomii fi Astroofiiziksii")
    st.write("Qabiyyeen Boqonnaa 1 asitti dhiyaata... (Koodii kee isa duraanii as keessa jiri)")

# --- BOQONNAA 2 (Kilaasii kee isa mul'achuu dide) ---
elif menu == "Boqonnaa 2: Fiiziksii Urjiilee":
    st.header("⭐ Boqonnaa 2: Fiiziksii Urjiilee (Stellar Physics & Evolution)")
    st.write(
        "Urjiileen kan dhalatan duumessa interstellar gaasii keessatti uumama **Protostars** jedhamuun. "
        "Ho'i fi dhiibbaan giddu-galeessaa yoo dabalu, dhoohiinsa **Nuclear Fusion** (wal-itti makama hayidiroojiinii "
        "gara heeliyeemitti) eegala. Kuni madda ifa fi ho'a urjiiti."
    )
    
    st.divider()

    st.subheader("📊 Hertzsprung-Russell (H-R) Diagram")
    st.write(
        "H-R Diagram-iin urjiilee *Luminosity* (ifinna) fi *Effective Temperature* (ho'a) isaanii irratti "
        "hirkachuun addaan baasa. Urjiileen jireenya isaanii keessaa baay'ee naannoo **Main Sequence** irratti dabarsu."
    )
    
    st.markdown("""
    H-R Diagram keessatti urjiileen iddoo gurguddoo afuritti qoodamu:
    1. **Main Sequence (Urjoota Hanga Idilee):** Aduu keenya dabalatee urjiilee anniisaa hidhata nuyi argannu.
    2. **Giants (Urjoota Gurguddoo):** Urjiilee ho'i isaanii gadi bu'aa garuu guddina jabaa qaban.
    3. **Supergiants (Urjoota Gar-malee Gurguddoo):** Urjiilee hanga (mass) fi ifinna addaa qaban.
    4. **White Dwarfs (Urjoota Diqqoo Addii):** Urjiilee du'an kanneen giddu-galeessi isaanii qofa hafe.
    """)

    st.divider()

    st.subheader("🔄 2.1. Marsaa Jireenya Urjootaa (Stellar Life Cycle)")
    st.write(
        "Urjiin tokko jireenya ishee keessatti hanga (mass) ishee irratti hundaa'uun karaa lamaan "
        "du'a ishee gahuu dandeessi. Kunis hydrostatic equilibrium (madaallii dhiibbaa keessaa fi harkisa alaa) "
        "irratti hundaa'a."
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔹 Urjiilee Hanga Giddu-galeessaa (Low-Mass Stars)")
        st.markdown("""
        * **Nebula** $\\rightarrow$ **Main Sequence** (Akka Aduu)
        * Anniisaa fixatanii gara **Red Giant**-itti bal'atu.
        * Qabiyyeen alaa dhangala'ee **Planetary Nebula** uuma.
        * Giddu-galeessi ishee gara **White Dwarf** (Urjii Diqqoo Addii) tti jijjiirama.
        """)
        
    with col2:
        st.markdown("### 🔺 Urjiilee Hanga Jabaa Qaban (High-Mass Stars)")
        st.markdown("""
        * **Nebula** $\\rightarrow$ **Massive Main Sequence**
        * Saffisaan anniisaa fixatanii gara **Red Supergiant**-itti bal'atu.
        * Dhoohiinsa jabaa **Supernova** jedhamuun dhoohu.
        * Hanga hafe irratti hundaa'uun gara **Neutron Star** (Urjii Niyuutiroonii) ykn **Black Hole** (Boolla Gurraacha) tti jijjiiramu.
        """)

    st.divider()

    st.subheader("📝 2.2. Murteessitoota Fiiziksii Urjootaa (Key Equations)")
    st.write(
        "Urjiilee keessatti seerotni fiiziksii ifinna fi anniisaa safaruuf gargaaran isaan armaan gadiiti:"
    )
    
    st.latex(r"L = 4\pi R^2 \sigma T^4")
    st.write(
        "As keessatti, **L** ifinna (Luminosity), **R** raadiyaasii urjichaa, **T** ho'a ishee (Temperature), "
        "fi $\\sigma$ immoo cosmic constant Stefan-Boltzmann ($5.67 \\times 10^{-8}\\, \\text{W/m}^2\\text{K}^4$) dha."
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
    import streamlit as st

st.header("📜 1. Seerota Astroofiziksii (Laws of Astrophysics)")

# 1.1 Big Bang Theory
st.subheader("💥 1.1. Tiyoori Big Baang (The Big Bang Theory)")
st.write(
    "Tiyoorin kun yuunivarsiin akkamitti akka eegale ibsa. Yuunivarsiin waggoota biliyoona 13.8 dura qabxii "
    "baay'ee xiqqoo, ho'aa fi tuuta'aa taate tokko irraa dhohuun (expansion) gara bal'achuu amma jiruutti akka dhufe barsiisa."
)
st.write(
    "*This theory explains the origin of the universe. It states that the universe began approximately 13.8 billion years "
    "ago from an extremely hot and dense point that began to expand and continues to do so today.*"
)

with st.expander("💡 Yaadolee Ijoo Tiyoori Big Bang (Key Concepts)"):
    st.markdown("""
    * **A. Singulaariitii (Singularity):** Iddoo yuunivarsiin itti eegale yoo ta'u, hammi isaa zeerootti dhihaata, dhiibbaa fi ho'i isaa immoo daangaa hin qabu (infinite).  
      *_The initial state of the universe, which was infinitely small, hot, and dense._*
    * **B. Bal'achuu Yuunivarsii (Expansion):** Big Baang booda yuunivarsiin bal'achuu fi qabana'uu eegale. Akkuma ruda (balloon) tokko afuufnu keessatti galaksiwwan walirraa fagaachaa deemu.  
      *_After the initial event, the universe began to stretch and cool. Much like a balloon being inflated, galaxies move away from each other as space itself expands._*
    * **C. Uumama Atomootaa (Nucleosynthesis):** Daqiiqaa muraasa jalqabaa keessatti, yuunivarsiin baay'ee waan ho'eef, elementoonni jalqabaa akka Haayidiroojiinii (Hydrogen) fi Heeliyamii (Helium) uumaman.  
      *_In the first few minutes, the universe was hot enough to act like a star's core, creating the first light elements, primarily Hydrogen and Helium._*
    """)

# 1.2 Newton's Law
st.subheader("🍏 1.2. Seera Harkisa Addunyaa Niwuuton (Newton's Law of Universal Gravitation)")
st.write(
    "Seerri kun humna harkisaa wantoota lama gidduu jiru ibsa. Pilaaneetonni akkamitti Aduu akka naanna’an "
    "fi urjiiwwan akkamitti walitti qabamanii galaaksii uuman nuuf ibsa."
)
st.latex(r"F = G \frac{m_1 m_2}{r^2}")
st.markdown("""
* $F$ = Humna harkisaa (Gravitational force)
* $G$ = Constant harkisa addunyaa ($6.674 \times 10^{-11} \text{ m}^3\text{kg}^{-1}\text{s}^{-2}$)
* $m_1, m_2$ = Ulfaatinna wantoota lamaanii (Masses of the objects)
* $r$ = Fageenya gidduu isaanii jiru (Distance between centers)
""")

# 1.3 Kepler's Laws
st.subheader("🪐 1.3. Seerota Keppler (Kepler's Laws of Planetary Motion)")
st.write("Seerotni kunniin akkamitti pilaaneetonni Aduu akka naanna'an bifa killeetiin (ellipse) ibsu.")

col_kep1, col_kep2, col_kep3 = st.columns(3)
with col_kep1:
    st.markdown("#### **Seera 1ffaa: Law of Ellipses**")
    st.latex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1")
    st.caption("Pilaaneetonni karaa killeetiin naanna'u.")
with col_kep2:
    st.markdown("#### **Seera 2ffaa: Law of Equal Areas**")
    st.latex(r"\frac{dA}{dt} = \text{constant}")
    st.caption("Yeroo wal-qixatti bal'ina wal-qixa uumu.")
with col_kep3:
    st.markdown("#### **Seera 3ffaa: Law of Harmonies**")
    st.latex(r"P^2 = \left( \frac{4\pi^2}{G(M + m)} \right) a^3")
    st.caption("Yeroo naannoo ($P$) fi fageenya ($a$) walitti hidha.")

# 1.4 Radiation Laws
st.subheader("🌡️ 1.4. Seera Raadiyaashiniin 'Blackbody' (Radiation Laws)")
st.write("Seerotni kunniin ho'a urjii tokkoo irratti hundaa'uun anniisaa fi halluu ishee addaan baasuuf gargaaru.")

tab1, tab2, tab3 = st.tabs(["Wien's Law", "Stefan-Boltzmann", "Planck's Law"])
with tab1:
    st.markdown("### Seera Wien")
    st.latex(r"\lambda_{\text{max}} = \frac{b}{T}")
    st.write("Urjiin baay'ee ho'aan halluu cuquliisa (short wavelength), kan ho'i isaa gadi bu'aan ammoo diimaa ta'a.")
with tab2:
    st.markdown("### Seera Stefan-Boltzmann")
    st.latex(r"E = \sigma T^4 \quad \text{ykn} \quad P = \sigma AT^4")
    st.write("Anniisaan maddisiifamu ho'a gubbaa urjichaa irratti hundaa'a.")
with tab3:
    st.markdown("### Seera Planck")
    st.latex(r"B_{\lambda}(T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\frac{hc}{\lambda k_B T}} - 1}")

st.divider()

# --- SECTION 2: COMPACT OBJECTS ---
st.header("🕳️ 2. Wantoota Suntuuraman (Compact Objects)")
st.write(
    "Compact Objects jedhamanii kan waamaman, urjiiwwan jireenya isaanii fixanii gara dhumaatti gara wanta "
    "ulfaatina guddaa qabuu fi bal'ina xiqqaatti (infinitely dense remnants) jijjiiramanidha."
)

col_co1, col_co2, col_co3 = st.columns(3)

with col_co1:
    st.markdown("### ⚪ White Dwarfs")
    st.write("Urjiilee hanga Aduu qabaniin uumamu. **Electron Degeneracy Pressure**-dhaan utubamu.")
    st.latex(r"M_{ch} \approx 1.4 M_{\odot}")
    st.caption("Chandrasekhar Limit")

with col_co2:
    st.markdown("### 🌀 Neutron Stars")
    st.write("Urjiilee baay'ee gurguddoo (10-25x Sun) irraa Supernova booda uumama. Niyuutiroonii qofa.")
    st.latex(r"\rho \approx 10^{17} \text{ kg/m}^3")
    st.caption("Nuclear Density")

with col_co3:
    st.markdown("### 🕳️ Black Holes")
    st.write("Harkisni jabaatee ifni illee keessaa bahuu hin danda'u. Gara Singularity-tti kottoonfata.")
    st.latex(r"R_s = \frac{2GM}{c^2}")
    st.caption("Schwarzschild Radius")

st.divider()

# --- SECTION 3: H-R & P-PDOT DIAGRAMS ---
st.header("📊 3. Diyaagiraamiiwwan Xiinxalaa (Astrophysical Diagrams)")

tab_hr, tab_ppdot = st.tabs(["Hertzsprung-Russell (H-R) Diagram", "P-Pdot Diagram"])

with tab_hr:
    st.subheader("Hertzsprung-Russell Diagram")
    st.write(
        "Diyaagiraamiin kun walitti dhufeenya **Luminosity** (ifa/axis Y) fi **Temperature** (ho'a/axis X) "
        "urjiiwwanii gidduu jiru agarsiisa. Urjiin kamiyyuu evoluushinii ishee kanaan safarama."
    )
    st.latex(r"L = 4\pi R^2 \sigma T^4")
    st.info("Neutron star-n guddinni ishee $R$ baay'ee xiqqaa waan ta'eef, H-R diagram irratti jala-bitaatti argamti.")

with tab_ppdot:
    st.subheader("P-Pdot ($P-\\dot{P}$) Diagram")
    st.write(
        "Diyaagiraamiin kun walitti dhufeenya yeroo naannoo urjii Niiwutiroonii ($P$) fi saffisa inni ittiin "
        "suuta deemaa jiru ($\\dot{P}$) agarsiisa. Kun 'H-R diagram of pulsars' jedhamee waamama."
    )
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("**Characteristic Age (Umurii Evoluushinii):**")
        st.latex(r"\tau = \frac{P}{2\dot{P}}")
    with col_p2:
        st.markdown("**Magnetic Field Strength (Humna Maagneetikii):**")
        st.latex(r"B \propto \sqrt{P\dot{P}}")

st.divider()

# --- SECTION 4: SUMMARY TABLE ---
st.subheader("📊 Cuunfaa Amaloota Wantoota Suntuuraman")
st.markdown("""
| Amala (Property) | Normal Pulsar | Millisecond Pulsar (MSP) | Magnetar |
| :--- | :--- | :--- | :--- |
| **Period ($P$)** | $0.1 - 5 \text{ s}$ | $1 - 10 \text{ ms}$ | $1 - 10 \text{ s}$ |
| **Magnetic Field ($B$)** | $10^{12} \text{ G}$ | $10^8 - 10^9 \text{ G}$ | $10^{14} - 10^{15} \text{ G}$ |
| **Age ($\tau$)** | Young / Middle-aged | Very Old (Recycled) | Very Young |
""")

# --- SECTION 5: EXTREME DENSITY ---
st.subheader("🔬 4. Rukkina Addaa Urjii Niiwutiroonii (Extreme Density)")
st.write(
    "**Afaan Oromoo:** Rukkinni urjii Niiwutiroonii baay'ee ol-aanaa waan ta'eef, wanta as irratti argamu "
    "falaana xinnoo (teaspoon) tokko yoo furan, ulfaatinni isaa lafa irratti tulluu guddatti (biliyoona heduu) tilmaamama."
)
st.write(
    "**English:** *The density of a neutron star is so extreme that a single teaspoon of its material would weigh "
    "billions of tons on Earth, equivalent to packing the entire mass of an atomic nucleus into a highly compressed macroscopic scale.*"
)
st.latex(r"\rho = \frac{M}{V} \approx 10^{17} \text{ kg/m}^3")
import streamlit as st
# --- SECTION 1: THEORY OF RELATIVITY ---
st.header("🎬 1. Ti'oorii Relatiivitiii (Einstein’s Theory of Relativity)")

col_rel1, col_rel2 = st.columns(2)
with col_rel1:
    st.markdown("### 🇪🇹 Afaan Oromoo")
    st.write(
        "Ti'ooriin kun 'Gravity'n' (harkisni) maal akka ta'e bal'inaan ibsa. Keessattuu 'Black Holes' "
        "(boolla gurraacha) fi babal'achuu uumama caccabaa (universe) irratti hojjata. "
        "Ti'ooriin Relatiivitii saayinsii fiiziksii keessatti yaada bu'uuraa Albeert Anishtaayin (Albert Einstein) "
        "maddisiise dha. Inni kun bakka lamatti qoodama: **Special Relativity** (Relatiivitii Addaa) fi "
        "**General Relativity** (Relatiivitii Waliigalaa)."
    )

with col_rel2:
    st.markdown("### 🇬🇧 English")
    st.write(
        "*This theory explains gravity on a massive scale. It is essential for understanding black holes "
        "and the expansion of the universe. The Theory of Relativity is a fundamental concept developed by "
        "Albert Einstein, divided into two parts: Special Relativity and General Relativity.*"
    )

st.write("---")

# 1.1 Special Relativity
st.subheader("🚀 1.1. Relatiivitii Addaa (Special Relativity - 1905)")
st.write(
    "**Afaan Oromoo:** Ti'ooriin kun waa'ee walitti dhufeenya yeroo, fageenyaa, fi ulfaatinna wantoota saffisa guddaan "
    "(saffisa ibsaatti dhihaatun) socho'anii ibsa. Yaada kana keessatti wanti guddaan \"Saffisni Ibsaa\" (Speed of Light) "
    "dhaabbataa dha. Wantoonni yoo baay'ee saffisan yeroon isaaniif ni suuta deema (Time dilation)."
)
st.write(
    "**English:** *This theory focuses on the relationship between space and time. Its core postulate is that the "
    "speed of light is constant for all observers, and it introduces concepts like time dilation and mass-energy equivalence.*"
)

# Formulas for Special Relativity
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("#### **A. Foormulaa Beekamaa (Mass-Energy Equivalence):**")
    st.latex(r"E = mc^2")
    st.markdown("""
    * $E$ = Anniisaa (Energy)
    * $m$ = Ulfaatinna (Mass)
    * $c$ = Saffisa ibsaa ($3 \times 10^8 \text{ m/s}$)
    """)

with col_f2:
    st.markdown("#### **B. Foormulaa 'Time Dilation' (Yeroon suuta deemuu):**")
    st.latex(r"t' = \frac{t}{\sqrt{1 - \frac{v^2}{c^2}}}")
    st.markdown("""
    * $t'$ = Yeroo namni socho'u lakkaa'u
    * $t$ = Yeroo namni dhaabbatu tokko lakkaa'u
    * $v$ = Saffisa wantichaa
    """)

st.write("---")

# 1.2 General Relativity
st.subheader("🪐 1.2. Relatiivitii Waliigalaa (General Relativity - 1915)")
st.write(
    "**Afaan Oromoo:** Inni kun waa'ee Harkisa Biiftuu (Gravity) ibsa. Harkisni humna wantoonni wal-harkisuuf "
    "fayyadaman qofa utuu hin taane, 'Space-time' (bakka fi yeroo) akka micciiramu (curvature) kan taasisudha. "
    "Wantoonni ulfaatinna guddaa qaban (akka urjiiwwanii) 'Space-time' micciiruun akka wantoonni biroo isatti jiganiif sababa ta'u."
)
st.write(
    "**English:** *This theory explains gravity as the curvature of space-time caused by mass and energy. "
    "Massive objects, like stars and planets, warp the fabric of space-time around them.*"
)

st.markdown("#### **Walqixxaattoo Dirree (Einstein Field Equations):**")
st.latex(r"G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}")
st.markdown("""
* $G_{\mu\nu}$ = Qaxxaamura 'Space-time' (Curvature of space-time)
* $\Lambda$ = Cosmological constant
* $g_{\mu\nu}$ = Metric tensor
* $T_{\mu\nu}$ = Hamma annisaa fi ulfaatinna jiru (Energy-momentum tensor)
* $G$ = Gravitational constant
""")

st.divider()

# --- SECTION 2: DARK MATTER & DARK ENERGY ---
st.header("🌌 2. Tiyoori \"Dark Matter\" fi \"Dark Energy\"")

col_dm, col_de = st.columns(2)
with col_dm:
    st.markdown("### 🌑 Dark Matter")
    st.write(
        "**Afaan Oromoo:** Kun wanta ijaan hin argamne garuu harkisa hawaa (gravity) qabudha. "
        "Galaksiwwan akka walitti qabamanii turan gargaara."
    )
    st.write(
        "**English:** *An invisible substance that does not emit light but exerts gravitational pull, "
        "holding galaxies together.*"
    )

with col_de:
    st.markdown("### ⚡ Dark Energy")
    st.write(
        "**Afaan Oromoo:** Kun immoo humni yuunivarsiin saffisaan akka bal'atu godhudha."
    )
    st.write(
        "**English:** *A mysterious force that is causing the expansion of the universe to accelerate.*"
    )

st.divider()

# --- SECTION 3: PAULI EXCLUSION PRINCIPLE ---
st.header("🔬 3. Seera Paawulii (Pauli Exclusion Principle)")
st.write(
    "**Afaan Oromoo:** Seerri kun astrofiiziksii keessatti baay'ee barbaachisadha. Urjiileen du'an (White Dwarfs) "
    "akka guutummaatti hin jignee fi jabaatanii akka dhaabbatan kan godhu **\"electron degeneracy pressure\"** jedhamudha, "
    "kunis seera kanaan ibsama."
)
st.write(
    "**English:** *In astrophysics, this principle explains how 'White Dwarf' stars remain stable. "
    "It creates electron degeneracy pressure, which prevents the star from collapsing further under its own gravity.*"
)

with st.expander("❓ Maaliif Seerotni Kun Baay'atu?"):
    st.write(
        "Astrofiiziksiin fiiziksii wantoota xixinnoo (Quantum Mechanics) fi fiiziksii wantoota gurguddaa (Relativity) walitti fida. "
        "Kanaafuu, wantota adda addaa ibsuuf seerota hedduu fayyadamna:"
    )
    st.markdown("""
    * **Sochii pilaaneetotaa ibsuuf:** Seera Niwtanii fi Keeppler.
    * **Ifa urjiilee qorachuuf:** Seera Wiin fi Isteefaan-Booltsimaan.
    * **Uumama yuunivarsii hubachuuf:** Seera Huble fi Big Bang.
    """)

st.divider()

# --- SECTION 4: COMPACT OBJECTS ---
st.header("💀 4. Compact Objects (Wantoota Suntuuraman)")
st.write(
    "** Astrofiiziksii keessatti, Compact Objects (Wantoota dhangala’oo ykn kanneen walitti suntuuraman) "
    "jedhamanii kan waamaman, urjiiwwan jireenya isaanii fixanii gara dhumaatti gara wanta ulfaatina guddaa qabuu fi "
    "bal'ina xiqqaatti jijjiiramanidha. Sababni isaan compact object jedhamaniif hanga guddaa qabaatanii iddoo xiqqoo waan qabaniif."
)
st.write(
    "In astrophysics, a compact object is a generic term used to describe the incredibly dense remnants "
    "left behind after a star has finished its nuclear burning cycle and 'died.' Unlike normal stars, compact objects "
    "do not produce energy through nuclear fusion. Instead, they are held up against the inward crush of gravity by "
    "quantum mechanical forces (degeneracy pressure) or, in the case of black holes, they have collapsed completely.*"
)

st.markdown("### ⚖️ 4.1. Sababa Bu'uuraa: Wal'aansoo Humnoota Lamaa (The Fundamental Cause)")
st.write(
    "Urjiin tokko yeroo lubbuun jirtu humnoota lama gidduu madaallii qabdi. Yeroo boba'aan (Hydrogen) dhumatu, humni fusion ni dhaabbata. "
    "Sana booda, humni harkisaa (gravity) injifatee urjittii gadi cuunpha. Kunis **\"Gravitational Collapse\"** jedhama."
)

col_h1, col_h2 = st.columns(2)
with col_h1:
    st.info("**1. Nuclear Fusion:** Annisaa keessaa gara alaatti dhiibu (Pushing outward).")
with col_h2:
    st.warning("**2. Gravity:** Humna harkisaa kan urjittii gara keessaatti kottoonfachiisu (Pulling inward).")

st.write("Urjiin tokko gara \"Compact Object\" akkamiitti akka jijjiiramtu kan murteessu **hamma (mass)** urjichaa isa jalqabaati. Kanneen keessaa gurguddoon sadii fageenyaan qoratamu:")

# Three types of compact objects
tab_wd, tab_ns, tab_bh = st.tabs(["White Dwarfs", "Neutron Stars", "Black Holes"])

with tab_wd:
    st.subheader("⚪ White Dwarfs (Urjiiwwan Adii Xiqqoo)")
    st.write(
        "Urjiilee hamma Aduu keenyaa qabaniin uumama. Urjiin tun erga dhootee booda gidduun (core) ishee hafu baay'ee tuuta'aadha. "
        "Inni akka hin jignee kan ittisu dhiibbaa elektiroonotaati (**Electron Degeneracy Pressure**)."
    )
    st.write(
        "*These are remnants of low to medium-mass stars. They are roughly the size of Earth but have the mass of the Sun.*"
    )
    st.markdown("**Chandrasekhar Limit:** Ulfaatinni 'White Dwarf' tokkoo hamma murtaa'e ($1.4 M_{\odot}$) caaluu hin danda'u.")
    st.latex(r"M_{ch} \approx 1.4 M_{\odot}")
    st.caption("(Asitti $M_{\odot}$ jechuun ulfaatina Aduu jechuudha.)")

with tab_ns:
    st.subheader("🌀 Neutron Stars (Urjiiwwan Niwuutiroonii)")
    st.write(
        "Urjiilee Aduu keenya caalaa dacha 10-25 gurguddatan irraa uumama. Urjiin tun yeroo jigtu (Supernova), "
        "atoomonni keessa jiran caccabanii proton fi electron walitti makamuun Neutron qofa uumu. Guddina magaalaa tokkoo "
        "(km 10-20) qabaatus, ulfaatina Aduu dachaa 1.4 hanga 3 qaba."
    )
    st.write(
        "*Created from massive stars that end in a Supernova. The core is so compressed that protons and electrons merge into neutrons. "
        "They are incredibly dense (e.g., a teaspoon of neutron star material would weigh as much as a mountain).*"
    )
    st.markdown("**Density (Rukkina):** Rukkinni isaanii baay'ee ol-aanaa dha.")
    st.latex(r"\rho \approx 10^{17} \text{ kg/m}^3")

with tab_bh:
    st.subheader("🕳️ Black Holes (Boolla Gurraacha)")
    st.write(
        "Kun urjiilee baay'ee gurguddaa (Aduu dacha 20-30 ol) irraa uumama. Humni harkisaa (gravity) isaanii baay'ee jabaa "
        "waan ta'eef, ifti illee keessaa bahuu hin danda'u. Gravitiin isaa humna kamuu (niwutironota iyyuu) waan mo'atuuf "
        "wanti sun hundi gara qaxxaamura (**singularity**) tokkootti kottoonfata. Daangaa **event horizon** jedhamuun beekama, "
        "wanti tokko alaa gara keessatti yoo seene lammata hin deebi'u."
    )
    st.write(
        "*The final stage for the most massive stars. Gravity is so strong that even light cannot escape its pull. "
        "The core collapses completely into a point of infinite density.*"
    )
    st.markdown("**Schwarzschild Radius:** Fageenya naannoo boolla gurraachaa (Event Horizon) kan ifni keessaa bahuu hin dandeenye.")
    st.latex(r"R_s = \frac{2GM}{c^2}")
    st.markdown("""
    * $G$ = Gravitational constant
    * $M$ = Mass of the black hole
    * $c$ = Speed of light
    """)

st.divider()

# --- SUMMARY POINTS ---
st.subheader("📌 Yaadolee Ijoo Ati Beekuu Qabdu (Key Points to Remember)")
st.markdown("""
1. **Chandrasekhar Limit:** Urjiin tokko gara White Dwarf ta'uuf humni ishee hamma Aduu keenyaa dacha 1.4 caaluu hin qabu. Yoo kana caale gara Neutron Star-tti jijjiirama.
2. **Density (Tuuta'iinsa):** Wantoonni kun \"Compact\" (walitti dhuunfatani) kan jedhamaniif, hamma baay'ee guddaa ta'e iddoo baay'ee xiqqoo keessatti waan qabaniif.
3. **End of Evolution:** Wantoonni kun mallattoo \"du'a\" urjiileeti; annisaa haaraa hin maddisiisan, garuu haftee isaanii keessatti fiiziksii ajaa'ibsiisaa qabu.
""")
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time


# Headings fi Ibsa
st.title("🌌 Rotating Neutron Star: 3D Animation & Energy Loss")
st.write("Malli kun sochii 3D urji Niiwutiroonii fi chaartii anniisaa gadi bu'uu walfaana agarsiisa.")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Parametara Urjichaa")
speed = st.sidebar.slider("Saffisa Naannoo (Rotation Speed)", 1, 10, 5)
inertia = st.sidebar.slider("Moment of Inertia (I)", 1.0, 3.0, 1.5, step=0.1)

# Walqixxaattoo Anniisaa
st.latex(r"\frac{dE}{dt} = - \frac{32}{5} \frac{G I^2 \Omega^6}{c^5}")

# --- INITIAL DATA ---
E_initial = 100.0
current_energy = E_initial
time_steps = []
energy_values = []

# --- 3D SPHERE DATA ---
u, v = np.linspace(0, 2*np.pi, 15), np.linspace(0, np.pi, 15)
x_sp = 1.0 * np.outer(np.cos(u), np.sin(v))
y_sp = 1.0 * np.outer(np.sin(u), np.sin(v))
z_sp = 1.0 * np.outer(np.ones(np.size(u)), np.cos(v))

# Placeholders
st.subheader("🔄 1. 3D Pulsar Rotation")
plot_3d_placeholder = st.empty()

st.subheader("📉 2. Real-time Energy Loss Graph")
plot_graph_placeholder = st.empty()

st.subheader("📋 3. Live Data Table")
table_placeholder = st.empty()

# --- ANIMATION LOOP ---
t = 0
while True:
    # --- 1. GENERATE 3D PLOT ---
    angle = (t * speed * 0.1) % (2 * np.pi)
    fig_3d = go.Figure()
    
    # Core
    fig_3d.add_trace(go.Surface(x=x_sp, y=y_sp, z=z_sp, colorscale="Blues", showscale=False))
    
    # Beams
    bx = [0, 4.0 * np.sin(0.2) * np.cos(angle)]
    by = [0, 4.0 * np.sin(0.2) * np.sin(angle)]
    bz = [0, 4.0 * np.cos(0.2)]
    fig_3d.add_trace(go.Scatter3d(x=bx, y=by, z=bz, mode='lines', line=dict(color='cyan', width=6), showlegend=False))
    fig_3d.add_trace(go.Scatter3d(x=[-i for i in bx], y=[-i for i in by], z=[-i for i in bz], mode='lines', line=dict(color='cyan', width=6), showlegend=False))
    
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(range=[-4,4], backgroundcolor="black"),
            yaxis=dict(range=[-4,4], backgroundcolor="black"),
            zaxis=dict(range=[-4,4], backgroundcolor="black"),
            aspectmode='cube'
        ),
        paper_bgcolor="black", height=400, margin=dict(r=0, l=0, b=0, t=0)
    )
    
    # --- 2. CALCULATE ENERGY LOSS & GENERATE 2D GRAPH ---
    loss_rate = 0.008 * (speed ** 2) * inertia
    current_energy = max(0.0, current_energy - loss_rate)
    
    # Reset yoo anniisaan guutummaatti dhume
    if current_energy <= 0:
        current_energy = E_initial
        time_steps = []
        energy_values = []
        
    time_steps.append(t * 0.1)
    energy_values.append(current_energy)
    
    if len(time_steps) > 40:
        time_steps.pop(0)
        energy_values.pop(0)
        
    fig_graph = go.Figure()
    fig_graph.add_trace(go.Scatter(x=time_steps, y=energy_values, mode='lines+markers', line=dict(color='red', width=3)))
    fig_graph.update_layout(
        xaxis=dict(title="Yeroo (Time)"),
        yaxis=dict(title="Anniisaa Hafee (%)", range=[0, 105]),
        height=250, margin=dict(r=0, l=0, b=0, t=0)
    )
    
    # --- 3. RE-RENDER PLACEHOLDERS ---
    plot_3d_placeholder.plotly_chart(fig_3d, use_container_width=True)
    plot_graph_placeholder.plotly_chart(fig_graph, use_container_width=True)
    
    data_table = f"""
    | Maqaa Parametaraa | Gatiikkaa Ammaa |
    | :--- | :--- |
    | **Yeroo (Step)** | {t} |
    | **Moment of Inertia ($I$)** | {inertia} |
    | **Angular Velocity ($\Omega$)** | {speed} rad/s |
    | **Anniisaa Hafee (Current Energy)** | **{current_energy:.2f} %** |
    """
    table_placeholder.markdown(data_table)
    
    time.sleep(0.06)
    t += 1
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# --- PEJII FI LAYOUT QOPHEESSUU ---
st.set_page_config(page_title="Neutron Star Simulation Lab", layout="wide")

# Mataduree fi sarara diimaa jala muree jiru
st.header("🪐 Neutron Star Radiative Energy Loss Lab", divider="red")
st.write(
    "Simulaasila kanaan Urjii Niiwutiroonii (Neutron Star) ariitiin naanna'u fi raadiyaashinii "
    "annisaa gadi lakkisu bifa 2D fi 3D tiin walfaana qorachuun ni danda'ama."
)

# --- SIDEBAR CONTROLS (INPUTS) ---
st.sidebar.header("⚙️ Parametara Urjichaa")
B_field = st.sidebar.slider("Magnetic Field (B in 10^12 Gauss)", 1.0, 10.0, 5.0)
speed = st.sidebar.slider("Saffisa Naannoo (Rotation Speed)", 1, 10, 5)
inertia = st.sidebar.slider("Moment of Inertia (I)", 1.0, 3.0, 1.5, step=0.1)
alpha = st.sidebar.slider("Magnetic Inclination Angle (α in degrees)", 0, 90, 45)

# Animation dhaabuu fi eegaluuf button sidebar irratti
run_sim = st.sidebar.checkbox("Start / Resume Animation", value=True)

# Calculate Energy Loss rate
alpha_rad = np.radians(alpha)
omega_2d = speed * 10  
E_loss_rate = (B_field**2) * (omega_2d**4) * (np.sin(alpha_rad)**2)

# Display Metrics
col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric(label="Relative Energy Loss Rate (Ė)", value=f"{E_loss_rate:,.2f}")
with col_m2:
    st.latex(r"\frac{dE}{dt} = - \frac{32}{5} \frac{G I^2 \Omega^6}{c^5}")

# --- INITIAL DATA FOR ENERGY GRAPH ---
E_initial = 100.0
current_energy = E_initial
time_steps = []
energy_values = []

# --- 3D SPHERE DATA ---
u, v = np.linspace(0, 2*np.pi, 20), np.linspace(0, np.pi, 20)
x_sp = 1.0 * np.outer(np.cos(u), np.sin(v))
y_sp = 1.0 * np.outer(np.sin(u), np.sin(v))
z_sp = 1.0 * np.outer(np.ones(np.size(u)), np.cos(v))

# --- PLACEHOLDERS FOR VIEWPORTS ---
col_views_1, col_views_2 = st.columns(2)
with col_views_1:
    st.subheader("🖼️ 2D Pulsar View")
    plot_2d_spot = st.empty()

with col_views_2:
    st.subheader("🔄 3D Dynamic View")
    plot_3d_spot = st.empty()

st.subheader("📉 Real-time Energy Decay & Parameters")
plot_graph_spot = st.empty()
table_spot = st.empty()

# --- ANIMATION LOOP ---
t = 0
while run_sim:
    # ==========================================
    # 1. UPDATE 2D PLOTLY ANIMATION
    # ==========================================
    theta_2d = np.radians(t * speed * 3)
    mag_angle = theta_2d + alpha_rad
    x_mag = 8 * np.cos(mag_angle)
    y_mag = 8 * np.sin(mag_angle)
    
    fig_2d = go.Figure()
    # Draw Core Star
    fig_2d.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=50, color='#00d2ff'), showlegend=False))
    # Draw Beams
    fig_2d.add_trace(go.Scatter(x=[0, x_mag], y=[0, y_mag], mode='lines', line=dict(color='#ff007f', width=4, dash='dash'), showlegend=False))
    fig_2d.add_trace(go.Scatter(x=[0, -x_mag], y=[0, -y_mag], mode='lines', line=dict(color='#ff007f', width=4, dash='dash'), showlegend=False))
    
    # Radiation Waves
    for r in range(3, 9, 2):
        fig_2d.add_trace(go.Scatter(x=[x_mag*r/8], y=[y_mag*r/8], mode='markers', marker=dict(size=20, symbol='circle-open', color='#ff007f'), showlegend=False))
        fig_2d.add_trace(go.Scatter(x=[-x_mag*r/8], y=[-y_mag*r/8], mode='markers', marker=dict(size=20, symbol='circle-open', color='#ff007f'), showlegend=False))
        
    fig_2d.update_layout(
        xaxis=dict(range=[-10, 10], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[-10, 10], showgrid=False, zeroline=False, visible=False),
        paper_bgcolor="black", plot_bgcolor="black", height=380, margin=dict(r=0, l=0, b=0, t=0)
    )
    plot_2d_spot.plotly_chart(fig_2d, use_container_width=True)

    # ==========================================
    # 2. UPDATE 3D PLOTLY ANIMATION
    # ==========================================
    angle_3d = (t * speed * 0.1) % (2 * np.pi)
    fig_3d = go.Figure()
    fig_3d.add_trace(go.Surface(x=x_sp, y=y_sp, z=z_sp, colorscale="Blues", showscale=False))
    
    bx = [0, 4.0 * np.sin(alpha_rad + 0.2) * np.cos(angle_3d)]
    by = [0, 4.0 * np.sin(alpha_rad + 0.2) * np.sin(angle_3d)]
    bz = [0, 4.0 * np.cos(alpha_rad + 0.2)]
    fig_3d.add_trace(go.Scatter3d(x=bx, y=by, z=bz, mode='lines', line=dict(color='cyan', width=6), showlegend=False))
    fig_3d.add_trace(go.Scatter3d(x=[-i for i in bx], y=[-i for i in by], z=[-i for i in bz], mode='lines', line=dict(color='cyan', width=6), showlegend=False))
    
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(range=[-4,4], backgroundcolor="black", showgrid=False),
            yaxis=dict(range=[-4,4], backgroundcolor="black", showgrid=False),
            zaxis=dict(range=[-4,4], backgroundcolor="black", showgrid=False),
            aspectmode='cube'
        ),
        paper_bgcolor="black", height=380, margin=dict(r=0, l=0, b=0, t=0)
    )
    plot_3d_spot.plotly_chart(fig_3d, use_container_width=True)

    # ==========================================
    # 3. CALCULATE ENERGY LOSS & DECAY GRAPH
    # ==========================================
    loss_rate = 0.0002 * E_loss_rate * inertia
    current_energy = max(0.0, current_energy - loss_rate)
    
    if current_energy <= 0:
        current_energy = E_initial
        time_steps = []
        energy_values = []
        
    time_steps.append(t * 0.1)
    energy_values.append(current_energy)
    
    if len(time_steps) > 40:
        time_steps.pop(0)
        energy_values.pop(0)
        
    fig_graph = go.Figure()
    fig_graph.add_trace(go.Scatter(x=time_steps, y=energy_values, mode='lines+markers', line=dict(color='red', width=3)))
    fig_graph.update_layout(
        xaxis=dict(title="Time Step"),
        yaxis=dict(title="Remaining Energy (%)", range=[0, 105]),
        height=230, margin=dict(r=0, l=0, b=0, t=0)
    )
    plot_graph_spot.plotly_chart(fig_graph, use_container_width=True)
    
    # ==========================================
    # 4. UPDATE LIVE DATA TABLE
    # ==========================================
    data_table = f"""
    | Parametara | Gatiikkaa Ammaa |
    | :--- | :--- |
    | **Time (t)** | {t} |
    | **Magnetic Field ($B$)** | {B_field} $\\times 10^{{12}}$ Gauss |
    | **Inclination Angle ($\\alpha$)** | {alpha}^\\circ |
    | **Energy Loss Rate ($\\dot{{E}}$)** | {E_loss_rate:,.2f} |
    | **Remaining Kinetic Energy** | **{current_energy:.2f} %** |
    """
    table_spot.markdown(data_table)
    
    time.sleep(0.03) 
    t += 1