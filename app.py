import streamlit as st
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="吉米隨機選號器", page_icon="🎲", layout="centered")

# 使用 CSS 加大字體與調整版面
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #d32f2f;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 吉米隨機選號器")
st.write("朋友你好！請先在滑桿選擇想產生的組數，再點擊按鈕。")

# --- 全域滑桿：選擇組數 ---
num_groups = st.slider("想要產生幾組號碼？", 1, 10, 5)

# 使用分頁
tab1, tab2, tab3 = st.tabs(["今彩 539", "大樂透 649", "威力彩"])

# --- 今彩 539 ---
with tab1:
    st.header("今彩 539")
    if st.button("🔮 產生 539 號碼", key="539"):
        st.balloons()
        for i in range(num_groups):
            nums = sorted(random.sample(range(1, 40), 5))
            formatted_nums = ' , '.join([f'{n:02d}' for n in nums])
            st.markdown(f"第 {i+1} 組：<span class='big-font'>{formatted_nums}</span>", unsafe_allow_html=True)

# --- 大樂透 649 ---
with tab2:
    st.header("大樂透 649")
    if st.button("🔮 產生大樂透號碼", key="649"):
        st.balloons()
        for i in range(num_groups):
            nums = sorted(random.sample(range(1, 50), 6))
            formatted_nums = ' , '.join([f'{n:02d}' for n in nums])
            st.markdown(f"第 {i+1} 組：<span class='big-font'>{formatted_nums}</span>", unsafe_allow_html=True)

# --- 威力彩 ---
with tab3:
    st.header("威力彩")
    if st.button("🔮 產生威力彩號碼", key="power"):
        st.balloons()
        for i in range(num_groups):
            z1 = sorted(random.sample(range(1, 39), 6))
            z2 = random.randint(1, 8)
            formatted_z1 = ' , '.join([f'{n:02d}' for n in z1])
            st.write(f"--- 第 {i+1} 組 ---")
            st.markdown(f"第一區：<span class='big-font'>{formatted_z1}</span>", unsafe_allow_html=True)
            st.markdown(f"第二區：<span style='font-size:25px; color:#ff9800; font-weight:bold;'>{z2:02d}</span>", unsafe_allow_html=True)

st.divider()
st.caption("Designed by Gemini吉米 | 祝您幸運中大獎！🎈")