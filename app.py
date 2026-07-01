import streamlit as st
import google.generativeai as genai
import time

# --- 1. PAGE SETUP (Lovable Style) ---
st.set_page_config(page_title="LikeBot Pro | AI Generator", page_icon="✨", layout="wide")

# --- 2. PREMIUM LOVABLE CSS THEME ---
# یہ CSS آپ کی ویب سائٹ کو بالکل LikeBot Pro جیسا ماڈرن اور کلین لک دے گی
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp { background-color: #FAFAFA; color: #111827; font-family: 'Inter', sans-serif; }
    
    /* Login & Glassmorphism Cards */
    .lovable-card { 
        background: #FFFFFF; padding: 40px; border-radius: 24px; 
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05); 
        border: 1px solid #F3F4F6; text-align: center;
    }
    
    /* Premium Inputs */
    .stTextInput>div>div>input { 
        border-radius: 12px; border: 1px solid #E5E7EB; 
        padding: 14px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); 
        background-color: #F9FAFB; color: #111827;
    }
    .stTextInput>div>div>input:focus { border-color: #6366F1; box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2); }
    
    /* Premium Buttons */
    .stButton>button { 
        background: linear-gradient(135deg, #6366F1, #4F46E5); 
        color: white; border-radius: 12px; border: none; 
        padding: 12px 24px; font-weight: 600; letter-spacing: 0.5px;
        transition: all 0.3s ease; width: 100%; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4); }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. SECURE LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
        <div class="lovable-card">
            <h1 style='color: #4F46E5; font-size: 2.5rem; margin-bottom: 10px;'>✨ LikeBot Pro</h1>
            <p style='color: #6B7280; font-size: 1.1rem; margin-top: 0;'>Sign in with your authorized Gmail</p>
        </div><br>
        """, unsafe_allow_html=True)
        
        email = st.text_input("Google Email Address", placeholder="e.g., asad@gmail.com")
        
        if st.button("Continue with Email"):
            if email and "@" in email:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("❌ Please enter a valid Gmail address.")
else:
    # ==========================================
    # --- 4. LIVE GEMINI DASHBOARD (LOVABLE UI) ---
    # ==========================================
    
    # Sidebar
    st.sidebar.markdown(f"### 👤 Profile\n**{st.session_state.user_email}**")
    st.sidebar.success("✅ Connected to Gemini Pro")
    if st.sidebar.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.rerun()

    # --- AI SETUP ---
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error("⚠️ Streamlit Secrets میں GEMINI_API_KEY ایڈ کریں۔")
        st.stop()

    st.markdown("<h2 style='color: #111827;'>✨ Live HTML AI Assistant</h2>", unsafe_allow_html=True)
    st.caption("Paste an eBay/Amazon link or describe your product. The AI will generate code with a copy button.")

    # --- CHAT MEMORY ---
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi Asad! I am your AI assistant. Send me a product link, and I will write a premium HTML template for you."}
        ]

    for msg in st.session_state.messages:
        avatar = "✨" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # --- LIVE CHAT INPUT ---
    if prompt := st.chat_input("Paste product link here..."):
        
        # User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
            
        # AI Response
        with st.chat_message("assistant", avatar="✨"):
            message_placeholder = st.empty()
            full_response = ""
            
            system_instruction = "You are an expert HTML designer. Provide premium HTML/CSS code. ALWAYS output code inside markdown code blocks (```html ... ```) so the copy button works."
            full_prompt = f"{system_instruction}\n\nUser request: {prompt}"
            
            with st.spinner("Analyzing and typing..."):
                try:
                    response = model.generate_content(full_prompt, stream=True)
                    
                    for chunk in response:
                        full_response += chunk.text
                        message_placeholder.markdown(full_response + " ▌")
                    
                    message_placeholder.markdown(full_response)
                except Exception as e:
                    full_response = f"❌ Error: {e}"
                    message_placeholder.error(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
