import streamlit as st
import os

st.set_page_config(page_title="المساعد الذكي لقانون المرور الجزائري", page_icon="🚨", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚨 المساعد الذكي الميداني لقانون المرور الجزائري</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>النظام الرقمي للبحث الفوري في التشريعات والنصوص القانونية الرسمية.</p>", unsafe_allow_html=True)
st.markdown("---")

law_files = [
    "مرسوم تنفيذ رقم 04-381.txt", 
    "مواد قانون المرور.txt", 
    "قانون المرور.txt"
]

def load_all_laws():
    all_content = {}
    for filename in law_files:
        if os.path.exists(filename):
            for encoding in ["utf-8", "cp1256", "iso-8859-6"]:
                try:
                    with open(filename, "r", encoding=encoding) as f:
                        all_content[filename] = f.read()
                        break
                except:
                    continue
    return all_content

laws_data = load_all_laws()

query = st.text_input("🔍 ابحث بكلمة مفتاحية (مثل: خوذة، سرعة، حزام، رخصة، كحول...):", "")

if query:
    st.markdown(f"### 📋 نتائج البحث عن: '{query}'")
    found_any = False
    keywords = query.split() # تقسيم الكلمات للبحث المرن
    
    for filename, text in laws_data.items():
        lines = text.split("\n") # البحث سطر بسطر أو فقرة بفقرة لضمان دقة أعلى
        for line in lines:
            if line.strip():
                # إذا كانت كل كلمات البحث أو بعضها موجودة في السطر
                if all(kw.lower() in line.lower() for kw in keywords):
                    found_any = True
                    st.markdown(f"""
                    <div style="background-color: #f3f4f6; padding: 12px; border-radius: 6px; margin-bottom: 10px; border-right: 5px solid #1E3A8A; color: #111827;">
                        <small style="color: #6B7280; font-weight: bold;">📁 المصدر: {filename}</small>
                        <p style="margin-top: 5px; line-height: 1.5;">{line}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
    if not found_any:
        st.warning("⚠️ لم يتم العثور على مطابقة دقيقة. جرب استخدام كلمة مفتاحية رئيسية واحدة مثل: خوذة، سرعة، حزام.")
else:
    st.info("💡 اكتب كلمة مفتاحية قصيرة في حقل البحث بالأعلى للبحث السريع داخل ملفاتك.")
