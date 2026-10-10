import streamlit as st
import os

# إعدادات صفحة الموقع
st.set_page_config(page_title="المساعد الذكي لقانون المرور الجزائري", page_icon="🚨", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚨 المساعد الذكي الميداني لقانون المرور الجزائري</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>النظام الرقمي للبحث الفوري في النصوص والتشريعات القانونية الرسمية.</p>", unsafe_allow_html=True)
st.markdown("---")

# قائمة بأسماء الملفات النصية المرفوعة في المستودع لديك
law_files = [
    "مرسوم تنفيذ رقم 04-381.txt", 
    "مواد قانون المرور.txt", 
    "قانون المرور.txt"
]

# دالة لقراءة كل النصوص المتاحة في الملفات
def load_all_laws():
    all_content = {}
    for filename in law_files:
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    all_content[filename] = f.read()
            except Exception as e:
                # محاولة قراءة بترميز مختلف في حال وجود مشكلة
                try:
                    with open(filename, "r", encoding="cp1256") as f:
                        all_content[filename] = f.read()
                except:
                    pass
    return all_content

laws_data = load_all_laws()

# حقل البحث في النصوص
query = st.text_input("🔍 ابحث عن أي مادة، مخالفة، جنحة، أو كلمة مفتاحية (مثال: سرعة، حزام، كحول، رخصة...):", "")

if query:
    st.markdown(f"### 📋 نتائج البحث عن: '{query}'")
    found_any = False
    
    for filename, text in laws_data.items():
        paragraphs = text.split("\n\n") # تقسيم النص إلى فقرات
        for p in paragraphs:
            if query.lower() in p.lower():
                found_any = True
                st.markdown(f"""
                <div style="background-color: #f3f4f6; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-right: 6px solid #1E3A8A; color: #111827;">
                    <small style="color: #6B7280; font-weight: bold;">📁 المصدر: {filename}</small>
                    <p style="margin-top: 8px; line-height: 1.6;">{p}</p>
                </div>
                """, unsafe_allow_html=True)
                
    if not found_any:
        st.warning("⚠️ لم يتم العثور على مطابقة لهذه الكلمة في ملفات المصادر الحالية. جرب كلمات مفتاحية أخرى.")
else:
    st.info("💡 اكتب كلمة مفتاحية في حقل البحث بالأعلى للبحث الآلي والمباشر داخل جميع مصادرك القانونية المرفوعة.")
