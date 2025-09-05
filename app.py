import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Teknik Servis Raporu", layout="wide")

# ---- ÜST BANNER ----
st.markdown(
    """
    <h1 style='text-align: center; color: black;'>
        🔧 TEKNİK SERVİS RAPORU
    </h1>
    """,
    unsafe_allow_html=True
)

# ---- METRİK KARTLAR ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Bugün Gelen", "8")
with col2:
    st.metric("Bu Hafta Gelen", "52")
with col3:
    st.metric("Bu Ay Gelen", "180")
with col4:
    st.metric("Bekleyen", "12")

st.markdown("---")

# ---- AYLIK TREND ----
st.subheader("📈 Aylık Trend")
months = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"]
data = {
    "Ay": months,
    "Ürün A": [10,20,25,21,23,30,22,26,21,25,24,32],
    "Ürün B": [2,5,7,6,8,12,7,5,6,7,8,11]
}
df = pd.DataFrame(data)

fig = px.line(df, x="Ay", y=["Ürün A","Ürün B"], markers=True)
st.plotly_chart(fig, use_container_width=True)

# ---- EN ÇOK ARIZA GELEN ----
st.subheader("🔧 En Çok Arıza Gelen Ürünler")
faults = pd.DataFrame({
    "Ürün": ["Ürün A","Ürün B","Ürün C","Ürün D","Ürün E"],
    "Adet": [25,18,15,10,8]
})
fig2 = px.bar(faults, x="Adet", y="Ürün", orientation="h", text="Adet")
fig2.update_traces(marker_color="royalblue", textposition="outside")
st.plotly_chart(fig2, use_container_width=True)

# ---- TABLO ----
st.subheader("📋 Bekleyenler")
data_table = {
    "Geliş Tarihi": ["01.09.2025","03.09.2025","05.09.2025"],
    "Ad": ["Ahmet","Elif","Mehmet"],
    "Soyad": ["Yılmaz","Demir","Kaya"],
    "Ürün Kodu": ["X7533","X8550","X7015"],
    "Ürün Adı": ["Akıllı Mama Kabı","Akıllı Su Pınarı","Panjur Motoru"],
    "Adet": [18,15,10],
    "Ay": [5,2,8],
    "Yapılan İşlem": ["Onarım Bekliyor","İade Bekliyor","Değişim Bekliyor"]
}
df_table = pd.DataFrame(data_table)
st.dataframe(df_table, use_container_width=True)
