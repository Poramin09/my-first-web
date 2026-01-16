import streamlit as st
import base64

#page---
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

#ฟังก์ชันเปลี่ยนหน้า
def change_page(page_name):
    st.session_state.page = page_name

#ตั้งค่าหน้าเว็บ
st.set_page_config(layout="wide", page_title="พรรคสดุ")

#ฟังก์ชันดึงรูปภาพ
def get_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

#ดึงรูป
bg_img = get_base64("home.jpg")
banner_img = get_base64("poster.png")

#ส่วนตกแต่ง
st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(255,255,255,0.4), rgba(255,255,255,0.4)), 
                      url("data:image/jpeg;base64,{bg_img}");
    background-size: cover;
    background-attachment: fixed;
}}
.main-banner {{
    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                      url("data:image/png;base64,{banner_img}");
    background-size: cover;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    border-radius: 20px;
}}
.nav-box {{
    background-color: rgba(0,0,0,0.8);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

#Logic(home)
if st.session_state.page == 'home':
    st.markdown('<div class="main-banner"><h2.5>พรรค สดุมาส่งแล้วคร้าฟ📦✨</h2.5></div>', unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    col1, col2 = st.columns(2)

    with col1:
        #สร้างกล่องข้อความของ คอลั่มแรก
        st.markdown('<div class="nav-box"><h3>📜 นโยบายพรรค</h3></div>', unsafe_allow_html=True)
        if st.button("คลิกอ่านนโยบาย", use_container_width=True):
            change_page('policy')
            st.rerun()
    with col2:
        st.markdown('<div class="nav-box"><h3>👥 สมาชิกพรรค</h3></div>',unsafe_allow_html=True)
        if st.button("สมาชิกพรรค", use_container_width=True):
            change_page('member')
            st.rerun()
elif st.session_state.page == 'policy':
    st.header("📖นโยบายพรรคของเรา มีดังนี้")
    st.write("📖การปรับปรุงห้องสมุด")
    st.write("🏆รวมกิจกรรม")
    st.write("🎧Podcast")
    st.write("🗃️ห้องว่าง")
    st.write("Website ของหาย")
    st.write("จิตแพทย์")
    st.write("ซ้อมประสบภัย")
    st.write("เพื่อนติวเพื่อน")
    st.write("รุ่นพี่แนะแนว/กิจกรรมค่ายต่างๆ")
    st.write("สานต่อนโยบายสภารุ่นก่อน")
    if st.button("⬅️ กลับ"):
        st.session_state.page = 'home'
        st.rerun()
elif st.session_state.page == 'member':
    st.header("👥รายชื่อสมาชิก")
    st.header("👑ประธานสภา")
    st.write("นางสาว A")
    st.header("👤สมาชิก")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    st.write("B")
    if st.button("⬅️ กลับ"):
        st.session_state.page = 'home'

        st.rerun()



