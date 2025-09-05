import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Teknik Servis Raporu", layout="wide")

# ---- CSS ----
st.markdown("""
    <style>
    h1 {font-size:26px !important;}
    h2 {font-size:20px !important;}
    h3 {font-size:16px !important;}
    .stMetric label {font-size:13px !important;}
    .stMetric div {font-size:15px !important;}
    table, th, td {font-size:12px !important;}
    .card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- BAŞLIK ----
col_logo, col_title, col_filter = st.columns([1,4,2])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png", width=80)
with col_title:
    st.markdown("<h1 style='text-align: center;'>🔧 Teknik Servis Raporu</h1>", unsafe_allow_html=True)
with col_filter:
    date_filter = st.selectbox("📅 Tarih Filtresi", ["Bugün", "Bu Hafta", "Bu Ay", "Tümü"])

st.markdown("---")

# ---- ÖRNEK METRİK VERİLER ----
if date_filter == "Bugün":
    bugun, hafta, ay, bekleyen = 8, 8, 8, 3
elif date_filter == "Bu Hafta":
    bugun, hafta, ay, bekleyen = 8, 52, 52, 12
elif date_filter == "Bu Ay":
    bugun, hafta, ay, bekleyen = 8, 52, 180, 15
else:
    bugun, hafta, ay, bekleyen = 500, 1200, 5400, 60

# ---- 1. ARIZALI GELEN ÜRÜNLER ----
st.markdown("<div class='card'><h2>📌 Arızalı Gelen Ürünler</h2>", unsafe_allow_html=True)

st.markdown("**🛒 E-Ticaret**")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**İade**")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bugün", bugun)
    c2.metric("Hafta", hafta)
    c3.metric("Ay", ay)
    c4.metric("Bekleyen", bekleyen)
with col2:
    st.markdown("**Arıza**")
    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Bugün", 3)
    c6.metric("Hafta", 12)
    c7.metric("Ay", 40)
    c8.metric("Bekleyen", 4)

st.markdown("**🏬 Mağaza**")
shops = {
    "Meydan": [2, 10, 35, 3],
    "Metropol": [1, 8, 28, 2],
    "Optimum": [3, 15, 42, 5],
    "Forum": [2, 12, 30, 4],
    "Piazza": [1, 7, 20, 1]
}
for shop, values in shops.items():
    st.markdown(f"**{shop}**")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Bugün", values[0])
    col2.metric("Hafta", values[1])
    col3.metric("Ay", values[2])
    col4.metric("Bekleyen", values[3])

st.markdown("</div>", unsafe_allow_html=True)

# ---- 2. EN ÇOK ARIZA GELEN ÜRÜNLER ----
st.markdown("<div class='card'><h2>🔧 En Çok Arıza Gelen İlk 5 Ürün</h2>", unsafe_allow_html=True)
faults = pd.DataFrame({
    "Ürün": ["Ürün A","Ürün B","Ürün C","Ürün D","Ürün E"],
    "Adet": [25,18,15,10,8]
})
fig1 = px.bar(faults, x="Adet", y="Ürün", orientation="h", text="Adet")
fig1.update_traces(marker_color="royalblue", textposition="outside")
fig1.update_layout(height=260, margin=dict(l=40, r=20, t=30, b=30))
st.plotly_chart(fig1, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---- 3. RED / ONAY ORANI ----
st.markdown("<div class='card'><h2>📊 Platform Onay / Red Oranı</h2>", unsafe_allow_html=True)
approval = pd.DataFrame({
    "Durum": ["Onaylanan", "Red Edilen"],
    "Adet": [85, 15]
})
fig2 = px.pie(approval, values="Adet", names="Durum", hole=0.4,
              color_discrete_sequence=["green","red"])
fig2.update_layout(height=260, margin=dict(l=20, r=20, t=30, b=30))
st.plotly_chart(fig2, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---- 4. MALİYET ANALİZİ ----
st.markdown("<div class='card'><h2>💰 Maliyet Analizi</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("Toplam Maliyet (₺)", "152.000")
col2.metric("İade Kaynaklı (₺)", "45.000")
col3.metric("Arıza Kaynaklı (₺)", "107.000")
st.markdown("</div>", unsafe_allow_html=True)

# ---- 5. BEKLEYENLER TABLO ----
st.markdown("<div class='card'><h2>📋 Bekleyenler Listesi</h2>", unsafe_allow_html=True)
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
st.dataframe(df_table, use_container_width=True, height=220)
st.markdown("</div>", unsafe_allow_html=True)

# ---- 6. YEDEK PARÇA BEKLEYEN ----
st.markdown("<div class='card'><h2>⚙️ Yedek Parça Bekleyen</h2>", unsafe_allow_html=True)

# küçük özet metrikler
c1, c2, c3 = st.columns(3)
c1.metric("Toplam Parça", 45)
c2.metric("Ortalama Bekleme Süresi (gün)", 6)
c3.metric("Acil Parçalar", 12)

# tablo detay
data_parts = {
    "Parça Kodu": ["P-1001","P-1002","P-1003","P-1004"],
    "Parça Adı": ["Motor Ünitesi","Su Pompası","Kontrol Kartı","LED Panel"],
    "Bekleyen Adet": [5, 12, 8, 20],
    "Bekleme Süresi (gün)": [2, 5, 7, 10],
    "Durum": ["Acil","Normal","Acil","Normal"]
}
df_parts = pd.DataFrame(data_parts)
st.dataframe(df_parts, use_container_width=True, height=220)

st.markdown("</div>", unsafe_allow_html=True)
# ---- 7. HURDA BEKLEYEN ÜRÜNLER ----
st.markdown("<div class='card'><h2>🗑️ Hurda Bekleyen Ürünler</h2>", unsafe_allow_html=True)

# özet metrikler
h1, h2 = st.columns(2)
h1.metric("Toplam Hurda Bekleyen", 18)
h2.metric("Acil Hurda İşlemi Gereken", 5)

# tablo detay
data_scrap = {
    "Ürün Kodu": ["H-2001","H-2002","H-2003","H-2004"],
    "Ürün Adı": ["Akıllı Fırın","Robot Süpürge","Kamera Ünitesi","LED TV Panel"],
    "Bekleyen Adet": [4, 7, 3, 4],
    "Durum": ["Normal","Acil","Normal","Normal"]
}
df_scrap = pd.DataFrame(data_scrap)
st.dataframe(df_scrap, use_container_width=True, height=220)

st.markdown("</div>", unsafe_allow_html=True)
