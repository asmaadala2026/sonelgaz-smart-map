import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="نظام مراقبة شبكة الغاز", layout="wide")

st.markdown("""
    <style>
    .main-title {color: #005b96; text-align: right; font-family: sans-serif;}
    .alert-text {color: #ff8c00; text-align: right; direction: rtl;}
    .success-text {color: #2e8b57; text-align: right; direction: rtl;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">نظام المراقبة الذكي لشبكة الغاز (نموذج أولي - وهران)</h1>', unsafe_allow_html=True)

# بيانات وهمية للصمامات في بئر الجير
nodes = pd.DataFrame({
    "id": [1, 2],
    "name": ["صمام رئيسي 1 (Vanne)", "صمام رئيسي 2 (Vanne)"],
    "lat": [35.7285, 35.7275],
    "lon": [-0.5405, -0.5395]
})

m = folium.Map(location=[35.728, -0.540], zoom_start=16)

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    simulate_btn = st.button("🚨 محاكاة هبوط الضغط (تسرب)", type="primary", use_container_width=True)
    
    if simulate_btn:
        st.markdown('<h4 class="alert-text">⚠️ تنبيه: هبوط مفاجئ في الضغط!</h4>', unsafe_allow_html=True)
        st.error("تم تحديد التسرب. يرجى غلق الصمامين المحددين باللون الأزرق لعزل المنطقة.")
        pipe_color = "red"
    else:
        st.markdown('<h4 class="success-text">✅ ضغط الغاز مستقر في الشبكة.</h4>', unsafe_allow_html=True)
        pipe_color = "green"

with col2:
    folium.PolyLine(
        locations=[[35.7285, -0.5405], [35.7275, -0.5395]],
        color=pipe_color,
        weight=6,
        opacity=0.8
    ).add_to(m)

    for index, row in nodes.iterrows():
        folium.Marker(
            [row["lat"], row["lon"]],
            popup=row["name"],
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    st_folium(m, width=900, height=500)
