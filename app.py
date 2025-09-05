import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sayfa yapılandırması
st.set_page_config(page_title="Teknik Servis Paneli", layout="wide")

# Özel CSS (tasarım için)
st.markdown("""
    <style>
        .main {
            background-color: #F5F7FA;
        }
        .card-container {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            flex: 1;
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            text-align: center;
        }
        .card h1 {
            font-size: 32px;
            color: #34495E;
            margin-bottom: 10px;
        }
        .card p {
            font-size: 15px;
            color: #7F8C8D;
        }
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #2C3E50;
            margin-top: 40px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Excel'den veri oku
excel_path = "teknik_servis_raporu.xlsx"
df = pd.read_excel(excel_path, sheet_name=None)

# Başlık
st.markdown("<h2 style='text-align: center; color:#2C3E50;'>📊 Teknik Servis Dashboard</h2><br>", unsafe_allow_html=True)

# Genel Bilgiler
genel = df['Genel Bilgiler'].iloc[0]

# 🔹 Kartlar
st.markdown("<div class='card-container'>", unsafe_allow_html=True)

st.markdown(f"""
    <div class='card'>
        <h1>{genel['Bugün Gelen']}</h1>
        <p>Bugün Gelen</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class='card'>
        <h1>{genel['Bu Hafta Gelen']}</h1>
        <p>Bu Hafta Gelen</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class='card'>
        <h1>{genel['Bu Ay Gelen']}</h1>
        <p>Bu Ay Gelen</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class='card'>
        <h1>{genel['Bekleyen']}</h1>
        <p>Bekleyen</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 🔹 En Çok Arıza Gelen Ürünler
st.markdown("<div class='section-title'>🔧 En Çok Arıza Gelen Ürünler</div>", unsafe_allow_html=True)
top_ariza = df['En Çok Arıza Gelen']
st.bar_chart(top_ariza.set_index('Ürün')['Arıza Sayısı'])

# 🔹 Aylık Trend Grafiği
st.markdown("<div class='section-title'>📈 Aylık Arıza Trendleri</div>", unsafe_allow_html=True)
trend = df['Aylık Trend']
fig, ax = plt.subplots()
ax.plot(trend['Ay'], trend['Mavi Trend'], label='Mavi', color='royalblue', linewidth=2)
ax.plot(trend['Ay'], trend['Turuncu Trend'], label='Turuncu', color='darkorange', linewidth=2)
ax.set_xlabel("Ay")
ax.set_ylabel("Arıza")
ax.legend()
st.pyplot(fig)

# 🔹 Bekleyenler Tablosu
st.markdown("<div class='section-title'>📋 Bekleyen Teknik Servisler</div>", unsafe_allow_html=True)
bekleyen = df['Bekleyenler']
st.dataframe(bekleyen, use_container_width=True)

# Yenile butonu
st.markdown(" ")
if st.button("🔄 Sayfayı Yenile"):
    st.rerun()
