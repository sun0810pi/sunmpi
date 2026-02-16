import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Anh muốn nói với em...",
    page_icon="💗",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.big-button button {
    background-color:#FFC0CB;
    color:black;
    font-size:28px;
    border-radius:18px;
    padding:18px 28px;
}

.popup {
    background:#FFC0CB;
    padding:18px;
    margin:8px;
    border-radius:12px;
    text-align:center;
    font-size:20px;
    animation: fade 0.4s ease-in-out;
}

@keyframes fade {
    from {opacity:0; transform:scale(0.8);}
    to {opacity:1; transform:scale(1);}
}
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "count" not in st.session_state:
    st.session_state.count = 0

# ---------- UI ----------
st.title("💗 Tmai needs the remedy.")

st.markdown('<div class="big-button">', unsafe_allow_html=True)
clicked = st.button("Muốn nói là...")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ACTION ----------
if clicked:
    st.session_state.count += 20

# ---------- POPUPS ----------
for i in range(st.session_state.count):
    message = random.choice([
        "Anh nhớ em lắm!!",
        "Anh yêu em 💗",
        "Đừng buồn nữa nhé",
        "Anh luôn ở đây",
        "Smile đi nào ✨"
    ])

    st.markdown(
        f'<div class="popup">{message}</div>',
        unsafe_allow_html=True
    )
    time.sleep(0.03)
