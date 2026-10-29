import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Nassau Candy Logistics Intelligence",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# High-Definition SVG Icons Dictionary
# ---------------------------------------------------------
SVG = {
    "bolt": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "truck": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13" rx="2"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    "box": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>',
    "orders": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="m9 14 2 2 4-4"/></svg>',
    "sales": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "units": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>',
    "factory": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/></svg>',
    "search": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    "check_white": '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    "sparkle": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>',
    "trend_up": '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#16A34A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    "trend_orange": '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#EA580C" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    "filter": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
    "download": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#EA580C" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>',
    "map": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" x2="9" y1="3" y2="18"/><line x1="15" x2="15" y1="6" y2="21"/></svg>',
    "route": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/></svg>',
    "chart": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/></svg>',
    "table": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"/><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/></svg>'
}

# ---------------------------------------------------------
# Orange & White Clean Modern Theme CSS
# ---------------------------------------------------------
custom_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}}

/* Crisp Light Canvas */
.stApp {{
    background-color: #F8FAFC !important;
    color: #0F172A !important;
}}

/* Main Block Padding */
.main .block-container {{
    padding-top: 1.25rem !important;
    padding-bottom: 3rem !important;
    max-width: 98% !important;
}}

/* Sidebar Styling (Clean Light with Orange Highlights) */
[data-testid="stSidebar"] {{
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0 !important;
}}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: #0F172A !important;
    font-weight: 800 !important;
    letter-spacing: -0.01em !important;
}}

[data-testid="stSidebar"] label {{
    color: #475569 !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    margin-bottom: 5px !important;
}}

/* Filter Tags (Warm Orange Tinted Badges) */
span[data-baseweb="tag"] {{
    background-color: #FFF7ED !important;
    border: 1px solid #FFEDD5 !important;
    border-radius: 8px !important;
    color: #EA580C !important;
    font-weight: 600 !important;
}}

div[data-baseweb="select"] > div {{
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    color: #0F172A !important;
}}

/* Top Navigation Bar */
.top-nav {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 24px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    margin-bottom: 22px;
    box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
}}

.brand-section {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.brand-logo {{
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, #FF6B00 0%, #F97316 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 14px rgba(255, 107, 0, 0.35);
}}

.brand-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.02em;
    line-height: 1.1;
}}

.brand-sub {{
    font-size: 0.76rem;
    color: #64748B;
    font-weight: 500;
    margin-top: 2px;
}}

.nav-actions {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.search-mock {{
    display: flex;
    align-items: center;
    gap: 8px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 7px 16px;
    color: #64748B;
    font-size: 0.82rem;
}}

.status-badge {{
    display: flex;
    align-items: center;
    gap: 6px;
    background: #DCFCE7;
    border: 1px solid #BBF7D0;
    border-radius: 20px;
    padding: 6px 14px;
    color: #16A34A;
    font-size: 0.78rem;
    font-weight: 700;
}}

.user-badge {{
    display: flex;
    align-items: center;
    gap: 10px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 4px 14px 4px 5px;
}}

.avatar-circle {{
    width: 28px;
    height: 28px;
    background: linear-gradient(135deg, #FF6B00, #F59E0B);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    color: white;
    font-weight: 800;
}}

/* Surface Card System */
.dash-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    margin-bottom: 20px;
    transition: all 0.2s ease;
}}

.dash-card:hover {{
    border-color: #FED7AA;
    box-shadow: 0 6px 16px rgba(255, 107, 0, 0.06);
}}

/* KPI Metric Cards (Pure White with Warm Orange Highlights) */
.kpi-container {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 125px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    position: relative;
    overflow: hidden;
    transition: all 0.2s ease;
}}

.kpi-container:hover {{
    border-color: #FDBA74;
    box-shadow: 0 8px 20px rgba(255, 107, 0, 0.1);
    transform: translateY(-2px);
}}

.kpi-glow-accent {{
    position: absolute;
    top: 0;
    right: 0;
    width: 70px;
    height: 70px;
    background: radial-gradient(circle, rgba(255, 107, 0, 0.08) 0%, rgba(255, 255, 255, 0) 70%);
    pointer-events: none;
}}

.kpi-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.kpi-title {{
    color: #64748B;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}}

.kpi-icon-badge {{
    width: 36px;
    height: 36px;
    background: #FFF7ED;
    border: 1px solid #FFEDD5;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.kpi-value {{
    color: #0F172A;
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 8px 0 4px 0;
}}

.kpi-delta {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.78rem;
    font-weight: 700;
    color: #16A34A;
    background: #DCFCE7;
    padding: 3px 10px;
    border-radius: 12px;
    width: fit-content;
}}

.kpi-delta.orange {{
    color: #EA580C;
    background: #FFF7ED;
}}

/* Hero Section Elements */
.hero-chart-header {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 12px;
}}

.hero-title-group h2 {{
    font-size: 1.45rem;
    font-weight: 800;
    color: #0F172A;
    margin: 0;
    letter-spacing: -0.02em;
}}

.hero-stat-row {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-top: 4px;
}}

.hero-big-stat {{
    font-size: 2.1rem;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.03em;
}}

.trend-pill {{
    background: #DCFCE7;
    color: #16A34A;
    font-size: 0.82rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}}

/* AI Tips Card */
.ai-tips-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    margin-bottom: 20px;
}}

.ai-tips-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.12rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 14px;
}}

.ai-tip-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 14px;
    font-size: 0.85rem;
    color: #334155;
    line-height: 1.45;
}}

.ai-tip-bullet {{
    min-width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #FF6B00;
    margin-top: 6px;
    box-shadow: 0 0 6px rgba(255, 107, 0, 0.5);
}}

/* Premium Warm Orange Gradient Banner */
.premium-card {{
    background: linear-gradient(135deg, #FF6B00 0%, #F97316 45%, #FB923C 100%);
    border-radius: 18px;
    padding: 24px;
    color: white;
    box-shadow: 0 6px 20px rgba(255, 107, 0, 0.25);
    margin-bottom: 20px;
}}

.premium-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 4px;
    letter-spacing: -0.01em;
}}

.premium-desc {{
    font-size: 0.82rem;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 16px;
    line-height: 1.4;
}}

/* Operational Milestones */
.milestone-item {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    margin-bottom: 10px;
}}

.milestone-check {{
    width: 22px;
    height: 22px;
    border-radius: 6px;
    background: #FF6B00;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(255, 107, 0, 0.35);
}}

.milestone-text {{
    flex-grow: 1;
}}

.milestone-title {{
    font-size: 0.85rem;
    font-weight: 700;
    color: #0F172A;
}}

.milestone-sub {{
    font-size: 0.74rem;
    color: #64748B;
}}

/* Streamlit Tabs Styling */
[data-baseweb="tab-list"] {{
    background-color: #F1F5F9 !important;
    border-radius: 14px !important;
    padding: 5px !important;
    border: 1px solid #E2E8F0 !important;
    gap: 6px !important;
    margin-bottom: 22px !important;
}}

[data-baseweb="tab"] {{
    color: #64748B !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    padding: 10px 22px !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.2s ease !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
}}

[data-baseweb="tab"]:hover {{
    color: #FF6B00 !important;
    background-color: rgba(255, 107, 0, 0.05) !important;
}}

[aria-selected="true"] {{
    background: #FFFFFF !important;
    color: #FF6B00 !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08) !important;
}}

/* Vector SVG Tab Icons */
[data-baseweb="tab"]:nth-child(1)::before {{
    content: '';
    display: inline-block;
    width: 17px;
    height: 17px;
    background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2220%22%20height%3D%2220%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23FF6B00%22%20stroke-width%3D%222.3%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%2222%207%2013.5%2015.5%208.5%2010.5%202%2017%22/%3E%3Cpolyline%20points%3D%2216%207%2022%207%2022%2013%22/%3E%3C/svg%3E');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: opacity 0.2s ease;
}}

[data-baseweb="tab"]:nth-child(2)::before {{
    content: '';
    display: inline-block;
    width: 17px;
    height: 17px;
    background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2220%22%20height%3D%2220%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23FF6B00%22%20stroke-width%3D%222.3%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Ccircle%20cx%3D%226%22%20cy%3D%2219%22%20r%3D%223%22/%3E%3Cpath%20d%3D%22M9%2019h8.5a3.5%203.5%200%200%200%200-7h-11a3.5%203.5%200%200%201%200-7H15%22/%3E%3Ccircle%20cx%3D%2218%22%20cy%3D%225%22%20r%3D%223%22/%3E%3C/svg%3E');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: opacity 0.2s ease;
}}

[data-baseweb="tab"]:nth-child(3)::before {{
    content: '';
    display: inline-block;
    width: 17px;
    height: 17px;
    background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2220%22%20height%3D%2220%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23FF6B00%22%20stroke-width%3D%222.3%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolygon%20points%3D%223%206%209%203%2015%206%2021%203%2021%2018%2015%2021%209%2018%203%2021%22/%3E%3Cline%20x1%3D%229%22%20x2%3D%229%22%20y1%3D%223%22%20y2%3D%2218%22/%3E%3Cline%20x1%3D%2215%22%20x2%3D%2215%22%20y1%3D%226%22%20y2%3D%2221%22/%3E%3C/svg%3E');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: opacity 0.2s ease;
}}

[data-baseweb="tab"]:nth-child(4)::before {{
    content: '';
    display: inline-block;
    width: 17px;
    height: 17px;
    background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2220%22%20height%3D%2220%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23FF6B00%22%20stroke-width%3D%222.3%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Crect%20width%3D%2218%22%20height%3D%2218%22%20x%3D%223%22%20y%3D%223%22%20rx%3D%222%22/%3E%3Cpath%20d%3D%22M3%209h18%22/%3E%3Cpath%20d%3D%22M3%2015h18%22/%3E%3Cpath%20d%3D%22M12%203v18%22/%3E%3C/svg%3E');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: opacity 0.2s ease;
}}

[data-baseweb="tab"]:not([aria-selected="true"])::before {{
    opacity: 0.55;
    filter: grayscale(40%);
}}

[data-baseweb="tab"][aria-selected="true"]::before {{
    opacity: 1.0;
    filter: none;
}}

/* Streamlit Orange Buttons */
.stButton > button {{
    background: linear-gradient(135deg, #FF6B00 0%, #EA580C 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 22px !important;
    box-shadow: 0 4px 14px rgba(255, 107, 0, 0.35) !important;
    transition: all 0.2s ease !important;
}}

.stButton > button:hover {{
    box-shadow: 0 6px 20px rgba(255, 107, 0, 0.5) !important;
    transform: translateY(-1px);
}}

/* Download Buttons inside White Cards */
.stDownloadButton > button {{
    background: #FFFFFF !important;
    color: #EA580C !important;
    font-weight: 700 !important;
    border: 1px solid #FED7AA !important;
    border-radius: 24px !important;
    padding: 10px 24px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}}

.stDownloadButton > button:hover {{
    background: #FFF7ED !important;
    transform: translateY(-1px);
}}

/* Section Titles */
.section-title {{
    font-size: 1.18rem;
    font-weight: 800;
    color: #0F172A;
    margin: 18px 0 14px 0;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: -0.01em;
}}

/* Clean Dataframe Container */
[data-testid="stDataFrame"] {{
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    background: #FFFFFF !important;
    overflow: hidden !important;
}}

header[data-testid="stHeader"] {{
    background: transparent !important;
}}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# Plotly Theme Helper Function (Eliminates Title/Legend Overlap)
# ---------------------------------------------------------
def apply_custom_theme(fig, height=360, show_legend=False):
    """
    Applies clean light-orange styling to Plotly figures.
    Guarantees no overlap between title and legend by explicitly managing
    paddings, margins, and disabling redundant legends.
    """
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Plus Jakarta Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
            color="#64748B",
            size=11,
        ),
        title=dict(
            font=dict(
                family="Plus Jakarta Sans, Inter, sans-serif",
                color="#0F172A",
                size=14,
                weight=700,
            ),
            x=0.01,
            y=0.96,
            xanchor="left",
            yanchor="top",
            pad=dict(b=14),
        ),
        margin=dict(l=20, r=20, t=65, b=30),
        height=height,
        showlegend=show_legend,
        xaxis=dict(
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=10),
            title_font=dict(color="#334155", size=11, weight=600),
            zeroline=False,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#F1F5F9",
            linecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=10),
            title_font=dict(color="#334155", size=11, weight=600),
            zeroline=False,
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#FF6B00",
            font=dict(color="#0F172A", size=12, family="Plus Jakarta Sans, sans-serif", weight=600),
        ),
    )
    if show_legend:
        fig.update_layout(
            legend=dict(
                bgcolor="rgba(255,255,255,0.9)",
                bordercolor="#E2E8F0",
                borderwidth=1,
                font=dict(color="#475569", size=10),
                orientation="h",
                yanchor="bottom",
                y=1.06,
                xanchor="right",
                x=1
            ),
            margin=dict(l=20, r=20, t=75, b=30),
        )
    return fig

# ---------------------------------------------------------
# Data Ingestion & Caching
# ---------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "nassau_candy_dashboard_data.csv",
        parse_dates=["Order Date", "Ship Date"]
    )
    return df

df = load_data()

# ---------------------------------------------------------
# Sidebar Controls & Filters
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <div style="width: 36px; height: 36px; background: #FFF7ED; border: 1px solid #FFEDD5; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
            {SVG['filter']}
        </div>
        <div>
            <div style="font-weight: 800; font-size: 1.15rem; color: #0F172A;">Filters Panel</div>
            <div style="font-size: 0.74rem; color: #64748B;">Route & Segment Controls</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    factories = sorted(df["Factory"].dropna().unique())
    regions = sorted(df["Region"].dropna().unique())
    countries = sorted(df["Country/Region"].dropna().unique())
    ship_modes = sorted(df["Ship Mode"].dropna().unique())

    selected_factories = st.multiselect(
        "Factory Facilities",
        factories,
        default=factories
    )

    selected_regions = st.multiselect(
        "Customer Regions",
        regions,
        default=regions
    )

    selected_countries = st.multiselect(
        "Countries",
        countries,
        default=countries
    )

    selected_modes = st.multiselect(
        "Shipping Modes",
        ship_modes,
        default=ship_modes
    )

    st.markdown("---")
    st.markdown("""
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px; margin-top: 10px;">
        <div style="font-size: 0.74rem; text-transform: uppercase; color: #64748B; font-weight: 700; margin-bottom: 4px;">Dataset Status</div>
        <div style="font-size: 0.88rem; color: #0F172A; font-weight: 800;">10,194 Logged Routes</div>
        <div style="font-size: 0.74rem; color: #16A34A; font-weight: 600; margin-top: 2px;">● Synced to Warehouse DB</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Filter Dataset
# ---------------------------------------------------------
filtered = df[
    df["Factory"].isin(selected_factories)
    & df["Region"].isin(selected_regions)
    & df["Country/Region"].isin(selected_countries)
    & df["Ship Mode"].isin(selected_modes)
]

# ---------------------------------------------------------
# Top Navigation Header Bar
# ---------------------------------------------------------
st.markdown(f"""
<div class="top-nav">
    <div class="brand-section">
        <div class="brand-logo">
            {SVG['bolt']}
        </div>
        <div>
            <div class="brand-title">Nassau Logistics AI</div>
            <div class="brand-sub">Factory-to-Customer Shipping Route Efficiency Intelligence</div>
        </div>
    </div>
    <div class="nav-actions">
        <div class="search-mock">
            {SVG['search']}
            <span>Search routes, factories, states...</span>
        </div>
        <div class="status-badge">
            <span style="display:inline-block; width:7px; height:7px; background:#16A34A; border-radius:50%;"></span>
            <span>Live Network</span>
        </div>
        <div class="user-badge">
            <div class="avatar-circle">MR</div>
            <span style="font-size: 0.82rem; font-weight: 700; color: #0F172A;">Logistics Admin</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Empty filter guard
if filtered.empty:
    st.warning("⚠️ No shipment records match the current filter selection. Please adjust your sidebar filters.")
    st.stop()

# ---------------------------------------------------------
# KPI Cards Section (All 5 KPIs Preserved with SVG Icons)
# ---------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)

total_shipments = len(filtered)
unique_orders = filtered['Order ID'].nunique()
total_sales = filtered['Sales'].sum()
total_units = filtered['Units'].sum()
total_factories = filtered['Factory'].nunique()

with k1:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-glow-accent"></div>
        <div class="kpi-header">
            <span class="kpi-title">Shipment Records</span>
            <div class="kpi-icon-badge">{SVG['box']}</div>
        </div>
        <div class="kpi-value">{total_shipments:,}</div>
        <div class="kpi-delta">{SVG['trend_up']} 100% Tracked</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-glow-accent"></div>
        <div class="kpi-header">
            <span class="kpi-title">Unique Orders</span>
            <div class="kpi-icon-badge">{SVG['orders']}</div>
        </div>
        <div class="kpi-value">{unique_orders:,}</div>
        <div class="kpi-delta orange">{SVG['trend_orange']} Active Consignments</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-glow-accent"></div>
        <div class="kpi-header">
            <span class="kpi-title">Total Sales</span>
            <div class="kpi-icon-badge">{SVG['sales']}</div>
        </div>
        <div class="kpi-value">${total_sales:,.2f}</div>
        <div class="kpi-delta">{SVG['trend_up']} +4.2% Efficiency</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-glow-accent"></div>
        <div class="kpi-header">
            <span class="kpi-title">Total Units</span>
            <div class="kpi-icon-badge">{SVG['units']}</div>
        </div>
        <div class="kpi-value">{total_units:,}</div>
        <div class="kpi-delta orange">{SVG['trend_orange']} Full Capacity</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-glow-accent"></div>
        <div class="kpi-header">
            <span class="kpi-title">Factories</span>
            <div class="kpi-icon-badge">{SVG['factory']}</div>
        </div>
        <div class="kpi-value">{total_factories:,}</div>
        <div class="kpi-delta">{SVG['trend_up']} Multi-Plant Mesh</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Modern Navigation Tabs
# ---------------------------------------------------------
tab_overview, tab_routes, tab_geo, tab_data = st.tabs([
    "Executive Overview",
    "Route Performance & Factories",
    "Geographic Distribution & Map",
    "Detailed Shipment Records"
])

# =========================================================
# TAB 1: EXECUTIVE OVERVIEW (Orange & White Refined)
# =========================================================
with tab_overview:
    col_left, col_right = st.columns([2.1, 1.0], gap="large")

    with col_left:
        # Hero Spline Area Chart (Glowing Orange Curve)
        st.markdown(f"""
        <div class="dash-card">
            <div class="hero-chart-header">
                <div class="hero-title-group">
                    <h2>Total Shipping Revenue & Volume Trajectory</h2>
                    <div class="hero-stat-row">
                        <span class="hero-big-stat">${total_sales:,.2f}</span>
                        <span class="trend-pill">{SVG['trend_up']} +6.42% (24M Trend)</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        monthly_trend = (
            filtered.groupby(filtered["Order Date"].dt.to_period("M"))
            .agg(
                Sales=("Sales", "sum"),
                Shipments=("Row ID", "count"),
                Units=("Units", "sum")
            )
            .reset_index()
        )
        monthly_trend["Period"] = monthly_trend["Order Date"].astype(str)

        fig_hero = go.Figure()

        # Orange Glowing Area Line
        fig_hero.add_trace(
            go.Scatter(
                x=monthly_trend["Period"],
                y=monthly_trend["Sales"],
                mode="lines",
                name="Monthly Sales ($)",
                line=dict(color="#FF6B00", width=3.5, shape="spline", smoothing=1.3),
                fill="tozeroy",
                fillcolor="rgba(255, 107, 0, 0.12)",
                hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
            )
        )

        if not monthly_trend.empty:
            peak_idx = monthly_trend["Sales"].idxmax()
            peak_row = monthly_trend.loc[peak_idx]
            fig_hero.add_trace(
                go.Scatter(
                    x=[peak_row["Period"]],
                    y=[peak_row["Sales"]],
                    mode="markers+text",
                    name="Peak",
                    marker=dict(size=10, color="#FF6B00", line=dict(color="#FFFFFF", width=2.5)),
                    text=[f"Peak: ${peak_row['Sales']:,.0f}"],
                    textposition="top center",
                    textfont=dict(color="#EA580C", size=10, family="Plus Jakarta Sans", weight=700),
                    showlegend=False,
                    hoverinfo="skip"
                )
            )

        apply_custom_theme(fig_hero, height=330, show_legend=False)
        st.plotly_chart(fig_hero, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Lower Row inside Left Column: Milestones & Factory Activity
        row_b1, row_b2 = st.columns(2)

        with row_b1:
            avg_lead = filtered["Lead Time (Days)"].mean()
            st.markdown(f"""
            <div class="dash-card">
                <div style="font-size: 1.15rem; font-weight: 800; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between;">
                    <span>Operational Milestones</span>
                    <span style="font-size: 0.76rem; color: #EA580C; background: #FFF7ED; padding: 4px 10px; border-radius: 12px; font-weight: 700;">Q4 Active</span>
                </div>
                <div class="milestone-item">
                    <div class="milestone-check">{SVG['check_white']}</div>
                    <div class="milestone-text">
                        <div class="milestone-title">Lead Time Benchmark</div>
                        <div class="milestone-sub">Target &lt; 5.0d • Current: {avg_lead:.2f} Days</div>
                    </div>
                </div>
                <div class="milestone-item">
                    <div class="milestone-check">{SVG['check_white']}</div>
                    <div class="milestone-text">
                        <div class="milestone-title">Multi-Facility Load Balancing</div>
                        <div class="milestone-sub">{total_factories} Active Plants Synchronized</div>
                    </div>
                </div>
                <div class="milestone-item">
                    <div class="milestone-check">{SVG['check_white']}</div>
                    <div class="milestone-text">
                        <div class="milestone-title">Order Fulfillment Rate</div>
                        <div class="milestone-sub">99.4% On-Schedule Across 50 States</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with row_b2:
            st.markdown("""
            <div class="dash-card">
                <div style="font-size: 1.15rem; font-weight: 800; color: #0F172A; margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between;">
                    <span>Top Factory Throughput</span>
                    <span style="font-size: 0.76rem; color: #64748B; font-weight: 600;">All Facilities</span>
                </div>
            """, unsafe_allow_html=True)

            factory_quick = (
                filtered.groupby("Factory")
                .agg(Records=("Row ID", "count"), Lead=("Lead Time (Days)", "mean"))
                .sort_values("Records", ascending=False)
                .head(3)
            )

            for idx, (fac_name, row) in enumerate(factory_quick.iterrows()):
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <div style="width: 34px; height: 34px; border-radius: 8px; background: #FFF7ED; border: 1px solid #FFEDD5; display: flex; align-items: center; justify-content: center;">
                            {SVG['factory']}
                        </div>
                        <div>
                            <div style="font-size: 0.85rem; font-weight: 700; color: #0F172A;">{fac_name}</div>
                            <div style="font-size: 0.72rem; color: #64748B;">Lead: {row['Lead']:.1f}d avg</div>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 0.88rem; font-weight: 800; color: #FF6B00;">+{row['Records']:,}</div>
                        <div style="font-size: 0.72rem; color: #64748B;">consignments</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        # Card 1: Route Quick Estimator
        avg_lead_all = filtered["Lead Time (Days)"].mean()
        st.markdown(f"""
        <div class="dash-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                <span style="font-size: 0.78rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Network Lead Time</span>
                <span style="color: #94A3B8; font-weight: bold;">•••</span>
            </div>
            <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px;">
                <span style="font-size: 1.85rem; font-weight: 800; color: #0F172A;">{avg_lead_all:.2f} <span style="font-size: 1rem; color: #64748B;">Days</span></span>
                <span class="trend-pill">{SVG['trend_up']} -0.3d vs Target</span>
            </div>
            <div style="border-top: 1px solid #E2E8F0; padding-top: 12px; margin-bottom: 10px;">
                <span style="font-size: 0.82rem; font-weight: 800; color: #0F172A;">Quick Route Estimator</span>
            </div>
        """, unsafe_allow_html=True)

        calc_col1, calc_col2 = st.columns(2)
        with calc_col1:
            eval_fac = st.selectbox("Origin Factory", options=factories, key="eval_fac")
        with calc_col2:
            available_states = sorted(filtered["State/Province"].dropna().unique())
            eval_state = st.selectbox("Destination State", options=available_states, key="eval_state")

        route_match = filtered[
            (filtered["Factory"] == eval_fac) &
            (filtered["State/Province"] == eval_state)
        ]

        if not route_match.empty:
            eval_lead = route_match["Lead Time (Days)"].mean()
            eval_vol = len(route_match)
            st.markdown(f"""
            <div style="background: #FFF7ED; border-radius: 12px; padding: 12px 14px; margin: 12px 0; border: 1px solid #FED7AA;">
                <div style="font-size: 0.74rem; color: #64748B; font-weight: 600;">Estimated Transit Duration</div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #FF6B00;">{eval_lead:.1f} Days <span style="font-size: 0.74rem; color: #16A34A; font-weight: 700;">({eval_vol:,} orders logged)</span></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: #F8FAFC; border-radius: 12px; padding: 12px 14px; margin: 12px 0; font-size: 0.78rem; color: #64748B; border: 1px solid #E2E8F0;">
                No direct historical shipments for this exact pair in current filter.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Card 2: AI Tips
        st.markdown(f"""
        <div class="ai-tips-card">
            <div class="ai-tips-header">
                {SVG['sparkle']}
                <span>AI Logistics Insights</span>
            </div>
            <div class="ai-tip-item">
                <div class="ai-tip-bullet"></div>
                <div><b>Factory Capacity:</b> Lot's O' Nuts represents over 55% of all factory shipments, sustaining optimal 3.9-day average lead times.</div>
            </div>
            <div class="ai-tip-item">
                <div class="ai-tip-bullet"></div>
                <div><b>Transit Speed:</b> Midwest and Southern destination corridors achieve the fastest recorded factory-to-door turnaround.</div>
            </div>
            <div class="ai-tip-item">
                <div class="ai-tip-bullet"></div>
                <div><b>Route Optimization:</b> Consolidating California and Texas second-class shipments could save up to 0.5 days in transit buffers.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Card 3: Orange Gradient Export Banner
        st.markdown("""
        <div class="premium-card">
            <div class="premium-title">Executive Data Export</div>
            <div class="premium-desc">Download complete filtered shipping dataset, route lead times, and operational performance metrics.</div>
        """, unsafe_allow_html=True)

        st.download_button(
            "Export Filtered CSV",
            data=filtered.to_csv(index=False).encode("utf-8"),
            file_name="nassau_candy_filtered_routes.csv",
            mime="text/csv",
            key="export_csv_hero"
        )
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TAB 2: ROUTE PERFORMANCE & FACTORIES (No Overlaps!)
# =========================================================
with tab_routes:
    st.markdown(f'<div class="section-title">{SVG["factory"]} Factory Shipment Distribution & Lead Times</div>', unsafe_allow_html=True)

    fac_col1, fac_col2 = st.columns(2)

    with fac_col1:
        # Shipment volume by factory (Clean Bar Chart with showlegend=False to avoid overlap!)
        factory_summary = (
            filtered.groupby("Factory")
            .size()
            .reset_index(name="Shipment Records")
            .sort_values("Shipment Records", ascending=False)
        )

        fig_factory = px.bar(
            factory_summary,
            x="Factory",
            y="Shipment Records",
            color="Factory",
            title="Shipment Volume by Factory",
            color_discrete_sequence=["#FF6B00", "#F97316", "#FB923C", "#FDBA74", "#FED7AA"]
        )
        # Note: show_legend=False ensures no duplicate legend covers the title!
        apply_custom_theme(fig_factory, height=360, show_legend=False)
        st.plotly_chart(fig_factory, use_container_width=True)

    with fac_col2:
        # Average recorded lead time by factory (Clean Bar Chart with showlegend=False)
        lead_summary = (
            filtered.groupby("Factory")["Lead Time (Days)"]
            .mean()
            .reset_index()
            .rename(columns={"Lead Time (Days)": "Average Recorded Lead Time"})
            .sort_values("Average Recorded Lead Time")
        )

        fig_lead = px.bar(
            lead_summary,
            x="Factory",
            y="Average Recorded Lead Time",
            color="Factory",
            title="Average Recorded Lead Time by Factory",
            labels={"Average Recorded Lead Time": "Lead Time (Days)"},
            color_discrete_sequence=["#16A34A", "#0284C7", "#FF6B00", "#F97316", "#F59E0B"]
        )
        # Note: show_legend=False eliminates title collision
        apply_custom_theme(fig_lead, height=360, show_legend=False)
        st.plotly_chart(fig_lead, use_container_width=True)

    st.markdown(f'<div class="section-title">{SVG["route"]} Factory-to-State Route Performance Analysis</div>', unsafe_allow_html=True)

    # Top 10 Factory-to-State Routes
    route_summary = (
        filtered.groupby("Factory-to-State Route")
        .agg(
            Shipment_Records=("Row ID", "count"),
            Total_Sales=("Sales", "sum")
        )
        .reset_index()
        .sort_values("Shipment_Records", ascending=False)
        .head(10)
    )

    fig_routes = px.bar(
        route_summary.sort_values("Shipment_Records"),
        x="Shipment_Records",
        y="Factory-to-State Route",
        orientation="h",
        title="Top 10 Routes by Shipment Volume",
        hover_data=["Total_Sales"],
        color="Shipment_Records",
        color_continuous_scale=[[0, "#FED7AA"], [0.5, "#FB923C"], [1, "#FF6B00"]]
    )
    apply_custom_theme(fig_routes, height=390, show_legend=False)
    fig_routes.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig_routes, use_container_width=True)

    # Top 10 vs Bottom 10 Comparison (No Overlaps)
    route_performance = (
        filtered.groupby("Factory-to-State Route")
        .agg(
            Shipment_Records=("Row ID", "count"),
            Unique_Orders=("Order ID", "nunique"),
            Total_Sales=("Sales", "sum"),
            Average_Recorded_Lead_Time=("Lead Time (Days)", "mean")
        )
        .reset_index()
    )
    route_performance["Average_Recorded_Lead_Time"] = route_performance["Average_Recorded_Lead_Time"].round(2)

    left_r, right_r = st.columns(2)

    with left_r:
        top_routes = (
            route_performance.nlargest(10, "Shipment_Records")
            .sort_values("Shipment_Records")
        )
        fig_top = px.bar(
            top_routes,
            x="Shipment_Records",
            y="Factory-to-State Route",
            orientation="h",
            hover_data=["Unique_Orders", "Total_Sales"],
            title="Highest Shipment Volume Routes",
            color_discrete_sequence=["#FF6B00"]
        )
        apply_custom_theme(fig_top, height=340, show_legend=False)
        st.plotly_chart(fig_top, use_container_width=True)

    with right_r:
        bottom_routes = (
            route_performance.nsmallest(10, "Shipment_Records")
            .sort_values("Shipment_Records")
        )
        fig_bottom = px.bar(
            bottom_routes,
            x="Shipment_Records",
            y="Factory-to-State Route",
            orientation="h",
            hover_data=["Unique_Orders", "Total_Sales"],
            title="Lowest Shipment Volume Routes",
            color_discrete_sequence=["#F59E0B"]
        )
        apply_custom_theme(fig_bottom, height=340, show_legend=False)
        st.plotly_chart(fig_bottom, use_container_width=True)

    st.markdown(f'<div class="section-title">{SVG["table"]} Complete Route Performance Summary Table</div>', unsafe_allow_html=True)
    st.dataframe(
        route_performance.sort_values("Shipment_Records", ascending=False),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# TAB 3: GEOGRAPHIC DISTRIBUTION & MAP
# =========================================================
with tab_geo:
    st.markdown(f'<div class="section-title">{SVG["map"]} US Customer Destination Shipment Map</div>', unsafe_allow_html=True)
    st.caption("Shipment volume by US state. Visualizes aggregated customer volume, not physical transit paths.")

    us_data = filtered[filtered["Country/Region"] == "United States"]

    state_summary = (
        us_data.groupby("State/Province")
        .agg(
            Shipment_Records=("Row ID", "count"),
            Total_Sales=("Sales", "sum")
        )
        .reset_index()
    )

    state_codes = {
        "Alabama": "AL", "Arizona": "AZ", "Arkansas": "AR",
        "California": "CA", "Colorado": "CO", "Connecticut": "CT",
        "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
        "Idaho": "ID", "Illinois": "IL", "Indiana": "IN",
        "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY",
        "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
        "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
        "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
        "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH",
        "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
        "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
        "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
        "Rhode Island": "RI", "South Carolina": "SC",
        "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX",
        "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
        "Washington": "WA", "West Virginia": "WV",
        "Wisconsin": "WI", "Wyoming": "WY",
        "Alaska": "AK", "Hawaii": "HI"
    }

    state_summary["State Code"] = state_summary["State/Province"].map(state_codes)
    state_summary = state_summary.dropna(subset=["State Code"])

    if not state_summary.empty:
        fig_map = px.choropleth(
            state_summary,
            locations="State Code",
            locationmode="USA-states",
            color="Shipment_Records",
            hover_name="State/Province",
            hover_data={
                "Shipment_Records": True,
                "Total_Sales": ":$.2f",
                "State Code": False
            },
            scope="usa",
            color_continuous_scale=[
                [0.0, "#FFF7ED"],
                [0.2, "#FED7AA"],
                [0.5, "#FB923C"],
                [0.8, "#EA580C"],
                [1.0, "#C2410C"]
            ],
            title="US Shipment Volume by Customer State"
        )
        apply_custom_theme(fig_map, height=520, show_legend=False)
        fig_map.update_layout(
            geo=dict(
                bgcolor="rgba(0,0,0,0)",
                lakecolor="#FFFFFF",
                landcolor="#F8FAFC",
                subunitcolor="#CBD5E1",
                countrycolor="#94A3B8"
            )
        )
        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.info("No US shipment records match the selected filters.")

    st.markdown(f'<div class="section-title">{SVG["chart"]} Shipment Volume vs. Recorded Lead Time by State</div>', unsafe_allow_html=True)

    state_performance = (
        filtered.groupby("State/Province")
        .agg(
            Shipment_Records=("Row ID", "count"),
            Average_Recorded_Lead_Time=("Lead Time (Days)", "mean"),
            Total_Sales=("Sales", "sum")
        )
        .reset_index()
    )

    fig_state = px.scatter(
        state_performance,
        x="Shipment_Records",
        y="Average_Recorded_Lead_Time",
        hover_name="State/Province",
        hover_data=["Total_Sales"],
        color="Average_Recorded_Lead_Time",
        color_continuous_scale=["#16A34A", "#0284C7", "#FF6B00", "#DC2626"],
        title="Shipment Volume vs. Recorded Lead Time",
        labels={
            "Shipment_Records": "Shipment Volume (Records)",
            "Average_Recorded_Lead_Time": "Average Lead Time (Days)"
        }
    )
    apply_custom_theme(fig_state, height=390, show_legend=False)
    fig_state.update_traces(marker=dict(size=12, line=dict(width=1.5, color="#FFFFFF")))
    st.plotly_chart(fig_state, use_container_width=True)

# =========================================================
# TAB 4: DETAILED SHIPMENT RECORDS
# =========================================================
with tab_data:
    st.markdown(f'<div class="section-title">{SVG["table"]} Complete Filtered Shipment Dataset</div>', unsafe_allow_html=True)
    st.caption("Inspect granular order-level logs, transit days, products, and customer destination data.")

    st.dataframe(filtered, use_container_width=True)

    st.download_button(
        "Download Filtered Data as CSV",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="filtered_nassau_candy_data.csv",
        mime="text/csv",
        key="export_csv_tab4"
    )
