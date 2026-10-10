import streamlit as st
import os

st.set_page_config(page_title="المساعد الميداني لقانون المرور", page_icon="🚨", layout="wide")
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚨 المساعد الميداني لقانون المرور الجزائري</h1>", unsafe_allow_html=True)

law_files = ["مرسوم تنفيذ رقم 04-381.txt", "مواد قانون المرور.txt", "قانون المرور.txt"]
laws_data = {}

for filename in law_files:
    if os.path.exists(filename):
        for enc in ["utf-8", "cp1256"]:
            try:
                with open(filename, "r", encoding=enc) as f:
                    laws_data[filename] = f.read()
                break
            except:
                pass

query = st.text_input("🔍 اكتب المخالفة (مثال: الهاتف، حزام الأمن، السرعة):")

if query:
    st.markdown("### 📋 النتائج القانونية:")
    found = False
    keywords = query.split()
    
    for filename, text in laws_data.items():
        paragraphs = text.split('\n')
        for p in paragraphs:
            if p.strip() and all(kw.lower() in p.lower() for kw in keywords):
                found = True
                st.info(f"**المصدر:** {filename}\n\n{p}")
                
    if not found:
        st.warning("⚠️ لم يتم العثور على مطابقة دقيقة. جرب كلمات مختصرة.")
