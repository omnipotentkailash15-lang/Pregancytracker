import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Yatra+One&family=Hind:wght@300;400;500;600&family=Kalam:wght@400;700&display=swap');

    :root {
        --saffron: #FF6B35;
        --gold: #F4A300;
        --deep-green: #2D6A4F;
        --light-green: #52B788;
        --cream: #FFF8EF;
        --ivory: #FDFAF5;
        --deep-brown: #3D2B1F;
        --light-brown: #8B5E3C;
        --lotus-pink: #E8A0B4;
        --sky: #87CEEB;
        --card-bg: rgba(255,255,255,0.85);
        --border: rgba(244,163,0,0.2);
    }

    /* ── Base ── */
    .stApp {
        background: linear-gradient(135deg, #FFF8EF 0%, #F0F7EE 50%, #FFF0E6 100%);
        font-family: 'Hind', sans-serif;
        color: var(--deep-brown);
    }

    /* Hide default streamlit elements */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 1.5rem !important; max-width: 1200px; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2D6A4F 0%, #1B4332 60%, #0A2518 100%) !important;
        border-right: 2px solid var(--gold);
    }
    [data-testid="stSidebar"] * { color: #F0EDE8 !important; }

    .sidebar-logo {
        text-align: center;
        padding: 1.5rem 0.5rem 1rem;
    }
    .sidebar-logo .lotus { font-size: 2.5rem; display: block; margin-bottom: 0.3rem; }
    .sidebar-logo h2 { font-family: 'Yatra One', serif; font-size: 1.4rem; line-height: 1.3; color: #F0EDE8 !important; }
    .sidebar-logo .gold { color: var(--gold) !important; }
    .sidebar-logo .tagline { font-size: 0.7rem; color: #A8D5BA !important; font-style: italic; }

    .sidebar-footer p { font-size: 0.65rem; color: #7FB99A !important; text-align: center; line-height: 1.5; }

    /* ── Nav Buttons ── */
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(164,211,138,0.2) !important;
        color: #D4EDD9 !important;
        border-radius: 8px !important;
        margin: 2px 0 !important;
        font-size: 0.82rem !important;
        padding: 0.4rem 0.8rem !important;
        text-align: left !important;
        transition: all 0.2s ease !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(244,163,0,0.2) !important;
        border-color: var(--gold) !important;
        color: #FFD700 !important;
    }

    /* ── Page Titles ── */
    .page-title {
        font-family: 'Yatra One', serif;
        font-size: 2rem;
        color: var(--deep-green);
        margin: 0 0 0.3rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.08);
    }
    .page-sub {
        color: var(--light-brown);
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
        font-style: italic;
    }

    /* ── Cards ── */
    .card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border);
        box-shadow: 0 4px 20px rgba(45,106,79,0.08);
        backdrop-filter: blur(10px);
    }
    .glass-card {
        background: rgba(255,255,255,0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(244,163,0,0.25);
    }

    /* ── Progress Card ── */
    .progress-card {
        background: linear-gradient(135deg, #2D6A4F, #1B4332) !important;
        color: white;
        text-align: center;
        border: 2px solid var(--gold) !important;
    }
    .greeting { font-size: 0.9rem; color: #A8D5BA; margin-bottom: 0.5rem; }
    .week-display { margin: 0.5rem 0; }
    .week-num { font-family: 'Yatra One'; font-size: 4rem; color: var(--gold); line-height: 1; }
    .week-label { display: block; color: #A8D5BA; font-size: 0.8rem; }
    .trimester-badge {
        display: inline-block; padding: 0.2rem 0.8rem;
        border-radius: 20px; font-size: 0.75rem; margin: 0.5rem 0;
    }
    .t1 { background: rgba(135,206,235,0.3); border: 1px solid #87CEEB; color: #87CEEB; }
    .t2 { background: rgba(244,163,0,0.3); border: 1px solid var(--gold); color: var(--gold); }
    .t3 { background: rgba(232,160,180,0.3); border: 1px solid var(--lotus-pink); color: var(--lotus-pink); }
    .progress-bar-wrap {
        background: rgba(255,255,255,0.15); border-radius: 20px;
        height: 8px; margin: 0.8rem 0 0.3rem;
    }
    .progress-bar-fill {
        background: linear-gradient(90deg, var(--gold), #FFD700);
        height: 100%; border-radius: 20px;
        transition: width 0.5s ease;
    }
    .progress-text { font-size: 0.75rem; color: #A8D5BA; }
    .edd-text { font-size: 0.8rem; color: var(--gold); margin-top: 0.3rem; }

    /* ── Tip Card ── */
    .tip-card { background: linear-gradient(135deg, #FFF8EF, #FFF0D6) !important; border-left: 4px solid var(--gold) !important; }
    .tip-card h4 { color: var(--deep-green); margin-bottom: 0.5rem; }
    .tip-text { color: var(--deep-brown); font-size: 0.9rem; line-height: 1.6; }
    .herb-badge { display: inline-block; background: var(--deep-green); color: white; padding: 0.2rem 0.7rem; border-radius: 12px; font-size: 0.75rem; margin-top: 0.5rem; }

    /* ── Welcome Card ── */
    .welcome-card { text-align: center; padding: 2rem !important; }
    .welcome-icon { font-size: 3rem; margin-bottom: 0.5rem; }
    .sanskrit { margin-top: 1rem; color: var(--light-brown); font-size: 0.85rem; }

    /* ── Metric Cards ── */
    .metric-card {
        background: white; border-radius: 12px;
        padding: 0.8rem; text-align: center;
        border: 1px solid var(--border);
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }
    .metric-label { font-size: 0.72rem; color: var(--light-brown); margin-bottom: 0.3rem; }
    .metric-value { font-family: 'Yatra One'; font-size: 1.3rem; color: var(--deep-green); }
    .metric-unit { font-size: 0.65rem; color: var(--light-brown); }

    /* ── Setup Banner ── */
    .setup-banner {
        background: linear-gradient(135deg, #FFF3CD, #FFE0B2);
        border-left: 4px solid var(--gold);
        border-radius: 12px; padding: 1rem 1.4rem; margin-bottom: 1.5rem;
    }
    .setup-banner h3 { color: var(--deep-brown); margin: 0 0 0.3rem; }
    .setup-banner p { color: var(--light-brown); margin: 0; font-size: 0.9rem; }

    /* ── Week Header ── */
    .week-header {
        padding: 1rem 1.4rem; border-radius: 12px; margin-bottom: 1rem;
        display: flex; align-items: center; gap: 1.5rem;
    }
    .week-header.t1 { background: linear-gradient(90deg, #E3F2FD, #F0F8FF); border: 1px solid #87CEEB; }
    .week-header.t2 { background: linear-gradient(90deg, #FFF8E1, #FFFDE7); border: 1px solid var(--gold); }
    .week-header.t3 { background: linear-gradient(90deg, #FCE4EC, #FFF0F5); border: 1px solid var(--lotus-pink); }
    .wh-week { font-family: 'Yatra One'; font-size: 1.3rem; color: var(--deep-green); }
    .wh-tri { font-size: 0.85rem; color: var(--light-brown); }
    .wh-size { font-size: 0.85rem; color: var(--deep-brown); font-weight: 500; }

    /* ── Section Cards ── */
    .section-card h3 { color: var(--deep-green); font-size: 1rem; margin-bottom: 0.7rem; border-bottom: 1px solid var(--border); padding-bottom: 0.4rem; }
    .section-card p { font-size: 0.87rem; line-height: 1.7; color: var(--deep-brown); }

    /* ── List Items ── */
    .list-item {
        padding: 0.35rem 0.5rem; margin: 0.25rem 0;
        border-radius: 8px; font-size: 0.84rem;
        background: rgba(82,183,136,0.08);
        border-left: 3px solid var(--light-green);
        color: var(--deep-brown);
    }
    .list-item.caution {
        background: rgba(255,107,53,0.08);
        border-left-color: var(--saffron);
    }
    .caution-card { border-left: 4px solid var(--saffron) !important; }
    .caution-card h3 { color: var(--saffron) !important; }

    /* ── Dosha Tags ── */
    .dosha-tag {
        display: inline-block; background: linear-gradient(90deg, var(--deep-green), var(--light-green));
        color: white; padding: 0.2rem 0.8rem; border-radius: 12px; font-size: 0.75rem; margin-top: 0.5rem;
    }

    /* ── Herb Card ── */
    .herb-card { border-top: 4px solid var(--light-green) !important; }
    .h-green { border-top-color: #2D6A4F !important; }
    .h-teal { border-top-color: #00897B !important; }
    .h-pink { border-top-color: #E8A0B4 !important; }
    .h-purple { border-top-color: #7B3FA0 !important; }
    .h-yellow { border-top-color: #F4A300 !important; }
    .h-gold { border-top-color: #B8860B !important; }
    .herb-header { margin-bottom: 0.7rem; }
    .herb-title { font-family: 'Yatra One'; font-size: 1.1rem; color: var(--deep-green); }
    .herb-latin { font-size: 0.72rem; color: var(--light-brown); font-style: italic; }
    .herb-benefit { font-size: 0.85rem; color: var(--deep-brown); margin: 0.4rem 0; }
    .herb-detail { font-size: 0.82rem; color: var(--light-brown); margin: 0.2rem 0; }
    .herb-caution { font-size: 0.78rem; color: var(--saffron); margin-top: 0.5rem; padding: 0.3rem; background: rgba(255,107,53,0.08); border-radius: 6px; }

    /* ── Rasayana Card ── */
    .rasayana-card { background: linear-gradient(135deg, #FFF8EF, #FFF3E0) !important; border: 1px solid var(--gold) !important; }
    .rasayana-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.7rem; margin-top: 0.8rem; }
    .ras-item { background: white; padding: 0.6rem; border-radius: 10px; font-size: 0.82rem; border: 1px solid var(--border); }

    /* ── Routine ── */
    .routine-item {
        display: flex; align-items: stretch;
        background: white; border-radius: 12px; margin-bottom: 0.5rem;
        border: 1px solid var(--border); overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .r-time {
        background: var(--deep-green); color: white;
        padding: 0.8rem; min-width: 160px; font-size: 0.78rem;
        display: flex; align-items: center; font-weight: 500;
    }
    .r-gold .r-time { background: #A07000; }
    .r-blue .r-time { background: #1565C0; }
    .r-green .r-time { background: #2D6A4F; }
    .r-orange .r-time { background: #E65100; }
    .r-purple .r-time { background: #6A1B9A; }
    .r-content { padding: 0.8rem 1rem; }
    .r-title { font-weight: 600; color: var(--deep-brown); font-size: 0.9rem; }
    .r-desc { font-size: 0.82rem; color: var(--light-brown); margin-top: 0.2rem; }

    /* ── Yoga Card ── */
    .yoga-card { background: linear-gradient(135deg, #F0F7EE, #E8F5E9) !important; border: 1px solid #A5D6A7 !important; }
    .yoga-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.7rem; margin-top: 0.8rem; }
    .yoga-item { background: white; padding: 0.8rem; border-radius: 10px; text-align: center; border: 1px solid #C8E6C9; }
    .yoga-name { font-weight: 600; color: var(--deep-green); font-size: 0.9rem; }
    .yoga-desc { font-size: 0.75rem; color: var(--light-brown); margin: 0.2rem 0; }
    .yoga-time { font-size: 0.72rem; background: var(--deep-green); color: white; padding: 0.15rem 0.5rem; border-radius: 10px; display: inline-block; margin-top: 0.2rem; }

    /* ── Meal Items ── */
    .meal-item {
        display: flex; align-items: center; gap: 1rem;
        padding: 0.7rem 0.8rem; border-radius: 10px; margin-bottom: 0.4rem;
        background: rgba(82,183,136,0.06); border-left: 3px solid var(--light-green);
    }
    .meal-time { min-width: 100px; font-weight: 600; color: var(--deep-green); font-size: 0.82rem; }
    .meal-desc { font-size: 0.85rem; color: var(--deep-brown); }

    /* ── Avoid Items ── */
    .avoid-item {
        display: flex; justify-content: space-between; align-items: center;
        padding: 0.6rem 0.8rem; border-radius: 10px; margin-bottom: 0.4rem;
        background: rgba(255,107,53,0.06); border-left: 3px solid var(--saffron);
    }
    .avoid-food { font-weight: 600; color: var(--deep-brown); font-size: 0.85rem; }
    .avoid-reason { font-size: 0.78rem; color: var(--light-brown); }

    /* ── Super Foods ── */
    .super-food-card {
        background: white; border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 0.5rem;
        border: 1px solid var(--border); display: flex; flex-direction: column; gap: 0.2rem;
    }
    .sf-name { font-weight: 700; color: var(--deep-green); font-size: 0.95rem; }
    .sf-desc { font-size: 0.82rem; color: var(--light-brown); }
    .sf-benefit { font-size: 0.8rem; color: var(--saffron); }

    /* ── Maas Cards ── */
    .maas-header-card { text-align: center; background: linear-gradient(135deg, #2D6A4F, #1B4332) !important; color: white !important; }
    .maas-num { font-family: 'Yatra One'; font-size: 4rem; color: var(--gold); line-height: 1; }
    .maas-title { font-size: 1.2rem; color: white; }
    .maas-sanskrit { font-size: 0.8rem; color: #A8D5BA; font-style: italic; margin-top: 0.3rem; }

    /* ── Dosha Quiz ── */
    .dosha-score-card {
        background: white; border-radius: 14px; padding: 1.2rem; text-align: center;
        border: 2px solid var(--border); margin-bottom: 1rem;
    }
    .active-dosha { border-color: var(--gold) !important; background: linear-gradient(135deg, #FFF8EF, #FFFDE7) !important; }
    .ds-emoji { font-size: 2rem; }
    .ds-name { font-family: 'Yatra One'; font-size: 1.1rem; color: var(--deep-green); }
    .ds-score { font-size: 1.5rem; font-weight: 700; color: var(--deep-brown); }
    .ds-bar { background: #E8F5E9; border-radius: 10px; height: 6px; margin-top: 0.5rem; }
    .ds-fill { background: linear-gradient(90deg, var(--light-green), var(--deep-green)); height: 100%; border-radius: 10px; }
    .dosha-result-card { background: linear-gradient(135deg, #FFF8EF, #F0F7EE) !important; border: 2px solid var(--gold) !important; }
    .dosha-result-card h2 { color: var(--deep-green); font-family: 'Yatra One'; }
    .dosha-result-card h3 { color: var(--deep-brown); margin-top: 1rem; }

    /* ── Season Cards ── */
    .season-card h3 { color: var(--deep-green); margin-bottom: 0.7rem; }

    /* ── Symptom Cards ── */
    .emergency-card { background: rgba(255,107,53,0.06) !important; border: 2px solid var(--saffron) !important; }
    .emergency-card h3 { color: var(--saffron); }

    /* ── Mantra Cards ── */
    .mantra-card { background: linear-gradient(135deg, #F9F0FF, #F3E5F5) !important; border: 1px solid #CE93D8 !important; text-align: center; }
    .mantra-card h3, .mantra-name { color: #6A1B9A; font-family: 'Yatra One'; font-size: 1.1rem; margin-bottom: 0.5rem; }
    .mantra-text { font-family: 'Kalam', cursive; font-size: 1rem; color: var(--deep-brown); line-height: 1.8; margin: 0.5rem 0; }
    .mantra-meaning { font-size: 0.82rem; color: var(--light-brown); font-style: italic; }
    .mantra-benefit { font-size: 0.8rem; color: var(--saffron); margin-top: 0.3rem; }

    /* ── Garbhasanskar ── */
    .sanskar-card { background: linear-gradient(135deg, #FFF8EF, #FCEFC7) !important; border: 1px solid #F4A300 !important; }
    .music-grid, .art-grid {
        display: grid; grid-template-columns: repeat(3, 1fr);
        gap: 0.7rem; margin: 0.8rem 0;
    }
    .music-item, .art-item {
        background: white; border-radius: 10px; padding: 0.7rem; text-align: center;
        border: 1px solid var(--border);
    }
    .music-raga { font-weight: 600; color: var(--deep-green); font-size: 0.85rem; }
    .music-effect { font-size: 0.72rem; color: var(--light-brown); }
    .art-item { font-size: 0.82rem; color: var(--deep-brown); }
    .meditation-steps { display: flex; flex-direction: column; gap: 0.5rem; margin: 0.8rem 0; }
    .med-step {
        display: flex; align-items: center; gap: 0.8rem;
        background: white; border-radius: 10px; padding: 0.6rem 0.8rem;
        font-size: 0.85rem; border: 1px solid var(--border);
    }
    .step-num {
        background: var(--deep-green); color: white;
        width: 24px; height: 24px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.75rem; font-weight: 700; flex-shrink: 0;
    }
    .meditation-quote { font-style: italic; color: var(--light-brown); text-align: center; margin-top: 1rem; font-size: 0.85rem; }

    .story-card {
        background: white; border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 0.5rem;
        border-left: 4px solid #6A1B9A;
    }
    .story-title { font-weight: 700; color: #6A1B9A; }
    .story-desc { font-size: 0.82rem; color: var(--light-brown); margin-top: 0.2rem; }

    /* ── Streamlit Overrides ── */
    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid var(--light-green) !important;
        background: linear-gradient(135deg, var(--deep-green), var(--light-green)) !important;
        color: white !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(45,106,79,0.3) !important;
    }
    .stSlider > div { color: var(--deep-green); }
    .stSelectbox label, .stTextInput label, .stDateInput label, .stRadio label {
        color: var(--deep-brown) !important;
        font-weight: 500 !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: var(--deep-brown) !important;
        font-size: 0.85rem !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: var(--deep-green) !important;
    }
    </style>
    """, unsafe_allow_html=True)
