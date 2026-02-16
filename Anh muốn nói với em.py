import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ---------- BACKGROUND ----------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top,
                #fff0f6,
                #ffe6f2,
                #ffd6ec);
}

/* center layout */
.wrap{
    height:85vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

/* title */
.title{
    font-size:58px;
    font-weight:800;
    background: linear-gradient(90deg,#ff4da6,#ff99cc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:25px;
}

/* heart button */
.heartbtn{
    font-size:70px;
    cursor:pointer;
    animation:beat 1s infinite;
    user-select:none;
}

@keyframes beat{
    0%{transform:scale(1)}
    50%{transform:scale(1.25)}
    100%{transform:scale(1)}
}

/* sub text */
.sub{
    font-size:20px;
    margin-top:12px;
    margin-bottom:30px;
    color:#444;
}

/* streamlit button style */
div.stButton > button {
    font-size:22px;
    padding:14px 36px;
    border-radius:16px;
    background: linear-gradient(135deg,#ff7eb3,#ff4da6);
    color:white;
    border:none;
    box-shadow:0 6px 18px rgba(0,0,0,0.2);
}

div.stButton > button:hover {
    transform:scale(1.08);
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown('<div class="wrap">', unsafe_allow_html=True)
st.markdown('<div class="title">Anh muốn nói với em là...</div>', unsafe_allow_html=True)

# Heart clickable (JS side trigger)
heart_clicked = st.button("💗", key="heart")

st.markdown('<div class="sub">Bấm vào trái tim hoặc nút dưới đây</div>', unsafe_allow_html=True)

btn_clicked = st.button("Bấm vào đây")

st.markdown('</div>', unsafe_allow_html=True)


# ---------- POPUP ----------
if heart_clicked or btn_clicked:

    html = """
    <html>
    <body style="margin:0; overflow:hidden;
                 background:radial-gradient(circle,#fff0f6,#ffd6ec);">

    <script>

    let msgs=[
        "Anh nhớ em 💗",
        "Anh yêu em",
        "Đừng buồn nữa nhé",
        "Quay lại đi mà 🥺",
        "Anh luôn ở đây",
        "Smile đi ✨"
    ];

    function spawn(){
        let d=document.createElement("div");

        let x=Math.random()*window.innerWidth;
        let y=Math.random()*window.innerHeight;

        d.innerHTML=msgs[Math.floor(Math.random()*msgs.length)];

        d.style.position="absolute";
        d.style.left=x+"px";
        d.style.top=y+"px";
        d.style.padding="14px 18px";
        d.style.fontSize="18px";
        d.style.fontWeight="600";
        d.style.borderRadius="14px";
        d.style.background="rgba(255,192,203,0.92)";
        d.style.boxShadow="0 10px 24px rgba(0,0,0,0.2)";
        d.style.animation="pop .3s ease";

        document.body.appendChild(d);
    }

    let style=document.createElement("style");
    style.innerHTML=`
    @keyframes pop{
        from{transform:scale(0);opacity:0}
        to{transform:scale(1);opacity:1}
    }`;
    document.head.appendChild(style);

    let c=0;
    let flood=setInterval(()=>{
        spawn();
        c++;
        if(c>160){clearInterval(flood);}
    },35);

    </script>
    </body>
    </html>
    """

    components.html(html, height=900)
