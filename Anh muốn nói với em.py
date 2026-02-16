import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ---------- LANDING STYLE ----------
st.markdown("""
<style>

/* nền gradient */
body {
    background: linear-gradient(135deg,#ffe6f2,#fff0f6);
}

/* căn giữa toàn bộ */
.center-wrap {
    height: 80vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

/* title cute */
.title {
    font-size:56px;
    font-weight:800;
    background: linear-gradient(90deg,#ff4da6,#ff99cc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:30px;
}

/* trái tim đập */
.heart {
    width:60px;
    height:60px;
    background:#ff4da6;
    position:relative;
    transform: rotate(-45deg);
    animation: beat 1s infinite;
    margin-bottom:30px;
}

.heart:before,
.heart:after{
    content:"";
    width:60px;
    height:60px;
    background:#ff4da6;
    border-radius:50%;
    position:absolute;
}

.heart:before{ top:-30px; left:0;}
.heart:after{ left:30px; top:0;}

@keyframes beat{
    0%{transform:scale(1) rotate(-45deg);}
    50%{transform:scale(1.25) rotate(-45deg);}
    100%{transform:scale(1) rotate(-45deg);}
}

/* nút đẹp */
.center-btn button{
    font-size:26px;
    padding:18px 40px;
    border-radius:18px;
    border:none;
    color:white;
    background: linear-gradient(135deg,#ff7eb3,#ff4da6);
    box-shadow:0 8px 20px rgba(0,0,0,0.2);
    transition:0.3s;
}

.center-btn button:hover{
    transform:scale(1.1);
}

</style>
""", unsafe_allow_html=True)

# ---------- LANDING ----------
st.markdown("""
<div class="center-wrap">
    <div class="title">Anh muốn nói với em là...</div>
    <div class="heart"></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="center-btn">', unsafe_allow_html=True)
clicked = st.button("Bấm vào đây 💗")
st.markdown('</div>', unsafe_allow_html=True)


# ---------- POPUP FLOOD ----------
if clicked:

    html = """
    <html>
    <body style="margin:0; overflow:hidden;
                 background:linear-gradient(135deg,#ffe6f2,#fff0f6);">

    <script>

    let msgs=[
        "Anh nhớ em 💗",
        "Anh yêu em",
        "Đừng buồn nữa nhé",
        "Quay lại đi mà 🥺",
        "Anh luôn ở đây",
        "Smile đi ✨",
        "You mean a lot to me"
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
        d.style.background="rgba(255,192,203,0.9)";
        d.style.boxShadow="0 8px 20px rgba(0,0,0,0.2)";
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
        if(c>150){clearInterval(flood);}
    },35);

    </script>
    </body>
    </html>
    """

    components.html(html, height=900)
