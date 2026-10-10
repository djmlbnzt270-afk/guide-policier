import streamlit as st
import os

st.set_page_config(page_title="المساعد الذكي لقانون المرور الجزائري", page_icon="🚨", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚨 المساعد الذكي الميداني لقانون المرور الجزائري</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>النظام الرقمي للبحث في النصوص القانونية الرسمية.</p>", unsafe_allow_html=True)
st.markdown("---")

# دالة لقراءة الملف النصي المرفوع في المستودع
def load_laws():
    file_path = "laws.txt" # اسم ملف النصوص الذي سترفعه في GitHub
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "ملاحظة: يرجى رفع ملف 'laws.txt' إلى المستودع ليتم عرض النصوص."

laws_text = load_laws()

# حقل البحث في النصوص
query = st.text_input("🔍 ابحث عن أي مادة، مخالفة، أو كلمة مفتاحية في النصوص القانونية:", "")

if query:
    st.markdown("### 📋 نتائج البحث في النصوص الرسمية:")
    # تقسيم النص إلى أسطر أو فقرات للبحث عن الكلمة المفتاحية وعرضها
    paragraphs = laws_text.split("\n\n") # تقسيم النصوص حسب الفقرات
    found = False
    
    for p in paragraphs:
        if query.lower() in p.lower():
            st.markdown(f"""
            <div style="background-color: #f3f4f6; padding: 15px; border-radius: 5px; margin-bottom: 10px; border-right: 5px solid #1E3A8A;">
                {p}
            </div>
            """, unsafe_allow_html=True)
            found = True
            
    if not found:
        st.warning("⚠️ لم يتم العثور على مطابقة لهذه الكلمة في الملف النصي الحالي.")
else:
    st.info("💡 اكتب كلمة مفتاحية (مثل رقم المادة، سرعة، حزام، كحول...) للبحث الفوري داخل النصوص الرسمية.")
