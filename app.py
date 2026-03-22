import streamlit as st
import os

# --- 1. 網頁基礎設定 ---
st.set_page_config(page_title="Eva醫師 | 植牙IQ大挑戰", page_icon="🦷")

# --- 2. 定義檔案名稱 (請務必與您左側檔案列表完全一致) ---
LOGO_FILENAME = "Dr. Eva Q版頭像.jpg"
BGM_FILENAME = "重拾笑容的時光bgm.mp3"

# --- 3. 音樂播放邏輯 ---
if os.path.exists(BGM_FILENAME):
    with open(BGM_FILENAME, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
else:
    st.sidebar.error("找不到音樂檔，請檢查檔名")

# --- 4. 遊戲狀態控制 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- 5. 遊戲關卡流程 ---

# [首頁]
if st.session_state.step == 0:
    if os.path.exists(LOGO_FILENAME):
        st.image(LOGO_FILENAME, width=150)
    st.title("🦷 植牙 IQ 大挑戰")
    st.write("### 歡迎來到 Eva 醫師的微創診間")
    st.write("只需 5 題，帶您深入淺出認識現代『力學導向』的植牙技術。")
    if st.button("開始挑戰"):
        st.session_state.step = 1
        st.rerun()

# [Q1]
elif st.session_state.step == 1:
    st.subheader("Q1: 聽說植牙要鑽很多次洞、傷口很大，是真的嗎？")
    q1 = st.radio("您的答案：", ["是的，分次鑽孔很正常", "不一定，『一鑽到位』技術更微創"])
    if st.button("下一題"):
        if "一鑽到位" in q1: st.session_state.score += 1
        st.session_state.step = 2
        st.rerun()

# [Q2]
elif st.session_state.step == 2:
    st.subheader("Q2: 決定植牙位置最關鍵的參考標準是？")
    q2 = st.radio("您的答案：", ["數位導引板的數據", "參考患者自己的『對咬牙』力學"])
    if st.button("下一題"):
        if "對咬牙" in q2: st.session_state.score += 1
        st.session_state.step = 3
        st.rerun()

# [Q3]
elif st.session_state.step == 3:
    st.subheader("Q3: 有糖尿病或高血壓的患者，適合植牙嗎？")
    q3 = st.radio("您的答案：", ["完全不適合", "控制穩定下，微創手術負擔更小"])
    if st.button("下一題"):
        if "控制穩定" in q3: st.session_state.score += 1
        st.session_state.step = 4
        st.rerun()

# [Q4]
elif st.session_state.step == 4:
    st.subheader("Q4: 為什麼『一鑽植牙』能縮短療程時間？")
    q4 = st.radio("您的答案：", ["因為減少了不必要的步驟", "因為拔牙、植牙、補骨可一次完成"])
    if st.button("最後一題"):
        if "一次完成" in q4: st.session_state.score += 1
        st.session_state.step = 5
        st.rerun()

# [Q5]
elif st.session_state.step == 5:
    st.subheader("Q5: 植牙完後就永遠不會壞，不需要特別保養？")
    q5 = st.radio("您的答案：", ["對，假牙不會蛀牙", "錯，仍需預防植體周圍炎"])
    if st.button("看結果"):
        if "錯" in q5: st.session_state.score += 1
        st.session_state.step = 6
        st.rerun()

# [結果頁面]
elif st.session_state.step == 6:
    st.balloons()
    st.title("🎉 挑戰完成！")
    st.write(f"### 您的植牙 IQ 得分： {st.session_state.score} / 5")
    st.write("---")
    st.info("💡 **Eva 醫師的專業叮嚀：** 好的植牙不只看技術，更要看是否符合您的力學結構。")
    st.link_button("👉 預約專業力學評估 (Line)", "https://line.me/R/ti/p/@your_id")
    if st.button("重新挑戰"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()