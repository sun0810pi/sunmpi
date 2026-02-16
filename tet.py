import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide", page_title="🧧 Chúc Mừng Năm Mới", page_icon="🧧")

# ===== ĐỌC VÀ ENCODE NHẠC TẾT =====
try:
    with open("tet.mp3", "rb") as f:
        audio_data = f.read()
        music_base64 = base64.b64encode(audio_data).decode()
except:
    music_base64 = ""

# ===== HTML CODE =====
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
    font-family: 'Georgia', 'Times New Roman', serif;
    background: linear-gradient(135deg, #ff8800 0%, #ffaa00 25%, #ffdd00 50%, #ff9900 75%, #ff6600 100%);
    background-size: 400% 400%;
    animation: gradientMove 20s ease infinite;
    min-height: 100vh;
    position: relative;
}

@keyframes gradientMove {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== FLOATING ELEMENTS ========== */
.floaters {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
}

.floater {
    position: absolute;
    font-size: 28px;
    opacity: 0;
    animation: float linear infinite;
}

@keyframes float {
    0% {
        transform: translateY(-10vh) translateX(0) rotate(0deg);
        opacity: 0;
    }
    10% { opacity: 0.8; }
    90% { opacity: 0.3; }
    100% {
        transform: translateY(110vh) translateX(var(--drift)) rotate(360deg);
        opacity: 0;
    }
}

/* ========== LANTERNS ========== */
.lantern {
    position: fixed;
    width: 45px;
    height: 65px;
    background: linear-gradient(180deg, #ff0000, #cc0000, #ff0000);
    border-radius: 0 0 22px 22px;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.8);
    pointer-events: none;
    animation: swing 3.5s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 24px;
    font-weight: 900;
}

.lantern::after {
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 32px;
    height: 10px;
    background: #8b0000;
    border-radius: 5px;
}

@keyframes swing {
    0%, 100% { transform: rotate(-6deg); }
    50% { transform: rotate(6deg); }
}

/* ========== MAIN CONTAINER ========== */
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10;
}

/* ========== TITLE ========== */
.title {
    font-size: clamp(48px, 10vw, 85px);
    font-weight: 900;
    background: linear-gradient(90deg, #ff0000, #ffd700, #ff0000);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 45px;
    animation: shimmerTitle 3s ease infinite;
    text-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
    letter-spacing: 5px;
}

@keyframes shimmerTitle {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== RED ENVELOPE ========== */
.envelope {
    width: 210px;
    height: 290px;
    position: relative;
    cursor: pointer;
    margin: 30px auto;
    transition: transform 0.3s ease;
}

.envelope:hover {
    transform: scale(1.15);
}

.envelope:active {
    transform: scale(0.95);
}

.envelope-bg {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff1744 50%, #d32f2f 100%);
    border-radius: 12px;
    position: relative;
    box-shadow: 
        0 25px 60px rgba(0, 0, 0, 0.5),
        0 0 80px rgba(255, 215, 0, 0.6),
        inset 0 0 50px rgba(255, 215, 0, 0.3);
    animation: glow 2s ease-in-out infinite;
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), 0 0 60px rgba(255, 215, 0, 0.6);
    }
    50% {
        box-shadow: 0 30px 70px rgba(0, 0, 0, 0.6), 0 0 100px rgba(255, 215, 0, 0.9);
    }
}

.envelope-border {
    position: absolute;
    top: 12px;
    left: 12px;
    right: 12px;
    bottom: 12px;
    border: 3px solid gold;
    border-radius: 10px;
}

.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 105px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        4px 4px 0 rgba(139, 0, 0, 0.5);
    animation: pulse 2.2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.08); }
}

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: 40px;
    font-size: clamp(22px, 5vw, 28px);
    color: white;
    font-weight: 800;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* ========== COUNTER ========== */
.counter {
    position: fixed;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 0, 0, 0.9);
    border: 3px solid gold;
    border-radius: 40px;
    padding: 12px 30px;
    color: gold;
    font-weight: 800;
    font-size: 20px;
    z-index: 500;
    box-shadow: 0 8px 30px rgba(255, 0, 0, 0.6);
}

.counter-num {
    font-size: 30px;
    font-weight: 900;
}

/* ========== HORSES ========== */
.horse {
    position: fixed;
    font-size: 48px;
    pointer-events: none;
    z-index: 100;
    animation: horseRun 2.2s ease-out forwards;
    filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.9));
}

@keyframes horseRun {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 1;
    }
    30% {
        transform: translate(var(--hx1), var(--hy1)) rotate(180deg) scale(1.3);
    }
    60% {
        transform: translate(var(--hx2), var(--hy2)) rotate(360deg) scale(1.1);
    }
    100% {
        transform: translate(var(--hx3), var(--hy3)) rotate(540deg) scale(0.4);
        opacity: 0;
    }
}

/* ========== MONEY ========== */
.money {
    position: fixed;
    width: 55px;
    height: 28px;
    background: linear-gradient(135deg, #228b22, #32cd32);
    border: 2px solid gold;
    border-radius: 4px;
    pointer-events: none;
    z-index: 90;
    animation: moneyFly 1.8s ease-out forwards;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
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

/* ========== FIREWORKS ========== */
.firework {
    position: fixed;
    width: 6px;
    height: 6px;
    background: gold;
    border-radius: 50%;
    pointer-events: none;
    z-index: 80;
    animation: explode 1.3s ease-out forwards;
    box-shadow: 0 0 15px currentColor;
}

@keyframes explode {
    0% {
        transform: translate(0, 0);
        opacity: 1;
    }
    100% {
        transform: translate(var(--fx), var(--fy));
        opacity: 0;
    }
}

/* ========== CONFETTI ========== */
.confetti {
    position: fixed;
    font-size: 20px;
    pointer-events: none;
    z-index: 85;
    animation: confettiDrop 2.5s ease-out forwards;
}

@keyframes confettiDrop {
    0% {
        transform: translate(0, 0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--cx), var(--cy)) rotate(720deg);
        opacity: 0;
    }
}

/* ========== BLESSING SCROLL ========== */
.scroll {
    position: fixed;
    width: 370px;
    min-height: 210px;
    pointer-events: none;
    z-index: 300;
    animation: scrollShow 4.2s ease-out forwards;
}

@keyframes scrollShow {
    0% {
        transform: translateY(50px) scale(0.3) rotate(-10deg);
        opacity: 0;
    }
    15% {
        transform: translateY(0) scale(1.05) rotate(2deg);
        opacity: 1;
    }
    88% {
        opacity: 1;
    }
    100% {
        transform: translateY(-40px) scale(0.9) rotate(-3deg);
        opacity: 0;
    }
}

.scroll-paper {
    background: linear-gradient(180deg, #8b0000, #cc0000, #8b0000);
    border: 4px solid gold;
    border-radius: 12px;
    padding: 30px 20px;
    position: relative;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.7),
        0 0 40px rgba(255, 215, 0, 0.7),
        inset 0 0 30px rgba(255, 215, 0, 0.3);
}

.scroll-text {
    color: gold;
    font-size: 23px;
    font-weight: 800;
    text-align: center;
    line-height: 1.7;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.8), 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.scroll-couplet {
    margin-top: 18px;
    padding-top: 18px;
    border-top: 2px solid rgba(255, 215, 0, 0.5);
    font-size: 18px;
    font-style: italic;
    line-height: 1.9;
}

.scroll-seal {
    position: absolute;
    bottom: 12px;
    right: 15px;
    width: 48px;
    height: 48px;
    background: #cc0000;
    border: 2px solid #8b0000;
    border-radius: 4px;
    color: white;
    font-size: 22px;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    transform: rotate(-8deg);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
}

/* ========== RIPPLE ========== */
.ripple {
    position: fixed;
    border: 5px solid rgba(255, 215, 0, 1);
    border-radius: 50%;
    pointer-events: none;
    z-index: 70;
    animation: ripple 1.2s ease-out forwards;
    box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
}

@keyframes ripple {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 550px;
        height: 550px;
        opacity: 0;
    }
}

/* ========== MUSIC BUTTON ========== */
.music-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: rgba(255, 0, 0, 0.9);
    border: 3px solid gold;
    border-radius: 40px;
    padding: 14px 26px;
    color: gold;
    font-weight: 700;
    font-size: 17px;
    cursor: pointer;
    z-index: 500;
    transition: transform 0.3s ease;
    box-shadow: 0 6px 25px rgba(255, 0, 0, 0.6);
}

.music-btn:hover {
    transform: scale(1.12);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .envelope {
        width: 160px;
        height: 220px;
    }
    
    .envelope-fu {
        font-size: 75px;
    }
    
    .title {
        font-size: 36px;
    }
    
    .subtext {
        font-size: 20px;
    }
    
    .scroll {
        width: 300px;
    }
    
    .scroll-text {
        font-size: 19px;
    }
    
    .scroll-couplet {
        font-size: 16px;
    }
}

</style>
</head>

<body>

<!-- Floaters Container -->
<div class="floaters" id="floaters"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Counter -->
<div class="counter">
    🎊 <span class="counter-num" id="counter">0</span> Lời Chúc 🎊
</div>

<!-- Main Content -->
<div class="container">
    <div class="title">Chúc Mừng Năm Mới</div>
    
    <div class="envelope" id="envelope">
        <div class="envelope-bg">
            <div class="envelope-border"></div>
            <div class="envelope-fu">福</div>
        </div>
    </div>
    
    <div class="subtext">🧧 Nhấn Nhận Lộc 🧧</div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn">🎵 Nhạc Tết</div>

<!-- Background Music -->
<audio id="music" loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>

// ========== INIT FLOATERS ==========
const floaters = document.getElementById('floaters');
const floaterIcons = ['🌸', '🌺', '🏵️', '💮', '🌼', '🎋'];

for (let i = 0; i < 45; i++) {
    const div = document.createElement('div');
    div.className = 'floater';
    div.textContent = floaterIcons[Math.floor(Math.random() * floaterIcons.length)];
    div.style.left = Math.random() * 100 + '%';
    div.style.fontSize = (22 + Math.random() * 18) + 'px';
    div.style.setProperty('--drift', (Math.random() - 0.5) * 350 + 'px');
    div.style.animationDuration = (16 + Math.random() * 16) + 's';
    div.style.animationDelay = Math.random() * 10 + 's';
    floaters.appendChild(div);
}

// ========== INIT LANTERNS ==========
const lanternsDiv = document.getElementById('lanterns');
const positions = [
    { left: '10%', top: '10%' },
    { left: '25%', top: '5%' },
    { left: '50%', top: '3%' },
    { left: '75%', top: '7%' },
    { left: '90%', top: '12%' }
];

positions.forEach((pos, i) => {
    const lantern = document.createElement('div');
    lantern.className = 'lantern';
    lantern.style.left = pos.left;
    lantern.style.top = pos.top;
    lantern.style.zIndex = '2';
    lantern.style.animationDelay = (i * 0.3) + 's';
    lanternsDiv.appendChild(lantern);
});

// ========== MUSIC CONTROL ==========
let playing = false;
const music = document.getElementById('music');
const musicBtn = document.getElementById('musicBtn');

musicBtn.onclick = () => {
    if (playing) {
        music.pause();
        musicBtn.textContent = '🎵 Nhạc Tết (Tắt)';
        playing = false;
    } else {
        music.play().catch(e => console.log('Play error:', e));
        musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
        playing = true;
    }
};

// Auto-play on first click
document.body.addEventListener('click', function autoPlay() {
    if (!playing) {
        music.play().then(() => {
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
        }).catch(e => {});
    }
}, { once: true });

// ========== BLESSINGS & COUPLETS ==========
const blessings = [
    "Chúc mừng năm mới",
    "An khang thịnh vượng",
    "Vạn sự như ý",
    "Tấn tài tấn lộc",
    "Phúc lộc đầy nhà",
    "Sức khỏe dồi dào",
    "Tiền vô như nước",
    "Gia đình hạnh phúc",
    "Công danh phát đạt",
    "Xuân về ngàn lộc",
    "Trăm năm hạnh phúc",
    "Vạn sự cát tường",
    "Tài lộc tràn trề",
    "Phát tài phát lộc",
    "Như ý cát tường",
    "Ngựa phi ngàn dặm",
    "Mã đáo thành công",
    "Vạn mã bôn tẩu",
    "Thiên hạ thái bình",
    "Quốc thái dân an",
    "Cát tường như ý",
    "Lộc tới nhà đầy",
    "Phúc đức viên mãn",
    "Tài vận hanh thông",
    "Gia tài vạn quán",
    "Lộc đến tài sinh",
    "Phát lộc phát tài",
    "Ngũ phúc lâm môn"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Đào hồng nở thắm tươi xuân mới<br>Hạc bay lượn múa cõi trần gian",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa",
    "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình",
    "Phúc đến nhà đầy vui sướng mãi<br>Lộc về trong phố ấm no luôn",
    "Đất trời đổi mới xuân tươi thắm<br>Nhà cửa sum vầy phúc lộc đầy",
    "Ngựa phi về tới lập công liền<br>Vạn dặm bôn tẩu nghĩa khí đầy",
    "Mã đáo thành công xuân rạng rỡ<br>Tài lộc tràn trề đêm tuyệt vời",
    "Ngựa vàng phi nhanh tới nhà lớn<br>Lộc đỏ tràn về khắp cõi đời",
    "Xuân đến Bính Ngọ phúc lộc tới<br>Tết sang năm Ngựa tấn tài hanh",
    "Gà gáy lời xưa còn dư vang<br>Ngựa phi công mới đến đầy nhà",
    "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm",
    "Ngựa vàng chở đến muôn điều may<br>Xuân mới rạng ngời nghìn sự vui",
    "Trúc xanh thẳng ngắn xuân ân cả<br>Ngựa phi vượt núi đạo đức tròn",
    "Mai nở vàng tươi trong nhà lớn<br>Ngựa phi bôn tẩu khắp đất trời",
    "Năm Ngựa phi mau rước lộc về<br>Tết đến sum vầy đoàn tụ đầy"
];

// ========== COUNTER ==========
let count = 0;
const counter = document.getElementById('counter');

function updateCounter() {
    count++;
    counter.textContent = count;
}

// ========== EFFECTS ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 275) + 'px';
    ripple.style.top = (y - 275) + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 1200);
}

function createHorses(x, y) {
    const num = 14;
    for (let i = 0; i < num; i++) {
        const horse = document.createElement('div');
        horse.className = 'horse';
        horse.textContent = '🐴';
        horse.style.left = x + 'px';
        horse.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const d1 = 170 + Math.random() * 70;
        const d2 = 300 + Math.random() * 100;
        const d3 = 500 + Math.random() * 150;
        
        horse.style.setProperty('--hx1', Math.cos(angle) * d1 + 'px');
        horse.style.setProperty('--hy1', Math.sin(angle) * d1 - 70 + 'px');
        horse.style.setProperty('--hx2', Math.cos(angle) * d2 + 'px');
        horse.style.setProperty('--hy2', Math.sin(angle) * d2 - 140 + 'px');
        horse.style.setProperty('--hx3', Math.cos(angle) * d3 + 'px');
        horse.style.setProperty('--hy3', Math.sin(angle) * d3 - 250 + 'px');
        
        document.body.appendChild(horse);
        setTimeout(() => horse.remove(), 2200);
    }
}

function createMoney(x, y) {
    const num = 18;
    for (let i = 0; i < num; i++) {
        const money = document.createElement('div');
        money.className = 'money';
        money.textContent = '💵';
        money.style.left = x + 'px';
        money.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 140 + Math.random() * 220;
        
        money.style.setProperty('--mx', Math.cos(angle) * dist + 'px');
        money.style.setProperty('--my', Math.sin(angle) * dist - 80 + 'px');
        money.style.setProperty('--mr', (Math.random() - 0.5) * 720 + 'deg');
        
        document.body.appendChild(money);
        setTimeout(() => money.remove(), 1800);
    }
}

function createFireworks(x, y) {
    const num = 35;
    const colors = ['gold', '#ff0000', '#ffd700', '#ff6b00', '#ffcc00'];
    
    for (let i = 0; i < num; i++) {
        const fw = document.createElement('div');
        fw.className = 'firework';
        fw.style.left = x + 'px';
        fw.style.top = y + 'px';
        fw.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 160 + Math.random() * 200;
        
        fw.style.setProperty('--fx', Math.cos(angle) * dist + 'px');
        fw.style.setProperty('--fy', Math.sin(angle) * dist + 'px');
        
        document.body.appendChild(fw);
        setTimeout(() => fw.remove(), 1300);
    }
}

function createConfetti(x, y) {
    const num = 40;
    const icons = ['●', '■', '▲', '◆', '★', '✦'];
    const colors = ['#ff0000', '#ffd700', '#ff6b00', '#ffcc00'];
    
    for (let i = 0; i < num; i++) {
        const conf = document.createElement('div');
        conf.className = 'confetti';
        conf.textContent = icons[Math.floor(Math.random() * icons.length)];
        conf.style.color = colors[Math.floor(Math.random() * colors.length)];
        conf.style.left = x + 'px';
        conf.style.top = y + 'px';
        
        const cx = (Math.random() - 0.5) * 550;
        const cy = Math.random() * 550 + 180;
        
        conf.style.setProperty('--cx', cx + 'px');
        conf.style.setProperty('--cy', cy + 'px');
        
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), 2500);
    }
}

function createScroll() {
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    const x = Math.random() * (window.innerWidth - 400) + 200;
    const y = Math.random() * (window.innerHeight - 300) + 150;
    
    scroll.style.left = x + 'px';
    scroll.style.top = y + 'px';
    
    scroll.innerHTML = `
        <div class="scroll-paper">
            <div class="scroll-text">
                ${blessing}
                <div class="scroll-couplet">${couplet}</div>
            </div>
            <div class="scroll-seal">印</div>
        </div>
    `;
    
    document.body.appendChild(scroll);
    setTimeout(() => scroll.remove(), 4200);
}

// ========== MAIN CLICK HANDLER ==========
const envelope = document.getElementById('envelope');

envelope.addEventListener('click', function(e) {
    updateCounter();
    
    if (!playing) {
        music.play().catch(e => {});
        playing = true;
        musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
    }
    
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    
    createRipple(cx, cy);
    createHorses(cx, cy);
    createMoney(cx, cy);
    createFireworks(cx, cy);
    createConfetti(cx, cy);
    
    const numScrolls = count === 1 ? 8 : 5;
    let scrollCount = 0;
    
    const interval = setInterval(() => {
        createScroll();
        scrollCount++;
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
        }
    }, 270);
});

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)