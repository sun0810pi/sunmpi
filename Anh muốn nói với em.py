import streamlit as st

st.set_page_config(layout="centered")

# ========= STATE =========
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False


# ========= CLICK HANDLER =========
def open_popup():
    st.session_state.show_popup = True


# ========= CSS / UI =========
st.markdown("""
<style>

/* ---------- BACKGROUND ---------- */

body {
    background: linear-gradient(270deg,#000000,#1a001a,#000000);
    background-size: 400% 400%;
    animation: bgmove 15s ease infinite;
}

@keyframes bgmove {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}


/* ---------- FLOATING HEARTS ---------- */

.hearts span {
    position: fixed;
    bottom: -50px;
    font-size: 18px;
    animation: floatUp linear infinite;
    opacity: 0.6;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) scale(1);
        opacity:0;
    }
    20% {opacity:0.7;}
    100% {
        transform: translateY(-110vh) scale(1.4);
        opacity:0;
    }
}

/* ---------- MAIN HEART ---------- */

.heart {
    font-size:120px;
    text-align:center;
    cursor:pointer;
    animation: beat 1.2s infinite ease-in-out;
    filter: drop-shadow(0 0 20px rgba(255,0,90,0.9));
    transition: transform .2s ease;
}

.heart:hover {
    transform: scale(1.2);
}

@keyframes beat {
    0% {transform:scale(1);}
    25% {transform:scale(1.25);}
    40% {transform:scale(1);}
    60% {transform:scale(1.18);}
    100% {transform:scale(1);}
}

/* ---------- EXPLOSION ---------- */

.explosion span{
    position:absolute;
    font-size:24px;
    animation: explode .8s forwards;
}

@keyframes explode{
    from{
        transform:translate(0,0);
        opacity:1;
    }
    to{
        transform:translate(var(--x), var(--y));
        opacity:0;
    }
}

/* ---------- SUBTEXT ---------- */

.sub {
    text-align:center;
    font-size:18px;
    color:#ff9ecf;
    margin-top:-10px;
    margin-bottom:20px;
}


/* ---------- POPUP ---------- */

.popup {
    position:fixed;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    background:rgba(0,0,0,0.75);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    box-shadow:0 0 40px rgba(255,0,120,0.7);
    animation:fadeIn .4s ease;
    text-align:center;
    z-index:999;
}

@keyframes fadeIn{
    from{opacity:0; transform:translate(-50%,-30%);}
    to{opacity:1; transform:translate(-50%,-50%);}
}

.title {
    font-size:40px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)


# ========= FLOATING HEART HTML =========

floating_html = "<div class='hearts'>"
for i in range(20):
    floating_html += f"<span style='left:{i*5}%; animation-duration:{6+i%5}s'>❤️</span>"
floating_html += "</div>"

st.markdown(floating_html, unsafe_allow_html=True)


# ========= TITLE =========
st.markdown("<div class='title'>Anh muốn nói với em là...</div>", unsafe_allow_html=True)

# ========= HEART BUTTON =========
if st.button("❤️", on_click=open_popup):
    pass

st.markdown("<div class='sub'>Bấm vào trái tim hoặc nút phía trên ❤️</div>", unsafe_allow_html=True)


# ========= POPUP =========
if st.session_state.show_popup:

    explosion = "<div class='explosion'>"
    coords = [
        ("100px","0"),("-100px","0"),
        ("0","100px"),("0","-100px"),
        ("70px","70px"),("-70px","70px"),
        ("70px","-70px"),("-70px","-70px"),
    ]
    for x,y in coords:
        explosion += f"<span style='--x:{x}; --y:{y}'>❤️</span>"
    explosion += "</div>"

    st.markdown(explosion, unsafe_allow_html=True)

    st.markdown("""
    <div class="popup">
        <h2 style="color:#ffb6e6">
        Anh thích em nhiều hơn em nghĩ đó ❤️
        </h2>
        <p style="color:white">
        (đây chỉ là demo — bạn sửa text tùy ý 😏)
        </p>
    </div>
    """, unsafe_allow_html=True)
