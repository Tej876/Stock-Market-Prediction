"""
Organic Minimalist Design System
Bespoke palette sampled directly from user swatch:
- #FEFAF3 (Warm Linen Ivory Canvas)
- #F6E2E9 (Soft Blush Rose Petal)
- #B8CFB3 (Matcha Celadon / Soft Sage)
- #84A282 (Deep Sage Eucalyptus)
- #263228 (Deep Forest Charcoal Ink)

Zero emojis. Generous spatial gaps. Full-width bordered segmented tabs.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* Global Canvas */
html, body, .stApp {
    background-color: #FEFAF3 !important;
    color: #263228 !important;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}

/* Dashboard Frame Container */
.dashboard-frame {
    max-width: 780px;
    margin: 10px auto 40px auto;
    background: #FFFFFF;
    border: 1.5px solid #B8CFB3;
    border-radius: 24px;
    padding: 36px 42px;
    box-shadow: 0 12px 36px rgba(132, 162, 130, 0.12);
}

/* Header Top Bar */
.top-bar {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-bottom: 26px;
    padding-bottom: 16px;
    border-bottom: 1.5px solid #ECE5DC;
}

.top-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #263228;
    letter-spacing: -0.02em;
    margin: 0;
}

/* Container padding and page width */
.block-container {
    max-width: 840px !important;
    padding-top: 2.2rem !important;
    padding-bottom: 4rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}

/* Full-Width Tab Bar across Entire Header */
.stTabs, [data-testid="stTabs"] {
    width: 100% !important;
    margin-bottom: 32px !important;
}

/* Hide default BaseWeb border and underline bars */
.stTabs [data-baseweb="tab-border"],
[data-testid="stTabs"] [data-baseweb="tab-border"] {
    display: none !important;
}
.stTabs [data-baseweb="tab-highlight"],
[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    display: none !important;
}

/* Tab Rail Container: Spans entire 100% header space with generous padding and gap */
.stTabs [data-baseweb="tab-list"],
[data-testid="stTabs"] [data-baseweb="tab-list"],
[role="tablist"] {
    width: 100% !important;
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: stretch !important;
    gap: 16px !important;
    background-color: #F4EFE6 !important;
    padding: 8px 10px !important;
    border-radius: 18px !important;
    border: 1.5px solid #E2D9CE !important;
    box-sizing: border-box !important;
}

/* Base / Inactive Tab: Equally distributed, compressed relative to active */
.stTabs [data-baseweb="tab"],
[data-testid="stTabs"] [data-baseweb="tab"],
[role="tab"] {
    flex: 1 1 0% !important;
    min-width: 0 !important;
    height: 52px !important;
    border-radius: 12px !important;
    color: #5F6D5E !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0 16px !important;
    background-color: #FAF7F2 !important;
    border: 1.5px solid #E2D9CE !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    box-sizing: border-box !important;
    cursor: pointer !important;
    transition: flex 0.4s cubic-bezier(0.25, 1, 0.5, 1), 
                background-color 0.25s ease, 
                color 0.25s ease, 
                border 0.25s ease, 
                box-shadow 0.25s ease !important;
}

/* Hover state on Inactive Tabs */
.stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]),
[role="tab"]:hover:not([aria-selected="true"]) {
    color: #263228 !important;
    background-color: #ECE5DC !important;
    border-color: #B8CFB3 !important;
}

/* Active / Pressed Tab: Dynamically expands to become significantly wider & highlighted */
.stTabs [data-baseweb="tab"][aria-selected="true"],
[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"],
[role="tab"][aria-selected="true"] {
    flex: 1.85 1 0% !important;
    background-color: #84A282 !important;
    color: #FEFAF3 !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    border: 2.5px solid #4D684B !important;
    box-shadow: 0 4px 16px rgba(132, 162, 130, 0.35) !important;
}

/* Tab typography & content alignment */
.stTabs [data-baseweb="tab"] p,
[data-testid="stTabs"] [data-baseweb="tab"] p,
[role="tab"] p {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: inherit !important;
    font-weight: inherit !important;
    color: inherit !important;
    margin: 0 !important;
    padding: 0 !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
    overflow: hidden !important;
}

.stTabs [data-baseweb="tab"] > div,
[data-testid="stTabs"] [data-baseweb="tab"] > div {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Page Section Titles */
.page-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #263228;
    margin: 16px 0 6px 0;
    letter-spacing: -0.015em;
}

.page-subtitle {
    font-size: 0.92rem;
    color: #5F6D5E;
    margin-bottom: 26px;
    line-height: 1.5;
}

/* Form Input Labels */
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    color: #263228 !important;
    margin-bottom: 6px !important;
}

/* Pill Input Boxes */
input[type="text"], input[type="number"], .stSelectbox [data-baseweb="select"] {
    background-color: #FDFBF7 !important;
    color: #263228 !important;
    border: 1.5px solid #B8CFB3 !important;
    border-radius: 9999px !important;
    padding: 10px 20px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.95rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 1px 3px rgba(132, 162, 130, 0.08) !important;
}

input[type="text"]:focus, input[type="number"]:focus, .stSelectbox [data-baseweb="select"]:focus-within {
    border-color: #84A282 !important;
    box-shadow: 0 0 0 3px rgba(132, 162, 130, 0.22) !important;
}

/* Hide Stepper Arrows on number inputs */
input[type="number"]::-webkit-inner-spin-button, 
input[type="number"]::-webkit-outer-spin-button { 
    -webkit-appearance: none; 
    margin: 0; 
}

/* Full-Width Pill Action Button */
.stButton>button {
    width: 100% !important;
    background: #84A282 !important;
    color: #FEFAF3 !important;
    border: none !important;
    border-radius: 9999px !important;
    padding: 14px 28px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
    margin-top: 22px !important;
    margin-bottom: 26px !important;
    transition: all 0.2s ease-in-out !important;
    box-shadow: 0 4px 14px rgba(132, 162, 130, 0.3) !important;
}

.stButton>button:hover {
    background: #6F8C6D !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(132, 162, 130, 0.4) !important;
}

.stButton>button:active {
    transform: translateY(1px) !important;
}

/* Result Cards with Generous Spatial Gaps (28px) */
.result-card-sage {
    background: #FBF9F4;
    border: 1.5px solid #B8CFB3;
    border-left: 5px solid #84A282;
    border-radius: 16px;
    padding: 24px 28px;
    margin-top: 28px !important;
    margin-bottom: 28px !important;
    box-shadow: 0 4px 16px rgba(132, 162, 130, 0.08);
}

.result-card-blush {
    background: #FDFBF8;
    border: 1.5px solid #E5C7D2;
    border-left: 5px solid #F6E2E9;
    border-radius: 16px;
    padding: 24px 28px;
    margin-top: 28px !important;
    margin-bottom: 28px !important;
    box-shadow: 0 4px 16px rgba(246, 226, 233, 0.2);
}

.result-label {
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #5F6D5E;
    font-weight: 700;
}

.result-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.95rem;
    font-weight: 700;
    color: #263228;
    margin: 6px 0;
}

.result-badge-blush {
    background: #F6E2E9;
    color: #643D48;
    border: 1px solid #E5C7D2;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 700;
}

.result-badge-sage {
    background: #EAF2E8;
    color: #2E4E2C;
    border: 1px solid #B8CFB3;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 700;
}

/* Expander Containers with Adequate Gap */
.streamlit-expanderHeader {
    background: #FAF7F2 !important;
    border: 1.5px solid #E2D9CE !important;
    border-radius: 12px !important;
    color: #263228 !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    padding: 14px 18px !important;
    margin-top: 24px !important;
}

.streamlit-expanderContent {
    background: #FAF7F2 !important;
    border: 1.5px solid #E2D9CE !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
    padding: 20px !important;
}

/* Hide streamlit default chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

def get_plotly_layout(title=""):
    return {
        "title": {
            "text": title,
            "font": {"family": "Plus Jakarta Sans, sans-serif", "size": 14, "color": "#263228"},
            "x": 0.02,
            "xanchor": "left"
        },
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "#F7F3EB",
        "font": {"family": "Plus Jakarta Sans, sans-serif", "color": "#5F6D5E", "size": 11},
        "margin": {"l": 45, "r": 20, "t": 45, "b": 40},
        "xaxis": {
            "gridcolor": "#E6DFD4",
            "zerolinecolor": "#D5CEAC",
            "linecolor": "#D5CEAC"
        },
        "yaxis": {
            "gridcolor": "#E6DFD4",
            "zerolinecolor": "#D5CEAC",
            "linecolor": "#D5CEAC"
        },
        "legend": {
            "font": {"color": "#263228", "size": 10},
            "bgcolor": "#FAF7F2",
            "bordercolor": "#E2D9CE",
            "borderwidth": 1
        }
    }
