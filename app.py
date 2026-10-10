import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="المساعد الذكي لقانون المرور الجزائري", page_icon="🚨", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚨 المساعد الذكي الميداني لقانون المرور الجزائري (Gemini)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>النظام الذكي لتحليل المخالفات والجنح بناءً على النصوص القانونية الرسمية الخاصة بك.</p>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.markdown("### ⚙️ إعدادات الذكاء الاصطناعي")
api_key = st.sidebar.text_input("🔑 أضف مفتاح Gemini API Key:", type="password")
st.sidebar.markdown("[الحصول على مفتاح مجاني من Google AI Studio](https://aistudio.google.com/)")

law_files = [
    "مرسوم تنفيذ رقم 04-381.txt", 
    "مواد قانون المرور.txt", 
    "قانون المرور.txt"
]

combined_laws = ""
for filename in law_files:
    if os.path.exists(filename):
        for encoding in ["utf-8", "cp1256", "iso-8859-6"]:
            try:
                with open(filename, "r", encoding=encoding) as f:
                    combined_laws += f"\n\n--- [مصدر قانوني: {filename}] ---\n" + f.read()
                break
            except:
                continue

query = st.text_area("💬 صف الحالة أو المخالفة الميدانية (مثال: السائق يتجاوز السرعة ولا يربط حزام الأمن ويستعمل الهاتف):", "")

if query:
    if not api_key:
        st.warning("⚠️ يرجى إدخال مفتاح Gemini API Key في الشريط الجانبي من اليسار لتفعيل التحليل الذكي.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # استخدام النموذج الاحترافي الذي أوصت به رسالة الخطأ من جوجل
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            أنت مساعد قانوني محترف ومحقق ميداني متخصص في قانون المرور الجزائري والمرسوم التنفيذي 04-381.
            بناءً على النصوص القانونية والمصادر التالية المرفوعة حصرياً من المستخدم:
            {combined_laws}
            
            قم بتحليل الحالة الميدانية أو المخالفة التي أدخلها المستخدم، وأعطني تقريراً منظماً واحترافياً يحتوي على العناصر التالية بدقة:
            1. التصنيف (مخالفة من أي درجة / جنحة)
            2. المادة القانونية المطبقة
            3. محتوى المخالفة
            4. الغرامة المالية المقررة
            5. العقوبات التكميلية
            6. الإجراءات الميدانية الفورية
            7. ملاحظات وتدابير إضافية
            
            حالة المخالفة المراد تحليلها: {query}
            """
            
            with st.spinner("جاري التحليل الذكي ومراجعة مصادرك القانونية..."):
                response = model.generate_content(prompt)
                st.markdown("### 📊 تقرير المعاينة القانونية الذكي:")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بنموذج الذكاء الاصطناعي: {e}")
