import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sayfa ayarları
st.set_page_config(page_title="Teknik Servis Paneli", layout="wide")

# CSS ile özel kart stilleri
st.markdown("""
    <style>
        .card {
            background-color: #F0F2F6;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #3E64FF;
            font-size: 30px;
        }
        .card p {
            font-size: 16px;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

# Excel dosyasını oku
excel_path = "teknik_servis_raporu.xlsx"
df = pd.read_excel(excel_path, sheet_name=None)

# Genel Bilgiler
genel = df["Genel Bilgiler"].iloc[0]

st.markdown("<h1 style='text-align: center;'>📊 Teknik Servis Dashboard</h1><br>", unsafe_allow_html=True)

# Kart görünümü
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="card">
            <h2>{genel['Bugün Gelen']}</h2>
            <p>Bugün Gelen</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="card">
            <h2>{genel['Bu Hafta Gelen']}</h2>
            <p>Bu Hafta Gelen</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card">
            <h2>{genel['Bu Ay Gelen']}</h2>
            <p>Bu Ay Gelen</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="card">
            <h2>{genel['Bekleyen']}</h2>
            <p>Bekleyen</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Grafik: En Çok Arıza Gelen Ürünler
st.markdown("### 🔧 En Çok Arıza Gelen Ürünler")
top_ariza = df['En Çok Arıza Gelen']
st.bar_chart(top_ariza.set_index("Ürün")["Arıza Sayısı"])

st.markdown("---")

# Trend Grafiği
st.markdown("### 📈 Aylık Arıza Trendleri")
trend = df["Aylık Trend"]
fig, ax = plt.subplots()
ax.plot(trend["Ay"], trend["Mavi Trend"], label="Mavi", color="blue", linewidth=2)
ax.plot(trend["Ay"], trend["Turuncu Trend"], label="Turuncu", color="orange", linewidth=2)
ax.set_xlabel("Ay")
ax.set_ylabel("Adet")
ax.legend()
st.pyplot(fig)

st.markdown("---")

# Bekleyen Liste
st.markdown("### 📋 Bekleyenler")
bekleyen = df["Bekleyenler"]
st.dataframe(bekleyen, use_container_width=True)

# Yenile Butonu
if st.button("🔄 Sayfayı Yenile"):
    st.rerun()
