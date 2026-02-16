import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ---------- LANDING UI ----------
st.markdown("""
<style>

.main-title{
    font-size:48px;
    font-weight:700;
    text-align:center;
    background: linear-gradient(90deg,#ff4da6,#ff99cc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-top:120px;
}

.center-btn button{
    font-size:26px;
    background: linear-gradient(135deg,#ff7eb3,#ff4da6);
    color:white;
    border-radius:18px;
    padding:18px 36px;
    border:none;
    box-shadow:0 8px 18px rgba(0,0,0,0.2);
    transition:0.25s;
}

.center-btn button:hover{
    transform:scale(1.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Anh muốn nói với em là...</div>', unsafe_allow_html=True)

st.markdown('<div class="center-btn">', unsafe_allow_html=True)
clicked = st.button("Bấm vào đây 💗")
st.markdown('</div>', unsafe_allow_html=True)


# ---------- POPUP FLOOD ----------
if clicked:

    html = """
    <html>
    <body style="margin:0; overflow:hidden; background:linear-gradient(135deg,#fff0f6,#ffe6f2);">

    <script>

    let msgs = [
        "Anh nhớ em 💗",
        "Anh yêu em",
        "Đừng buồn nữa nhé",
        "Quay lại đi mà 🥺",
        "Anh luôn ở đây",
        "Smile đi ✨",
        "You mean a lot to me"
    ];

    function popup(){
        let d = document.createElement("div");

        let x = Math.random()*window.innerWidth;
        let y = Math.random()*window.innerHeight;

        d.innerHTML = msgs[Math.floor(Math.random()*msgs.length)];

        d.style.position="absolute";
        d.style.left=x+"px";
        d.style.top=y+"px";

        d.style.padding="14px 18px";
        d.style.fontSize="18px";
        d.style.fontWeight="600";
        d.style.borderRadius="14px";

        /* glass style */
        d.style.background="rgba(255,192,203,0.85)";
        d.style.backdropFilter="blur(6px)";
        d.style.boxShadow="0 10px 20px rgba(0,0,0,0.2)";

        d.style.animation="pop 0.35s ease";

        document.body.appendChild(d);
    }

    let style = document.createElement("style");
    style.innerHTML=`
        @keyframes pop{
            from{transform:scale(0);opacity:0}
            to{transform:scale(1);opacity:1}
        }
    `;
    document.head.appendChild(style);

    let count = 0;

    let flood = setInterval(()=>{
        popup();
        count++;

        if(count > 140){
            clearInterval(flood);
        }
    }, 35);

    </script>
    </body>
    </html>
    """

    components.html(html, height=900)
