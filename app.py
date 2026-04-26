import streamlit as st
from datetime import date, datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from helpers import calculate_week, get_trimester, get_days_remaining
from utils.styles import inject_css
from data.ayurveda_data import (
    get_weekly_data, get_dosha_info, get_seasonal_advice,
    MAAS_DATA, PRASAVA_TIPS, SATTVIC_FOODS
)

st.set_page_config(
    page_title="गर्भावस्था आयुर्वेद",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_css()

# ─── Session State ───────────────────────────────────────────────────────────
if "lmp_date" not in st.session_state:
    st.session_state.lmp_date = None
if "dosha" not in st.session_state:
    st.session_state.dosha = None
if "name" not in st.session_state:
    st.session_state.name = ""
if "page" not in st.session_state:
    st.session_state.page = "home"

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sidebar-logo'>
        <span class='lotus'>🪷</span>
        <h2>गर्भावस्था<br><span class='gold'>आयुर्वेद</span></h2>
        <p class='tagline'>प्रकृति की गोद में सुरक्षित मातृत्व</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    pages = {
        "🏠 गृह": "home",
        "📅 सप्ताह-दर-सप्ताह": "weekly",
        "🌿 आहार विधान": "diet",
        "🧘 दिनचर्या": "routine",
        "💊 रसायन & हर्ब्स": "herbs",
        "🌸 मासानुमासिक": "maas",
        "🔮 दोष परीक्षण": "dosha",
        "🌙 ऋतु अनुसार": "seasonal",
        "🩺 लक्षण सहायक": "symptoms",
        "📖 गर्भसंस्कार": "sanskar",
    }

    for label, key in pages.items():
        btn_class = "nav-btn-active" if st.session_state.page == key else "nav-btn"
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div class='sidebar-footer'>
        <p>⚕️ यह ऐप केवल सूचनात्मक है।<br>
        चिकित्सक परामर्श अनिवार्य है।</p>
    </div>
    """, unsafe_allow_html=True)

# ─── Helper ───────────────────────────────────────────────────────────────────
def show_setup_banner():
    st.markdown("""
    <div class='setup-banner'>
        <h3>🪷 अपनी जानकारी भरें</h3>
        <p>बेहतर अनुभव के लिए कृपया गृह पृष्ठ पर अपनी जानकारी दर्ज करें।</p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════
def page_home():
    st.markdown("<h1 class='page-title'>🪷 गर्भावस्था आयुर्वेद केंद्र</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>आयुर्वेद की प्राचीन विद्या से अपने मातृत्व को समृद्ध बनाएं</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("<div class='card glass-card'>", unsafe_allow_html=True)
        st.markdown("### 📝 आपकी जानकारी")

        name = st.text_input("माँ का नाम", value=st.session_state.name, placeholder="आपका नाम यहाँ लिखें...")
        lmp = st.date_input(
            "अंतिम माहवारी की तारीख (LMP)",
            value=st.session_state.lmp_date or (date.today() - timedelta(weeks=10)),
            min_value=date.today() - timedelta(weeks=42),
            max_value=date.today()
        )
        dosha = st.selectbox(
            "आपकी प्रकृति (दोष)",
            ["जानें नहीं (परीक्षण करें →)", "वात", "पित्त", "कफ", "वात-पित्त", "पित्त-कफ", "वात-कफ", "त्रिदोषज"],
            index=0
        )

        if st.button("✅ सहेजें", use_container_width=True):
            st.session_state.name = name
            st.session_state.lmp_date = lmp
            st.session_state.dosha = dosha if "परीक्षण" not in dosha else st.session_state.dosha
            st.success("जानकारी सहेज ली गई! 🌸")
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if st.session_state.lmp_date:
            week = calculate_week(st.session_state.lmp_date)
            trimester = get_trimester(week)
            days_left = get_days_remaining(st.session_state.lmp_date)
            edd = st.session_state.lmp_date + timedelta(weeks=40)
            progress = min(week / 40, 1.0)

            st.markdown(f"""
            <div class='card progress-card'>
                <div class='greeting'>नमस्ते, {st.session_state.name or 'माँ'} 🌸</div>
                <div class='week-display'>
                    <span class='week-num'>{week}</span>
                    <span class='week-label'>सप्ताह</span>
                </div>
                <div class='trimester-badge t{trimester}'>{trimester}{'वाँ' if trimester==1 else 'रा'} त्रैमास</div>
                <div class='progress-bar-wrap'>
                    <div class='progress-bar-fill' style='width:{progress*100:.1f}%'></div>
                </div>
                <div class='progress-text'>{progress*100:.0f}% पूर्ण • {days_left} दिन शेष</div>
                <div class='edd-text'>प्रसव तिथि: {edd.strftime('%d %B %Y')}</div>
            </div>
            """, unsafe_allow_html=True)

            # Quick Tips
            weekly = get_weekly_data(week)
            st.markdown(f"""
            <div class='card tip-card'>
                <h4>🌿 इस सप्ताह का आयुर्वेदिक संदेश</h4>
                <p class='tip-text'>{weekly['aaj_ka_sandesh']}</p>
                <div class='herb-badge'>🌱 {weekly['herb']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='card welcome-card'>
                <div class='welcome-icon'>🪷</div>
                <h3>आयुर्वेद में स्वागत है!</h3>
                <p>अपनी LMP तारीख भरें और<br>अपनी यात्रा शुरू करें।</p>
                <div class='sanskrit'>
                    <em>"गर्भिणी परमो धर्मः"</em><br>
                    <small>गर्भवती माता सर्वोच्च धर्म है</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Stats Row
    if st.session_state.lmp_date:
        week = calculate_week(st.session_state.lmp_date)
        weekly = get_weekly_data(week)
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        metrics = [
            ("🍃 अनुशंसित रस", weekly['rasa'], ""),
            ("🧘 प्राणायाम", weekly['pranayama'], ""),
            ("🌙 निद्रा", weekly['sleep'], "घंटे"),
            ("💧 जल", weekly['water'], "गिलास/दिन"),
        ]
        for col, (label, val, unit) in zip([c1,c2,c3,c4], metrics):
            with col:
                st.markdown(f"""
                <div class='metric-card'>
                    <div class='metric-label'>{label}</div>
                    <div class='metric-value'>{val}<span class='metric-unit'> {unit}</span></div>
                </div>
                """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: WEEKLY
# ═══════════════════════════════════════════════════════════════════════════════
def page_weekly():
    st.markdown("<h1 class='page-title'>📅 सप्ताह-दर-सप्ताह विकास</h1>", unsafe_allow_html=True)

    if not st.session_state.lmp_date:
        show_setup_banner(); return

    week = calculate_week(st.session_state.lmp_date)
    selected_week = st.slider("सप्ताह चुनें", 1, 40, week)
    data = get_weekly_data(selected_week)
    trimester = get_trimester(selected_week)

    st.markdown(f"""
    <div class='week-header t{trimester}'>
        <span class='wh-week'>सप्ताह {selected_week}</span>
        <span class='wh-tri'>{trimester}{'वाँ' if trimester==1 else 'रा'} त्रैमास</span>
        <span class='wh-size'>शिशु आकार: {data['baby_size']}</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class='card section-card'>
            <h3>👶 शिशु विकास</h3>
            <p>{data['baby_dev']}</p>
        </div>
        <div class='card section-card'>
            <h3>🌿 आयुर्वेदिक दृष्टि</h3>
            <p>{data['ayurveda_view']}</p>
            <div class='dosha-tag'>प्रमुख दोष: {data['dominant_dosha']}</div>
        </div>
        <div class='card section-card'>
            <h3>🌱 अनुशंसित हर्ब</h3>
            <p class='herb-main'>{data['herb']}</p>
            <p>{data['herb_benefit']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card section-card'>
            <h3>🍽️ आहार विधान</h3>
            {''.join(f"<div class='list-item'>✅ {item}</div>" for item in data['diet'])}
        </div>
        <div class='card section-card'>
            <h3>🧘 दिनचर्या</h3>
            {''.join(f"<div class='list-item'>🌸 {item}</div>" for item in data['routine'])}
        </div>
        <div class='card section-card caution-card'>
            <h3>⚠️ परहेज करें</h3>
            {''.join(f"<div class='list-item caution'>❌ {item}</div>" for item in data['avoid'])}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card mantra-card'>
        <h3>🕉️ इस सप्ताह का मंत्र</h3>
        <div class='mantra-text'>{data['mantra']}</div>
        <div class='mantra-meaning'>{data['mantra_meaning']}</div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DIET
# ═══════════════════════════════════════════════════════════════════════════════
def page_diet():
    st.markdown("<h1 class='page-title'>🍽️ आयुर्वेदिक आहार विधान</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>सात्त्विक आहार से माता और शिशु दोनों स्वस्थ रहते हैं</p>", unsafe_allow_html=True)

    tabs = st.tabs(["🌅 सुबह", "🌞 दोपहर", "🌙 रात", "🚫 निषिद्ध", "💎 सुपरफूड्स"])

    meal_plans = {
        "🌅 सुबह": [
            ("उठते ही", "गुनगुना पानी + शहद + नींबू (यदि पित्त न हो)"),
            ("नाश्ता", "दलिया / पोहा / इडली / अंकुरित अनाज"),
            ("फल", "आम, केला, अनार, सेब (मौसम अनुसार)"),
            ("दूध", "हल्दी दूध या अश्वगंधा दूध — प्रकृति अनुसार"),
        ],
        "🌞 दोपहर": [
            ("मुख्य भोजन", "खिचड़ी / दाल-चावल / रोटी-सब्जी"),
            ("सब्जियाँ", "परवल, लौकी, तोरई, पालक, मेथी"),
            ("दही/छाछ", "छाछ (पित्त के लिए उत्तम), दही नहीं"),
            ("घी", "देसी गाय का घी अवश्य"),
        ],
        "🌙 रात": [
            ("हल्का भोजन", "खिचड़ी / मूंग दाल सूप"),
            ("समय", "सूर्यास्त से पहले या 7 बजे तक"),
            ("दूध", "सोने से पहले केसर-इलायची दूध"),
            ("परहेज", "भारी, तला, मसालेदार नहीं"),
        ],
        "🚫 निषिद्ध": [],
        "💎 सुपरफूड्स": [],
    }

    with tabs[0]:
        for time, item in meal_plans["🌅 सुबह"]:
            st.markdown(f"""
            <div class='meal-item'>
                <span class='meal-time'>{time}</span>
                <span class='meal-desc'>{item}</span>
            </div>
            """, unsafe_allow_html=True)

    with tabs[1]:
        for time, item in meal_plans["🌞 दोपहर"]:
            st.markdown(f"""
            <div class='meal-item'>
                <span class='meal-time'>{time}</span>
                <span class='meal-desc'>{item}</span>
            </div>
            """, unsafe_allow_html=True)

    with tabs[2]:
        for time, item in meal_plans["🌙 रात"]:
            st.markdown(f"""
            <div class='meal-item'>
                <span class='meal-time'>{time}</span>
                <span class='meal-desc'>{item}</span>
            </div>
            """, unsafe_allow_html=True)

    with tabs[3]:
        avoid_foods = [
            ("🥩 मांस-मछली", "विशेषतः प्रथम त्रैमास में"),
            ("🍺 मद्य", "पूर्णतः वर्जित"),
            ("☕ अत्यधिक चाय/कॉफी", "दिन में 1 से अधिक नहीं"),
            ("🌶️ अत्यधिक तीखा", "पित्त बढ़ाता है"),
            ("🧅 कच्चा प्याज-लहसुन", "तामसिक आहार"),
            ("🍟 जंक फूड", "वात-पित्त दोनों बिगाड़ता है"),
            ("🥶 ठंडा बासी", "पाचन शक्ति कमज़ोर करता है"),
            ("🍫 अत्यधिक मीठा", "कफ और मधुमेह का खतरा"),
        ]
        for food, reason in avoid_foods:
            st.markdown(f"""
            <div class='avoid-item'>
                <span class='avoid-food'>{food}</span>
                <span class='avoid-reason'>{reason}</span>
            </div>
            """, unsafe_allow_html=True)

    with tabs[4]:
        for food, desc, benefit in SATTVIC_FOODS:
            st.markdown(f"""
            <div class='super-food-card'>
                <div class='sf-name'>{food}</div>
                <div class='sf-desc'>{desc}</div>
                <div class='sf-benefit'>✨ {benefit}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ROUTINE
# ═══════════════════════════════════════════════════════════════════════════════
def page_routine():
    st.markdown("<h1 class='page-title'>🧘 आयुर्वेदिक दिनचर्या</h1>", unsafe_allow_html=True)

    routine_data = [
        ("🌅 4:00 - 6:00", "ब्रह्म मुहूर्त", "उठना, ईश्वर स्मरण, धीमी सैर", "gold"),
        ("🚿 6:00 - 7:00", "शौच-स्नान", "हल्के गुनगुने पानी से स्नान, अभ्यंग (तेल मालिश)", "blue"),
        ("🧘 7:00 - 8:00", "योग-प्राणायाम", "अनुलोम-विलोम, भ्रामरी, यिन योग", "green"),
        ("🍽️ 8:00 - 9:00", "प्रातः आहार", "पोषण से भरपूर सात्त्विक नाश्ता", "orange"),
        ("🌿 9:00 - 12:00", "हल्की गतिविधि", "हल्का काम, पढ़ना, गर्भसंस्कार संगीत", "purple"),
        ("☀️ 12:00 - 1:00", "मध्याह्न भोजन", "मुख्य पोषक भोजन, शांति से खाएं", "orange"),
        ("😴 1:00 - 2:00", "विश्राम", "बायीं करवट सोना (वास्तु+रक्त संचार)", "blue"),
        ("🌸 2:00 - 5:00", "सौम्य गतिविधि", "हल्की कला, भजन, गर्भसंस्कार पाठ", "green"),
        ("🌆 5:00 - 6:00", "संध्या सैर", "ताज़ी हवा में धीमी सैर", "gold"),
        ("🍵 6:00 - 7:00", "संध्या भोजन", "हल्का, सुपाच्य भोजन — जल्दी खाएं", "orange"),
        ("📖 7:00 - 9:00", "शांत समय", "श्लोक, ध्यान, परिवार के साथ", "purple"),
        ("🌙 9:00 - 9:30", "निद्रा प्रस्तुति", "केसर दूध, पैर मालिश, दीप ध्यान", "blue"),
        ("💤 9:30", "निद्रा", "बायीं करवट, 7-8 घंटे", "green"),
    ]

    for time, title, desc, color in routine_data:
        st.markdown(f"""
        <div class='routine-item r-{color}'>
            <div class='r-time'>{time}</div>
            <div class='r-content'>
                <div class='r-title'>{title}</div>
                <div class='r-desc'>{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card yoga-card'>
        <h3>🧘 अनुशंसित प्राणायाम</h3>
        <div class='yoga-grid'>
            <div class='yoga-item'>
                <div class='yoga-name'>अनुलोम-विलोम</div>
                <div class='yoga-desc'>तनाव मुक्ति, ऑक्सीजन</div>
                <div class='yoga-time'>10 मिनट</div>
            </div>
            <div class='yoga-item'>
                <div class='yoga-name'>भ्रामरी</div>
                <div class='yoga-desc'>शिशु को सुनाई देता है</div>
                <div class='yoga-time'>5 मिनट</div>
            </div>
            <div class='yoga-item'>
                <div class='yoga-name'>उज्जायी</div>
                <div class='yoga-desc'>थायरॉइड, ऊर्जा</div>
                <div class='yoga-time'>5 मिनट</div>
            </div>
            <div class='yoga-item'>
                <div class='yoga-name'>शीतली</div>
                <div class='yoga-desc'>पित्त शमन, ठंडक</div>
                <div class='yoga-time'>3 मिनट</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HERBS
# ═══════════════════════════════════════════════════════════════════════════════
def page_herbs():
    st.markdown("<h1 class='page-title'>💊 रसायन एवं औषधि</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>⚠️ किसी भी जड़ी-बूटी का उपयोग आयुर्वेदिक वैद्य की सलाह से करें</p>", unsafe_allow_html=True)

    herbs = [
        {
            "name": "🌿 अश्वगंधा", "latin": "Withania somnifera",
            "benefit": "तनाव निवारण, शक्तिवर्धन, गर्भाशय मजबूती",
            "when": "द्वितीय-तृतीय त्रैमास में (वैद्य परामर्श से)",
            "how": "दूध के साथ 1/4 चम्मच",
            "caution": "प्रथम त्रैमास में सावधानी",
            "color": "green"
        },
        {
            "name": "🌱 शतावरी", "latin": "Asparagus racemosus",
            "benefit": "गर्भपोषण, दूध उत्पादन, हार्मोन संतुलन",
            "when": "पूरी गर्भावस्था में उत्तम",
            "how": "शतावरी कल्प या चूर्ण — दूध के साथ",
            "caution": "कफ प्रकृति में कम मात्रा",
            "color": "teal"
        },
        {
            "name": "🪷 लोध्र", "latin": "Symplocos racemosa",
            "benefit": "गर्भाशय टोनिंग, रक्तस्राव रोकने में",
            "when": "वैद्य निर्देशित समय पर",
            "how": "काढ़ा या चूर्ण",
            "caution": "स्वयं उपयोग न करें",
            "color": "pink"
        },
        {
            "name": "🌸 शंखपुष्पी", "latin": "Convolvulus pluricaulis",
            "benefit": "बुद्धि वर्धन, तनाव मुक्ति, स्मृति",
            "when": "पूरी गर्भावस्था",
            "how": "स्वरस या चूर्ण — शहद के साथ",
            "caution": "अत्यधिक मात्रा से बचें",
            "color": "purple"
        },
        {
            "name": "💛 हरिद्रा", "latin": "Curcuma longa (हल्दी)",
            "benefit": "सूजन रोधी, एंटीऑक्सीडेंट, रोग प्रतिरोधक",
            "when": "पूरी गर्भावस्था (भोजन में)",
            "how": "दूध में 1/4 चम्मच, या खाने में",
            "caution": "पूरक के रूप में अत्यधिक नहीं",
            "color": "yellow"
        },
        {
            "name": "🔴 लाल रसायन (सुवर्ण प्राश)", "latin": "Swarna Bhasma युक्त",
            "benefit": "गर्भ बल, शिशु बुद्धि, ओज वर्धन",
            "when": "विशेषज्ञ निर्देशित",
            "how": "केवल वैद्य से प्राप्त करें",
            "caution": "स्वर्ण युक्त — विशेषज्ञ आवश्यक",
            "color": "gold"
        },
    ]

    cols = st.columns(2)
    for i, herb in enumerate(herbs):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='card herb-card h-{herb["color"]}'>
                <div class='herb-header'>
                    <div class='herb-title'>{herb["name"]}</div>
                    <div class='herb-latin'>{herb["latin"]}</div>
                </div>
                <div class='herb-benefit'>✨ {herb["benefit"]}</div>
                <div class='herb-detail'><b>कब:</b> {herb["when"]}</div>
                <div class='herb-detail'><b>कैसे:</b> {herb["how"]}</div>
                <div class='herb-caution'>⚠️ {herb["caution"]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card rasayana-card'>
        <h3>💎 प्रमुख रसायन योग</h3>
        <div class='rasayana-grid'>
            <div class='ras-item'><b>च्यवनप्राश</b><br>रोग प्रतिरोधक, ओजवर्धन</div>
            <div class='ras-item'><b>त्रिफला</b><br>पाचन, कब्ज निवारण</div>
            <div class='ras-item'><b>सुवर्णप्राश</b><br>गर्भ बल, शिशु विकास</div>
            <div class='ras-item'><b>अश्वगंधा घृत</b><br>बल, स्थिरता, वात शमन</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: MAAS (Month by Month)
# ═══════════════════════════════════════════════════════════════════════════════
def page_maas():
    st.markdown("<h1 class='page-title'>🌸 मासानुमासिक आयुर्वेद</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>चरक संहिता और सुश्रुत संहिता के अनुसार गर्भावस्था के नव मास</p>", unsafe_allow_html=True)

    if st.session_state.lmp_date:
        week = calculate_week(st.session_state.lmp_date)
        current_month = min((week // 4) + 1, 9)
        default_month = current_month
    else:
        default_month = 1

    selected_month = st.select_slider(
        "मास चुनें",
        options=list(range(1, 10)),
        value=default_month,
        format_func=lambda x: f"{x}वाँ मास"
    )

    month_data = MAAS_DATA[selected_month - 1]

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div class='card maas-header-card'>
            <div class='maas-num'>{selected_month}</div>
            <div class='maas-title'>{month_data['name']}</div>
            <div class='maas-sanskrit'>{month_data['sanskrit']}</div>
        </div>
        <div class='card section-card'>
            <h3>👶 गर्भ विकास</h3>
            <p>{month_data['garbha_vikas']}</p>
        </div>
        <div class='card section-card'>
            <h3>🌿 आयुर्वेद विधान</h3>
            <p>{month_data['vidhaan']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card section-card'>
            <h3>🍽️ मास-विशेष आहार</h3>
            {''.join(f"<div class='list-item'>🌸 {item}</div>" for item in month_data['aahar'])}
        </div>
        <div class='card section-card'>
            <h3>💊 अनुशंसित औषध</h3>
            {''.join(f"<div class='list-item'>🌱 {item}</div>" for item in month_data['aushadh'])}
        </div>
        <div class='card section-card caution-card'>
            <h3>⚠️ विशेष सावधानी</h3>
            {''.join(f"<div class='list-item caution'>❌ {item}</div>" for item in month_data['savdhani'])}
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DOSHA
# ═══════════════════════════════════════════════════════════════════════════════
def page_dosha():
    st.markdown("<h1 class='page-title'>🔮 प्रकृति परीक्षण</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>अपनी आयुर्वेदिक प्रकृति जानें और व्यक्तिगत सलाह पाएं</p>", unsafe_allow_html=True)

    questions = [
        ("शरीर की बनावट", ["पतली, हड्डियाँ उभरी", "मध्यम, सुडौल", "भारी, मोटी"]),
        ("त्वचा", ["रूखी, खुरदरी", "गर्म, तैलीय, लाली", "मुलायम, ठंडी, चिकनी"]),
        ("बाल", ["रूखे, घुंघराले", "पतले, जल्दी सफेद", "घने, चिकने"]),
        ("पाचन", ["अनियमित, गैस", "तेज़, जलन", "धीमा, भारी"]),
        ("स्वभाव", ["चिंतित, चंचल", "तीव्र, क्रोधी", "शांत, सहनशील"]),
        ("नींद", ["कम, अनियमित", "कम पर गहरी", "अधिक, गहरी"]),
        ("बोलने का तरीका", ["तेज़, बहुत बोलना", "तीखा, स्पष्ट", "धीमा, कम बोलना"]),
        ("स्मृति", ["जल्दी सीखे, जल्दी भूले", "तेज़ स्मृति", "धीमी पर स्थायी"]),
    ]

    if "dosha_answers" not in st.session_state:
        st.session_state.dosha_answers = {}

    with st.form("dosha_quiz"):
        for i, (q, options) in enumerate(questions):
            answer = st.radio(
                f"**{i+1}. {q}**",
                options,
                key=f"dq_{i}",
                horizontal=True
            )
            st.session_state.dosha_answers[i] = options.index(answer)

        submitted = st.form_submit_button("🔮 प्रकृति जानें", use_container_width=True)

    if submitted or st.session_state.dosha_answers:
        answers = st.session_state.dosha_answers
        vata = sum(1 for v in answers.values() if v == 0)
        pitta = sum(1 for v in answers.values() if v == 1)
        kapha = sum(1 for v in answers.values() if v == 2)

        dominant = max([(vata, "वात"), (pitta, "पित्त"), (kapha, "कफ")], key=lambda x: x[0])[1]
        info = get_dosha_info(dominant)

        c1, c2, c3 = st.columns(3)
        for col, (name, score, emoji) in zip([c1,c2,c3], [
            ("वात", vata, "💨"), ("पित्त", pitta, "🔥"), ("कफ", kapha, "🌊")
        ]):
            with col:
                st.markdown(f"""
                <div class='dosha-score-card {"active-dosha" if name == dominant else ""}'>
                    <div class='ds-emoji'>{emoji}</div>
                    <div class='ds-name'>{name}</div>
                    <div class='ds-score'>{score}/{len(questions)}</div>
                    <div class='ds-bar'><div class='ds-fill' style='width:{score/len(questions)*100}%'></div></div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='card dosha-result-card'>
            <h2>आपकी प्रकृति: {dominant} 🎯</h2>
            <p>{info['description']}</p>
            <h3>गर्भावस्था में विशेष सलाह:</h3>
            {''.join(f"<div class='list-item'>🌿 {tip}</div>" for tip in info['pregnancy_tips'])}
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: SEASONAL
# ═══════════════════════════════════════════════════════════════════════════════
def page_seasonal():
    st.markdown("<h1 class='page-title'>🌙 ऋतु अनुसार आयुर्वेद</h1>", unsafe_allow_html=True)

    seasons = {
        "🌸 वसंत (मार्च-अप्रैल)": "vasant",
        "☀️ ग्रीष्म (मई-जून)": "grishma",
        "🌧️ वर्षा (जुलाई-अगस्त)": "varsha",
        "🍂 शरद (सितंबर-अक्टूबर)": "sharad",
        "❄️ हेमंत (नवंबर-दिसंबर)": "hemant",
        "🌨️ शिशिर (जनवरी-फरवरी)": "shishir",
    }

    selected_season = st.selectbox("ऋतु चुनें", list(seasons.keys()))
    season_key = seasons[selected_season]
    data = get_seasonal_advice(season_key)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class='card season-card'>
            <h3>🍽️ आहार</h3>
            {''.join(f"<div class='list-item'>✅ {item}</div>" for item in data['diet'])}
        </div>
        <div class='card season-card'>
            <h3>💊 विशेष औषध</h3>
            {''.join(f"<div class='list-item'>🌱 {item}</div>" for item in data['herbs'])}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card season-card'>
            <h3>🧘 दिनचर्या</h3>
            {''.join(f"<div class='list-item'>🌸 {item}</div>" for item in data['routine'])}
        </div>
        <div class='card season-card caution-card'>
            <h3>⚠️ परहेज</h3>
            {''.join(f"<div class='list-item caution'>❌ {item}</div>" for item in data['avoid'])}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card tip-card'>
        <h3>💡 ऋतु-विशेष संदेश</h3>
        <p>{data['special_message']}</p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: SYMPTOMS
# ═══════════════════════════════════════════════════════════════════════════════
def page_symptoms():
    st.markdown("<h1 class='page-title'>🩺 लक्षण सहायक</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>⚠️ यह सूचनात्मक है — गंभीर लक्षणों में तुरंत डॉक्टर से मिलें</p>", unsafe_allow_html=True)

    symptoms_data = {
        "🤢 मतली / उल्टी (Morning Sickness)": {
            "ayurveda": "वात-कफ असंतुलन",
            "remedies": [
                "अदरक की चाय (छोटे घूंट में)",
                "धनिया-पुदीना रस",
                "नींबू सूंघना या पानी में मिलाना",
                "थोड़ा-थोड़ा बार-बार खाना",
                "इलायची चबाना",
            ],
            "avoid": ["खाली पेट रहना", "तेज़ महक", "वसायुक्त भोजन"],
        },
        "💤 अत्यधिक थकान": {
            "ayurveda": "ओज क्षय, वात वृद्धि",
            "remedies": [
                "दोपहर में 30-45 मिनट विश्राम",
                "अश्वगंधा दूध (वैद्य सलाह से)",
                "खजूर + घी",
                "हल्का योग, गहरी साँस",
            ],
            "avoid": ["रात जागना", "अत्यधिक परिश्रम"],
        },
        "🔥 सीने में जलन (Heartburn)": {
            "ayurveda": "पित्त वृद्धि",
            "remedies": [
                "नारियल पानी",
                "ठंडा दूध (कफ न हो तो)",
                "धनिया-जीरा पानी",
                "बाईं करवट सोना",
                "खाने के बाद न लेटना",
            ],
            "avoid": ["तीखा, खट्टा, गर्म", "रात को भारी खाना"],
        },
        "🦵 पैरों में सूजन": {
            "ayurveda": "कफ-वात, अपान वायु",
            "remedies": [
                "पैर ऊँचे करके बैठना",
                "हल्की पैर मालिश (तिल तेल)",
                "जल सेवन बढ़ाएं",
                "नमक कम करें",
                "छाछ पियें",
            ],
            "avoid": ["देर तक खड़े रहना", "अत्यधिक नमक"],
        },
        "😫 कब्ज": {
            "ayurveda": "वात वृद्धि, अपान विकृति",
            "remedies": [
                "त्रिफला रात को (वैद्य से)",
                "गुनगुना पानी + घी",
                "ईसबगोल",
                "फल और फाइबर",
                "हल्की सैर",
            ],
            "avoid": ["बासी भोजन", "शुष्क आहार", "तनाव"],
        },
        "😴 नींद न आना": {
            "ayurveda": "वात विकृति",
            "remedies": [
                "ब्राह्मी + दूध रात को",
                "पैर तलवों में घी मलना",
                "शयन से पहले ध्यान",
                "लैवेंडर या चंदन अगरबत्ती",
            ],
            "avoid": ["रात को स्क्रीन", "कैफीन शाम को"],
        },
    }

    selected_symptom = st.selectbox("लक्षण चुनें", list(symptoms_data.keys()))
    data = symptoms_data[selected_symptom]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class='card section-card'>
            <h3>🔮 आयुर्वेदिक कारण</h3>
            <p class='dosha-tag'>{data['ayurveda']}</p>
        </div>
        <div class='card section-card'>
            <h3>🌿 आयुर्वेदिक उपाय</h3>
            {''.join(f"<div class='list-item'>✅ {r}</div>" for r in data['remedies'])}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card section-card caution-card'>
            <h3>❌ परहेज करें</h3>
            {''.join(f"<div class='list-item caution'>🚫 {a}</div>" for a in data['avoid'])}
        </div>
        <div class='card emergency-card'>
            <h3>🚨 तुरंत डॉक्टर से मिलें यदि:</h3>
            <div class='list-item caution'>तेज़ दर्द, रक्तस्राव</div>
            <div class='list-item caution'>बच्चे की हलचल कम हो</div>
            <div class='list-item caution'>तेज़ बुखार, सिरदर्द</div>
            <div class='list-item caution'>दृष्टि धुंधली, चेहरे पर सूजन</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: GARBHASANSKAR
# ═══════════════════════════════════════════════════════════════════════════════
def page_sanskar():
    st.markdown("<h1 class='page-title'>📖 गर्भसंस्कार</h1>", unsafe_allow_html=True)
    st.markdown("<p class='page-sub'>शिशु के मन और चरित्र का निर्माण गर्भ से ही होता है — आयुर्वेद का अद्भुत ज्ञान</p>", unsafe_allow_html=True)

    tabs = st.tabs(["🎵 संगीत", "📚 कथाएं", "🧘 ध्यान", "🎨 कला", "🙏 मंत्र"])

    with tabs[0]:
        st.markdown("""
        <div class='card sanskar-card'>
            <h3>🎵 गर्भसंस्कार संगीत</h3>
            <p>शोध में सिद्ध हुआ है कि शिशु गर्भ में 16वें सप्ताह से सुनना शुरू करता है।</p>
            <div class='music-grid'>
                <div class='music-item'><div class='music-raga'>राग भैरवी</div><div class='music-effect'>शांति, नींद</div></div>
                <div class='music-item'><div class='music-raga'>राग यमन</div><div class='music-effect'>बुद्धि विकास</div></div>
                <div class='music-item'><div class='music-raga'>राग दरबारी</div><div class='music-effect'>गहरी शांति</div></div>
                <div class='music-item'><div class='music-raga'>राग बागेश्री</div><div class='music-effect'>प्रेम, कोमलता</div></div>
                <div class='music-item'><div class='music-raga'>राग तोड़ी</div><div class='music-effect'>एकाग्रता</div></div>
                <div class='music-item'><div class='music-raga'>भजन/स्तोत्र</div><div class='music-effect'>आध्यात्मिकता</div></div>
            </div>
            <p><b>समय:</b> सुबह 7-8 बजे और शाम 5-6 बजे — 20-30 मिनट</p>
        </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        stories = [
            ("अभिमन्यु की कथा", "चक्रव्यूह का ज्ञान माँ के गर्भ में मिला — एकाग्रता और ज्ञान"),
            ("प्रह्लाद की कथा", "भक्ति और सत्य का संस्कार गर्भ में मिला"),
            ("महाभारत/रामायण", "धर्म, सत्य, प्रेम के महान आख्यान"),
            ("जातक कथाएं", "बुद्ध के पूर्व जन्म की कथाएं — नैतिकता"),
            ("पंचतंत्र", "बुद्धि, चतुराई, मैत्री की कहानियां"),
        ]
        for title, desc in stories:
            st.markdown(f"""
            <div class='card story-card'>
                <div class='story-title'>{title}</div>
                <div class='story-desc'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("""
        <div class='card sanskar-card'>
            <h3>🧘 गर्भसंस्कार ध्यान विधि</h3>
            <div class='meditation-steps'>
                <div class='med-step'><span class='step-num'>1</span><span>आरामदायक स्थिति में बैठें या लेटें</span></div>
                <div class='med-step'><span class='step-num'>2</span><span>5 गहरी साँसें लें</span></div>
                <div class='med-step'><span class='step-num'>3</span><span>शिशु पर ध्यान केंद्रित करें</span></div>
                <div class='med-step'><span class='step-num'>4</span><span>प्रेम और शांति की भावना भेजें</span></div>
                <div class='med-step'><span class='step-num'>5</span><span>मन में शिशु से बात करें</span></div>
                <div class='med-step'><span class='step-num'>6</span><span>15-20 मिनट रोज़ करें</span></div>
            </div>
            <p class='meditation-quote'><em>"माता भावयते यद्यत् तद्भवेद् गर्भसंभवम्" <br>— माँ जो सोचती है, शिशु वही बनता है</em></p>
        </div>
        """, unsafe_allow_html=True)

    with tabs[3]:
        st.markdown("""
        <div class='card sanskar-card'>
            <h3>🎨 गर्भसंस्कार कला</h3>
            <p>रंग, रेखाएं और सौंदर्य — माँ की कला शिशु के सौंदर्यबोध को जगाती है।</p>
            <div class='art-grid'>
                <div class='art-item'>🖌️ चित्रकारी<br><small>प्रकृति, देवी-देवता</small></div>
                <div class='art-item'>🏺 मिट्टी कार्य<br><small>हाथ से बनाना</small></div>
                <div class='art-item'>🌺 फूल सज्जा<br><small>रंगोली, पुष्प</small></div>
                <div class='art-item'>📿 मनका<br><small>ध्यान के साथ</small></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tabs[4]:
        mantras = [
            ("गायत्री मंत्र", "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं...", "बुद्धि, प्रकाश"),
            ("महामृत्युञ्जय", "ॐ त्र्यम्बकं यजामहे...", "स्वास्थ्य, रक्षा"),
            ("सरस्वती वंदना", "या कुन्देन्दुतुषारहारधवला...", "ज्ञान, विद्या"),
            ("गर्भ रक्षा मंत्र", "ॐ नमो भगवते वासुदेवाय", "शिशु सुरक्षा"),
        ]
        for name, mantra, benefit in mantras:
            st.markdown(f"""
            <div class='card mantra-card'>
                <div class='mantra-name'>{name}</div>
                <div class='mantra-text'>{mantra}</div>
                <div class='mantra-benefit'>✨ {benefit}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# ROUTER
# ═══════════════════════════════════════════════════════════════════════════════
page_map = {
    "home": page_home,
    "weekly": page_weekly,
    "diet": page_diet,
    "routine": page_routine,
    "herbs": page_herbs,
    "maas": page_maas,
    "dosha": page_dosha,
    "seasonal": page_seasonal,
    "symptoms": page_symptoms,
    "sanskar": page_sanskar,
}

page_map.get(st.session_state.page, page_home)()
