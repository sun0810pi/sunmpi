import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Anh muốn nói với em", layout="wide")

st.title("💗 Tmai needs the remedy.")

if st.button("Muốn nói là..."):

    html = """
    <html>
    <body style="margin:0; overflow:hidden; background:white;">

    <script>
    let messages = [
        "Anh nhớ em lắm!!",
        "Anh yêu em 💗",
        "Đừng buồn nữa nhé",
        "Quay lại đi mà 🥺",
        "Anh luôn ở đây",
        "Smile đi nào ✨"
    ];

    function createPopup(){
        let div = document.createElement("div");

        let x = Math.random()*window.innerWidth;
        let y = Math.random()*window.innerHeight;

        div.innerHTML = messages[Math.floor(Math.random()*messages.length)];

        div.style.position="absolute";
        div.style.left=x+"px";
        div.style.top=y+"px";
        div.style.background="#FFC0CB";
        div.style.padding="14px";
        div.style.borderRadius="12px";
        div.style.fontSize="18px";
        div.style.fontWeight="bold";
        div.style.boxShadow="0 0 10px rgba(0,0,0,0.3)";
        div.style.zIndex=9999;

        document.body.appendChild(div);
    }

    // FLOOD giống tkinter
    let count = 0;
    let interval = setInterval(()=>{
        createPopup();
        count++;

        if(count > 120){ // số popup
            clearInterval(interval);
        }
    }, 40); // tốc độ spam

    </script>
    </body>
    </html>
    """

    components.html(html, height=800)
