import streamlit as st
from src.inference import predict_label

def run_app():
    # ===== DARK THEME CONFIG =====
    st.set_page_config(
        page_title="🌐 NEWS CLASSIFIER",
        page_icon="📡",
        layout="centered"
    )
    
        # Initialize session state variables
    if 'title' not in st.session_state:
        st.session_state.title = ""
    if 'description' not in st.session_state:
        st.session_state.description = ""

    # Custom CSS with Large Fonts
    st.markdown("""
    <style>
    :root {
        --primary: #8A2BE2;
        --secondary: #20B2AA;
    }
    
    html, body, [class*="css"] {
        background-color: #0E1117;
        color: #FAFAFA;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Mega Headers */
    .header {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
        line-height: 1.2 !important;
    }
    
    .subheader {
        color: #BBBBBB;
        font-size: 1.8rem !important;
        margin-bottom: 2rem !important;
    }
    
    /* Enlarged Inputs */
    .stTextInput input, .stTextArea textarea {
        font-size: 1.4rem !important;
        background-color: #1E1E1E !important;
        border: 1px solid #444 !important;
        color: #FFF !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }
    
    /* Jumbo Button */
    .stButton button {
        font-size: 1.6rem !important;
        padding: 18px 32px !important;
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        margin: 1rem 0 !important;
    }
    
    /* XL Result Card */
    .result-card {
        padding: 2rem;
        font-size: 1.8rem !important;
        border-radius: 16px;
        background: linear-gradient(135deg, #1A1A2E, #16213E);
        border-left: 6px solid var(--primary);
    }
    
    .category-icon {
        font-size: 2.5rem !important;
    }
    
    /* Bigger Status Text */
    .stSpinner > div {
        font-size: 1.5rem !important;
    }
    
    .stAlert {
        font-size: 1.4rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ===== APP LAYOUT =====
    st.markdown('<p class="header">🌐 NEWS CLASSIFIER</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Instant Article Categorization</p>', 
               unsafe_allow_html=True)
    
    # Vertical Input Section
    title = st.text_input(
        "**📌 NEWS HEADLINE**",
        placeholder="Enter headline...",
        key="title",
        value=st.session_state.title
    )
    
    description = st.text_area(
        "**📝 ARTICLE CONTENT**",
        placeholder="Paste full text here...",
        height=200,
        key="description",
        value=st.session_state.description
    )

    # Button Columns
    col1, col2 = st.columns([5, 3])
    
    with col1:
        if st.button("**ANALYZE NOW**"):
            if not title.strip() or not description.strip():
                st.error("❌ Please provide both headline and content")
            else:
                with st.spinner("🔍 ANALYZING CONTENT..."):
                    category = predict_label(title=title, description=description)
                
                icon_map = {
                    "World": "🌍",
                    "Sports": "⚽", 
                    "Business": "💼",
                    "Sci/Tech": "🔬"
                }
                
                st.markdown(f"""
                <div class="result-card">
                    <h2>
                        <span class="category-icon">{icon_map.get(category, "✨")}</span>
                        <span style="color: var(--secondary)">RESULT:</span> 
                        <strong>{category.upper()}</strong>
                    </h2>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        if st.button("**🗑️ CLEAR**", 
                   key="clear_btn", 
                   help="Clear all inputs",
                   on_click=lambda: [st.session_state.update({"title": "", "description": ""}), st.rerun()]):
            pass

if __name__ == "__main__":
    run_app()