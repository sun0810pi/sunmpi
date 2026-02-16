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
    music_base64 = ""  # Fallback if file doesn't exist

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
    background: linear-gradient(135deg, #ff6b00 0%, #ffa500 25%, #ffcc00 50%, #ff8c00 75%, #ff4500 100%);
    background-size: 400% 400%;
    animation: gradientShift 20s ease infinite;
    position: relative;
    min-height: 100vh;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ========== PEACH BLOSSOMS BACKGROUND ========== */
.blossoms {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
}

.blossom {
    position: absolute;
    font-size: 30px;
    opacity: 0;
    animation: fallBlossom linear infinite;
    filter: drop-shadow(0 0 8px rgba(255, 192, 203, 0.8));
}

@keyframes fallBlossom {
    0% {
        transform: translateY(-10vh) translateX(0) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.9;
    }
    50% {
        opacity: 0.7;
    }
    90% {
        opacity: 0.4;
    }
    100% {
        transform: translateY(110vh) translateX(var(--drift)) rotate(720deg);
        opacity: 0;
    }
}

/* ========== LANTERNS BACKGROUND ========== */
.lanterns {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
}

.lantern {
    position: absolute;
    width: 40px;
    height: 60px;
    background: linear-gradient(180deg, #ff0000 0%, #cc0000 50%, #ff0000 100%);
    border-radius: 0 0 20px 20px;
    box-shadow: 
        0 0 20px rgba(255, 215, 0, 0.8),
        inset 0 5px 10px rgba(255, 255, 255, 0.3);
    animation: swingLantern 4s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 20px;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.9);
}

.lantern::after {
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 30px;
    height: 10px;
    background: #8b0000;
    border-radius: 5px;
}

@keyframes swingLantern {
    0%, 100% {
        transform: translateX(-15px) rotate(-5deg);
    }
    50% {
        transform: translateX(15px) rotate(5deg);
    }
}

/* ========== GOLDEN PARTICLES ========== */
.particles {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 3;
}

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: gold;
    border-radius: 50%;
    opacity: 0;
    animation: sparkle linear infinite;
    box-shadow: 0 0 10px gold;
}

@keyframes sparkle {
    0% {
        transform: translateY(100vh) scale(0);
        opacity: 0;
    }
    20% {
        opacity: 1;
    }
    80% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-10vh) scale(1.5);
        opacity: 0;
    }
}

/* ========== CENTER CONTAINER ========== */
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10;
}

/* ========== TITLE ========== */
.title {
    font-size: clamp(40px, 8vw, 80px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff0000, #ffd700, #ff0000, #ffd700);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 50px;
    animation: titleGlow 3s ease-in-out infinite, titleWave 5s ease-in-out infinite;
    filter: drop-shadow(0 0 30px rgba(255, 215, 0, 1));
    letter-spacing: 4px;
    text-shadow: 0 0 40px gold;
}

@keyframes titleGlow {
    0%, 100% { 
        filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.8)); 
    }
    50% { 
        filter: drop-shadow(0 0 60px rgba(255, 215, 0, 1)); 
    }
}

@keyframes titleWave {
    0%, 100% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
}

/* ========== RED ENVELOPE (LÌ XÌ) ========== */
.envelope-container {
    position: relative;
    display: inline-block;
    margin: 40px 0;
}

.envelope {
    width: 200px;
    height: 280px;
    position: relative;
    cursor: pointer;
    margin: auto;
    transform-style: preserve-3d;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.envelope:hover {
    transform: scale(1.15) rotateY(10deg);
}

.envelope:active {
    transform: scale(0.95);
}

/* Envelope body */
.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 50%, #d32f2f 100%);
    border-radius: 10px;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.5),
        0 0 80px rgba(255, 215, 0, 0.6),
        inset 0 0 50px rgba(255, 215, 0, 0.3);
    position: relative;
    overflow: hidden;
    animation: envelopeGlow 2s ease-in-out infinite;
}

@keyframes envelopeGlow {
    0%, 100% {
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.5),
            0 0 60px rgba(255, 215, 0, 0.6),
            inset 0 0 40px rgba(255, 215, 0, 0.3);
    }
    50% {
        box-shadow: 
            0 25px 70px rgba(0, 0, 0, 0.6),
            0 0 100px rgba(255, 215, 0, 0.9),
            inset 0 0 60px rgba(255, 255, 255, 0.4);
    }
}

/* Golden border decoration */
.envelope-body::before {
    content: '';
    position: absolute;
    top: 10px;
    left: 10px;
    right: 10px;
    bottom: 10px;
    border: 3px solid gold;
    border-radius: 8px;
    box-shadow: inset 0 0 20px rgba(255, 215, 0, 0.6);
}

/* 福 Character */
.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 100px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        3px 3px 0 rgba(139, 0, 0, 0.5);
    z-index: 2;
    animation: fuPulse 2s ease-in-out infinite;
}

@keyframes fuPulse {
    0%, 100% {
        transform: translate(-50%, -50%) scale(1);
    }
    50% {
        transform: translate(-50%, -50%) scale(1.1);
    }
}

/* Decorative patterns */
.envelope-pattern {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(255, 215, 0, 0.1) 0%, transparent 50%);
}

/* Corner decorations */
.corner-deco {
    position: absolute;
    width: 30px;
    height: 30px;
    background: gold;
    clip-path: polygon(0 0, 100% 0, 0 100%);
}

.corner-deco.top-left { top: 0; left: 0; }
.corner-deco.top-right { top: 0; right: 0; transform: rotate(90deg); }
.corner-deco.bottom-left { bottom: 0; left: 0; transform: rotate(-90deg); }
.corner-deco.bottom-right { bottom: 0; right: 0; transform: rotate(180deg); }

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: 50px;
    font-size: clamp(20px, 4vw, 28px);
    color: #fff;
    font-weight: 700;
    animation: pulse 2.5s ease-in-out infinite;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        2px 2px 4px rgba(0, 0, 0, 0.5);
    background: linear-gradient(90deg, #ff0000, #ffd700, #ff0000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

@keyframes pulse {
    0%, 100% { opacity: 0.8; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.08); }
}

/* ========== LION DANCE ANIMATION ========== */
.lion {
    position: fixed;
    font-size: 45px;
    pointer-events: none;
    z-index: 100;
    animation: lionJump 2s ease-out forwards;
    filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.9));
}

@keyframes lionJump {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    30% {
        transform: translate(var(--tx1), var(--ty1)) scale(1.3) rotate(180deg);
        opacity: 1;
    }
    60% {
        transform: translate(var(--tx2), var(--ty2)) scale(1.1) rotate(360deg);
        opacity: 0.8;
    }
    100% {
        transform: translate(var(--tx3), var(--ty3)) scale(0.5) rotate(540deg);
        opacity: 0;
    }
}

/* ========== BLESSING SCROLL ========== */
.scroll {
    position: fixed;
    width: 350px;
    min-height: 200px;
    pointer-events: none;
    z-index: 200;
    animation: scrollAppear 4s ease-out forwards;
}

.scroll-content {
    position: relative;
    background: linear-gradient(180deg, #8b0000 0%, #cc0000 50%, #8b0000 100%);
    border-radius: 15px;
    padding: 30px 20px;
    border: 5px solid gold;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.6),
        0 0 40px rgba(255, 215, 0, 0.7),
        inset 0 0 30px rgba(255, 215, 0, 0.3);
}

.scroll-content::before,
.scroll-content::after {
    content: '';
    position: absolute;
    width: 30px;
    height: 100%;
    background: linear-gradient(90deg, #4a2511, #8b4513, #4a2511);
    top: 0;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
}

.scroll-content::before {
    left: -35px;
    border-radius: 15px 0 0 15px;
}

.scroll-content::after {
    right: -35px;
    border-radius: 0 15px 15px 0;
}

.scroll-text {
    color: gold;
    font-size: 22px;
    font-weight: 700;
    text-align: center;
    line-height: 1.6;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.8),
        2px 2px 4px rgba(0, 0, 0, 0.7);
    font-family: 'Georgia', serif;
}

.scroll-couplet {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 2px solid rgba(255, 215, 0, 0.5);
    font-size: 18px;
    font-style: italic;
    line-height: 1.8;
}

@keyframes scrollAppear {
    0% {
        transform: translateY(50px) scale(0) rotate(-10deg);
        opacity: 0;
    }
    20% {
        transform: translateY(0) scale(1.1) rotate(2deg);
        opacity: 1;
    }
    85% {
        opacity: 1;
    }
    100% {
        transform: translateY(-30px) scale(0.9) rotate(-2deg);
        opacity: 0;
    }
}

/* ========== FIREWORKS ========== */
.firework {
    position: fixed;
    width: 5px;
    height: 5px;
    background: gold;
    border-radius: 50%;
    pointer-events: none;
    z-index: 150;
    animation: fireworkExplode 1.2s ease-out forwards;
    box-shadow: 0 0 10px gold;
}

@keyframes fireworkExplode {
    0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--fx), var(--fy)) scale(0);
        opacity: 0;
    }
}

/* ========== RIPPLE EFFECT ========== */
.ripple {
    position: fixed;
    border-radius: 50%;
    border: 5px solid rgba(255, 215, 0, 0.9);
    pointer-events: none;
    animation: rippleExpand 1.2s ease-out forwards;
    box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
}

@keyframes rippleExpand {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 500px;
        height: 500px;
        opacity: 0;
    }
}

/* ========== MUSIC CONTROL ========== */
.music-control {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: rgba(255, 0, 0, 0.85);
    backdrop-filter: blur(10px);
    border: 3px solid gold;
    border-radius: 50px;
    padding: 14px 24px;
    color: gold;
    font-weight: 700;
    font-size: 16px;
    cursor: pointer;
    z-index: 1000;
    transition: all 0.3s ease;
    box-shadow: 
        0 5px 25px rgba(255, 0, 0, 0.6),
        0 0 30px rgba(255, 215, 0, 0.4);
}

.music-control:hover {
    transform: scale(1.15);
    box-shadow: 
        0 8px 35px rgba(255, 0, 0, 0.8),
        0 0 50px rgba(255, 215, 0, 0.7);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .envelope {
        width: 150px;
        height: 210px;
    }
    
    .envelope-fu {
        font-size: 70px;
    }
    
    .title {
        font-size: 32px;
        margin-bottom: 35px;
    }
    
    .subtext {
        font-size: 18px;
        margin-top: 35px;
    }
    
    .scroll {
        width: 280px;
        font-size: 18px;
    }
    
    .scroll-text {
        font-size: 18px;
    }
    
    .scroll-couplet {
        font-size: 15px;
    }
}

</style>
</head>

<body>

<!-- Peach Blossoms -->
<div class="blossoms" id="blossomsContainer"></div>

<!-- Lanterns -->
<div class="lanterns" id="lanternsContainer"></div>

<!-- Golden Particles -->
<div class="particles" id="particlesContainer"></div>

<!-- Main Content -->
<div class="container">
    <div class="title">Chúc Mừng Năm Mới</div>
    
    <div class="envelope-container">
        <div class="envelope" id="mainEnvelope">
            <div class="envelope-body">
                <div class="envelope-pattern"></div>
                <div class="envelope-fu">福</div>
                <div class="corner-deco top-left"></div>
                <div class="corner-deco top-right"></div>
                <div class="corner-deco bottom-left"></div>
                <div class="corner-deco bottom-right"></div>
            </div>
        </div>
    </div>
    
    <div class="subtext">🧧 Nhấn vào lì xì 🧧</div>
</div>

<!-- Music Control -->
<div class="music-control" id="musicControl" onclick="toggleMusic()">
    🎵 Nhạc Tết
</div>

<!-- Background Music -->
<audio id="bgMusic" autoplay loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>
// ========== CREATE PEACH BLOSSOMS ==========
const blossomsContainer = document.getElementById('blossomsContainer');
const blossomEmojis = ['🌸', '🌺', '🏵️', '💮'];

for (let i = 0; i < 40; i++) {
    const blossom = document.createElement('div');
    blossom.className = 'blossom';
    blossom.innerHTML = blossomEmojis[Math.floor(Math.random() * blossomEmojis.length)];
    blossom.style.left = Math.random() * 100 + '%';
    blossom.style.fontSize = (20 + Math.random() * 20) + 'px';
    blossom.style.setProperty('--drift', (Math.random() - 0.5) * 300 + 'px');
    blossom.style.animationDuration = (15 + Math.random() * 15) + 's';
    blossom.style.animationDelay = Math.random() * 10 + 's';
    blossomsContainer.appendChild(blossom);
}

// ========== CREATE LANTERNS ==========
const lanternsContainer = document.getElementById('lanternsContainer');
const lanternPositions = [
    { left: '10%', top: '10%' },
    { left: '25%', top: '5%' },
    { left: '75%', top: '8%' },
    { left: '90%', top: '12%' },
    { left: '15%', top: '80%' },
    { left: '85%', top: '85%' }
];

lanternPositions.forEach((pos, index) => {
    const lantern = document.createElement('div');
    lantern.className = 'lantern';
    lantern.style.left = pos.left;
    lantern.style.top = pos.top;
    lantern.style.animationDelay = (index * 0.3) + 's';
    lanternsContainer.appendChild(lantern);
});

// ========== CREATE GOLDEN PARTICLES ==========
const particlesContainer = document.getElementById('particlesContainer');
for (let i = 0; i < 100; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDuration = (8 + Math.random() * 10) + 's';
    particle.style.animationDelay = Math.random() * 8 + 's';
    particlesContainer.appendChild(particle);
}

// ========== MUSIC CONTROL ==========
let musicPlaying = false;
const bgMusic = document.getElementById('bgMusic');
const musicControl = document.getElementById('musicControl');

function toggleMusic() {
    if (musicPlaying) {
        bgMusic.pause();
        musicControl.innerHTML = '🎵 Nhạc Tết (Tắt)';
        musicPlaying = false;
    } else {
        bgMusic.muted = false;
        bgMusic.play().catch(e => console.log('Play blocked:', e));
        musicControl.innerHTML = '🎵 Nhạc Tết (Bật)';
        musicPlaying = true;
    }
}

// Auto-start music on first interaction
document.body.addEventListener('click', function startMusic() {
    if (!musicPlaying) {
        bgMusic.muted = false;
        bgMusic.play().then(() => {
            musicPlaying = true;
            musicControl.innerHTML = '🎵 Nhạc Tết (Bật)';
        }).catch(e => console.log('Autoplay blocked'));
    }
}, { once: true });

// ========== BLESSING MESSAGES ==========
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
    "Vạn sự cát tường"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Đào hồng nở thắm tươi xuân mới<br>Hạc bay lượn múa cõi trần gian",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa",
    "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình"
];

// ========== CREATE RIPPLE ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 250) + 'px';
    ripple.style.top = (y - 250) + 'px';
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 1200);
}

// ========== CREATE LION DANCE ==========
function createLionDance(x, y) {
    const numLions = 12;
    
    for (let i = 0; i < numLions; i++) {
        const angle = (i / numLions) * Math.PI * 2;
        const distance1 = 200 + Math.random() * 100;
        const distance2 = 350 + Math.random() * 150;
        const distance3 = 500 + Math.random() * 200;
        
        const lion = document.createElement('div');
        lion.className = 'lion';
        lion.innerHTML = '🦁';
        lion.style.left = x + 'px';
        lion.style.top = y + 'px';
        
        const tx1 = Math.cos(angle) * distance1;
        const ty1 = Math.sin(angle) * distance1 - 100;
        const tx2 = Math.cos(angle) * distance2;
        const ty2 = Math.sin(angle) * distance2 - 200;
        const tx3 = Math.cos(angle) * distance3;
        const ty3 = Math.sin(angle) * distance3 - 300;
        
        lion.style.setProperty('--tx1', tx1 + 'px');
        lion.style.setProperty('--ty1', ty1 + 'px');
        lion.style.setProperty('--tx2', tx2 + 'px');
        lion.style.setProperty('--ty2', ty2 + 'px');
        lion.style.setProperty('--tx3', tx3 + 'px');
        lion.style.setProperty('--ty3', ty3 + 'px');
        
        document.body.appendChild(lion);
        
        setTimeout(() => lion.remove(), 2000);
    }
}

// ========== CREATE FIREWORKS ==========
function createFireworks(x, y) {
    const numSparks = 30;
    
    for (let i = 0; i < numSparks; i++) {
        const angle = (i / numSparks) * Math.PI * 2;
        const distance = 150 + Math.random() * 200;
        
        const firework = document.createElement('div');
        firework.className = 'firework';
        firework.style.left = x + 'px';
        firework.style.top = y + 'px';
        
        const fx = Math.cos(angle) * distance;
        const fy = Math.sin(angle) * distance;
        
        firework.style.setProperty('--fx', fx + 'px');
        firework.style.setProperty('--fy', fy + 'px');
        
        // Random colors
        const colors = ['gold', '#ff0000', '#ffd700', '#ff6b00', '#ffcc00'];
        firework.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        document.body.appendChild(firework);
        
        setTimeout(() => firework.remove(), 1200);
    }
}

// ========== CREATE SCROLL BLESSING ==========
function createScrollBlessing() {
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    const x = Math.random() * (window.innerWidth - 400) + 200;
    const y = Math.random() * (window.innerHeight - 300) + 150;
    
    scroll.style.left = x + 'px';
    scroll.style.top = y + 'px';
    
    scroll.innerHTML = `
        <div class="scroll-content">
            <div class="scroll-text">
                ${blessing}
                <div class="scroll-couplet">${couplet}</div>
            </div>
        </div>
    `;
    
    document.body.appendChild(scroll);
    
    setTimeout(() => scroll.remove(), 4000);
}

// ========== MAIN ENVELOPE CLICK HANDLER ==========
let clickCount = 0;
const mainEnvelope = document.getElementById('mainEnvelope');

mainEnvelope.addEventListener('click', function(e) {
    clickCount++;
    
    // Auto-start music
    if (!musicPlaying) {
        toggleMusic();
    }
    
    // Get envelope center
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Create effects
    createRipple(centerX, centerY);
    createLionDance(centerX, centerY);
    createFireworks(centerX, centerY);
    
    // Spam scrolls
    const numScrolls = clickCount === 1 ? 8 : 5;
    let scrollCount = 0;
    
    const interval = setInterval(() => {
        createScrollBlessing();
        scrollCount++;
        
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
        }
    }, 250);
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)
