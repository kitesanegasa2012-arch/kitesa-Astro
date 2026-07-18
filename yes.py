<!-- ============================================================
     KITESA ASTRO — Kutaa 17 hanga 24
     Qopheessaa: Barsiisaa Qixxeessaa Nagaasaa Fayisaa (MSc Astrophysics, Wallaga University)
     Ibsa: Kutaan kun itti-fufiinsa barreeffama duraanii (Kutaa 1–16) yoo ta'u,
     akkuma jirutti gara xumura HTML kan dabalamteef qopheesse.
     ============================================================ -->
<div id="kitesa-astro-root">
<style>
  #kitesa-astro-root{
    --bg-void:#080a14;
    --bg-panel:#0f1324;
    --bg-panel-2:#131832;
    --line:#242b4a;
    --text-hi:#f1f0fa;
    --text-mid:#b8bdd8;
    --text-low:#7c82a6;

    --c17-gold:#f2c14e;
    --c18-cyan:#4fd8e8;
    --c19-magenta:#ea5aa8;
    --c20-violet:#9d7cf5;
    --c21-teal:#43e0a5;
    --c22-slate:#8f93c9;
    --c23-orange:#ff9457;
    --c24-blue:#5ac8ff;

    font-family:"Manrope",-apple-system,"Noto Sans",sans-serif;
    background:var(--bg-void);
    color:var(--text-hi);
    border-radius:18px;
    overflow:hidden;
    border:1px solid var(--line);
    position:relative;
  }

  #kitesa-astro-root *{box-sizing:border-box;}

  #kitesa-astro-root .star-veil{
    position:absolute; inset:0; pointer-events:none; z-index:0; opacity:.55;
    background:
      radial-gradient(1.5px 1.5px at 12% 18%, #fff, transparent 60%),
      radial-gradient(1px 1px at 26% 62%, #fff, transparent 60%),
      radial-gradient(1.5px 1.5px at 41% 8%, #fff, transparent 60%),
      radial-gradient(1px 1px at 58% 44%, #fff, transparent 60%),
      radial-gradient(1.5px 1.5px at 73% 71%, #fff, transparent 60%),
      radial-gradient(1px 1px at 84% 22%, #fff, transparent 60%),
      radial-gradient(1.5px 1.5px at 91% 58%, #fff, transparent 60%),
      radial-gradient(1px 1px at 6% 84%, #fff, transparent 60%),
      radial-gradient(1px 1px at 66% 90%, #fff, transparent 60%);
    background-repeat:no-repeat;
  }

  #kitesa-astro-root .layout{
    position:relative; z-index:1;
    display:flex; min-height:640px; max-height:86vh;
  }

  /* ---------- SIDEBAR ---------- */
  #kitesa-astro-root .sidebar{
    width:250px; flex:0 0 250px;
    background:linear-gradient(180deg,var(--bg-panel-2),var(--bg-panel));
    border-right:1px solid var(--line);
    padding:20px 14px; overflow-y:auto;
  }
  #kitesa-astro-root .sidebar h1{
    font-family:"Space Grotesk",sans-serif;
    font-size:15px; letter-spacing:.06em; text-transform:uppercase;
    color:var(--text-hi); margin:2px 6px 2px;
  }
  #kitesa-astro-root .sidebar .sub{
    font-size:11px; color:var(--text-low); margin:0 6px 18px; line-height:1.5;
  }
  #kitesa-astro-root .nav-group-label{
    font-size:10px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--text-low); margin:16px 8px 6px;
  }
  #kitesa-astro-root .nav-btn{
    display:flex; align-items:center; gap:10px;
    width:100%; text-align:left; background:transparent; border:1px solid transparent;
    color:var(--text-mid); font-size:13.5px; font-family:inherit; font-weight:600;
    padding:9px 10px; border-radius:10px; cursor:pointer; margin-bottom:3px;
    transition:background .15s, color .15s, border-color .15s;
  }
  #kitesa-astro-root .nav-btn .ic{font-size:15px; width:18px; text-align:center;}
  #kitesa-astro-root .nav-btn .num{
    font-family:"JetBrains Mono",monospace; font-size:10px; color:var(--text-low);
    margin-left:auto;
  }
  #kitesa-astro-root .nav-btn:hover{ background:rgba(255,255,255,.04); color:var(--text-hi); }
  #kitesa-astro-root .nav-btn.active{
    background:var(--dot); color:var(--text-hi); border-color:var(--dot);
    box-shadow:0 0 0 1px var(--dot) inset;
  }
  #kitesa-astro-root .nav-btn.active{ background:color-mix(in srgb, var(--dot) 16%, transparent); }

  /* ---------- MAIN ---------- */
  #kitesa-astro-root .main{ flex:1; overflow-y:auto; padding:30px 40px 60px; }
  #kitesa-astro-root .page{ display:none; animation:fadeIn .35s ease; }
  #kitesa-astro-root .page.active{ display:block; }
  @keyframes fadeIn{ from{opacity:0; transform:translateY(6px);} to{opacity:1; transform:translateY(0);} }

  #kitesa-astro-root .eyebrow{
    font-family:"JetBrains Mono",monospace; font-size:12px; letter-spacing:.08em;
    color:var(--accent); text-transform:uppercase; margin-bottom:6px;
  }
  #kitesa-astro-root h2.page-title{
    font-family:"Space Grotesk",sans-serif; font-size:30px; margin:0 0 6px;
    color:var(--text-hi); line-height:1.25;
  }
  #kitesa-astro-root .page-title .accent-word{ color:var(--accent); }
  #kitesa-astro-root .page-lede{ color:var(--text-mid); font-size:14.5px; margin:0 0 26px; max-width:760px; line-height:1.7;}

  #kitesa-astro-root h3.sec{
    font-family:"Space Grotesk",sans-serif; font-size:19px; color:var(--text-hi);
    margin:34px 0 12px; padding-bottom:10px; border-bottom:1px solid var(--line);
    display:flex; align-items:center; gap:10px;
  }
  #kitesa-astro-root h3.sec .tag{
    font-family:"JetBrains Mono",monospace; font-size:11px; font-weight:700;
    color:var(--bg-void); background:var(--accent); border-radius:6px; padding:3px 7px;
  }
  #kitesa-astro-root h4.sub{ font-family:"Space Grotesk",sans-serif; font-size:14.5px; color:var(--accent); margin:20px 0 8px;}
  #kitesa-astro-root p{ color:var(--text-mid); font-size:14.5px; line-height:1.85; margin:0 0 14px; }
  #kitesa-astro-root strong{ color:var(--text-hi); }
  #kitesa-astro-root .en{
    color:var(--text-low); font-size:13px; font-style:italic; line-height:1.75;
    border-left:2px solid var(--line); padding-left:12px; margin:0 0 14px;
  }

  #kitesa-astro-root .card{
    background:var(--bg-panel); border:1px solid var(--line); border-radius:14px;
    padding:18px 20px; margin:14px 0;
  }
  #kitesa-astro-root .grid2{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }
  #kitesa-astro-root .grid3{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; }
  @media (max-width:820px){ #kitesa-astro-root .grid2, #kitesa-astro-root .grid3{ grid-template-columns:1fr; } }

  #kitesa-astro-root .card.accented{ border-color:color-mix(in srgb, var(--accent) 45%, var(--line)); }
  #kitesa-astro-root .card .card-h{ font-family:"Space Grotesk",sans-serif; font-size:15px; color:var(--accent); margin:0 0 8px; }

  #kitesa-astro-root .eqn{
    background:#00030c; border:1px solid var(--line); border-radius:10px;
    padding:14px 18px; margin:12px 0; overflow-x:auto; color:var(--text-hi); font-size:15px;
  }
  #kitesa-astro-root .eqn-cap{ font-size:12px; color:var(--text-low); margin-top:-8px; margin-bottom:14px; }

  #kitesa-astro-root ul.oro{ margin:0 0 14px; padding-inline-start:20px; color:var(--text-mid); }
  #kitesa-astro-root ul.oro li{ margin-bottom:6px; font-size:14.5px; line-height:1.7; }
  #kitesa-astro-root ul.oro li strong{ color:var(--text-hi); }

  #kitesa-astro-root .divider{ height:1px; background:var(--line); margin:28px 0; border:none; }

  #kitesa-astro-root .badge-row{ display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 18px; }
  #kitesa-astro-root .badge{
    font-family:"JetBrains Mono",monospace; font-size:11.5px; color:var(--text-hi);
    background:var(--bg-panel-2); border:1px solid var(--line); border-radius:999px; padding:5px 12px;
  }

  #kitesa-astro-root table.oro{ width:100%; border-collapse:collapse; margin:12px 0 20px; font-size:13.5px; }
  #kitesa-astro-root table.oro th{
    text-align:right; font-family:"Space Grotesk",sans-serif; color:var(--accent);
    border-bottom:1px solid var(--accent); padding:9px 12px; font-weight:600;
  }
  #kitesa-astro-root table.oro th:first-child, #kitesa-astro-root table.oro td:first-child{ text-align:left; }
  #kitesa-astro-root table.oro td{ padding:9px 12px; border-bottom:1px solid var(--line); color:var(--text-mid); text-align:right; }
  #kitesa-astro-root table.oro tr:last-child td{ border-bottom:none; }

  #kitesa-astro-root .tabbar{ display:flex; gap:6px; margin:16px 0 0; flex-wrap:wrap; }
  #kitesa-astro-root .tabbtn{
    font-family:inherit; font-weight:700; font-size:13px; color:var(--text-mid);
    background:var(--bg-panel); border:1px solid var(--line); border-bottom:none;
    padding:9px 16px; border-radius:10px 10px 0 0; cursor:pointer;
  }
  #kitesa-astro-root .tabbtn.active{ color:var(--bg-void); background:var(--accent); }
  #kitesa-astro-root .tabpanel{
    display:none; background:var(--bg-panel); border:1px solid var(--line); border-radius:0 10px 10px 10px;
    padding:18px 20px;
  }
  #kitesa-astro-root .tabpanel.active{ display:block; }

  /* profile card */
  #kitesa-astro-root .profile-hero{ display:flex; gap:22px; align-items:flex-start; }
  #kitesa-astro-root .profile-avatar{
    width:88px; height:88px; border-radius:50%; flex:0 0 88px;
    background:radial-gradient(circle at 35% 30%, #fff8, var(--accent) 45%, #1a0f2e 100%);
    box-shadow:0 0 30px color-mix(in srgb, var(--accent) 55%, transparent);
  }
  #kitesa-astro-root .kv{ display:grid; grid-template-columns:150px 1fr; gap:6px 14px; margin:14px 0; }
  #kitesa-astro-root .kv .k{ color:var(--text-low); font-size:13px; }
  #kitesa-astro-root .kv .v{ color:var(--text-hi); font-size:13.5px; font-weight:600; }

  /* ---------- ANIMATION PANEL (kutaa 24) ---------- */
  #kitesa-astro-root .sim-wrap{ display:grid; grid-template-columns:300px 1fr; gap:20px; margin-top:10px; }
  @media (max-width:900px){ #kitesa-astro-root .sim-wrap{ grid-template-columns:1fr; } }
  #kitesa-astro-root .sim-controls .ctrl{ margin-bottom:20px; }
  #kitesa-astro-root .sim-controls label{ display:flex; justify-content:space-between; font-size:13px; color:var(--text-mid); margin-bottom:8px; }
  #kitesa-astro-root .sim-controls label b{ color:var(--c24-blue); font-family:"JetBrains Mono",monospace; }
  #kitesa-astro-root input[type=range]{
    width:100%; accent-color:var(--c24-blue); height:4px;
  }
  #kitesa-astro-root .stage{
    background:radial-gradient(ellipse at 50% 40%, #0d1230 0%, #05060f 75%);
    border:1px solid var(--line); border-radius:14px; overflow:hidden; position:relative;
  }
  #kitesa-astro-root canvas{ display:block; width:100%; }
  #kitesa-astro-root .sim-btn{
    font-family:"JetBrains Mono",monospace; font-weight:700; font-size:12.5px;
    background:transparent; color:var(--c24-blue); border:1px solid var(--c24-blue);
    border-radius:8px; padding:9px 14px; cursor:pointer; width:100%;
  }
  #kitesa-astro-root .sim-btn:hover{ background:color-mix(in srgb, var(--c24-blue) 18%, transparent); }

  #kitesa-astro-root .foot-note{
    margin-top:44px; padding-top:16px; border-top:1px solid var(--line);
    color:var(--text-low); font-size:12px; text-align:center;
  }

  #kitesa-astro-root .main::-webkit-scrollbar, #kitesa-astro-root .sidebar::-webkit-scrollbar{ width:8px; }
  #kitesa-astro-root .main::-webkit-scrollbar-thumb, #kitesa-astro-root .sidebar::-webkit-scrollbar-thumb{
    background:var(--line); border-radius:8px;
  }
</style>

<div class="star-veil"></div>

<div class="layout">
  <!-- ================= SIDEBAR ================= -->
  <nav class="sidebar">
    <h1>🌌 Kitesa Astro</h1>
    <p class="sub">Itti-fufiinsa barreeffamaa — Kutaa 17 hanga 24</p>

    <div class="nav-group-label">Seensa</div>
    <button class="nav-btn" data-page="galataa" style="--dot:#c9a7ff">
      <span class="ic">🙏</span> Galataa <span class="num"></span>
    </button>
    <button class="nav-btn" data-page="profaayilii" style="--dot:#c9a7ff">
      <span class="ic">👤</span> Waa'ee Qorataa <span class="num"></span>
    </button>

    <div class="nav-group-label">Qabiyyee Haaraa</div>
    <button class="nav-btn" data-page="k17" style="--dot:var(--c17-gold)">
      <span class="ic">📜</span> Seerota Bu'uuraa <span class="num">17</span>
    </button>
    <button class="nav-btn" data-page="k18" style="--dot:var(--c18-cyan)">
      <span class="ic">⭐</span> Fiiziksii Urjiilee <span class="num">18</span>
    </button>
    <button class="nav-btn" data-page="k19" style="--dot:var(--c19-magenta)">
      <span class="ic">🕳️</span> Wantoota Suntuuraman <span class="num">19</span>
    </button>
    <button class="nav-btn" data-page="k20" style="--dot:var(--c20-violet)">
      <span class="ic">📊</span> Diyaagiraamiiwwan Xiinxalaa <span class="num">20</span>
    </button>
    <button class="nav-btn" data-page="k21" style="--dot:var(--c21-teal)">
      <span class="ic">🎬</span> Ti'oorii Relatiivitii <span class="num">21</span>
    </button>
    <button class="nav-btn" data-page="k22" style="--dot:var(--c22-slate)">
      <span class="ic">🌑</span> Dark Matter & Dark Energy <span class="num">22</span>
    </button>
    <button class="nav-btn" data-page="k23" style="--dot:var(--c23-orange)">
      <span class="ic">🔬</span> Seera Paawulii <span class="num">23</span>
    </button>
    <button class="nav-btn active" data-page="k24" style="--dot:var(--c24-blue)">
      <span class="ic">🌀</span> Animeeshinii 3D <span class="num">24</span>
    </button>
  </nav>

  <!-- ================= MAIN ================= -->
  <main class="main">

    <!-- ============ GALATAA ============ -->
    <section class="page" id="page-galataa" style="--accent:#c9a7ff;">
      <div class="eyebrow">Seensa</div>
      <h2 class="page-title">🙏 <span class="accent-word">Galataa</span></h2>
      <p class="page-lede">Barreeffama fi appilikeeshinii kana milkeessuu keessatti gahee kan qaban hundaaf galata koo.</p>

      <div class="card accented">
        <div class="card-h">🛐 Uumaa Koo Waaqayyoon</div>
        <p>Jalqabaa fi xumura hojii kootii kan ta'e, sammuu koo naaf banee saayinsii hawwaa gadi fageenyaan akkan qoradhu humna, beekumsaa fi obsa naaf kenne, Waaqayyo Uumaa kootiif galanni guddaan, kan dhumaa hin qabne haa ta'u.</p>
      </div>

      <div class="card accented">
        <div class="card-h">🔬 Gorsaa Koo</div>
        <p>Appilikeeshinii kana kalaquuf jalqabaa irraa eegalee hanga dhumaatti ogummaa saayinsawaa, gorsa, qajeelfamaa fi deeggarsa wal irraa hin cinne naaf kennaa kan turan, ammas na waliin kan jiran barsiisaa koo, gorsaa koo fi Yuunivarsiitii Wallaggaatti barsiisaa astiroonoomii fi gargaaraa piroofeesaraa kan ta'an <strong>Dr. Darajjee Wakgaarii Amantee</strong>, baay'ee guddaan galateeffadha.</p>
      </div>

      <div class="card accented">
        <div class="card-h">🏡 Maatii Koo</div>
        <p>Duraan dursee maatii koo, dhalachuu koo irraa eegalanii nama ta'uu kootiif na guddisuu fi na barsiisuun bu'uura cimaa naaf kaa'an — <strong>haadha koo</strong>, deessuu koo fi dandeessuu koo kan taate <strong>Aadde Mulee Baqqalaa</strong>, fi <strong>abbaa koo</strong>, lafa kana irratti utubaa jireenya kootii kan ta'an <strong>Barsiisaa Nagaasaa Fayisaa</strong>, waan hundaan na bira dhaabbachaa waan jiraniif; akkasumas obboleeyyan koo <strong>Qixxaattuu Nagaasaa, Darajjee Nagaasaa, Lalisaa Nagaasaa, Eebbisaa Nagaasaa</strong> fi <strong>Eebbisee Nagaasaa</strong> kallattii hundaan deggersa obbolummaa naaf taasisaniif, galanni koo guddaan isaaniif haa ta'u. Har'a kanaan na geessan; isin lafee dugdaa fi ifa jireenya kootii dha!</p>
        <p>Halkanii fi guyyaa osoo hin jedhin, yeroo ani qo'annoo fi qorannoon rarra'ee jiru kanneen obsaan na eegaa turan — jaalala, onnee fi humna itti fufiinsaa naaf kennitee kan jirtu jaalallee haadha manaa koo <strong>Barsiistuu Araaree Taaddasaa</strong>, akkasumas ijoollee koo, abdiiwwan koo <strong>Hiikaa</strong> fi <strong>Latii</strong> — galanni ani isiniif qabu ibsa jechaatii oli. Isin hundi keessanuu miidhagina fi utubaa jireenya kootii dha!</p>
      </div>
    </section>

    <!-- ============ PROFAAYILII ============ -->
    <section class="page" id="page-profaayilii" style="--accent:#c9a7ff;">
      <div class="eyebrow">Seensa</div>
      <h2 class="page-title">👤 <span class="accent-word">Waa'ee Qorataa</span> fi Piroofaayilii</h2>
      <p class="page-lede">Barsiisaa fi qorataa fiiziksii dhaloota boruuf ifa ta'an.</p>

      <div class="card accented">
        <div class="profile-hero">
          <div class="profile-avatar"></div>
          <div>
            <p style="margin:0 0 8px;"><strong>Barsiisaa Qixxeessaa Nagaasaa Fayisaa</strong> qorataa fi barsiisaa Fiiziksii fi Astiroofiiziksii yoo ta'an, Yuunivarsiitii Wallaggaa (Wallaga University) keessatti digrii lammaffaa (MSc) isaanii Fiiziksii Urjiilee fi Hawwaa irratti xumuratanii jiru. Qo'annoon isaanii inni guddaan <strong>Urjiilee Niiwutiroonii Naanna'an (Rotating Neutron Stars)</strong> irratti kan xiyyeeffate dha.</p>
          </div>
        </div>
        <div class="kv">
          <div class="k">Maqaa</div><div class="v">Qixxeessaa Nagaasaa Fayisaa</div>
          <div class="k">Barnoota</div><div class="v">MSc in Astrophysics — Wallaga University</div>
          <div class="k">Hojii</div><div class="v">Barsiisaa Fiiziksii & Qorataa Saayinsii Hawwaa</div>
          <div class="k">Xiyyeeffannoo Qo'annoo</div><div class="v">Pulsars, Rotating Neutron Stars, Gravitational Waves, Stellar Evolution</div>
        </div>
      </div>

      <div class="card" style="border-left:3px solid #c9a7ff;">
        <p style="margin:0;">💡 Barsiisaa Qixxeessaan barsiisaa fi qorataa fiiziksii dhaloota boruuf ifa ta'an dha.</p>
      </div>
    </section>

    <!-- ============ KUTAA 17 ============ -->
    <section class="page" id="page-k17" style="--accent:var(--c17-gold);">
      <div class="eyebrow">Kutaa 17</div>
      <h2 class="page-title">📜 <span class="accent-word">Seerota Bu'uuraa</span> Astiroonoomii fi Astiroofiiziksii</h2>
      <p class="page-lede">Kutaan kun seenaa fi ilaalcha addunyaa astiroonoomii, hirmaannaa Afrikaa fi Oromoo, akkasumas seerota fiiziksii bu'uuraa kan qaamolee hawwaa hunda bulchan ibsa.</p>

      <h3 class="sec"><span class="tag">17.1</span> Seenaa fi Ilaalcha Astiroonoomii Addunyaa</h3>
      <p>Saayinsiin hawwaa kaleessa dhalate miti. Ilmi namaa hundi uumama tana qorachuu fi kalandarii tolfachuuf bara dheeraaf samii ol ilaalaa tureera.</p>
      <ul class="oro">
        <li><strong>Ilaalcha Durii (Ancient Astronomy):</strong> Giriikonni durii (fkn, Pitolomee) lafti gidduu-galeessa uumamaati, hunduu lafa naanna'u jedhanii amanu turan (<em>Geocentric Model</em>). Baabilooniyoonnii fi Chaayinoonnis sochii urjootaa irratti hundaa'anii kalandarii qopheessu turan.</li>
        <li><strong>Revolushinii Saayinsii Hawwaa:</strong> Bara giddu-galeessaa keessa Nikolaas Kooperonikas aduutu gidduu-galeessa, pilaaneetonni immoo aduu naanna'u jedhee mirkaneesse (<em>Heliocentric Model</em>). Adeemsa kana Gaaliliyoo Gaalilii teleskooppii uumuun, Yoohaanis Keepiler seerota sochii pilaaneetotaa baasuun, fi Isaaq Niiwutan seera harkisa uumamaa (gravity) kaa'uun caalaatti gabbisan.</li>
        <li><strong>Astiroonoomii Ammayyaa:</strong> Jaarraa 20ffaa fi 21ffaa keessa satalaayitoonni fi teleskooppiiwwan hawwaa (akka Hubble fi James Webb) saayinsii kana sadarkaa hunda caaluun guddisanii jiru.</li>
      </ul>

      <h3 class="sec"><span class="tag">17.2</span> Afrikaa fi Saayinsii Hawwaa</h3>
      <p>Ardii Afrikaa keessatti beekumsi hawwaa durii akkuma jirutti, ammas saayinsii ammayyaan guddinni guddaan galmeeffamaa jira.</p>
      <div class="grid2">
        <div class="card">
          <div class="card-h">Beekumsa Durii (Archaeoastronomy)</div>
          <p style="margin:0;">Naannoo <strong>Nabta Playa</strong> (Sudaan fi Gibxii gidduutti) dhagoolee durii dhaha (calendar) hordofuuf bifa addaan dhaabbatan uumamaniiru — kalandarii addunyaa isa jalqabaa keessaa tokko. Saba <strong>Dogon</strong> (Mali) keessa jiraatan immoo urjii <em>Sirius B</em>, kan ijaan hin argamne, beekuun isaanii addunyaa dinqisiisaniiru.</p>
        </div>
        <div class="card">
          <div class="card-h">Guddina Ammayyaa</div>
          <p style="margin:0;">Afrikaa Kibbaatti teleskooppiin addunyaa irratti beekamaa ta'e <strong>SALT</strong> (South African Large Telescope) fi piroojektiin teleskooppii raadiyoo isa guddaa addunyaa <strong>SKA</strong> (Square Kilometre Array) argamu.</p>
        </div>
      </div>

      <h3 class="sec"><span class="tag">17.3</span> Astiroonoomii Itoophiyaa</h3>
      <p>Itoophiyaan saayinsii hawwaa ammayyaatti dhiyeenya kana yoo makamteyyuu, seenaa durii wal-qabsiisu qabdi.</p>
      <ul class="oro">
        <li><strong>Ilaalcha Aadaa fi Amantii:</strong> Kalandariin Itoophiyaa durii sochii aduu fi ji'aa irratti hundaa'a. Fakkeenyaaf, <em>Kitaaba Henok</em> keessatti maalummaan sochii hawwaa bifa kanaan ibsameera.</li>
        <li><strong>Ijaarama Ammayyaa:</strong> Bara 2004 (Kaleendarii Itoophiyaa) keessa Hawaasni Saayinsii Hawwaa Itoophiyaa (ESSS) hundeeffame. Har'a <strong>Riisarchii fi Inistiitiyuutii Saayinsii Hawwaa fi Teeknoolojii (ESSTI)</strong> fi Daawwitii (Teleskooppii) Ambhoo/Injabaaraa fayyadamuun qorannoowwan adda addaa gaggeeffamaa jiru. Itoophiyaanis satalaayitii jalqabaa hawwaatti darbatteetti.</li>
      </ul>

      <h3 class="sec"><span class="tag">17.4</span> Astiroonoomii Aadaa Oromoo (Dhaha Oromoo)</h3>
      <p>Oromoon saba beekumsa hawwaa saayinsawaa afaaniin dhalootaa gara dhalootaatti dabarsaa dhufe dha. Keessumaa Oromoon Booranaa sirna dhaha (kalandarii) addunyaa irratti dorgomaa ta'e qaba.</p>
      <div class="card">
        <div class="card-h">Bu'uura Dhaha Oromoo</div>
        <p>Dhahi Oromoo kalandarii aduu qofa yookiin ji'a qofa irratti hundaa'e miti. Inni <strong>urjii fi ji'a</strong> wal bira qabuun (Sidereal Calendar) lakkaa'ama. Sirni Gadaa guyyaa itti dhalatu, itti aangoo dabarsu fi ayyaana adda addaa kan murteessu dhaha kanaan.</p>
        <p style="margin:0;"><strong>Urjiiwwan Dhahaa (torban guguddoo):</strong> Lammii, Buusaa (Pleiades), Algajimaa, Arba Gadduu, Urjii Wallaa, Bakkalcha (Venus), fi Karaa Curree (Milky Way).</p>
      </div>
      <p><strong>Madaallii Ammayyaa waliin:</strong> Kalandariin ammayyaa aduu irratti hundaa'ee waggaatti guyyaa 365 herrega; dhahi Oromoo immoo sochii urjootaa fi ji'aa madaaluun guyyoota fi ji'oota maqaa addaa (fkn, Bittotessa, Cabsa) kennuun sirriitti hojjeta.</p>

      <h3 class="sec"><span class="tag">17.5</span> Tiyoorii Big Bang</h3>
      <p>Tiyooriin kun yuunivarsiin akkamitti akka eegale ibsa. Yuunivarsiin waggoota biliyoona 13.8 dura qabxii xiqqoo, baay'ee ho'aa fi tuuta'aa ta'e tokko irraa dhoo'uun (expansion) gara bal'achuu ammaa jirutti akka geesse barsiisa.</p>
      <div class="en">This theory explains the origin of the universe. It states that the universe began approximately 13.8 billion years ago from an extremely hot and dense point that began to expand and continues to do so today.</div>
      <div class="grid3">
        <div class="card"><div class="card-h">Singulaariitii</div><p style="margin:0;font-size:13.5px;">Iddoo yuunivarsiin itti eegale; hammi isaa zeerootti dhihaata, ho'i fi dhiibbaan isaa immoo daangaa hin qabu (infinite).</p></div>
        <div class="card"><div class="card-h">Bal'achuu Yuunivarsii</div><p style="margin:0;font-size:13.5px;">Akkuma buluulii (balloon) afuufamu, galaaksiiwwan walirraa fagaachaa deemu.</p></div>
        <div class="card"><div class="card-h">Uumama Elementootaa</div><p style="margin:0;font-size:13.5px;">Daqiiqoota jalqabaa keessatti, elementoonni jalqabaa akka Haayidiroojinii fi Heeliyeemii uumaman.</p></div>
      </div>

      <h3 class="sec"><span class="tag">17.6</span> Seera Harkisa Addunyaa Niwuutan</h3>
      <p>Seerri kun humna harkisaa wantoota lama gidduu jiru ibsa. Pilaaneetonni akkamitti aduu akka naanna'anii fi urjiiwwan akkamitti walitti qabamanii galaaksii akka uuman nuuf ibsa.</p>
      <div class="eqn">F = G · (m₁m₂ / r²)</div>
      <ul class="oro">
        <li><strong>F</strong> — Humna harkisaa (Gravitational force)</li>
        <li><strong>G</strong> — Dhaabbataa harkisa addunyaa (6.674 × 10⁻¹¹ m³kg⁻¹s⁻²)</li>
        <li><strong>m₁, m₂</strong> — Ulfaatina wantoota lamaanii</li>
        <li><strong>r</strong> — Fageenya gidduu isaanii jiru</li>
      </ul>

      <h3 class="sec"><span class="tag">17.7</span> Seerota Keepilar (Kepler's Laws)</h3>
      <p>Seerota kunneen pilaaneetonni akkamitti aduu naanna'an bifa killee (ellipse) ta'een ibsu.</p>
      <div class="grid3">
        <div class="card"><div class="card-h">Seera 1ffaa — Law of Ellipses</div><div class="eqn" style="font-size:13.5px;">x²/a² + y²/b² = 1</div><p style="margin:0;font-size:13px;">Pilaaneetonni karaa killeetiin naanna'u.</p></div>
        <div class="card"><div class="card-h">Seera 2ffaa — Law of Equal Areas</div><div class="eqn" style="font-size:13.5px;">dA/dt = dhaabbataa</div><p style="margin:0;font-size:13px;">Yeroo wal-qixa keessatti bal'ina wal-qixa uumu.</p></div>
        <div class="card"><div class="card-h">Seera 3ffaa — Law of Harmonies</div><div class="eqn" style="font-size:13.5px;">P² = [4π² / G(M+m)]·a³</div><p style="margin:0;font-size:13px;">Yeroo naannoo (P) fi fageenya (a) walitti hidha.</p></div>
      </div>

      <h3 class="sec"><span class="tag">17.8</span> Seerota Raadiyeeshinii "Blackbody"</h3>
      <p>Seerota kunneen ho'a urjii tokkoo irratti hundaa'uun anniisaa fi halluu ishee addaan baasuuf gargaaru.</p>
      <div class="tabbar" data-tabgroup="rad17">
        <button class="tabbtn active" data-tab="wien">Seera Wien</button>
        <button class="tabbtn" data-tab="sb">Stefan-Boltzmann</button>
        <button class="tabbtn" data-tab="planck">Seera Planck</button>
      </div>
      <div class="tabpanel active" data-tabgroup="rad17" data-tab="wien">
        <div class="eqn">λ_max = b / T</div>
        <p style="margin:0;">Urjiin baay'ee ho'aan halluu cuquliisa (dheerina dachaasaa gabaabaa) qabaata; kan ho'i isaa gadi bu'e immoo diimaa ta'a.</p>
      </div>
      <div class="tabpanel" data-tabgroup="rad17" data-tab="sb">
        <div class="eqn">E = σT⁴ &nbsp; ykn &nbsp; P = σAT⁴</div>
        <p style="margin:0;">Anniisaan maddisiifamu ho'a gubbaa urjichaa irratti hundaa'a; σ dhaabbataa Stefan-Boltzmann (5.67 × 10⁻⁸ W/m²K⁴) dha.</p>
      </div>
      <div class="tabpanel" data-tabgroup="rad17" data-tab="planck">
        <div class="eqn">B_λ(T) = (2hc² / λ⁵) · 1 / (e^(hc/λk_BT) − 1)</div>
        <p style="margin:0;">Raabsa anniisaa urjii tokko dheerina dachaasaa hunda irratti kan ibsu, seera Wien fi Stefan-Boltzmann lamaanuu keessaa kan maddisiisu dha.</p>
      </div>
    </section>

    <!-- ============ KUTAA 18 ============ -->
    <section class="page" id="page-k18" style="--accent:var(--c18-cyan);">
      <div class="eyebrow">Kutaa 18</div>
      <h2 class="page-title">⭐ <span class="accent-word">Fiiziksii Urjiilee</span> fi Marsaa Jireenyaa</h2>
      <p class="page-lede">Akkamitti urjiin akka dhalattu, akka guddattuu fi akka du'aan ishee gahuu — Stellar Physics & Evolution.</p>

      <h3 class="sec"><span class="tag">18.1</span> Uumama Urjiilee</h3>
      <p>Urjiileen kan dhalatan duumessa gaasii interstellar keessatti; uumamni jalqabaa <strong>Protostars</strong> jedhama. Ho'i fi dhiibbaan giddu-galeessaa yoo dabalu, dhoo'iinsi <strong>Nuclear Fusion</strong> (walitti makama Haayidiroojinii gara Heeliyeemiitti) ni eegala. Kun madda ifaa fi ho'a urjiiti.</p>

      <h3 class="sec"><span class="tag">18.2</span> Hertzsprung–Russell (H-R) Diagram</h3>
      <p>H-R Diagram-iin urjiilee <em>Luminosity</em> (ifinna) fi <em>Effective Temperature</em> (ho'a) isaanii irratti hundaa'uun addaan baasa. Urjiileen yeroo jireenya isaanii keessaa baay'ee naannoo <strong>Main Sequence</strong> irratti dabarsu.</p>
      <ul class="oro">
        <li><strong>Main Sequence</strong> — Urjoota hanga idileessaa, aduu keenya dabalatee, urjiilee anniisaa hidhata nuti argannu.</li>
        <li><strong>Giants</strong> — Urjoota ho'i isaanii gadi bu'aa garuu bal'ina jabaa qaban.</li>
        <li><strong>Supergiants</strong> — Urjoota hangaa (mass) fi ifinna addaa qaban.</li>
        <li><strong>White Dwarfs</strong> — Urjoota du'an, kanneen giddu-galeessi isaanii qofti hafe.</li>
      </ul>

      <h3 class="sec"><span class="tag">18.3</span> Marsaa Jireenya Urjootaa (Stellar Life Cycle)</h3>
      <p>Urjiin tokko jireenya ishee keessatti hanga (mass) ishee irratti hundaa'uun karaa lamaan du'a ishee gahuu dandeessi. Kunis <em>hydrostatic equilibrium</em> (madaallii dhiibbaa keessaa fi harkisa alaa) irratti hundaa'a.</p>
      <div class="grid2">
        <div class="card">
          <div class="card-h">🔹 Urjiilee Hanga Giddu-galeessaa (Low-Mass)</div>
          <ul class="oro" style="margin:0;">
            <li>Nebula → Main Sequence (akka Aduu)</li>
            <li>Boba'aa fixatanii gara <strong>Red Giant</strong>-tti bal'atu</li>
            <li>Qabiyyee alaa dhangalaasee <strong>Planetary Nebula</strong> uuma</li>
            <li>Giddu-galeessi ishee gara <strong>White Dwarf</strong> tti jijjiirama</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-h">🔺 Urjiilee Hanga Jabaa Qaban (High-Mass)</div>
          <ul class="oro" style="margin:0;">
            <li>Nebula → Massive Main Sequence</li>
            <li>Dafanii boba'aa fixatanii gara <strong>Red Supergiant</strong>-tti bal'atu</li>
            <li>Dhoo'iinsa jabaa <strong>Supernova</strong> ta'anii dhoo'u</li>
            <li>Hafteen isaanii gara <strong>Neutron Star</strong> ykn <strong>Black Hole</strong> tti jijjiirama</li>
          </ul>
        </div>
      </div>

      <h3 class="sec"><span class="tag">18.4</span> Murteessitoota Fiiziksii Urjootaa</h3>
      <p>Seerri ifinna urjii tokkoo raadiyaasii fi ho'a ishee waliin walqabsiisu:</p>
      <div class="eqn">L = 4πR²σT⁴</div>
      <p style="margin:0;"><strong>L</strong> ifinna (Luminosity), <strong>R</strong> raadiyaasii urjichaa, <strong>T</strong> ho'a ishee, <strong>σ</strong> immoo dhaabbataa Stefan-Boltzmann (5.67 × 10⁻⁸ W/m²K⁴) dha.</p>
    </section>

    <!-- ============ KUTAA 19 ============ -->
    <section class="page" id="page-k19" style="--accent:var(--c19-magenta);">
      <div class="eyebrow">Kutaa 19</div>
      <h2 class="page-title">🕳️ <span class="accent-word">Wantoota Suntuuraman</span> (Compact Objects)</h2>
      <p class="page-lede">Compact Objects jedhamanii kan waamaman, urjiiwwan jireenya isaanii xumuratanii gara wantoota ulfaatina guddaa fi bal'ina xiqqaa qaban jijjiiramanidha.</p>
      <div class="en">In astrophysics, a compact object is a generic term for the incredibly dense remnants left behind after a star finishes its nuclear-burning cycle and "dies." Unlike normal stars, compact objects do not generate energy through fusion — they are held up against gravity by quantum-mechanical degeneracy pressure, or, in the case of black holes, have collapsed completely.</div>

      <h3 class="sec"><span class="tag">19.1</span> Sababa Bu'uuraa — Wal'aansoo Humnoota Lamaa</h3>
      <p>Urjiin tokko yeroo lubbuun jirtu humnoota lama gidduu madaallii qabdi. Boba'aan (Hydrogen) yeroo dhumatu, humni fusion ni dhaabbata; ergasii humni harkisaa (gravity) injifatee urjii gadi cuunfa. Kunis <strong>Gravitational Collapse</strong> jedhama.</p>
      <div class="grid2">
        <div class="card" style="border-left:3px solid var(--c19-magenta);"><strong>Nuclear Fusion</strong> — anniisaa gara alaatti dhiibu (pushing outward).</div>
        <div class="card" style="border-left:3px solid var(--c19-magenta);"><strong>Gravity</strong> — humna harkisaa kan urjii gara keessaatti kottoomsu (pulling inward).</div>
      </div>
      <p>Urjiin tokko gara kamitti akka jijjiiramtu kan murteessu <strong>hangasaa (mass)</strong> jalqabaati. Gosoota sadan armaan gadiitti fageenyaan ilaalla.</p>

      <div class="tabbar" data-tabgroup="co19">
        <button class="tabbtn active" data-tab="wd">⚪ White Dwarfs</button>
        <button class="tabbtn" data-tab="ns">🌀 Neutron Stars</button>
        <button class="tabbtn" data-tab="bh">🕳️ Black Holes</button>
      </div>

      <div class="tabpanel active" data-tabgroup="co19" data-tab="wd">
        <p>Urjiilee hanga aduu keenyaa qabaniin uumamu. Erga boba'aan dhumee booda giddu-galeessi (core) ishee hafu baay'ee tuuta'aa dha; akka hin jignee kan ittisu dhiibbaa elektiroonotaati (<strong>Electron Degeneracy Pressure</strong>).</p>
        <div class="en">These are remnants of low- to medium-mass stars. Roughly the size of Earth, but with the mass of the Sun.</div>
        <p><strong>Chandrasekhar Limit:</strong> Ulfaatinni White Dwarf tokkoo hamma murtaa'e (1.4 M☉) caaluu hin danda'u; yoo caale gara Neutron Star tti jijjiirama.</p>
        <div class="eqn">M_ch ≈ 1.4 M☉</div>
      </div>

      <div class="tabpanel" data-tabgroup="co19" data-tab="ns">
        <p>Urjiilee aduu keenya caalaa dachaa 10–25 gurguddaatan irraa, Supernova booda uumamu. Atoomonni keessa jiran caccabanii pirootoonii fi elektiroonii walitti makamuun niiwutiroonii qofa uumu. Guddinni ishee magaalaa tokko qofa (km 10–20) ta'us, ulfaatina aduu dachaa 1.4–3 qabaatti.</p>
        <div class="en">Created from massive stars ending in supernova; a teaspoon of neutron-star material would weigh as much as a mountain.</div>
        <div class="eqn">ρ ≈ 10¹⁷ kg/m³</div>
      </div>

      <div class="tabpanel" data-tabgroup="co19" data-tab="bh">
        <p>Urjiilee baay'ee gurguddaa (aduu dachaa 20–30 ol) irraa uumamu. Humni harkisaa isaanii akka malee jabaa waan ta'eef ifni illee keessaa bahuu hin danda'u. Wanti hundi gara qaxxaamura tokkootti (<strong>singularity</strong>) kottoomu. Daangaan isaa <strong>event horizon</strong> jedhama; wanti tokko erga achi seenee booda deebi'ee hin baʼu.</p>
        <div class="en">Gravity is so strong not even light can escape; the core collapses into a point of infinite density.</div>
        <div class="eqn">Rₛ = 2GM / c²</div>
        <p style="margin:0;font-size:12.5px;">(Schwarzschild Radius — fageenya event horizon-ii kan ifni keessaa bahuu hin dandeenye)</p>
      </div>

      <h3 class="sec"><span class="tag">19.2</span> Cuunfaa Amaloota Wantoota Suntuuraman</h3>
      <table class="oro">
        <tr><th>Amala</th><th>Normal Pulsar</th><th>Millisecond Pulsar</th><th>Magnetar</th></tr>
        <tr><td>Period (P)</td><td>0.1 – 5 s</td><td>1 – 10 ms</td><td>1 – 10 s</td></tr>
        <tr><td>Magnetic Field (B)</td><td>10¹² G</td><td>10⁸ – 10⁹ G</td><td>10¹⁴ – 10¹⁵ G</td></tr>
        <tr><td>Umurii (τ)</td><td>Dargaggummaa / Giddu-galeessaa</td><td>Bayeessaa (Recycled)</td><td>Dargaggummaa baay'ee</td></tr>
      </table>

      <h3 class="sec"><span class="tag">19.3</span> Rukkina Addaa Urjii Niiwutiroonii</h3>
      <p>Rukkinni urjii niiwutiroonii akka malee ol-aanaa waan ta'eef, falaanaa xinnoo (teaspoon) tokko yoo furan ulfaatinni isaa lafa irratti tulluu guddaa (biliyoona hedduu toonii) tilmaamama.</p>
      <div class="en">The density of a neutron star is so extreme that a single teaspoon of its material would weigh billions of tons on Earth.</div>
      <div class="eqn">ρ = M/V ≈ 10¹⁷ kg/m³</div>
    </section>

    <!-- ============ KUTAA 20 ============ -->
    <section class="page" id="page-k20" style="--accent:var(--c20-violet);">
      <div class="eyebrow">Kutaa 20</div>
      <h2 class="page-title">📊 <span class="accent-word">Diyaagiraamiiwwan</span> Xiinxala Urjiilee</h2>
      <p class="page-lede">H-R Diagram fi P-Pdot Diagram — meeshaalee ijoo fiiziksii urjiilee keessatti fayyadaman.</p>

      <h3 class="sec"><span class="tag">20.1</span> H-R Diagram Deep Dive</h3>
      <p>H-R Diagram-iin meeshaa fiiziksii urjiilee keessatti baay'ee barbaachisaa dha. Gadi fageenyaan yoo ilaallu, ho'i fi ifinni urjiilee akkamitti akka jijjiiraman agarsiisa.</p>
      <ul class="oro">
        <li><strong>Axis-X:</strong> Effective Temperature (T_eff, Kelvin) — gara bitaatti ho'aa, gara mirgaatti qorraa deema.</li>
        <li><strong>Axis-Y:</strong> Luminosity (L/L☉) — gara olitti ifinna guddaa agarsiisa.</li>
      </ul>
      <div class="card accented">
        <p style="margin:0;">💡 Neutron star tokko guddinni ishee (R) baay'ee xiqqaa waan ta'eef, H-R diagram irratti gara jala-bitaatti argamti.</p>
      </div>

      <h3 class="sec"><span class="tag">20.2</span> P-Pdot Diagram (Rotating Neutron Stars)</h3>
      <p>Diyaagiraamiin <strong>P-Pdot</strong> (Period vs. Period derivative) urjiilee niiwutiroonii (Pulsars) umrii isaaniif hamma maagineetiksii isaanii addaan baasuuf gargaara. Sababa kanaaf "H-R Diagram of Pulsars" jedhamees waamama.</p>
      <div class="grid2">
        <div class="card">
          <div class="card-h">Characteristic Age (Umurii Evoluushinii)</div>
          <div class="eqn" style="margin:0;">τ = P / (2·Ṗ)</div>
        </div>
        <div class="card">
          <div class="card-h">Magnetic Field Strength</div>
          <div class="eqn" style="margin:0;">B ∝ √(P·Ṗ)</div>
        </div>
      </div>

      <h3 class="sec"><span class="tag">20.3</span> Radiative Energy Loss (f⁶ Relation)</h3>
      <p>Urjiin niiwutiroonii tokko yeroo naanna'u, anniisaa isaa bifa electromagnetic radiation fi gravitational waves-tiin of irraa gadi lakkisa. Anniisaan gadi lakkifamu kun sochii naannoo (frequency, f) waliin walqabsiisa addaa qaba:</p>
      <div class="eqn">Ė ∝ f⁶</div>
      <p style="margin:0;">Kun walqabsiisa <em>model-agnostic</em> ta'ee, astiroofiiziksii keessatti amaloota evoluushinii urjiilee niiwutiroonii qorachuuf gargaara.</p>
    </section>

    <!-- ============ KUTAA 21 ============ -->
    <section class="page" id="page-k21" style="--accent:var(--c21-teal);">
      <div class="eyebrow">Kutaa 21</div>
      <h2 class="page-title">🎬 <span class="accent-word">Ti'oorii Relatiivitii</span> — Albeert Anishtaayin</h2>
      <p class="page-lede">Ti'ooriin kun 'Gravity' maal akka ta'e bal'inaan ibsa — keessattuu boolla gurraacha fi bal'achuu yuunivarsii hubachuuf murteessaa dha.</p>
      <div class="en">The Theory of Relativity is a fundamental concept developed by Albert Einstein, divided into Special Relativity and General Relativity.</div>

      <h3 class="sec"><span class="tag">21.1</span> Relatiivitii Addaa (Special Relativity — 1905)</h3>
      <p>Ti'ooriin kun waa'ee walitti dhufeenya yeroo, fageenyaa fi ulfaatina wantoota saffisa guddaan (saffisa ifaatti dhihaatan) socho'anii ibsa. Yaada kana keessatti wanti guddaan "Saffisa Ifaa" (Speed of Light) dhaabbataa dha. Wantoonni yoo baay'ee saffisan, yeroon isaaniif ni suuta deema (<em>Time Dilation</em>).</p>
      <div class="grid2">
        <div class="card">
          <div class="card-h">Mass–Energy Equivalence</div>
          <div class="eqn" style="margin:0 0 8px;">E = mc²</div>
          <p style="margin:0;font-size:13px;">E = anniisaa, m = ulfaatina, c = saffisa ifaa (3 × 10⁸ m/s)</p>
        </div>
        <div class="card">
          <div class="card-h">Time Dilation</div>
          <div class="eqn" style="margin:0 0 8px;">t′ = t / √(1 − v²/c²)</div>
          <p style="margin:0;font-size:13px;">t′ = yeroo namni socho'u lakkaa'u, t = yeroo namni dhaabbatu lakkaa'u, v = saffisa wantichaa</p>
        </div>
      </div>

      <h3 class="sec"><span class="tag">21.2</span> Relatiivitii Waliigalaa (General Relativity — 1915)</h3>
      <p>Kun waa'ee harkisa biiftuu (gravity) ibsa. Harkisni humna wantoonni ittiin wal harkisan qofa utuu hin taane, "Space-time" (bakka fi yeroo) akka micciiramu (curvature) kan taasisu dha. Wantoonni ulfaatina guddaa qaban (akka urjiilee) space-time micciiruudhaan wantoonni biroo akka isaanitti jiigan taasisu.</p>
      <div class="card">
        <div class="card-h">Walqixxaattoo Dirree (Einstein Field Equations)</div>
        <div class="eqn">G_μν + Λg_μν = (8πG/c⁴)·T_μν</div>
        <ul class="oro" style="margin:0;">
          <li><strong>G_μν</strong> — qaxxaamura space-time (curvature)</li>
          <li><strong>Λ</strong> — cosmological constant</li>
          <li><strong>g_μν</strong> — metric tensor</li>
          <li><strong>T_μν</strong> — hamma anniisaa fi ulfaatina jiru (energy-momentum tensor)</li>
        </ul>
      </div>
    </section>

    <!-- ============ KUTAA 22 ============ -->
    <section class="page" id="page-k22" style="--accent:var(--c22-slate);">
      <div class="eyebrow">Kutaa 22</div>
      <h2 class="page-title">🌑 <span class="accent-word">Dark Matter</span> fi Dark Energy</h2>
      <p class="page-lede">Yuunivarsii keessatti waan ijaan hin argamneef humna itti fufiinsaan hin hubatamne — garuu bal'ina qaamolee hawwaa hunda kan too'atu.</p>

      <div class="grid2">
        <div class="card accented">
          <div class="card-h">🌑 Dark Matter</div>
          <p>Kun wanta ijaan hin argamne ta'ee, garuu harkisa hawwaa (gravity) qabu. Galaaksiiwwan akka walitti qabamanii turan gargaara.</p>
          <div class="en" style="margin:0;">An invisible substance that does not emit light but exerts gravitational pull, holding galaxies together.</div>
        </div>
        <div class="card accented">
          <div class="card-h">⚡ Dark Energy</div>
          <p>Kun immoo humna yuunivarsiin ittiin saffisaan bal'atu.</p>
          <div class="en" style="margin:0;">A mysterious force causing the expansion of the universe to accelerate.</div>
        </div>
      </div>
    </section>

    <!-- ============ KUTAA 23 ============ -->
    <section class="page" id="page-k23" style="--accent:var(--c23-orange);">
      <div class="eyebrow">Kutaa 23</div>
      <h2 class="page-title">🔬 <span class="accent-word">Seera Paawulii</span> (Pauli Exclusion Principle)</h2>
      <p class="page-lede">Seerri kun astiroofiiziksii keessatti baay'ee barbaachisaa dha.</p>

      <p>Urjiileen du'an (White Dwarfs) akka guutummaatti hin jignee fi jabaatanii akka dhaabbatan kan godhu <strong>"electron degeneracy pressure"</strong> jedhamu dha; kunis seera Paawuliitiin ibsama.</p>
      <div class="en">In astrophysics, this principle explains how white-dwarf stars remain stable — it creates electron degeneracy pressure, which prevents the star from collapsing further under its own gravity.</div>

      <h3 class="sec"><span class="tag">23.1</span> Maaliif Seerotni Kun Baay'atu?</h3>
      <p>Astiroofiiziksiin fiiziksii wantoota xixiqqoo (Quantum Mechanics) fi fiiziksii wantoota gurguddaa (Relativity) walitti fida. Kanaafuu, wantoota adda addaa ibsuuf seerota hedduutu barbaachisa:</p>
      <ul class="oro">
        <li><strong>Sochii pilaaneetotaa ibsuuf</strong> — seera Niwutan fi Keepilar</li>
        <li><strong>Ifa urjiilee qorachuuf</strong> — seera Wien fi Stefan-Boltzmann</li>
        <li><strong>Uumama yuunivarsii hubachuuf</strong> — seera Hubble fi Big Bang</li>
      </ul>
    </section>

    <!-- ============ KUTAA 24 — ANIMEESHINII ============ -->
    <section class="page active" id="page-k24" style="--accent:var(--c24-blue);">
      <div class="eyebrow">Kutaa 24 · Meeshaa Xiinxalaa</div>
      <h2 class="page-title">🌀 <span class="accent-word">Animeeshinii 3D</span> — Urjii Niiwutiroonii Naanna'aa</h2>
      <p class="page-lede">Malli kun sochii urjii niiwutiroonii fi chaartii anniisaa gadi bu'uu walfaana, yeroo dhugaa keessatti (real-time) agarsiisa.</p>

      <div class="eqn">dE/dt = − (32/5) · (G·I²·Ω⁶ / c⁵)</div>
      <div class="eqn-cap">Radiative energy-loss equation kan sochii urjii niiwutiroonii bulchu</div>

      <div class="sim-wrap">
        <div class="sim-controls">
          <div class="card">
            <div class="ctrl">
              <label>Saffisa Naannoo (Ω) <b id="k24-speed-val">5</b></label>
              <input type="range" id="k24-speed" min="1" max="10" value="5" step="1">
            </div>
            <div class="ctrl">
              <label>Moment of Inertia (I) <b id="k24-inertia-val">1.5</b></label>
              <input type="range" id="k24-inertia" min="1.0" max="3.0" value="1.5" step="0.1">
            </div>
            <button class="sim-btn" id="k24-reset">↺ Anniisaa Deebisi (Reset)</button>
          </div>

          <div class="card" style="margin-top:14px;">
            <div class="card-h" style="margin-bottom:10px;">📋 Gatiiwwan Yeroo Ammaa</div>
            <div class="kv" style="grid-template-columns:1fr 1fr;">
              <div class="k">Yeroo (step)</div><div class="v" id="k24-t">0</div>
              <div class="k">Ω (rad/s)</div><div class="v" id="k24-omega">5</div>
              <div class="k">I</div><div class="v" id="k24-I">1.5</div>
              <div class="k">Anniisaa hafte</div><div class="v" id="k24-energy" style="color:var(--c24-blue);">100.00 %</div>
            </div>
          </div>
        </div>

        <div>
          <div class="stage">
            <canvas id="k24-star-canvas" height="320"></canvas>
          </div>
          <div class="card" style="margin-top:14px;">
            <div class="card-h" style="margin-bottom:6px;">📉 Anniisaa Gadi Bu'uu — Yeroo Dhugaa</div>
            <canvas id="k24-chart-canvas" height="170"></canvas>
          </div>
        </div>
      </div>
    </section>

    <div class="foot-note">🌌 Kitesa Astro — Qophii Barsiisaa Qixxeessaa Nagaasaa Fayisaa · Kutaa 17–24</div>
  </main>
</div>
</div>

<script>
(function(){
  const root = document.getElementById('kitesa-astro-root');

  /* ---------- NAV ---------- */
  const navBtns = root.querySelectorAll('.nav-btn');
  const pages = root.querySelectorAll('.page');
  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      navBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const target = 'page-' + btn.dataset.page;
      pages.forEach(p => p.classList.toggle('active', p.id === target));
    });
  });

  /* ---------- TABS ---------- */
  const tabBtns = root.querySelectorAll('.tabbtn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const group = btn.dataset.tabgroup, tab = btn.dataset.tab;
      root.querySelectorAll('.tabbtn[data-tabgroup="'+group+'"]').forEach(b => b.classList.toggle('active', b === btn));
      root.querySelectorAll('.tabpanel[data-tabgroup="'+group+'"]').forEach(p => p.classList.toggle('active', p.dataset.tab === tab));
    });
  });

  /* ---------- SIMULATION: rotating neutron star + energy chart ---------- */
  const starCanvas = root.querySelector('#k24-star-canvas');
  const chartCanvas = root.querySelector('#k24-chart-canvas');
  const sctx = starCanvas.getContext('2d');
  const cctx = chartCanvas.getContext('2d');

  const speedInput = root.querySelector('#k24-speed');
  const inertiaInput = root.querySelector('#k24-inertia');
  const speedVal = root.querySelector('#k24-speed-val');
  const inertiaVal = root.querySelector('#k24-inertia-val');
  const resetBtn = root.querySelector('#k24-reset');

  const tOut = root.querySelector('#k24-t');
  const omegaOut = root.querySelector('#k24-omega');
  const IOut = root.querySelector('#k24-I');
  const energyOut = root.querySelector('#k24-energy');

  function resizeCanvases(){
    const w1 = starCanvas.parentElement.clientWidth;
    starCanvas.width = w1; starCanvas.height = 320;
    const w2 = chartCanvas.parentElement.clientWidth;
    chartCanvas.width = w2; chartCanvas.height = 170;
  }
  window.addEventListener('resize', resizeCanvases);
  resizeCanvases();

  let t = 0;
  let energy = 100.0;
  const E_INITIAL = 100.0;
  let history = [];
  let stars = [];
  for(let i=0;i<70;i++){
    stars.push({x:Math.random(), y:Math.random(), r:Math.random()*1.4+0.3, tw:Math.random()*Math.PI*2});
  }

  function drawStarfield(w,h){
    stars.forEach(s => {
      const tw = 0.5 + 0.5*Math.sin(s.tw + t*0.05);
      sctx.beginPath();
      sctx.arc(s.x*w, s.y*h, s.r, 0, Math.PI*2);
      sctx.fillStyle = 'rgba(255,255,255,'+(0.25+0.5*tw)+')';
      sctx.fill();
    });
  }

  function drawNeutronStar(){
    const w = starCanvas.width, h = starCanvas.height;
    sctx.clearRect(0,0,w,h);
    drawStarfield(w,h);

    const cx = w/2, cy = h/2;
    const speed = parseFloat(speedInput.value);
    const angle = (t * speed * 0.05) % (Math.PI*2);
    const tiltY = Math.sin(t*0.02) * 0.25;

    // outer glow
    const glowR = 78;
    const grad = sctx.createRadialGradient(cx,cy,4,cx,cy,glowR);
    grad.addColorStop(0,'rgba(120,200,255,0.55)');
    grad.addColorStop(1,'rgba(120,200,255,0)');
    sctx.fillStyle = grad;
    sctx.beginPath(); sctx.arc(cx,cy,glowR,0,Math.PI*2); sctx.fill();

    // beams (rotating, two opposite)
    const beamLen = Math.min(w,h)*0.42;
    [angle, angle+Math.PI].forEach((a,i) => {
      const ex = cx + Math.cos(a)*beamLen;
      const ey = cy + Math.sin(a)*beamLen*(0.35+tiltY*0.6);
      const bgrad = sctx.createLinearGradient(cx,cy,ex,ey);
      bgrad.addColorStop(0,'rgba(90,200,255,0.95)');
      bgrad.addColorStop(1,'rgba(90,200,255,0)');
      sctx.strokeStyle = bgrad;
      sctx.lineWidth = 10;
      sctx.lineCap = 'round';
      sctx.beginPath(); sctx.moveTo(cx,cy); sctx.lineTo(ex,ey); sctx.stroke();
    });

    // core sphere
    const coreR = 30;
    const coreGrad = sctx.createRadialGradient(cx-8,cy-10,3,cx,cy,coreR);
    coreGrad.addColorStop(0,'#eaf7ff');
    coreGrad.addColorStop(0.4,'#7fd4ff');
    coreGrad.addColorStop(1,'#1a3a6b');
    sctx.fillStyle = coreGrad;
    sctx.beginPath(); sctx.ellipse(cx,cy,coreR,coreR*(0.92+tiltY*0.1),0,0,Math.PI*2); sctx.fill();

    // rotation ring hint
    sctx.strokeStyle = 'rgba(120,200,255,0.35)';
    sctx.lineWidth = 1.5;
    sctx.beginPath();
    sctx.ellipse(cx,cy,coreR+14,(coreR+14)*0.32,angle*0.5,0,Math.PI*2);
    sctx.stroke();
  }

  function drawChart(){
    const w = chartCanvas.width, h = chartCanvas.height;
    cctx.clearRect(0,0,w,h);

    const pad = 28;
    cctx.strokeStyle = 'rgba(255,255,255,0.12)';
    cctx.lineWidth = 1;
    cctx.beginPath();
    cctx.moveTo(pad,8); cctx.lineTo(pad,h-pad); cctx.lineTo(w-8,h-pad);
    cctx.stroke();

    cctx.fillStyle = 'rgba(184,189,216,0.8)';
    cctx.font = '10px monospace';
    cctx.fillText('100%', 2, 14);
    cctx.fillText('0%', 10, h-pad+4);

    if(history.length < 2) return;
    const maxN = 60;
    const data = history.slice(-maxN);
    const stepX = (w - pad - 12) / (maxN-1);

    cctx.beginPath();
    data.forEach((v,i) => {
      const x = pad + i*stepX;
      const y = 8 + (1 - v/100) * (h - pad - 8);
      if(i===0) cctx.moveTo(x,y); else cctx.lineTo(x,y);
    });
    cctx.strokeStyle = '#ff6b8b';
    cctx.lineWidth = 2.4;
    cctx.stroke();

    // last point marker
    const lastV = data[data.length-1];
    const lx = pad + (data.length-1)*stepX;
    const ly = 8 + (1 - lastV/100) * (h - pad - 8);
    cctx.beginPath(); cctx.arc(lx,ly,3.5,0,Math.PI*2);
    cctx.fillStyle = '#ff6b8b'; cctx.fill();
  }

  function tick(){
    const speed = parseFloat(speedInput.value);
    const inertia = parseFloat(inertiaInput.value);
    speedVal.textContent = speed.toFixed(0);
    inertiaVal.textContent = inertia.toFixed(1);

    const lossRate = 0.008 * (speed**2) * inertia;
    energy = Math.max(0, energy - lossRate);
    if(energy <= 0){
      energy = E_INITIAL;
      history = [];
      t = 0;
    }
    history.push(energy);
    if(history.length > 60) history.shift();

    tOut.textContent = t;
    omegaOut.textContent = speed.toFixed(0) + ' rad/s';
    IOut.textContent = inertia.toFixed(1);
    energyOut.textContent = energy.toFixed(2) + ' %';

    drawNeutronStar();
    drawChart();

    t++;
    requestAnimationFrame(tick);
  }

  resetBtn.addEventListener('click', () => {
    energy = E_INITIAL; history = []; t = 0;
  });

  requestAnimationFrame(tick);
})();
</script>
</div>
