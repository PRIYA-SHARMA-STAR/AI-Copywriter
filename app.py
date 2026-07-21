import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
st.set_page_config(
    page_title="AI Copywriter",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<h1 style='text-align:center;font-size:55px;'>
🤖 AI Copywriter
</h1>
<p style='text-align:center;font-size:20px;color:#CBD5E1'>
Create marketing content with AI in seconds 🚀
</p>
""", unsafe_allow_html=True)
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
st.sidebar.info(
    """
    AI Marketing Copy Generator

    Developed using:
    • Streamlit
    • Groq API
    • Python
    """
)
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
    width=90
)
st.sidebar.title("🤖 AI Copywriter")
st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Developer")
st.sidebar.success("Priya Sharma")
st.sidebar.write("🤖 AI Model")
st.sidebar.info("Llama 3.3 70B")
st.sidebar.write("⚡ API")
st.sidebar.success("Groq")
st.sidebar.markdown("---")
st.sidebar.caption("Version 2.0")
st.markdown("""
<style>
[data-testid="stHeader"]{
    background:transparent;
}
            /* Background */
.stApp{
    background:
        radial-gradient(circle at top left,#3b82f6 0%,transparent 35%),
        radial-gradient(circle at bottom right,#8b5cf6 0%,transparent 35%),
        linear-gradient(135deg,#0f172a,#111827,#1e1b4b);
    background-attachment: fixed;
}
/* Glass Card */
.block-container{
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:
    0 10px 40px rgba(0,0,0,0.35);
    padding:40px;
}
/* Headings */
h1,h2,h3{
    color:white !important;
    text-align:center;
}
/* Labels */
label,p,span{
    color:white !important;
    font-weight:bold;
}
/* Textbox */
.stTextInput input,
.stTextArea textarea{
    background:white !important;
    color:black !important;
    border-radius:10px;
}
/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:white;
    color:black;
    border-radius:10px;
}
/* Slider */
.stSlider{
    color:white;
}
/* Button */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    background:linear-gradient(90deg,#2563eb,#8b5cf6);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    transition:0.3s;
}
.stButton>button:hover{
    transform:translateY(-3px);
    box-shadow:0 8px 25px rgba(59,130,246,.5);
}
 /* Divider */
hr{
    border:1px solid rgba(255,255,255,0.2);
}
/* Slider Text */
.stSlider label{
    color:white !important;
}
/* Caption */
[data-testid="stCaptionContainer"]{
    color:#d1d5db;
}
            /* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}
footer{
    visibility:hidden;
}
/* Hide Deploy Button */
[data-testid="stAppDeployButton"]{
    display:none;
}
/* Hide Deploy Menu */
.stAppDeployButton{
    display:none;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    product_name = st.text_input("📦 Product Name", placeholder="e.g. Smart Water Bottle")
    platform = st.selectbox(
    "📱 Platform",
    [
        "💼 LinkedIn",
        "📸 Instagram",
        "📧 Email"
    ]
)
with col2:
    tone = st.selectbox(
    "🎭 Tone",
    [
        "💼 Professional",
        "😊 Friendly",
        "😎 Casual",
        "😂 Funny"
    ]
)
description = st.text_area(
    "📝 Product Description",
    placeholder="Describe your product here...",
    height=180
)
temperature = st.slider(
    "🔥 Creativity",
    0.0, 1.0, 0.7
)
st.divider()
top_p = st.slider(
    "🎯 Focus",
    0.0, 1.0, 0.9
)
st.markdown("### ✨ Generate High-Quality Marketing Content")
if st.button("🚀 Generate Marketing Copy"):
    if not product_name or not description:
        st.warning("⚠️ Please enter Product Name and Description.")
        st.stop()
    try:
        prompt = f"""
        You are an expert marketing copywriter.
        Product Name: {product_name}
        Product Description: {description}
        Platform: {platform}
        Tone: {tone}
        Write an attractive marketing copy.
        """
        with st.spinner("Generating amazing content..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                top_p=top_p,
            )
        st.success("API Connected")
        st.success("✅ Marketing Copy Generated Successfully!")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📱 Platform", platform)
        with col2:
            st.metric("🎭 Tone", tone)
        with col3:
            st.metric(
                "📝 Words",
                len(response.choices[0].message.content.split())
            )
        st.markdown("---")
        st.markdown("## ✨ Generated Marketing Copy")

        st.markdown(f"""
<div style="
background:linear-gradient(135deg,rgba(255,255,255,0.15),rgba(255,255,255,0.08));
backdrop-filter:blur(18px);
padding:30px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.25);
box-shadow:0 10px 30px rgba(0,0,0,0.35);
color:white;
font-size:18px;
line-height:1.9;
">

<h3 style="margin-top:0;color:#60A5FA;">
📢 AI Generated Content
</h3>

<hr style="border:1px solid rgba(255,255,255,0.15);">

<p style="white-space:pre-wrap;">
{response.choices[0].message.content}
</p>

</div>
""", unsafe_allow_html=True)
        st.markdown("### 📥 Export")
        st.download_button(
            label="📥 Download as TXT",
            data=response.choices[0].message.content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
    except Exception as e:
        st.error(e)
        st.divider()
st.caption("🚀 BE SMART,GENERATE SMART ")