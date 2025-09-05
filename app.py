import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Teknik Servis Dashboard", layout="wide")

# Stil: Başlık
st.markdown("<h1 style='text-align: center; color: navy;'>📊 Teknik Servis Dashboard</h1>", unsafe_allow_html=True)

# Excel'den veri oku
excel_path = "teknik_servis_raporu.xlsx"
df = pd.read_excel(excel_path, sheet_name=None)

# --- Genel Bilgiler ---
genel = df['Genel Bilgiler']
st.markdown("### 🚀 Genel Durum")
cols = st.columns(4)
cols[0].metric("📦 Bugün Gelen", genel.loc[0, 'Bugün Gelen'])
cols[1].metric("📅 Bu Hafta Gelen", genel.loc[0, 'Bu Hafta Gelen'])
cols[2].metric("🗓️ Bu Ay Gelen", genel.loc[0, 'Bu Ay Gelen'])
cols[3].metric("🕒 Bekleyen", genel.loc[0, 'Bekleyen'])

st.markdown("---")

# --- En Çok Arıza Gelen Ürünler ---
st.markdown("### 🔧 En Çok Arıza Gelen Ürünler")
top_ariza = df['En Çok Arıza Gelen']
bar = top_ariza.set_index('Ürün')
st.bar_chart(bar)

st.markdown("---")

# --- Aylık Trend ---
st.markdown("### 📈 Aylık Arıza Trendleri")
trend = df['Aylık Trend']
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(trend['Ay'], trend['Mavi Trend'], label='Mavi Trend', color='blue', linewidth=2)
ax.plot(trend['Ay'], trend['Turuncu Trend'], label='Turuncu Trend', color='orange', linewidth=2)
ax.set_xlabel("Ay")
ax.set_ylabel("Arıza Sayısı")
ax.legend()
st.pyplot(fig)

st.markdown("---")

# --- Bekleyenler ---
st.markdown("### 📋 Bekleyen İşlem Listesi")
bekleyen = df['Bekleyenler']
st.dataframe(bekleyen, use_container_width=True)

# Yenile Butonu
st.markdown("### 🔄 Sayfayı Yenile")
if st.button("Yenile"):
    st.rerun()
