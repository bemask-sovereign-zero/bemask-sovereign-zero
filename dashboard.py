import streamlit as st
import pandas as pd
import numpy as np

# ==============================================================================
# 1. CONFIGURAZIONE PAGINA
# ==============================================================================
st.set_page_config(
    page_title="BEMASK SOVEREIGN ZERO // ENTERPRISE NCC-1701", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. INIEZIONE CSS & SFONDO ENTERPRISE NCC-1701 VINTAGE SCI-FI
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800;900&family=Inter:wght@400;600;700;900&display=swap');
    
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* SFONDO PITCH BLACK CON WATERMARK ENTERPRISE NCC-1701 */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #020408 !important;
        background-image: 
            radial-gradient(circle at 50% 30%, rgba(0, 229, 255, 0.05) 0%, transparent 60%),
            radial-gradient(1px 1px at 20px 30px, #ffffff 100%, transparent),
            radial-gradient(1.5px 1.5px at 150px 180px, rgba(0, 229, 255, 0.8) 100%, transparent),
            radial-gradient(1px 1px at 280px 70px, #ffffff 100%, transparent),
            radial-gradient(2px 2px at 420px 310px, rgba(228, 208, 10, 0.7) 100%, transparent),
            radial-gradient(1px 1px at 600px 120px, #ffffff 100%, transparent),
            radial-gradient(1.5px 1.5px at 800px 260px, rgba(0, 229, 255, 0.6) 100%, transparent);
        background-repeat: repeat;
        background-size: 100% 100%, 350px 350px, 400px 400px, 250px 250px, 500px 500px, 300px 300px, 450px 450px;
        color: #E2E8F0 !important;
        font-family: 'Inter', sans-serif;
    }

    .stApp::before {
        content: "";
        position: fixed;
        bottom: 20px;
        right: 25px;
        width: 480px;
        height: 240px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/USS_Enterprise_NCC-1701.svg/1280px-USS_Enterprise_NCC-1701.svg.png');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.07;
        pointer-events: none;
        z-index: 0;
        filter: invert(1) drop-shadow(0 0 15px #00E5FF);
    }

    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 100% !important;
        position: relative;
        z-index: 1;
    }

    .top-header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #040812;
        border: 1px solid #16243D;
        border-radius: 8px;
        padding: 8px 18px;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 25px rgba(0,0,0,0.9), inset 0 0 12px rgba(0, 229, 255, 0.15);
    }
    .brand-title {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 900;
        font-size: 1.02rem;
        letter-spacing: 1.5px;
        color: #FFFFFF;
        text-shadow: 0 0 8px rgba(0, 229, 255, 0.6);
    }
    .brand-separator { color: #334155; font-weight: 800; margin: 0 8px; }
    .brand-module {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.84rem;
        font-weight: 700;
        color: #00E5FF;
    }
    .brand-ship {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.76rem;
        font-weight: 800;
        color: #E4D00A;
        background: rgba(228, 208, 10, 0.12);
        padding: 2px 8px;
        border-radius: 4px;
        border: 1px solid #716200;
        letter-spacing: 1px;
    }

    [data-testid="stExpander"] {
        background-color: rgba(4, 7, 13, 0.95) !important;
        border: 1px solid #172033 !important;
        border-radius: 6px !important;
        margin-bottom: 8px !important;
        overflow: hidden;
    }
    [data-testid="stExpander"] summary {
        background-color: #080D1A !important;
        color: #00E5FF !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.80rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.8px !important;
        padding: 6px 12px !important;
    }

    /* SCROLLBAR FLUIDA PER LA GRIGLIA NATIVA */
    [data-testid="stDataFrame"] > div {
        overflow-x: auto !important;
    }

    .quote-card {
        background: #060B14;
        border: 1px solid #1E293B;
        border-radius: 6px;
        padding: 8px 10px;
        margin-bottom: 6px;
    }
    .quote-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 800;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #1E293B;
        padding-bottom: 4px;
    }
    .tratt-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.74rem;
        padding: 2.5px 0;
        border-bottom: 1px dashed #10192A;
    }
    .tratt-tag {
        font-weight: 800;
        font-size: 0.70rem;
        padding: 1px 4px;
        border-radius: 3px;
    }
    .tratt-tag-or { color: #94A3B8; background: #0E1726; }
    .tratt-tag-bb { color: #00E5FF; background: #082132; }
    .tratt-tag-hb { color: #E4D00A; background: #262208; }
    .tratt-tag-fb { color: #2DD4BF; background: #082622; }
    .tratt-price-night { font-weight: 700; color: #FFFFFF; }
    .tratt-total-stay { font-weight: 800; color: #94A3B8; font-size: 0.68rem; }
    .quote-stay-summary {
        margin-top: 6px;
        padding-top: 5px;
        border-top: 1px solid #1E293B;
        font-size: 0.68rem;
        color: #64748B;
        font-family: 'Inter', sans-serif;
    }

    .border-citrino   { border: 1px solid #716200; border-top: 2px solid #E4D00A; }
    .border-elettrico { border: 1px solid #005F73; border-top: 2px solid #00E5FF; }
    .border-smeraldo  { border: 1px solid #005238; border-top: 2px solid #00C988; }
    .border-cobalto   { border: 1px solid #1D4ED8; border-top: 2px solid #3B82F6; }
    .border-tanzanite { border: 1px solid #312E81; border-top: 2px solid #6366F1; }
    .border-ametista  { border: 1px solid #581C87; border-top: 2px solid #A855F7; }
    .border-granato   { border: 1px solid #7F1D1D; border-top: 2px solid #E11D48; }
    .border-topazio   { border: 1px solid #78350F; border-top: 2px solid #F59E0B; }
    .border-tormalina { border: 1px solid #134E4A; border-top: 2px solid #14B8A6; }

    .color-citrino   { color: #E4D00A; }
    .color-elettrico { color: #00E5FF; }
    .color-smeraldo  { color: #00C988; }
    .color-cobalto   { color: #60A5FA; }
    .color-tanzanite { color: #818CF8; }
    .color-ametista  { color: #C084FC; }
    .color-granato   { color: #FB7185; }
    .color-topazio   { color: #FBBF24; }
    .color-tormalina { color: #2DD4BF; }

    .lbl-inline {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 700;
        color: #64748B;
        display: flex;
        align-items: center;
        height: 26px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. VALORI DI DEFAULT ORIGINARI
# ==============================================================================
DEFAULT_OR = [40.0, 50.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 112.0]
DEFAULT_B  = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
DEFAULT_P1 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
DEFAULT_P2 = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]

def esegui_master_reset():
    st.session_state.or_values = DEFAULT_OR[:]
    st.session_state.b_values = DEFAULT_B[:]
    st.session_state.p1_values = DEFAULT_P1[:]
    st.session_state.p2_values = DEFAULT_P2[:]
    st.session_state.manual_overrides = {}
    st.session_state.fascia_consolidata = "Fascia D (0%)"
    st.session_state.moltiplicatore_attivo = 1.0
    
    st.session_state["num_suppl_large_2a"] = 20.0
    st.session_state["chk_attiva_floor"] = True
    
    st.session_state["sl_delta_large_cap"] = 10.0
    st.session_state["sl_delta_dus_cap"] = 15.0
    st.session_state["sl_delta_mat_sup"] = 10.0
    st.session_state["sl_delta_tpl_mat"] = 10.0
    st.session_state["sl_delta_tpl_comf"] = 10.0
    st.session_state["sl_delta_fam_tpl"] = 15.0
    
    st.session_state["num_dus_EASY LIFE"] = 20.0
    st.session_state["num_dus_MATSTD"] = 20.0
    st.session_state["num_dus_SUPMAT"] = 20.0
    st.session_state["num_dus_TPLSTD"] = 30.0
    st.session_state["num_dus_TPLCOMF"] = 30.0
    
    st.session_state["num_sconto_a"] = 100.0
    st.session_state["num_sconto_b"] = 50.0
    st.session_state["num_sconto_c"] = 30.0
    st.session_state["num_sconto_d"] = 20.0
    st.session_state["num_sconto_R"] = 10.0
    
    for i in range(9):
        st.session_state[f"or_{i}"] = float(DEFAULT_OR[i])
        st.session_state[f"b_{i}"] = float(DEFAULT_B[i])
        st.session_state[f"p1_{i}"] = float(DEFAULT_P1[i])
        st.session_state[f"p2_{i}"] = float(DEFAULT_P2[i])

if "initialized_benchmarks" not in st.session_state:
    st.session_state.initialized_benchmarks = True
    esegui_master_reset()

# Header Bar con USS Enterprise Reference
col_top_l, col_top_r = st.columns([4.2, 0.8])
with col_top_l:
    st.markdown(f"""
        <div class="top-header-bar">
            <div>
                <span class="brand-title">BEMASK SOVEREIGN ZERO</span>
                <span class="brand-separator">//</span>
                <span class="brand-module">COCKPIT NCC-1701 & AUDIT RADIALE 24 FASCE</span>
                <span class="brand-separator">//</span>
                <span class="brand-ship">USS ENTERPRISE CLASS</span>
            </div>
            <div>
                <span style="font-size:0.75rem; color:#64748B; font-family:'JetBrains Mono';">FASCIA ATTIVA:</span>
                <span style="color:#00E5FF; font-weight:800; font-family:'JetBrains Mono'; margin-left:4px;">{st.session_state.fascia_consolidata}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
with col_top_r:
    if st.button("🚨 MASTER RESET", help="Ripristina istantaneamente tutti i parametri originari", use_container_width=True):
        esegui_master_reset()
        st.rerun()

# ==============================================================================
# 4. ANAGRAFICA COMPLETA DELLE 9 CAMERE
# ==============================================================================
CAMERE_META = [
    {"nome": "CAPITANO", "border": "border-citrino",   "color": "color-citrino",   "rank": 0, "max_pax": 1},
    {"nome": "LARGE",    "border": "border-elettrico", "color": "color-elettrico", "rank": 1, "max_pax": 2},
    {"nome": "EASY LIFE","border": "border-smeraldo",  "color": "color-smeraldo",  "rank": 2, "max_pax": 2},
    {"nome": "MATSTD",   "border": "border-cobalto",   "color": "color-cobalto",   "rank": 3, "max_pax": 2},
    {"nome": "SUPMAT",   "border": "border-tanzanite", "color": "color-tanzanite", "rank": 4, "max_pax": 2},
    {"nome": "TPLSTD",   "border": "border-ametista",  "color": "color-ametista",  "rank": 5, "max_pax": 3},
    {"nome": "TPLCOMF",  "border": "border-granato",   "color": "color-granato",   "rank": 6, "max_pax": 3},
    {"nome": "FAMSTD",   "border": "border-topazio",   "color": "color-topazio",   "rank": 7, "max_pax": 4},
    {"nome": "FAMECO",   "border": "border-tormalina", "color": "color-tormalina", "rank": 8, "max_pax": 5},
]

ORDINE_CAMERE = [m["nome"] for m in CAMERE_META]

# ==============================================================================
# 5. CASSETTI PARAMETRI OPERATIVI E SALVAGUARDIA
# ==============================================================================
with st.expander("🗄️ REGOLE PARTICOLARI // SUPPLEMENTO LARGE & DUS (%)", expanded=False):
    col_reg1, col_reg2 = st.columns([1.2, 2.8], gap="medium")
    with col_reg1:
        st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #00E5FF; margin-bottom: 4px;'>// LARGE: SUPPLEMENTO 2° ADULTO (€)</div>", unsafe_allow_html=True)
        suppl_large_2a = st.number_input(
            "Suppl. Fisso 2° Letto (€)", 
            min_value=0.0, max_value=100.0, step=5.0, 
            key="num_suppl_large_2a"
        )
    with col_reg2:
        st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #00E5FF; margin-bottom: 4px;'>// DUS: SCONTO USO SINGOLA SULL'O.R. BASE (%)</div>", unsafe_allow_html=True)
        dus_cols = st.columns(5)
        dus_sconti = {}
        cam_dus_list = [
            ("EASY LIFE", "Easy Life"),
            ("MATSTD",    "Mat Std"),
            ("SUPMAT",    "Mat Comf"),
            ("TPLSTD",    "Tpl Std"),
            ("TPLCOMF",   "Tpl Comf")
        ]
        for idx, (sigla, etichetta) in enumerate(cam_dus_list):
            with dus_cols[idx]:
                st.markdown(f"<div style='font-family: JetBrains Mono; font-size: 0.70rem; font-weight: 700; color: #94A3B8;'>{etichetta} %</div>", unsafe_allow_html=True)
                sconto_dus = st.number_input(
                    f"DUS_{sigla}", 
                    min_value=0.0, max_value=80.0, step=5.0, 
                    key=f"num_dus_{sigla}"
                )
                dus_sconti[sigla] = sconto_dus / 100.0

with st.expander("🗄️ SALVAGUARDIA // CLUSTER FLOOR ENGINE & SCONTI FASCE ETÀ (%)", expanded=False):
    col_fg, col_rid = st.columns([1.7, 2.3], gap="medium")
    with col_fg:
        st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #00E5FF; margin-bottom: 6px;'>// DELTA SCATTI TARIFFARI TRA CLUSTER (€)</div>", unsafe_allow_html=True)
        attiva_floor = st.checkbox("Attiva Waterfall Floor Guard Dinamico", key="chk_attiva_floor")
        c_sl1, c_sl2 = st.columns(2)
        with c_sl1:
            delta_large_cap = st.slider("Δ Large (1A) vs Capitano", 0.0, 40.0, step=1.0, key="sl_delta_large_cap")
            delta_dus_cap = st.slider("Δ Easy Life (DUS 1A) vs Capitano", 0.0, 40.0, step=1.0, key="sl_delta_dus_cap")
            delta_mat_sup = st.slider("Δ Sup vs Mat Standard", 0.0, 30.0, step=1.0, key="sl_delta_mat_sup")
        with c_sl2:
            delta_tpl_mat = st.slider("Δ Tripla vs Matrimoniale", 0.0, 50.0, step=1.0, key="sl_delta_tpl_mat")
            delta_tpl_comf = st.slider("Δ Tpl Comf vs Tpl Std", 0.0, 30.0, step=1.0, key="sl_delta_tpl_comf")
            delta_fam_tpl = st.slider("Δ Family vs Tripla", 0.0, 60.0, step=1.0, key="sl_delta_fam_tpl")

    with col_rid:
        st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #E4D00A; margin-bottom: 6px;'>// RIDUZIONE UNICA FASCE ETÀ (LETTO & VITTO %)</div>", unsafe_allow_html=True)
        r_cols = st.columns(5)
        sconti_fasce = {}
        defaults_riduzioni = {
            "a": "a (0-2 Infant)",
            "b": "b (3-8 Baby)",
            "c": "c (9-13 Junior)",
            "d": "d (14-15 Teen)",
            "R": "R (16-17 Rid)",
        }
        for idx, (k, label_txt) in enumerate(defaults_riduzioni.items()):
            with r_cols[idx]:
                st.markdown(f"<div style='font-family: JetBrains Mono; font-size: 0.72rem; font-weight: 800; color: #00E5FF; margin-bottom: 4px;'>{label_txt}</div>", unsafe_allow_html=True)
                sconto_val = st.number_input(
                    f"Sconto {k}", min_value=0.0, max_value=100.0, step=5.0, key=f"num_sconto_{k}"
                )
                sconti_fasce[k] = sconto_val / 100.0

# ==============================================================================
# 7. GENERATORE DATABASE 140 COMBINAZIONI (INCLUSA SUPERIOR MATRIMONIALE)
# ==============================================================================
def genera_database_140():
    records = []
    # CAPITANO
    records.append(("CAPITANO", "1A", "1 Adulto (Singola)", 1, 1, 1, ["A"]))

    # LARGE
    records.append(("LARGE", "1A", "1 Adulto (Uso Singola)", 1, 1, 1, ["A"]))
    records.append(("LARGE", "1Aa", "1 Adulto + 1 Infant", 2, 1, 1, ["A", "a"]))
    records.append(("LARGE", "1Ab", "1 Adulto + 1 Baby (3-8)", 2, 1, 1, ["A", "b"]))
    records.append(("LARGE", "1Ac", "1 Adulto + 1 Junior (9-13)", 2, 1, 1, ["A", "c"]))
    records.append(("LARGE", "1Ad", "1 Adulto + 1 Teen (14-15)", 2, 1, 1, ["A", "d"]))
    records.append(("LARGE", "1AR", "1 Adulto + 1 Ridotto (16-17)", 2, 1, 2, ["A", "R"]))
    records.append(("LARGE", "2A", "2 Adulti", 2, 2, 2, ["A", "A"]))

    # MATRIMONIALI (EASY LIFE, STANDARD E SUPERIOR COMFORT)
    for cam in ["EASY LIFE", "MATSTD", "SUPMAT"]:
        records.append((cam, "1A", "1 Adulto (DUS)", 1, 1, 1, ["A"]))
        records.append((cam, "1Aa", "1 Adulto + 1 Infant", 2, 1, 1, ["A", "a"]))
        records.append((cam, "1Ab", "1 Adulto + 1 Baby (3-8)", 2, 1, 1, ["A", "b"]))
        records.append((cam, "1Ac", "1 Adulto + 1 Junior (9-13)", 2, 1, 1, ["A", "c"]))
        records.append((cam, "1Ad", "1 Adulto + 1 Teen (14-15)", 2, 1, 1, ["A", "d"]))
        records.append((cam, "1AR", "1 Adulto + 1 Ridotto (16-17)", 2, 1, 2, ["A", "R"]))
        records.append((cam, "2A", "2 Adulti", 2, 2, 2, ["A", "A"]))
        records.append((cam, "2Aa", "2 Adulti + Culla", 3, 2, 2, ["A", "A", "a"]))
        records.append((cam, "1Aba", "1 Adulto + Baby + Culla", 3, 1, 1, ["A", "b", "a"]))
        records.append((cam, "1Aca", "1 Adulto + Junior + Culla", 3, 1, 1, ["A", "c", "a"]))
        records.append((cam, "1Ada", "1 Adulto + Teen + Culla", 3, 1, 1, ["A", "d", "a"]))
        records.append((cam, "1ARa", "1 Adulto + Ridotto + Culla", 3, 1, 2, ["A", "R", "a"]))

    # TRIPLE
    for cam in ["TPLSTD", "TPLCOMF"]:
        records.append((cam, "1A", "1 Adulto (DUS)", 1, 1, 1, ["A"]))
        records.append((cam, "1Aa", "1 Adulto + 1 Infant", 2, 1, 1, ["A", "a"]))
        records.append((cam, "1Ab", "1 Adulto + 1 Baby (3-8)", 2, 1, 1, ["A", "b"]))
        records.append((cam, "1Ac", "1 Adulto + 1 Junior (9-13)", 2, 1, 1, ["A", "c"]))
        records.append((cam, "1Ad", "1 Adulto + 1 Teen (14-15)", 2, 1, 1, ["A", "d"]))
        records.append((cam, "1AR", "1 Adulto + 1 Ridotto (16-17)", 2, 1, 2, ["A", "R"]))
        records.append((cam, "2A", "2 Adulti", 2, 2, 2, ["A", "A"]))
        records.append((cam, "2Aa", "2 Adulti + Infant / Culla", 3, 2, 2, ["A", "A", "a"]))
        records.append((cam, "2Ab", "2 Adulti + Baby (3-8)", 3, 2, 2, ["A", "A", "b"]))
        records.append((cam, "2Ac", "2 Adulti + Junior (9-13)", 3, 2, 2, ["A", "A", "c"]))
        records.append((cam, "2Ad", "2 Adulti + Teen (14-15)", 3, 2, 2, ["A", "A", "d"]))
        records.append((cam, "2AR", "2 Adulti + Ridotto (16-17)", 3, 2, 3, ["A", "A", "R"]))
        records.append((cam, "3A", "3 Adulti", 3, 3, 3, ["A", "A", "A"]))

    # FAMILY STD
    fam_std_combi = [
        ("2A", "2 Adulti", 2, 2, 2, ["A", "A"]),
        ("2Aa", "2 Adulti + Culla", 3, 2, 2, ["A", "A", "a"]),
        ("2Ab", "2 Adulti + Baby (3-8)", 3, 2, 2, ["A", "A", "b"]),
        ("2Ac", "2 Adulti + Junior (9-13)", 3, 2, 2, ["A", "A", "c"]),
        ("2Ad", "2 Adulti + Teen (14-15)", 3, 2, 2, ["A", "A", "d"]),
        ("2AR", "2 Adulti + Ridotto (16-17)", 3, 2, 3, ["A", "A", "R"]),
        ("3A", "3 Adulti", 3, 3, 3, ["A", "A", "A"]),
        ("3Aa", "3 Adulti + Culla", 4, 3, 3, ["A", "A", "A", "a"]),
        ("2A2a", "2 Adulti + 2 Culle", 4, 2, 2, ["A", "A", "a", "a"]),
        ("2A1a1b", "2 Adulti + Culla + Baby", 4, 2, 2, ["A", "A", "a", "b"]),
        ("2A1a1c", "2 Adulti + Culla + Junior", 4, 2, 2, ["A", "A", "a", "c"]),
        ("2A1a1d", "2 Adulti + Culla + Teen (14-15)", 4, 2, 2, ["A", "A", "a", "d"]),
        ("2A1a1R", "2 Adulti + Culla + Ridotto (16-17)", 4, 2, 3, ["A", "A", "a", "R"]),
        ("2A2b", "2 Adulti + 2 Baby (3-8)", 4, 2, 2, ["A", "A", "b", "b"]),
        ("2A1b1c", "2 Adulti + Baby + Junior", 4, 2, 2, ["A", "A", "b", "c"]),
        ("2A1b1d", "2 Adulti + Baby + Teen (14-15)", 4, 2, 2, ["A", "A", "b", "d"]),
        ("2A1b1R", "2 Adulti + Baby + Ridotto (16-17)", 4, 2, 3, ["A", "A", "b", "R"]),
        ("2A2c", "2 Adulti + 2 Junior (9-13)", 4, 2, 2, ["A", "A", "c", "c"]),
        ("2A1c1d", "2 Adulti + Junior + Teen (14-15)", 4, 2, 2, ["A", "A", "c", "d"]),
        ("2A1c1R", "2 Adulti + Junior + Ridotto (16-17)", 4, 2, 3, ["A", "A", "c", "R"]),
        ("2A2d", "2 Adulti + 2 Teen (14-15)", 4, 2, 2, ["A", "A", "d", "d"]),
        ("2A1d1R", "2 Adulti + Teen (14-15) + Ridotto (16-17)", 4, 2, 3, ["A", "A", "d", "R"]),
        ("2A2R", "2 Adulti + 2 Ridotti (16-17)", 4, 2, 4, ["A", "A", "R", "R"]),
        ("3Ab", "3 Adulti + Baby (3-8)", 4, 3, 3, ["A", "A", "A", "b"]),
        ("3Ac", "3 Adulti + Junior (9-13)", 4, 3, 3, ["A", "A", "A", "c"]),
        ("3Ad", "3 Adulti + Teen (14-15)", 4, 3, 3, ["A", "A", "A", "d"]),
        ("3AR", "3 Adulti + Ridotto (16-17)", 4, 3, 4, ["A", "A", "A", "R"]),
        ("4A", "4 Adulti", 4, 4, 4, ["A", "A", "A", "A"]),
        ("3A1a1b", "3 Adulti + Baby + Culla Extra", 5, 3, 3, ["A", "A", "A", "a", "b"]),
        ("3A1a1c", "3 Adulti + Junior + Culla Extra", 5, 3, 3, ["A", "A", "A", "a", "c"]),
        ("3A1a1d", "3 Adulti + Teen (14-15) + Culla Extra", 5, 3, 3, ["A", "A", "A", "a", "d"]),
        ("3A1a1R", "3 Adulti + Ridotto (16-17) + Culla Extra", 5, 3, 4, ["A", "A", "A", "a", "R"]),
        ("4Aa", "4 Adulti + Culla Extra", 5, 4, 4, ["A", "A", "A", "A", "a"]),
    ]
    for c, d, p, a, t, pax_list in fam_std_combi:
        records.append(("FAMSTD", c, d, p, a, t, pax_list))

    # FAMILY ECO
    for c, d, p, a, t, pax_list in fam_std_combi:
        records.append(("FAMECO", c, d, p, a, t, pax_list))
    records.append(("FAMECO", "4Ab", "4 Adulti + 1 Baby (3-8)", 5, 4, 4, ["A", "A", "A", "A", "b"]))
    records.append(("FAMECO", "4Ac", "4 Adulti + 1 Junior (9-13)", 5, 4, 4, ["A", "A", "A", "A", "c"]))
    records.append(("FAMECO", "4Ad", "4 Adulti + 1 Teen (14-15)", 5, 4, 4, ["A", "A", "A", "A", "d"]))
    records.append(("FAMECO", "4AR", "4 Adulti + 1 Ridotto (16-17)", 5, 4, 5, ["A", "A", "A", "A", "R"]))

    return pd.DataFrame(records, columns=["CAMERA", "CODICE", "DESCRIZIONE", "PAX", "ADULTI", "TASSA_PAX", "PAX_LIST"])

df_combi_140 = genera_database_140()

# ==============================================================================
# 8. MOTORE ALGEBRICO TRASPARENTE
# ==============================================================================
def calcola_prezzo_riga(camera_nome, codice, pax_list, or_val, b_val, p1_val, p2_val, trattamento="HB"):
    or_effettivo = or_val

    # Regola 1: Large 2A (Quota fissa trasparente)
    if camera_nome == "LARGE" and codice == "2A":
        or_effettivo = or_val + suppl_large_2a

    # Regola 2: DUS (1A)
    elif codice == "1A" and camera_nome in dus_sconti:
        or_effettivo = or_val * (1.0 - dus_sconti[camera_nome])

    totale = or_effettivo

    pasti_totali = 0.0
    for pax in pax_list:
        sconto = 0.0 if pax == "A" else sconti_fasce.get(pax, 0.0)

        pax_pasti = 0.0
        if trattamento in ["BB", "HB", "FB"]:
            pax_pasti += b_val * (1.0 - sconto)
        if trattamento in ["HB", "FB"]:
            pax_pasti += p1_val * (1.0 - sconto)
        if trattamento == "FB":
            pax_pasti += p2_val * (1.0 - sconto)

        pasti_totali += pax_pasti

    totale += pasti_totali
    return round(totale, 2)

or_arr = np.array(st.session_state.or_values)
b_arr  = np.array(st.session_state.b_values)
p1_arr = np.array(st.session_state.p1_values)
p2_arr = np.array(st.session_state.p2_values)

def get_delta_step(cam_nome, codice):
    if cam_nome == "LARGE" and codice == "1A":
        return delta_large_cap
    elif cam_nome == "EASY LIFE" and codice == "1A":
        return delta_dus_cap
    elif cam_nome == "SUPMAT":
        return delta_mat_sup
    elif cam_nome == "TPLSTD":
        return delta_tpl_mat
    elif cam_nome == "TPLCOMF":
        return delta_tpl_comf
    elif cam_nome == "FAMSTD":
        return delta_fam_tpl
    return 0.0

diz_trattamenti_completi = {"OR": [], "BB": [], "HB": [], "FB": []}
cache_floor_tratt = {"OR": {}, "BB": {}, "HB": {}, "FB": {}}

for tratt in ["OR", "BB", "HB", "FB"]:
    idx_el = ORDINE_CAMERE.index("EASY LIFE")
    p_easy_life_2a_benchmark = calcola_prezzo_riga(
        "EASY LIFE", "2A", ["A", "A"],
        or_arr[idx_el], b_arr[idx_el], p1_arr[idx_el], p2_arr[idx_el],
        trattamento=tratt
    )
    
    for _, row in df_combi_140.iterrows():
        cam = row["CAMERA"]
        cam_idx = ORDINE_CAMERE.index(cam)
        codice = row["CODICE"]
        pax_l = row["PAX_LIST"]
        combi_key = f"{cam}_{codice}_{tratt}"
        
        override_val = st.session_state.manual_overrides.get(combi_key, None)
        
        if override_val is not None and override_val > 0.0:
            p_finale = float(override_val)
        else:
            p_grezzo = calcola_prezzo_riga(
                cam, codice, pax_l, 
                or_arr[cam_idx], b_arr[cam_idx], p1_arr[cam_idx], p2_arr[cam_idx], 
                trattamento=tratt
            )
            p_finale = p_grezzo
            
            if cam == "LARGE" and codice == "2A":
                p_finale = min(p_finale, p_easy_life_2a_benchmark)

            if attiva_floor:
                chiave_equipaggio = "".join(sorted([p for p in pax_l if p != 'A'])) + f"_{len([p for p in pax_l if p == 'A'])}A"
                delta_applicabile = get_delta_step(cam, codice)
                
                if chiave_equipaggio in cache_floor_tratt[tratt] and cam != "FAMECO":
                    prezzo_minimo = cache_floor_tratt[tratt][chiave_equipaggio] + delta_applicabile
                    if p_finale < prezzo_minimo:
                        p_finale = prezzo_minimo
                
                if cam not in ["FAMECO", "LARGE"]:
                    cache_floor_tratt[tratt][chiave_equipaggio] = max(cache_floor_tratt[tratt].get(chiave_equipaggio, 0.0), p_finale)
        
        diz_trattamenti_completi[tratt].append(p_finale)

df_audit = df_combi_140.copy()
for tratt in ["OR", "BB", "HB", "FB"]:
    df_audit[f"PREZZO_{tratt}"] = diz_trattamenti_completi[tratt]

fasce_options = [f"Fascia {chr(65+i)} ({'+' if (i*4 - 12) >= 0 else ''}{i*4 - 12}%)" for i in range(24)]

# ==============================================================================
# 9. RADIOGRAFIA A SCHEMA NATIVO: 24 FASCE VERTICALI & SCROLLBAR FLUIDA A TUTTA LARGHEZZA
# ==============================================================================
st.markdown("<div style='margin-top: 10px; margin-bottom: 4px; font-family: JetBrains Mono; font-size: 0.90rem; font-weight: 900; color: #00E5FF;'>🛸 RADIOGRAFIA A SCHEMA NATIVO // 24 FASCE IN VERTICALE & SCROLLBAR FLUIDA</div>", unsafe_allow_html=True)
st.caption("Ogni riga rappresenta una fascia stagionale (dalla A alla Z). In orizzontale trovi la Tariffa Massima Piena (Prezzo Base di Camera) e tutte le combinazioni di equipaggio con barra di scorrimento orizzontale libera fino alle Family quadruple/quintuple.")

c_rad1, c_rad2, c_rad3, c_rad4 = st.columns([1.5, 1.0, 1.2, 1.3])
with c_rad1:
    camera_ispezione = st.selectbox(
        "Seleziona Camera da Ispezionare:",
        ORDINE_CAMERE,
        index=ORDINE_CAMERE.index("FAMSTD"),
        key="sb_camera_ispezione_v7"
    )
with c_rad2:
    filtro_capienza = st.selectbox(
        "Filtro Capienza Occupanti:",
        ["TUTTI GLI EQUIPAGGI", "2 PAX", "3 PAX", "4 PAX", "5 PAX"],
        key="sb_filtro_capienza_v7"
    )
with c_rad3:
    tratt_ispezione = st.selectbox(
        "Trattamento di Calcolo:",
        ["HB", "BB", "FB", "OR"],
        key="sb_tratt_ispezione_v7"
    )
with c_rad4:
    modalita_vista = st.selectbox(
        "Modalità Visualizzazione Matrice:",
        [
            "1. Prezzo Finito Camera (€)",
            "2. Riduzione in Valore Assoluto (€ rispetto al Max)",
            "3. Percentuale di Riduzione PMS (% costante)",
            "4. Controllo Congruenza / Deviazioni"
        ],
        key="sb_modalita_vista_v7"
    )

idx_cam_sel = ORDINE_CAMERE.index(camera_ispezione)
max_pax_cam = CAMERE_META[idx_cam_sel]["max_pax"]

df_cam_combi = df_audit[df_audit["CAMERA"] == camera_ispezione].copy()

# Applicazione del filtro rapido di capienza
if filtro_capienza != "TUTTI GLI EQUIPAGGI":
    pax_num_target = int(filtro_capienza.split()[0])
    df_cam_combi = df_cam_combi[df_cam_combi["PAX"] == pax_num_target]

base_or_cam = or_arr[idx_cam_sel]
base_pasti_cam = 0.0
if tratt_ispezione in ["BB", "HB", "FB"]: base_pasti_cam += b_arr[idx_cam_sel] * max_pax_cam
if tratt_ispezione in ["HB", "FB"]: base_pasti_cam += p1_arr[idx_cam_sel] * max_pax_cam
if tratt_ispezione == "FB": base_pasti_cam += p2_arr[idx_cam_sel] * max_pax_cam
tariffa_massima_base = base_or_cam + base_pasti_cam

nomi_24_fasce = [chr(65+i) for i in range(24)]
moltiplicatori_24 = [1.0 + (((i * 4) - 12) / 100.0) for i in range(24)]

righe_verticali_fasce = []

for i in range(24):
    f_nome = f"Fascia {nomi_24_fasce[i]}"
    molt = moltiplicatori_24[i]
    delta_str = f"{'+' if ((i*4)-12) >= 0 else ''}{(i*4)-12}%"
    
    prezzo_max_fascia = tariffa_massima_base * molt
    
    riga = {
        "FASCIA": f_nome,
        "DELTA": delta_str,
        "PREZZO_MAX_CAM": f"{prezzo_max_fascia:.0f} €" if "1." in modalita_vista else (
            "0.00 €" if "2." in modalita_vista else (
                "0.00 %" if "3." in modalita_vista else "🟢 BASE RACK"
            )
        )
    }
    
    for _, row_c in df_cam_combi.iterrows():
        cod = row_c["CODICE"]
        p_base = row_c[f"PREZZO_{tratt_ispezione}"]
        
        k_ov = f"{camera_ispezione}_{cod}_{tratt_ispezione}"
        if k_ov in st.session_state.manual_overrides:
            p_fascia = st.session_state.manual_overrides[k_ov] * molt
        else:
            p_fascia = p_base * molt
            
        if camera_ispezione == "LARGE" and cod == "2A":
            idx_el = ORDINE_CAMERE.index("EASY LIFE")
            p_el_base = df_audit[(df_audit["CAMERA"] == "EASY LIFE") & (df_audit["CODICE"] == "2A")][f"PREZZO_{tratt_ispezione}"].iloc[0]
            p_fascia = min(p_fascia, p_el_base * molt)
            
        diff_assoluta = prezzo_max_fascia - p_fascia
        pct_riduzione = round((diff_assoluta / prezzo_max_fascia) * 100.0, 2) if prezzo_max_fascia > 0 else 0.0
        
        pct_base_ref = round(((tariffa_massima_base - p_base) / tariffa_massima_base) * 100.0, 2)
        deviazione = abs(pct_riduzione - pct_base_ref) > 0.05
        
        if "1." in modalita_vista:
            riga[cod] = f"{p_fascia:.0f} €"
        elif "2." in modalita_vista:
            riga[cod] = f"-{diff_assoluta:.0f} €"
        elif "3." in modalita_vista:
            riga[cod] = f"-{pct_riduzione:.2f}%"
        else:
            riga[cod] = "⚠️ SPOSTATO" if deviazione else "🟢 COSTANTE"
            
    righe_verticali_fasce.append(riga)

df_matrice_schema_nativo = pd.DataFrame(righe_verticali_fasce)

col_cfg_nativo = {
    "FASCIA": st.column_config.TextColumn("Fascia", width=110),
    "DELTA": st.column_config.TextColumn("Δ Rack", width=80),
    "PREZZO_MAX_CAM": st.column_config.TextColumn("Max Pieno", width=100),
}
for _, row_c in df_cam_combi.iterrows():
    c_cod = row_c["CODICE"]
    c_desc = row_c["DESCRIZIONE"]
    col_cfg_nativo[c_cod] = st.column_config.TextColumn(f"{c_cod} ({c_desc})", width=135)

st.dataframe(
    df_matrice_schema_nativo,
    column_config=col_cfg_nativo,
    use_container_width=False,
    hide_index=True,
    height=480
)

st.markdown("---")

# ==============================================================================
# 10. PREVENTIVATORE VELOCE AL BANCO A SCHERMO CHIARO (CON QUADRO COMPLETO)
# ==============================================================================
with st.expander("⚡ PREVENTIVATORE VELOCE AL BANCO // QUADRO COMPLETO TRATTAMENTI", expanded=True):
    st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #00E5FF; margin-bottom: 4px;'>// 1. REGIA FASCE STAGIONALI & PARAMETRI SOGGIORNO</div>", unsafe_allow_html=True)
    c_fas1, c_fas2, c_fas3, c_fas4 = st.columns([2.0, 1.0, 0.8, 0.8])
    
    idx_default = fasce_options.index(st.session_state.fascia_consolidata) if st.session_state.fascia_consolidata in fasce_options else 3
    
    with c_fas1:
        fascia_selezionata = st.selectbox("Seleziona Fascia di Lavoro:", fasce_options, index=idx_default)
    
    with c_fas2:
        if st.button("🔒 CONSOLIDA FASCIA", use_container_width=True):
            st.session_state.fascia_consolidata = fascia_selezionata
            scostamento = float(fascia_selezionata.split("(")[1].replace("%)", ""))
            st.session_state.moltiplicatore_attivo = 1.0 + (scostamento / 100.0)
            st.rerun()

    with c_fas3:
        notti_stay = st.number_input("Notti Soggiorno:", min_value=1, max_value=30, value=7, step=1)
    with c_fas4:
        tassa_soggiorno_quota = st.number_input("Tassa €/Notte:", min_value=0.0, max_value=5.0, value=2.0, step=0.5)

    st.markdown("---")

    st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #E4D00A; margin-bottom: 6px;'>// 2. COMPOSIZIONE EQUIPAGGIO OSPITI (CONTATORI ANAGRAFICI)</div>", unsafe_allow_html=True)
    cnt1, cnt2, cnt3, cnt4, cnt5, cnt6 = st.columns(6)
    with cnt1:
        st.markdown("<div class='lbl-inline' style='color:#FFFFFF;'>Adulti (16+)</div>", unsafe_allow_html=True)
        num_a = st.number_input("Adulti", min_value=1, max_value=4, value=2, step=1, key="cnt_a")
    with cnt2:
        st.markdown("<div class='lbl-inline' style='color:#818CF8;'>Rid. R (16-17)</div>", unsafe_allow_html=True)
        num_R = st.number_input("Ridotti R", min_value=0, max_value=2, value=0, step=1, key="cnt_R")
    with cnt3:
        st.markdown("<div class='lbl-inline' style='color:#FB7185;'>Teen d (14-15)</div>", unsafe_allow_html=True)
        num_d = st.number_input("Teen d", min_value=0, max_value=2, value=0, step=1, key="cnt_d")
    with cnt4:
        st.markdown("<div class='lbl-inline' style='color:#00E5FF;'>Junior c (9-13)</div>", unsafe_allow_html=True)
        num_c = st.number_input("Junior c", min_value=0, max_value=2, value=0, step=1, key="cnt_c")
    with cnt5:
        st.markdown("<div class='lbl-inline' style='color:#E4D00A;'>Baby b (3-8)</div>", unsafe_allow_html=True)
        num_b = st.number_input("Baby b", min_value=0, max_value=2, value=0, step=1, key="cnt_b")
    with cnt6:
        st.markdown("<div class='lbl-inline' style='color:#2DD4BF;'>Infant a (0-2)</div>", unsafe_allow_html=True)
        num_a_inf = st.number_input("Infant a", min_value=0, max_value=2, value=0, step=1, key="cnt_inf")

    pax_costruiti = []
    pax_costruiti.extend(["A"] * num_a)
    pax_costruiti.extend(["R"] * num_R)
    pax_costruiti.extend(["d"] * num_d)
    pax_costruiti.extend(["c"] * num_c)
    pax_costruiti.extend(["b"] * num_b)
    pax_costruiti.extend(["a"] * num_a_inf)

    df_preventivo = df_audit[df_audit["PAX_LIST"].apply(lambda l: sorted(l) == sorted(pax_costruiti))].copy()
    
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    
    if len(df_preventivo) == 0:
        st.warning(f"Nessuna camera configurata per questa combinazione esatta: {len(pax_costruiti)} ospiti.")
    else:
        df_preventivo["RANK"] = df_preventivo["CAMERA"].apply(lambda c: ORDINE_CAMERE.index(c))
        df_preventivo = df_preventivo.sort_values("RANK")
        
        quote_cols = st.columns(len(df_preventivo))
        for idx, (_, row) in enumerate(df_preventivo.iterrows()):
            cam_nome = row["CAMERA"]
            meta = next(m for m in CAMERE_META if m["nome"] == cam_nome)
            tassa_pax = row["TASSA_PAX"]
            totale_tassa = tassa_pax * tassa_soggiorno_quota * notti_stay
            
            p_or = round(row["PREZZO_OR"] * st.session_state.moltiplicatore_attivo, 2)
            p_bb = round(row["PREZZO_BB"] * st.session_state.moltiplicatore_attivo, 2)
            p_hb = round(row["PREZZO_HB"] * st.session_state.moltiplicatore_attivo, 2)
            p_fb = round(row["PREZZO_FB"] * st.session_state.moltiplicatore_attivo, 2)
            
            tot_or = p_or * notti_stay + totale_tassa
            tot_bb = p_bb * notti_stay + totale_tassa
            tot_hb = p_hb * notti_stay + totale_tassa
            tot_fb = p_fb * notti_stay + totale_tassa
            
            with quote_cols[idx]:
                st.markdown(f"""
                    <div class="quote-card {meta['border']}">
                        <div class="quote-title">
                            <span class="{meta['color']}">{cam_nome}</span>
                            <span style="font-size:0.65rem; color:#64748B;">{row['CODICE']}</span>
                        </div>
                        <div class="tratt-row">
                            <span class="tratt-tag tratt-tag-or">RO</span>
                            <span class="tratt-price-night">{p_or:.0f} € <span style="font-size:0.62rem; color:#64748B;">/n</span></span>
                            <span class="tratt-total-stay">Tot: {tot_or:.0f} €</span>
                        </div>
                        <div class="tratt-row">
                            <span class="tratt-tag tratt-tag-bb">BB</span>
                            <span class="tratt-price-night">{p_bb:.0f} € <span style="font-size:0.62rem; color:#64748B;">/n</span></span>
                            <span class="tratt-total-stay">Tot: {tot_bb:.0f} €</span>
                        </div>
                        <div class="tratt-row">
                            <span class="tratt-tag tratt-tag-hb">HB</span>
                            <span class="tratt-price-night">{p_hb:.0f} € <span style="font-size:0.62rem; color:#64748B;">/n</span></span>
                            <span class="tratt-total-stay">Tot: {tot_hb:.0f} €</span>
                        </div>
                        <div class="tratt-row">
                            <span class="tratt-tag tratt-tag-fb">FB</span>
                            <span class="tratt-price-night">{p_fb:.0f} € <span style="font-size:0.62rem; color:#64748B;">/n</span></span>
                            <span class="tratt-total-stay">Tot: {tot_fb:.0f} €</span>
                        </div>
                        <div class="quote-stay-summary">
                            Soggiorno: <b>{notti_stay} notti</b><br>
                            Tassa inclusa ({tassa_pax}pax): <b>{totale_tassa:.0f} €</b>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

# ==============================================================================
# 11. CASSETTO: SOVRANITÀ ALBERGATORE // OVERRIDE MANUALE TRASPARENTE
# ==============================================================================
with st.expander("👑 SOVRANITÀ ALBERGATORE // IMPUTAZIONE MANUALE COMBINAZIONI CHIAVE", expanded=False):
    st.markdown("<div style='font-family: JetBrains Mono; font-size: 0.74rem; font-weight: 800; color: #00E5FF; margin-bottom: 4px;'>// GRIGLIA OVERRIDE MANUALE (€)</div>", unsafe_allow_html=True)
    st.caption("Seleziona il trattamento e digita la tariffa secca a mano. Lasciando 0.00 € comanda la formula di calcolo automatico.")

    c_ov_filtro, c_ov_tratt, c_ov_reset = st.columns([2, 1.2, 1.2])
    with c_ov_filtro:
        filtro_ov = st.selectbox(
            "Filtra Tipologia Camera:",
            ["TUTTE LE CAMERE", "TPLSTD", "TPLCOMF", "FAMSTD", "FAMECO", "LARGE", "EASY LIFE", "MATSTD", "SUPMAT"]
        )
    with c_ov_tratt:
        tratt_ov_target = st.selectbox("Trattamento da Personalizzare:", ["HB", "BB", "FB", "OR"])
    with c_ov_reset:
        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Reset Overrides Manuali", use_container_width=True):
            st.session_state.manual_overrides = {}
            st.rerun()

    df_editable_src = df_audit.copy()
    if filtro_ov != "TUTTE LE CAMERE":
        df_editable_src = df_editable_src[df_editable_src["CAMERA"] == filtro_ov]

    df_editable_src["KEY"] = df_editable_src["CAMERA"] + "_" + df_editable_src["CODICE"] + f"_{tratt_ov_target}"
    df_editable_src["OVERRIDE_EUR"] = df_editable_src["KEY"].apply(lambda k: float(st.session_state.manual_overrides.get(k, 0.0)))
    
    df_editor_view = df_editable_src[["CAMERA", "CODICE", "DESCRIZIONE", f"PREZZO_{tratt_ov_target}", "OVERRIDE_EUR", "KEY"]].copy()
    df_editor_view.rename(columns={f"PREZZO_{tratt_ov_target}": f"CALCOLO_AUTO_{tratt_ov_target}_EUR"}, inplace=True)

    edited_df = st.data_editor(
        df_editor_view,
        column_config={
            "CAMERA": st.column_config.TextColumn("Camera", disabled=True, width="small"),
            "CODICE": st.column_config.TextColumn("Codice", disabled=True, width="small"),
            "DESCRIZIONE": st.column_config.TextColumn("Equipaggio", disabled=True, width="medium"),
            f"CALCOLO_AUTO_{tratt_ov_target}_EUR": st.column_config.NumberColumn("Auto €", disabled=True, format="%.2f €"),
            "OVERRIDE_EUR": st.column_config.NumberColumn(f"Manuale {tratt_ov_target} € (0=Auto)", min_value=0.0, max_value=1500.0, step=1.0, format="%.2f €"),
            "KEY": None
        },
        use_container_width=True,
        hide_index=True,
        height=300,
        key="data_editor_overrides_streamlined"
    )

    cambiato = False
    for _, r in edited_df.iterrows():
        k = r["KEY"]
        val = float(r["OVERRIDE_EUR"])
        if val > 0.0:
            if st.session_state.manual_overrides.get(k) != val:
                st.session_state.manual_overrides[k] = val
                cambiato = True
        else:
            if k in st.session_state.manual_overrides:
                del st.session_state.manual_overrides[k]
                cambiato = True

    if cambiato:
        st.rerun()

# ==============================================================================
# 12. CASSETTO: BRIDGE PASSEPARTOUT // MATRICE PERCENTUALE UNIVERSALE & CSV
# ==============================================================================
with st.expander("🗄️ BRIDGE PASSEPARTOUT // MATRICE PERCENTUALE UNIVERSALE & CSV", expanded=False):
    tratt_export_pms = st.selectbox("Trattamento di Calcolo per Export PMS:", ["HB", "BB", "FB", "OR"])
    
    df_export_pms = df_audit[["CAMERA", "CODICE", "DESCRIZIONE", "TASSA_PAX", f"PREZZO_{tratt_export_pms}"]].copy()
    df_export_pms.rename(columns={f"PREZZO_{tratt_export_pms}": f"PREZZO_{tratt_export_pms}_EUR"}, inplace=True)
    
    csv_buffer = df_export_pms.to_csv(index=False, sep=";").encode('utf-8')
    st.download_button(
        label=f"💾 Scarica Matrice CSV Passepartout ({tratt_export_pms})",
        data=csv_buffer,
        file_name=f"matrice_passepartout_{tratt_export_pms.lower()}.csv",
        mime="text/csv"
    )
    st.dataframe(df_export_pms, use_container_width=True, hide_index=True, height=260)

# ==============================================================================
# 13. DETTAGLIO RACK BASE INPUT (9 CATEGORIE)
# ==============================================================================
with st.expander("🗄️ RACK INPUT CAMERE // MATRICI BASE (9 CATEGORIE)", expanded=False):
    for row_idx in range(3):
        g_cols = st.columns(3)
        for col_idx in range(3):
            i = row_idx * 3 + col_idx
            meta = CAMERE_META[i]
            with g_cols[col_idx]:
                st.markdown(f"""
                    <div class="room-rack {meta['border']}">
                        <div class="room-header {meta['color']}">{meta['nome']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                r1_c1, r1_c2 = st.columns([1.1, 2.2])
                with r1_c1:
                    st.markdown(f'<div class="lbl-inline {meta["color"]}">O.R. €</div>', unsafe_allow_html=True)
                with r1_c2:
                    st.session_state.or_values[i] = st.number_input(
                        "OR", value=float(st.session_state.or_values[i]), step=1.0, key=f"or_{i}"
                    )
                
                r2_c1, r2_c2, r2_c3, r2_c4, r2_c5, r2_c6 = st.columns([0.5, 1.2, 0.6, 1.2, 0.6, 1.2])
                with r2_c1:
                    st.markdown('<div class="lbl-inline">B</div>', unsafe_allow_html=True)
                with r2_c2:
                    st.session_state.b_values[i] = st.number_input(
                        "B", value=float(st.session_state.b_values[i]), step=1.0, key=f"b_{i}"
                    )
                with r2_c3:
                    st.markdown('<div class="lbl-inline">P1</div>', unsafe_allow_html=True)
                with r2_c4:
                    st.session_state.p1_values[i] = st.number_input(
                        "P1", value=float(st.session_state.p1_values[i]), step=1.0, key=f"p1_{i}"
                    )
                with r2_c5:
                    st.markdown('<div class="lbl-inline">P2</div>', unsafe_allow_html=True)
                with r2_c6:
                    st.session_state.p2_values[i] = st.number_input(
                        "P2", value=float(st.session_state.p2_values[i]), step=1.0, key=f"p2_{i}"
                    )