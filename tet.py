import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="🧧 Tết Bính Ngọ 2026", page_icon="🧧")

# ===== ENCODE MUSIC WITH FALLBACK =====
music_base64 = ""
if os.path.exists("tet.mp3"):
    try:
        with open("tet.mp3", "rb") as f:
            audio_data = f.read()
            music_base64 = base64.b64encode(audio_data).decode()
            print("✅ Music loaded successfully")
    except Exception as e:
        print(f"⚠️ Music load error: {e}")
else:
    print("⚠️ tet.mp3 not found - music will be disabled")

# ===== STABLE HTML =====
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    margin: 0;
    overflow: hidden;
    font-family: 'Georgia', serif;
    background: linear-gradient(135deg, #ff7700 0%, #ffaa00 25%, #ffdd00 50%, #ff9900 75%, #ff5500 100%);
    background-size: 400% 400%;
    animation: bgFlow 22s ease infinite;
    min-height: 100vh;
    position: relative;
}

@keyframes bgFlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== TEXTURE ========== */
.texture {
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: 
        repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255, 255, 255, 0.02) 2px, rgba(255, 255, 255, 0.02) 4px),
        repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0, 0, 0, 0.02) 2px, rgba(0, 0, 0, 0.02) 4px);
    opacity: 0.5;
    z-index: 1;
    pointer-events: none;
}

/* ========== FLOATERS ========== */
.floaters {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
    overflow: hidden;
}

.floater {
    position: absolute;
    font-size: 26px;
    opacity: 0;
    animation: floatAnim linear infinite;
}

@keyframes floatAnim {
    0% {
        transform: translateY(-10vh) rotate(0deg);
        opacity: 0;
    }
    10% { opacity: 0.8; }
    90% { opacity: 0.3; }
    100% {
        transform: translateY(110vh) translateX(var(--dx)) rotate(360deg);
        opacity: 0;
    }
}

/* ========== LANTERNS ========== */
.lantern {
    position: fixed;
    width: 48px;
    height: 68px;
    background: linear-gradient(180deg, #ff0000, #cc0000, #ff0000);
    border-radius: 0 0 24px 24px;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.8);
    pointer-events: none;
    z-index: 3;
    animation: lanternSwing 3.8s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 26px;
    font-weight: 900;
}

.lantern::after {
    content: '';
    position: absolute;
    top: -11px;
    left: 50%;
    transform: translateX(-50%);
    width: 36px;
    height: 11px;
    background: #8b0000;
    border-radius: 5px;
}

@keyframes lanternSwing {
    0%, 100% { transform: rotate(-6deg); }
    50% { transform: rotate(6deg); }
}

/* ========== MAIN ========== */
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 20;
}

.title {
    font-size: clamp(52px, 11vw, 92px);
    font-weight: 900;
    background: linear-gradient(90deg, #ff0000, #ffd700, #ff0000);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 48px;
    animation: titleShine 3.5s ease infinite;
    filter: drop-shadow(0 0 45px rgba(255, 215, 0, 0.9));
    letter-spacing: 6px;
}

@keyframes titleShine {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== ENVELOPE ========== */
.envelope {
    width: 215px;
    height: 295px;
    position: relative;
    cursor: pointer;
    margin: 32px auto;
    transition: transform 0.35s ease;
}

.envelope:hover {
    transform: scale(1.16);
}

.envelope:active {
    transform: scale(0.94);
}

.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff1744 50%, #d32f2f 100%);
    border-radius: 13px;
    position: relative;
    box-shadow: 
        0 28px 70px rgba(0, 0, 0, 0.6),
        0 0 90px rgba(255, 215, 0, 0.7),
        inset 0 0 55px rgba(255, 215, 0, 0.35);
    animation: envGlow 2.4s ease-in-out infinite;
}

@keyframes envGlow {
    0%, 100% {
        box-shadow: 0 28px 70px rgba(0, 0, 0, 0.6), 0 0 70px rgba(255, 215, 0, 0.7);
    }
    50% {
        box-shadow: 0 32px 80px rgba(0, 0, 0, 0.7), 0 0 110px rgba(255, 215, 0, 0.95);
    }
}

.envelope-border {
    position: absolute;
    top: 13px;
    left: 13px;
    right: 13px;
    bottom: 13px;
    border: 3px solid gold;
    border-radius: 11px;
}

.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 108px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 35px rgba(255, 215, 0, 1),
        0 0 55px rgba(255, 215, 0, 0.85),
        4px 4px 0 rgba(139, 0, 0, 0.55);
    animation: fuPulse 2.6s ease-in-out infinite;
}

@keyframes fuPulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.09); }
}

.subtext {
    margin-top: 42px;
    font-size: clamp(24px, 5vw, 30px);
    color: white;
    font-weight: 800;
    text-shadow: 
        0 0 22px rgba(255, 215, 0, 0.95),
        2px 2px 5px rgba(0, 0, 0, 0.6);
}

/* ========== COUNTER ========== */
.counter {
    position: fixed;
    top: 26px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(211, 47, 47, 0.92);
    border: 3px solid gold;
    border-radius: 42px;
    padding: 13px 32px;
    color: gold;
    font-weight: 800;
    font-size: 21px;
    z-index: 500;
    box-shadow: 0 9px 32px rgba(211, 47, 47, 0.65);
}

.counter-num {
    font-size: 32px;
    font-weight: 900;
}

/* ========== EFFECTS ========== */
.lion {
    position: fixed;
    font-size: 50px;
    pointer-events: none;
    z-index: 100;
    animation: lionJump 2.3s ease-out forwards;
    filter: drop-shadow(0 0 18px rgba(255, 215, 0, 0.95));
}

@keyframes lionJump {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 1;
    }
    33% {
        transform: translate(var(--lx1), var(--ly1)) rotate(180deg) scale(1.35);
    }
    66% {
        transform: translate(var(--lx2), var(--ly2)) rotate(360deg) scale(1.1);
    }
    100% {
        transform: translate(var(--lx3), var(--ly3)) rotate(540deg) scale(0.35);
        opacity: 0;
    }
}

.money {
    position: fixed;
    width: 56px;
    height: 29px;
    background: linear-gradient(135deg, #1b5e20, #43a047);
    border: 2px solid gold;
    border-radius: 5px;
    pointer-events: none;
    z-index: 95;
    animation: moneyFly 1.9s ease-out forwards;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 19px;
}

@keyframes moneyFly {
    0% {
        transform: translate(0, 0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--mx), var(--my)) rotate(var(--mr));
        opacity: 0;
    }
}

.firework {
    position: fixed;
    width: 7px;
    height: 7px;
    background: gold;
    border-radius: 50%;
    pointer-events: none;
    z-index: 90;
    animation: fwExplode 1.5s ease-out forwards;
    box-shadow: 0 0 16px currentColor;
}

@keyframes fwExplode {
    0% {
        transform: translate(0, 0);
        opacity: 1;
    }
    100% {
        transform: translate(var(--fx), var(--fy));
        opacity: 0;
    }
}

.confetti {
    position: fixed;
    font-size: 21px;
    pointer-events: none;
    z-index: 85;
    animation: confDrop 2.7s ease-out forwards;
}

@keyframes confDrop {
    0% {
        transform: translate(0, 0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--cx), var(--cy)) rotate(720deg);
        opacity: 0;
    }
}

/* ========== SCROLL - GUARANTEED TO SHOW ========== */
.scroll {
    position: fixed;
    width: 380px;
    min-height: 200px;
    pointer-events: none;
    z-index: 999;
    animation: scrollShow 4.3s ease-out forwards;
}

@keyframes scrollShow {
    0% {
        transform: translateY(55px) scale(0.5) rotate(-11deg);
        opacity: 0;
    }
    18% {
        transform: translateY(0) scale(1.08) rotate(2deg);
        opacity: 1;
    }
    87% {
        opacity: 1;
    }
    100% {
        transform: translateY(-42px) scale(0.88) rotate(-3deg);
        opacity: 0;
    }
}

.scroll-paper {
    background: linear-gradient(180deg, #7f0000, #b71c1c, #c62828, #d32f2f, #c62828, #b71c1c, #7f0000);
    border: 5px solid gold;
    border-radius: 13px;
    padding: 30px 20px;
    position: relative;
    box-shadow: 
        0 24px 68px rgba(0, 0, 0, 0.75),
        0 0 48px rgba(255, 215, 0, 0.85),
        inset 0 0 38px rgba(255, 215, 0, 0.4);
}

.scroll-text {
    color: gold;
    font-size: 24px;
    font-weight: 800;
    text-align: center;
    line-height: 1.72;
    text-shadow: 
        0 0 24px rgba(255, 215, 0, 0.92),
        3px 3px 6px rgba(0, 0, 0, 0.78);
}

.scroll-couplet {
    margin-top: 19px;
    padding-top: 19px;
    border-top: 3px solid rgba(255, 215, 0, 0.62);
    font-size: 20px;
    font-style: italic;
    line-height: 1.95;
}

/* ========== RIPPLE ========== */
.ripple {
    position: fixed;
    border: 6px solid rgba(255, 215, 0, 1);
    border-radius: 50%;
    pointer-events: none;
    z-index: 80;
    animation: rippleGrow 1.4s ease-out forwards;
    box-shadow: 0 0 38px rgba(255, 215, 0, 0.88);
}

@keyframes rippleGrow {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 580px;
        height: 580px;
        opacity: 0;
    }
}

/* ========== MUSIC BTN ========== */
.music-btn {
    position: fixed;
    bottom: 27px;
    right: 27px;
    background: rgba(211, 47, 47, 0.92);
    border: 3px solid gold;
    border-radius: 42px;
    padding: 15px 28px;
    color: gold;
    font-weight: 800;
    font-size: 18px;
    cursor: pointer;
    z-index: 500;
    transition: transform 0.35s ease;
    box-shadow: 0 7px 28px rgba(211, 47, 47, 0.65);
}

.music-btn:hover {
    transform: scale(1.13);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .envelope {
        width: 165px;
        height: 230px;
    }
    
    .envelope-fu {
        font-size: 78px;
    }
    
    .title {
        font-size: 37px;
    }
    
    .subtext {
        font-size: 21px;
    }
    
    .scroll {
        width: 305px;
    }
    
    .scroll-text {
        font-size: 20px;
    }
    
    .scroll-couplet {
        font-size: 17px;
    }
}

</style>
</head>

<body>

<!-- Background -->
<div class="texture"></div>

<!-- Floaters -->
<div class="floaters" id="floaters"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Counter -->
<div class="counter">
    🎊 <span class="counter-num" id="counter">0</span> Lời Chúc 🎊
</div>

<!-- Main -->
<div class="container">
    <div class="title">Tết Bính Ngọ 2026</div>
    
    <div class="envelope" id="envelope">
        <div class="envelope-body">
            <div class="envelope-border"></div>
            <div class="envelope-fu">福</div>
        </div>
    </div>
    
    <div class="subtext">🦁 Nhấn Nhận Phúc Lộc 🦁</div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn">🎵 Nhạc Tết</div>

<!-- Audio -->
<audio id="music" loop preload="auto">
""" + (f'<source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">' if music_base64 else '') + """
</audio>

<script>

console.log("🎊 TẾT APP LOADING...");

// ========== INIT FLOATERS ==========
const floaters = document.getElementById('floaters');
const icons = ['🌸', '🌺', '🏵️', '💮', '🌼'];

for (let i = 0; i < 40; i++) {
    const el = document.createElement('div');
    el.className = 'floater';
    el.textContent = icons[Math.floor(Math.random() * icons.length)];
    el.style.left = Math.random() * 100 + '%';
    el.style.fontSize = (23 + Math.random() * 16) + 'px';
    el.style.setProperty('--dx', (Math.random() - 0.5) * 380 + 'px');
    el.style.animationDuration = (17 + Math.random() * 17) + 's';
    el.style.animationDelay = Math.random() * 11 + 's';
    floaters.appendChild(el);
}

console.log("✅ Floaters created");

// ========== INIT LANTERNS ==========
const lanternsDiv = document.getElementById('lanterns');
const lPos = [
    { left: '9%', top: '9%' },
    { left: '24%', top: '5%' },
    { left: '50%', top: '3%' },
    { left: '76%', top: '7%' },
    { left: '91%', top: '11%' }
];

lPos.forEach((pos, i) => {
    const lan = document.createElement('div');
    lan.className = 'lantern';
    lan.style.left = pos.left;
    lan.style.top = pos.top;
    lan.style.animationDelay = (i * 0.35) + 's';
    lanternsDiv.appendChild(lan);
});

console.log("✅ Lanterns created");

// ========== MUSIC ==========
let playing = false;
const music = document.getElementById('music');
const musicBtn = document.getElementById('musicBtn');

const hasMusic = music.querySelector('source') !== null;

if (!hasMusic) {
    musicBtn.textContent = '🎵 Không có nhạc';
    musicBtn.style.opacity = '0.5';
    musicBtn.style.cursor = 'not-allowed';
    console.log("⚠️ No music file loaded");
}

musicBtn.onclick = () => {
    if (!hasMusic) return;
    
    if (playing) {
        music.pause();
        musicBtn.textContent = '🎵 Nhạc Tết (Tắt)';
        playing = false;
        console.log("⏸️ Music paused");
    } else {
        music.play().then(() => {
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
            playing = true;
            console.log("▶️ Music playing");
        }).catch(e => {
            console.log("❌ Play error:", e);
            alert("Nhạc không thể phát. Vui lòng bấm nút nhạc để thử lại.");
        });
    }
};

// Auto-play on first click
document.body.addEventListener('click', function autoPlay() {
    if (!playing && hasMusic) {
        music.play().then(() => {
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
            console.log("▶️ Auto-play success");
        }).catch(e => {
            console.log("⚠️ Auto-play blocked:", e);
        });
    }
}, { once: true });

// ========== CONTENT (60+ LINES) ==========
const blessings = [
    "Chúc mừng năm mới", "An khang thịnh vượng", "Vạn sự như ý",
    "Tấn tài tấn lộc", "Phúc lộc đầy nhà", "Sức khỏe dồi dào",
    "Tiền vô như nước", "Gia đình hạnh phúc", "Công danh phát đạt",
    "Xuân về ngàn lộc", "Trăm năm hạnh phúc", "Vạn sự cát tường",
    "Tài lộc tràn trề", "Phát tài phát lộc", "Như ý cát tường",
    "Thiên hạ thái bình", "Quốc thái dân an", "Lộc tới nhà đầy",
    "Phúc đức viên mãn", "Tài vận hanh thông", "Gia tài vạn quán",
    "Lộc đến tài sinh", "Phát lộc phát tài", "Ngũ phúc lâm môn",
    "Vạn sự hanh thông", "Phúc thọ khang ninh", "Tứ quý tam đa",
    "Kim ngọc mãn đường", "Phúc như Đông Hải", "Thọ tỉ Nam Sơn",
    "Tài lộc viên mãn", "Phúc lộc song toàn", "Cát tường như ý",
    "Vạn lộc qui nguyên", "Tam đa cửu như"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Đào hồng nở thắm tươi xuân mới<br>Lân múa lượn ca cõi nhân gian",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa",
    "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình",
    "Phúc đến nhà đầy vui sướng mãi<br>Lộc về trong phố ấm no luôn",
    "Đất trời đổi mới xuân tươi thắm<br>Nhà cửa sum vầy phúc lộc đầy",
    "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh",
    "Vàng son rực rỡ lân múa tưng bừng<br>Đỏ thắm tươi xinh xuân về sum vầy",
    "Gió xuân đưa lộc về nhà lớn<br>Mưa phúc nhuần tài khắp cõi người",
    "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm",
    "Trúc xanh thẳng ngắn xuân ân cả<br>Lân múa phi bay đạo đức tròn",
    "Mai nở vàng tươi trong nhà lớn<br>Phúc đến thành công khắp đất trời",
    "Hạc múa lân ca xuân rạng ngời<br>Rồng bay phượng múa phúc đầy nhà",
    "Ngàn năm phúc lộc đầy vườn xuân<br>Vạn dặm tài danh rực nẻo đường",
    "Xuân phát tài lộc đầy trời đất<br>Tết mang phúc đức khắp nhân gian",
    "Bông mai vàng ươm xuân tươi thắm<br>Chữ phúc đỏ tươi Tết rực rỡ",
    "Lân múa đường xuân đón lộc về<br>Phúc lâm cửa nhà mang tài đến",
    "Cửa nhà tứ quý kim ngọc mãn<br>Trong phố tam đa phúc lộc đầy",
    "Xuân đến Bính Ngọ phúc lộc tới<br>Lân múa rực rỡ tấn tài hanh",
    "Đào hồng khoe sắc nghênh tân xuân<br>Lân vũ bay múa chúc vạn lộc",
    "Năm mới lân múa đem phúc tới<br>Tết đến rực rỡ mang lộc về",
    "Phúc lộc song toàn đầy trời đất<br>Tài danh viên mãn khắp nhân gian",
    "Xuân về lân nhảy rộn ràng hát<br>Tết đến rồng bay tấn lộc vui",
    "Trống lân vang dội xuân sum vầy<br>Pháo hoa rực rỡ phúc đầy nhà",
    "Mười năm cây cối nay sum suê<br>Trăm tuổi phúc lành mai tươi thắm",
    "Đầu xuân cát tụng hân hoan khắp<br>Ngọ Tết khai xuân phúc lộc dồi",
    "Thiên ân đãi hậu dân no ấm<br>Địa lợi ban ưu nước thái bình"
];

console.log(`✅ Content loaded: ${blessings.length} blessings, ${couplets.length} couplets`);

// ========== COUNTER ==========
let count = 0;
const counter = document.getElementById('counter');

function updateCounter() {
    count++;
    counter.textContent = count;
    console.log(`📊 Counter: ${count}`);
}

// ========== EFFECTS ==========
function createRipple(x, y) {
    const rip = document.createElement('div');
    rip.className = 'ripple';
    rip.style.left = (x - 290) + 'px';
    rip.style.top = (y - 290) + 'px';
    document.body.appendChild(rip);
    setTimeout(() => rip.remove(), 1400);
}

function createLions(x, y) {
    const num = 16;
    for (let i = 0; i < num; i++) {
        const lion = document.createElement('div');
        lion.className = 'lion';
        lion.textContent = '🦁';
        lion.style.left = x + 'px';
        lion.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const d1 = 165 + Math.random() * 75;
        const d2 = 295 + Math.random() * 105;
        const d3 = 515 + Math.random() * 145;
        
        lion.style.setProperty('--lx1', Math.cos(angle) * d1 + 'px');
        lion.style.setProperty('--ly1', Math.sin(angle) * d1 - 75 + 'px');
        lion.style.setProperty('--lx2', Math.cos(angle) * d2 + 'px');
        lion.style.setProperty('--ly2', Math.sin(angle) * d2 - 150 + 'px');
        lion.style.setProperty('--lx3', Math.cos(angle) * d3 + 'px');
        lion.style.setProperty('--ly3', Math.sin(angle) * d3 - 260 + 'px');
        
        document.body.appendChild(lion);
        setTimeout(() => lion.remove(), 2300);
    }
    console.log(`🦁 ${num} lions created`);
}

function createMoney(x, y) {
    const num = 19;
    for (let i = 0; i < num; i++) {
        const mon = document.createElement('div');
        mon.className = 'money';
        mon.textContent = '💵';
        mon.style.left = x + 'px';
        mon.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 135 + Math.random() * 225;
        
        mon.style.setProperty('--mx', Math.cos(angle) * dist + 'px');
        mon.style.setProperty('--my', Math.sin(angle) * dist - 85 + 'px');
        mon.style.setProperty('--mr', (Math.random() - 0.5) * 800 + 'deg');
        
        document.body.appendChild(mon);
        setTimeout(() => mon.remove(), 1900);
    }
    console.log(`💵 ${num} money created`);
}

function createFireworks(x, y) {
    const num = 37;
    const colors = ['#ffd700', '#ff0000', '#ffcc00', '#ff6b00', '#ff1744'];
    
    for (let i = 0; i < num; i++) {
        const fw = document.createElement('div');
        fw.className = 'firework';
        fw.style.left = x + 'px';
        fw.style.top = y + 'px';
        fw.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 155 + Math.random() * 210;
        
        fw.style.setProperty('--fx', Math.cos(angle) * dist + 'px');
        fw.style.setProperty('--fy', Math.sin(angle) * dist + 'px');
        
        document.body.appendChild(fw);
        setTimeout(() => fw.remove(), 1500);
    }
    console.log(`🎆 ${num} fireworks created`);
}

function createConfetti(x, y) {
    const num = 42;
    const shapes = ['●', '■', '▲', '◆', '★', '✦'];
    const colors = ['#ff0000', '#ffd700', '#ff6b00', '#ffcc00'];
    
    for (let i = 0; i < num; i++) {
        const conf = document.createElement('div');
        conf.className = 'confetti';
        conf.textContent = shapes[Math.floor(Math.random() * shapes.length)];
        conf.style.color = colors[Math.floor(Math.random() * colors.length)];
        conf.style.left = x + 'px';
        conf.style.top = y + 'px';
        
        const cx = (Math.random() - 0.5) * 570;
        const cy = Math.random() * 570 + 190;
        
        conf.style.setProperty('--cx', cx + 'px');
        conf.style.setProperty('--cy', cy + 'px');
        
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), 2700);
    }
    console.log(`🎊 ${num} confetti created`);
}

// ========== SCROLL - BULLETPROOF ==========
function createScroll() {
    console.log("📜 Creating scroll...");
    
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    // Position calculation
    const maxX = window.innerWidth - 400;
    const maxY = window.innerHeight - 320;
    const x = Math.max(200, Math.min(maxX, Math.random() * maxX));
    const y = Math.max(160, Math.min(maxY, Math.random() * maxY));
    
    scroll.style.left = x + 'px';
    scroll.style.top = y + 'px';
    
    scroll.innerHTML = `
        <div class="scroll-paper">
            <div class="scroll-text">
                ${blessing}
                <div class="scroll-couplet">${couplet}</div>
            </div>
        </div>
    `;
    
    // Append to body
    document.body.appendChild(scroll);
    console.log(`✅ Scroll appended at (${Math.round(x)}, ${Math.round(y)})`);
    
    // Remove after animation
    setTimeout(() => {
        scroll.remove();
        console.log("🗑️ Scroll removed");
    }, 4300);
}

// ========== MAIN CLICK ==========
const envelope = document.getElementById('envelope');

envelope.addEventListener('click', function(e) {
    console.log("🎊 ENVELOPE CLICKED!");
    
    updateCounter();
    
    // Auto-play music
    if (!playing && hasMusic) {
        music.play().then(() => {
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
            console.log("▶️ Music started");
        }).catch(e => {
            console.log("⚠️ Music play failed:", e);
        });
    }
    
    // Get center position
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    
    console.log(`📍 Center: (${Math.round(cx)}, ${Math.round(cy)})`);
    
    // Create effects
    createRipple(cx, cy);
    createLions(cx, cy);
    createMoney(cx, cy);
    createFireworks(cx, cy);
    createConfetti(cx, cy);
    
    // Create scrolls with staggered timing
    const numScrolls = count === 1 ? 9 : 6;
    console.log(`📜 Will create ${numScrolls} scrolls`);
    
    let scrollCount = 0;
    const interval = setInterval(() => {
        createScroll();
        scrollCount++;
        
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
            console.log(`✅ All ${numScrolls} scrolls created`);
        }
    }, 275);
});

// Prevent context menu
document.addEventListener('contextmenu', e => e.preventDefault());

console.log("✅ APP READY!");

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)