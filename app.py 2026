import streamlit as st
import re
import urllib.parse

# پیج کنفیگریشن
st.set_page_config(page_title="Asad Official - VIP eBay Generator", page_icon="👑", layout="wide")

# پریمیم لک اینڈ فیل کے لیے CSS
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a, #0284c7);
        color: white; font-weight: bold; border-radius: 12px;
        padding: 12px 28px; border: none; transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(2, 132, 199, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.header("👑 Asad Official | Pure Enterprise eBay Generator")
st.caption("ایک طاقتور اور تیز ترین پلیٹ فارم جو بغیر کسی API یا بیرونی سرور کے پریمیم لسٹنگ کوڈ تیار کرتا ہے۔")

# کیٹیگری تھیم سلیکشن
theme_option = st.selectbox("🎯 Select Premium Category Theme:", [
    "Automotive / Hardware", "Art & Craft / Tools", "Skin Care / Beauty", 
    "Medical / Pharmacy", "Pet Care", "Garden / Organic", "Hygiene / Household"
])

theme_colors = {
    "Automotive / Hardware": {"brand": "#1e40af", "accent": "#94a3b8", "black": "#0f172a", "soft": "#f8fafc"},
    "Art & Craft / Tools": {"brand": "#7c2d12", "accent": "#f59e0b", "black": "#0f172a", "soft": "#fffbeb"},
    "Skin Care / Beauty": {"brand": "#9f1239", "accent": "#fcd34d", "black": "#4c0519", "soft": "#fff1f2"},
    "Medical / Pharmacy": {"brand": "#991b1b", "accent": "#fbbf24", "black": "#450a0a", "soft": "#fef2f2"},
    "Pet Care": {"brand": "#4c1d95", "accent": "#f59e0b", "black": "#2e1065", "soft": "#f5f3ff"},
    "Garden / Organic": {"brand": "#166534", "accent": "#84cc16", "black": "#052e16", "soft": "#f7fee7"},
    "Hygiene / Household": {"brand": "#14532d", "accent": "#4ade80", "black": "#052e16", "soft": "#f0fdf4"}
}
selected_colors = theme_colors[theme_option]

# ان پٹ فیلڈز
col1, col2 = st.columns(2)
with col1:
    product_title = st.text_input("📝 Product Title (پروڈکٹ کا نام):", placeholder="e.g., Premium Leather Car Seat Cover")
    product_price = st.text_input("💰 Product Price / Offer (آپشنل):", placeholder="e.g., $29.99")

with col2:
    product_features = st.text_area("⚡ Key Features (اہم خصوصیات - ہر لائن پر ایک لکھیں):", placeholder="Waterproof Material\nUniversal Fit\nEasy to Clean\nBreathable Design")

product_desc = st.text_area("ℹ️ Product Description (پروڈکٹ کی تفصیل):", placeholder="Write a short or detailed description here...")

if st.button("✨ Generate Premium VIP Code Instantly"):
    if not product_title:
        st.error("❌ برائے مہربانی پروڈکٹ کا نام (Title) لازمی درج کریں۔")
    else:
        # خصوصیات کو بلٹ پوائنٹس میں تبدیل کرنا
        features_list = product_features.split('\n')
        features_html = "".join([f"<li>🔑 {f.strip()}</li>" for f in features_list if f.strip()])
        
        # پریمیم ماسٹر ای بے ایچ ٹی ایم ایل ٹیمپلیٹ
        vip_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {{
            --brand-color: {selected_colors['brand']};
            --accent-glow: {selected_colors['accent']};
            --premium-black: {selected_colors['black']};
            --soft-bg: {selected_colors['soft']};
        }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: var(--soft-bg); color: var(--premium-black); }}
        .container {{ max-width: 1100px; margin: 30px auto; background: #ffffff; padding: 20px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 8px solid var(--brand-color); }}
        .hero-section {{ text-align: center; padding: 40px 20px; background: linear-gradient(135deg, var(--brand-color), var(--premium-black)); color: white; border-radius: 12px; margin-bottom: 30px; position: relative; overflow: hidden; }}
        .hero-section h1 {{ margin: 0; font-size: 2.5rem; letter-spacing: 1px; text-transform: uppercase; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
        .price-badge {{ display: inline-block; background: var(--accent-glow); color: var(--premium-black); font-weight: bold; padding: 8px 20px; border-radius: 50px; margin-top: 15px; font-size: 1.2rem; box-shadow: 0 4px 10px rgba(0,0,0,0.15); }}
        .grid-layout {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px; }}
        @media (max-width: 768px) {{ .grid-layout {{ grid-template-columns: 1fr; }} }}
        .info-box {{ background: var(--soft-bg); padding: 25px; border-radius: 12px; border-left: 5px solid var(--brand-color); }}
        .info-box h2 {{ margin-top: 0; color: var(--brand-color); font-size: 1.4rem; border-bottom: 2px solid rgba(0,0,0,0.05); padding-bottom: 10px; }}
        .info-box p {{ line-height: 1.6; font-size: 1.05rem; }}
        .info-box ul {{ list-style: none; padding: 0; }}
        .info-box ul li {{ padding: 10px 0; border-bottom: 1px dashed rgba(0,0,0,0.1); font-size: 1.05rem; display: flex; align-items: center; gap: 10px; }}
        .trust-bar {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; text-align: center; margin-top: 20px; padding: 20px; background: var(--premium-black); color: white; border-radius: 12px; }}
        .trust-item {{ font-weight: bold; font-size: 0.95rem; letter-spacing: 0.5px; color: var(--accent-glow); }}
        .footer {{ text-align: center; margin-top: 40px; font-size: 0.85rem; color: #64748b; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; }}
    </style>
</head>
<body>

<div class="container">
    <div class="hero-section">
        <h1>{product_title}</h1>
        {f'<div class="price-badge">{product_price}</div>' if product_price else ''}
    </div>

    <div class="grid-layout">
        <div class="info-box">
            <h2>📝 Product Description</h2>
            <p>{product_desc if product_desc else 'Premium quality product. Designed for durability and high performance. Perfect for everyday use.'}</p>
        </div>
        
        <div class="info-box">
            <h2>⚡ Key Specifications</h2>
            <ul>
                {features_html if features_html else '<li>🔑 High Quality Material</li><li>🔑 Durable & Reliable</li><li>🔑 Standard Fast Shipping</li><li>🔑 100% Satisfaction Guaranteed</li>'}
            </ul>
        </div>
    </div>

    <div class="trust-bar">
        <div class="trust-item">🚀 FAST & FREE SHIPPING</div>
        <div class="trust-item">🔒 SECURE PAYMENT</div>
        <div class="trust-item">⭐ TOP RATED SELLER</div>
        <div class="trust-item">🔄 30-DAYS RETURNS</div>
    </div>

    <div class="footer">
        <p>Thank you for shopping with us! Customer satisfaction is our top priority.</p>
    </div>
</div>

</body>
</html>"""

        st.success("🎉 آپ کا پریمیم VIP ای بے لسٹنگ کوڈ 100% کامیابی سے تیار ہو گیا ہے!")
        
        tab1, tab2 = st.tabs(["👀 Live Preview (کیسا دکھتا ہے)", "💻 Copy HTML Code (کوڈ کاپی کریں)"])
        with tab1:
            st.components.v1.html(vip_html, height=800, scrolling=True)
        with tab2:
            st.text_area("یہاں سے کوڈ کاپی کریں:", value=vip_html, height=500)
            st.download_button("📥 Download HTML File", data=vip_html, file_name="ebay_listing.html", mime="text/html")
