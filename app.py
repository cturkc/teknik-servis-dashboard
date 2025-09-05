import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Teknik Servis Dashboard")

# Excel dosyasını oku
excel_path = "teknik_servis_raporu.xlsx"
df = pd.read_excel(excel_path, sheet_name=None)  # Tüm sayfalar

# Genel Bilgiler (Örnek: 'Genel Bilgiler' sayfası)
genel = df['Genel Bilgiler']
st.subheader("Genel Bilgiler")
cols = st.columns(4)
cols[0].metric("Bugün Gelen", genel.loc[0, 'Bugün Gelen'])
cols[1].metric("Bu Hafta Gelen", genel.loc[0, 'Bu Hafta Gelen'])
cols[2].metric("Bu Ay Gelen", genel.loc[0, 'Bu Ay Gelen'])
cols[3].metric("Bekleyen", genel.loc[0, 'Bekleyen'])

# En Çok Arıza Gelen Ürünler
st.subheader("En Çok Arıza Gelen Ürünler")
top_ariza = df['En Çok Arıza Gelen']
st.bar_chart(top_ariza.set_index('Ürün')['Arıza Sayısı'])

# Aylık Trend Grafiği
st.subheader("Aylık Trend")
trend = df['Aylık Trend']
fig, ax = plt.subplots()
ax.plot(trend['Ay'], trend['Mavi Trend'], label='Mavi Trend', color='blue')
ax.plot(trend['Ay'], trend['Turuncu Trend'], label='Turuncu Trend', color='orange')
ax.set_xlabel("Ay")
ax.set_ylabel("Adet")
ax.legend()
st.pyplot(fig)

# Bekleyenler Tablosu
st.subheader("Bekleyenler")
bekleyen = df['Bekleyenler']
st.dataframe(bekleyen)

# Yenile butonu
if st.button("Yenile"):
    st.rerun()

