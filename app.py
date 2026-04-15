import streamlit as st
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="吉米隨機選號器", page_icon="🎲", layout="centered")

st.title("🎰 吉米隨機選號器")
st.write("朋友你好！點擊按鈕產生今日的幸運號碼。")

# 使用分頁
tab1, tab2, tab3 = st.tabs(["今彩 539", "大樂透 649", "威力彩"])

# --- 今彩 539 ---
with tab1:
    st.header("今彩 539")
    if st.button("🔮 產生 539 號碼", key="539"):
        nums = sorted(random.sample(range(1, 40), 5))
        st.success(f"號碼：{' , '.join([f'{n:02d}' for n in nums])}")
        st.balloons()

# --- 大樂透 649 ---
with tab2:
    st.header("大樂透 649")
    if st.button("🔮 產生大樂透號碼", key="649"):
        nums = sorted(random.sample(range(1, 50), 6))
        st.success(f"號碼：{' , '.join([f'{n:02d}' for n in nums])}")
        st.balloons()

# --- 威力彩 ---
with tab3:
    st.header("威力彩")
    if st.button("🔮 產生威力彩號碼", key="power"):
        z1 = sorted(random.sample(range(1, 39), 6))
        z2 = random.randint(1, 8)
        st.subheader("第一區")
        st.success(f"{' , '.join([f'{n:02d}' for n in z1])}")
        st.subheader("第二區")
        st.warning(f"{z2:02d}")
        st.balloons()

st.divider()
st.caption("Designed by Gemini吉米 | 僅供娛樂，祝您中獎！")