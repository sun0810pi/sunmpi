import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    overflow:hidden;
    background:
        radial-gradient(circle at top,#111,#000);
    font-family: 'Segoe UI', sans-serif;
}

/* CENTER WRAP */
.wrap{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    text-align:center;
}

/* TITLE */
.title{
    font-size:64px;
    font-weight:800;
    color:#ff6fa8;
    text-shadow:0 0 25px #ff3f9f;
    margin-bottom:40px;
}

/* BEATING HEART */
.heart{
    width:120px;
    height:120px;
    background:#ff2d75;
    position:relative;
    transform:rotate(-45deg);
    margin:auto;
    cursor:pointer;

    box-shadow:0 0 40px #ff2d75;

    animation:beat 1s infinite;
}

.heart:before,
.heart:after{
    content:"";
    width:120px;
    height:120px;
    background:#ff2d75;
    border-radius:50%;
    position:absolute;
}

.heart:before{ top:-60px; left:0;}
.heart:after{ left:60px; top:0;}

@keyframes beat{
    0%{ transform:scale(1) rotate(-45deg);}
    25%{ transform:scale(1.15) rotate(-45deg);}
    40%{ transform:scale(1) rotate(-45deg);}
    60%{ transform:scale(1.2) rotate(-45deg);}
    100%{ transform:scale(1) rotate(-45deg);}
}

/* SUBTEXT */
.sub{
    margin-top:30px;
    color:#ccc;
    font-size:20px;
}

/* POPUP STYLE */
.popup{
    position:absolute;
    padding:14px 18px;
    background:#ff8fb3;
    border-radius:14px;
    color:black;
    font-weight:600;
    box-shadow:0 10px 25px rgba(0,0,0,.6);
    animation:pop .25s ease;
}

@keyframes pop{
    from{transform:scale(.2);opacity:0}
    to{transform:scale(1);opacity:1}
}

/* floating hearts background */
.bgheart{
    position:absolute;
    color:#ff3f9f33;
    font-size:28px;
    animation:float 10s linear infinite;
}

@keyframes float{
    from{transform:translateY(100vh)}
    to{transform:translateY(-10vh)}
}

</style>
</head>

<body>

<div class="wrap">
    <div class="title">Anh muốn nói với em là...</div>
    <div class="heart" onclick="flood()"></div>
    <div class="sub">Bấm vào trái tim 💗</div>
</div>


<script>

/* floating background hearts */
for(let i=0;i<25;i++){
    let h=document.createElement("div")
    h.className="bgheart"
    h.innerHTML="❤"
    h.style.left=Math.random()*100+"vw"
    h.style.animationDuration=5+Math.random()*8+"s"
    document.body.appendChild(h)
}


/* POPUP FLOOD */
let msgs=[
"Anh nhớ em 💗",
"Anh yêu em",
"Quay lại đi mà 🥺",
"Anh luôn ở đây",
"Smile đi ✨",
"You mean everything to me",
"Đừng buồn nữa nhé"
]

function spawn(){
    let d=document.createElement("div")
    d.className="popup"

    d.innerHTML=msgs[Math.floor(Math.random()*msgs.length)]

    d.style.left=Math.random()*window.innerWidth+"px"
    d.style.top=Math.random()*window.innerHeight+"px"

    document.body.appendChild(d)
}

/* MAIN FLOOD */
function flood(){

    let count=0

    let spam=setInterval(()=>{
        spawn()
        count++

        if(count>220)
            clearInterval(spam)

    },25)

}

</script>
</body>
</html>
"""

components.html(html, height=900)
