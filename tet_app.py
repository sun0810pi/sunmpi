import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide", page_title="🧧 Nhặt Lì Xì Tết", page_icon="🧧")

# ===== ENCODE MUSIC =====
try:
    with open("tet.mp3", "rb") as f:
        audio_data = f.read()
        music_base64 = base64.b64encode(audio_data).decode()
except:
    music_base64 = ""

# ===== GAME NHẶT LÌ XÌ - MOBILE OPTIMIZED =====
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, maximum-scale=1.0">
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
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
    touch-action: manipulation;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ========== PEACH BLOSSOMS ========== */
.blossoms {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}

.blossom {
    position: absolute;
    font-size: 24px;
    opacity: 0;
    animation: fallBlossom linear infinite;
}

@keyframes fallBlossom {
    0% {
        transform: translateY(-10vh) rotate(0deg);
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
    width: 36px;
    height: 54px;
    background: linear-gradient(180deg, #ff0000 0%, #cc0000 50%, #ff0000 100%);
    border-radius: 0 0 18px 18px;
    box-shadow: 0 0 18px rgba(255, 215, 0, 0.7);
    pointer-events: none;
    z-index: 2;
    animation: swingLantern 4s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 18px;
    font-weight: 900;
}

@keyframes swingLantern {
    0%, 100% { transform: rotate(-4deg); }
    50% { transform: rotate(4deg); }
}

/* ========== SCREENS ========== */
.screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 10;
    opacity: 0;
    transition: opacity 0.4s ease;
}

.screen.active {
    display: flex;
    opacity: 1;
}

/* ========== INTRO SCREEN ========== */
.intro-container {
    text-align: center;
    z-index: 20;
    width: 90%;
    max-width: 500px;
    padding: 20px;
}

.title {
    font-size: clamp(32px, 9vw, 68px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff0000, #ffd700, #ff0000, #ffd700);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 30px;
    animation: titleWave 4s ease-in-out infinite;
    filter: drop-shadow(0 0 25px rgba(255, 215, 0, 0.9));
    letter-spacing: 3px;
}

@keyframes titleWave {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.intro-text {
    font-size: clamp(18px, 4.5vw, 24px);
    color: white;
    font-weight: 700;
    margin: 25px 0 35px 0;
    text-shadow: 0 0 18px rgba(255, 215, 0, 0.8), 2px 2px 4px rgba(0, 0, 0, 0.6);
}

.start-envelope {
    width: 140px;
    height: 190px;
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 50%, #d32f2f 100%);
    border: 4px solid gold;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    margin: 0 auto;
    position: relative;
    box-shadow: 
        0 15px 50px rgba(0, 0, 0, 0.5),
        0 0 60px rgba(255, 215, 0, 0.7),
        inset 0 0 30px rgba(255, 215, 0, 0.3);
    transition: all 0.3s ease;
    animation: envelopeFloat 2.5s ease-in-out infinite;
}

.start-envelope::before {
    content: '';
    position: absolute;
    top: 12px;
    left: 12px;
    right: 12px;
    bottom: 12px;
    border: 3px solid gold;
    border-radius: 8px;
    box-shadow: inset 0 0 20px rgba(255, 215, 0, 0.5);
}

.start-envelope-fu {
    font-size: 70px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 1),
        0 0 45px rgba(255, 215, 0, 0.8),
        3px 3px 0 rgba(139, 0, 0, 0.4);
    z-index: 1;
    animation: fuPulse 2s ease-in-out infinite;
}

@keyframes envelopeFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes fuPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.08); }
}

.start-envelope:hover {
    transform: translateY(-10px) scale(1.1);
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.6),
        0 0 80px rgba(255, 215, 0, 0.9),
        inset 0 0 40px rgba(255, 255, 255, 0.4);
}

.start-envelope:active {
    transform: translateY(-5px) scale(0.95);
}

/* ========== GAME SCREEN ========== */
.game-container {
    width: 100%;
    height: 100%;
    position: relative;
}

/* ========== HUD ========== */
.hud {
    position: fixed;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 12px;
    z-index: 100;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 95%;
}

.hud-item {
    background: linear-gradient(135deg, rgba(211, 47, 47, 0.95), rgba(255, 0, 0, 0.95));
    border: 2px solid gold;
    border-radius: 25px;
    padding: 8px 20px;
    font-size: clamp(15px, 3.8vw, 18px);
    font-weight: 800;
    color: gold;
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.4),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
    text-shadow: 0 0 12px rgba(255, 215, 0, 0.8), 1px 1px 3px rgba(0, 0, 0, 0.6);
    white-space: nowrap;
}

.hud-number {
    font-size: clamp(20px, 5vw, 26px);
    margin: 0 5px;
}

.timer-warning {
    animation: timerBlink 0.5s ease-in-out infinite;
}

@keyframes timerBlink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

/* ========== FALLING ITEMS ========== */
.falling-item {
    position: fixed;
    cursor: pointer;
    z-index: 50;
    animation: fall linear;
    transition: transform 0.15s ease;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
}

.falling-item:active {
    transform: scale(1.2);
}

.item-envelope {
    width: 45px;
    height: 65px;
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 50%, #d32f2f 100%);
    border: 2px solid gold;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    box-shadow: 
        0 4px 15px rgba(0, 0, 0, 0.3),
        inset 0 0 15px rgba(255, 215, 0, 0.3);
}

.item-scroll {
    width: 50px;
    height: 60px;
    background: linear-gradient(135deg, #8B4513 0%, #A0522D 50%, #8B4513 100%);
    border: 2px solid gold;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 
        0 4px 15px rgba(0, 0, 0, 0.3),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
}

@keyframes fall {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(calc(100vh + 100px)) rotate(var(--rotation));
        opacity: 1;
    }
}

.falling-item.collected {
    animation: collectAnim 0.5s ease-out forwards;
}

@keyframes collectAnim {
    0% {
        transform: scale(1) rotate(0deg);
        opacity: 1;
    }
    50% {
        transform: scale(1.5) rotate(180deg);
        opacity: 0.8;
    }
    100% {
        transform: scale(0) rotate(360deg);
        opacity: 0;
    }
}

/* ========== BLESSING POPUP ========== */
.blessing-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    width: min(85vw, 380px);
    pointer-events: none;
    z-index: 200;
    opacity: 0;
}

.blessing-popup.show {
    animation: popupShow 3s ease-out forwards;
}

@keyframes popupShow {
    0% {
        transform: translate(-50%, -50%) scale(0) rotate(-5deg);
        opacity: 0;
    }
    10% {
        transform: translate(-50%, -50%) scale(1.1) rotate(2deg);
        opacity: 1;
    }
    85% {
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -60%) scale(0.9) rotate(-2deg);
        opacity: 0;
    }
}

.popup-content {
    background: linear-gradient(180deg, #8B0000, #B71C1C, #D32F2F, #B71C1C, #8B0000);
    border: 3px solid gold;
    border-radius: 18px;
    padding: 25px 20px;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.7),
        0 0 50px rgba(255, 215, 0, 0.8),
        inset 0 0 30px rgba(255, 215, 0, 0.2);
}

.popup-text {
    color: gold;
    font-size: clamp(20px, 5vw, 26px);
    font-weight: 800;
    text-align: center;
    line-height: 1.7;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        0 0 35px rgba(255, 215, 0, 0.7),
        3px 3px 5px rgba(0, 0, 0, 0.7);
}

.popup-couplet {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 2px solid rgba(255, 215, 0, 0.6);
    font-size: clamp(16px, 4vw, 20px);
    font-style: italic;
    line-height: 1.9;
}

/* ========== END SCREEN ========== */
.end-container {
    text-align: center;
    width: 90%;
    max-width: 450px;
    padding: 20px;
}

.end-scroll {
    background: linear-gradient(180deg, #8B0000, #B71C1C, #D32F2F, #B71C1C, #8B0000);
    border: 4px solid gold;
    border-radius: 20px;
    padding: 35px 25px;
    box-shadow: 
        0 25px 70px rgba(0, 0, 0, 0.6),
        0 0 60px rgba(255, 215, 0, 0.8),
        inset 0 0 40px rgba(255, 215, 0, 0.2);
    animation: scrollAppear 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes scrollAppear {
    0% {
        transform: scale(0.5) rotate(-5deg);
        opacity: 0;
    }
    100% {
        transform: scale(1) rotate(0deg);
        opacity: 1;
    }
}

.end-title {
    font-size: clamp(32px, 8vw, 48px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        4px 4px 6px rgba(0, 0, 0, 0.6);
    margin-bottom: 22px;
}

.end-stats {
    color: #FFD700;
    font-size: clamp(22px, 5.5vw, 30px);
    font-weight: 800;
    margin: 20px 0;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        3px 3px 5px rgba(0, 0, 0, 0.6);
}

.total-counter {
    color: #FFD700;
    font-size: clamp(18px, 4.5vw, 22px);
    font-weight: 700;
    margin: 15px 0;
    padding: 15px;
    background: rgba(255, 215, 0, 0.15);
    border-radius: 15px;
    border: 2px solid rgba(255, 215, 0, 0.4);
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
}

.end-blessing {
    color: #FFD700;
    font-size: clamp(18px, 4.5vw, 22px);
    font-weight: 700;
    line-height: 1.8;
    margin-top: 20px;
    padding-top: 20px;
    border-top: 2px solid rgba(255, 215, 0, 0.5);
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.8), 2px 2px 4px rgba(0, 0, 0, 0.6);
}

.restart-btn {
    margin-top: 28px;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    border-radius: 40px;
    padding: 16px 40px;
    font-size: clamp(18px, 4.5vw, 24px);
    font-weight: 900;
    color: #8B0000;
    cursor: pointer;
    transition: transform 0.3s ease;
    box-shadow: 
        0 6px 25px rgba(255, 165, 0, 0.5),
        inset 0 0 20px rgba(255, 255, 255, 0.4);
}

.restart-btn:hover {
    transform: scale(1.08);
}

.restart-btn:active {
    transform: scale(0.95);
}

/* ========== MUSIC BUTTON ========== */
.music-btn {
    position: fixed;
    bottom: 18px;
    right: 18px;
    background: linear-gradient(135deg, rgba(211, 47, 47, 0.95), rgba(255, 0, 0, 0.95));
    border: 2px solid gold;
    border-radius: 30px;
    padding: 10px 22px;
    color: gold;
    font-weight: 700;
    font-size: clamp(13px, 3.2vw, 16px);
    cursor: pointer;
    z-index: 500;
    transition: transform 0.3s ease;
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.4),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
    text-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
}

.music-btn:hover {
    transform: scale(1.08);
}

.music-btn:active {
    transform: scale(0.95);
}

/* ========== PARTICLES ========== */
.particle {
    position: fixed;
    width: 3px;
    height: 3px;
    background: gold;
    border-radius: 50%;
    pointer-events: none;
    z-index: 40;
    box-shadow: 0 0 8px gold;
    animation: particleFloat linear infinite;
}

@keyframes particleFloat {
    0% {
        transform: translateY(100vh) scale(0);
        opacity: 0;
    }
    20% { opacity: 1; }
    80% { opacity: 0.7; }
    100% {
        transform: translateY(-10vh) scale(1.2);
        opacity: 0;
    }
}

/* ========== MOBILE OPTIMIZATIONS ========== */
@media (min-width: 900px) {
    .item-envelope {
        width: 62px;
        height: 88px;
        font-size: 36px;
    }
    
    .item-scroll {
        width: 66px;
        height: 78px;
        font-size: 32px;
    }
}

@media (max-width: 768px) {
    .hud {
        top: 10px;
        gap: 8px;
    }
    
    .hud-item {
        padding: 6px 16px;
    }
    
    .item-envelope {
        width: 40px;
        height: 58px;
        font-size: 24px;
    }
    
    .item-scroll {
        width: 44px;
        height: 54px;
        font-size: 22px;
    }
}

@media (max-width: 480px) {
    .hud-item {
        padding: 5px 14px;
        font-size: 14px;
    }
    
    .hud-number {
        font-size: 18px;
    }
}

@media (max-height: 700px) {
    .hud {
        top: 8px;
    }
    
    .end-scroll {
        padding: 25px 20px;
    }
}

</style>
</head>

<body>

<!-- Blossoms -->
<div class="blossoms" id="blossoms"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Particles -->
<div id="particles"></div>

<!-- SCREEN 1: INTRO -->
<div class="screen active" id="introScreen">
    <div class="intro-container">
        <div class="title">Chúc Mừng Năm Mới</div>
        <div class="intro-text">
            Lì xì và chiếu chỉ sẽ rơi xuống!<br>
            Nhấn vào để nhận lời chúc năm mới 🎊
        </div>
        <div class="start-envelope" onclick="startGame()">
            <div class="start-envelope-fu">福</div>
        </div>
    </div>
</div>

<!-- SCREEN 2: GAME -->
<div class="screen" id="gameScreen">
    <div class="game-container" id="gameContainer">
        <div class="hud">
            <div class="hud-item">
                ⏱️ <span class="hud-number" id="timer">30</span>s
            </div>
            <div class="hud-item">
                🧧 <span class="hud-number" id="collected">0</span> lời chúc
            </div>
        </div>
    </div>
</div>

<!-- SCREEN 3: END -->
<div class="screen" id="endScreen">
    <div class="end-container">
        <div class="end-scroll">
            <div class="end-title">🎊 Kết Thúc! 🎊</div>
            <div class="end-stats">
                Bạn đã nhặt được:<br>
                <span style="font-size: clamp(36px, 9vw, 54px);" id="finalCollected">0</span> lời chúc!
            </div>
            <div class="total-counter">
                🏆 Tổng cộng đã nhặt: <span id="totalEver">0</span> lời chúc
            </div>
            <div class="end-blessing" id="endBlessing"></div>
            <button class="restart-btn" onclick="restartGame()">
                🔄 Chơi Lại
            </button>
        </div>
    </div>
</div>

<!-- Blessing Popup -->
<div class="blessing-popup" id="blessingPopup">
    <div class="popup-content">
        <div class="popup-text" id="popupText"></div>
    </div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn" onclick="toggleMusic()">
    🎵 Nhạc
</div>

<!-- Audio -->
<audio id="bgMusic" loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>

console.log("🧧 NHẶT LÌ XÌ - MOBILE OPTIMIZED");

// ========== DEVICE DETECTION ==========
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent) || window.innerWidth < 768;

// ========== CREATE BLOSSOMS ==========
const blossomsContainer = document.getElementById('blossoms');
const blossomEmojis = ['🌸', '🌺', '🏵️', '💮'];
const blossomCount = isMobile ? 15 : 25;

for (let i = 0; i < blossomCount; i++) {
    const blossom = document.createElement('div');
    blossom.className = 'blossom';
    blossom.innerHTML = blossomEmojis[Math.floor(Math.random() * blossomEmojis.length)];
    blossom.style.left = Math.random() * 100 + '%';
    blossom.style.fontSize = (18 + Math.random() * 12) + 'px';
    blossom.style.setProperty('--drift', (Math.random() - 0.5) * 200 + 'px');
    blossom.style.animationDuration = (12 + Math.random() * 10) + 's';
    blossom.style.animationDelay = Math.random() * 8 + 's';
    blossomsContainer.appendChild(blossom);
}

// ========== CREATE LANTERNS ==========
const lanternsContainer = document.getElementById('lanterns');
const lanternPositions = [
    { left: '10%', top: '8%' },
    { left: '50%', top: '5%' },
    { left: '90%', top: '10%' },
    { left: '25%', top: '7%' },
    { left: '75%', top: '9%' }
];

const lanternCount = isMobile ? 3 : 5;
for (let i = 0; i < lanternCount; i++) {
    const lantern = document.createElement('div');
    lantern.className = 'lantern';
    lantern.style.left = lanternPositions[i].left;
    lantern.style.top = lanternPositions[i].top;
    lantern.style.animationDelay = (i * 0.3) + 's';
    lanternsContainer.appendChild(lantern);
}

// ========== CREATE PARTICLES ==========
const particlesContainer = document.getElementById('particles');
const particleCount = isMobile ? 30 : 60;

for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDuration = (6 + Math.random() * 8) + 's';
    particle.style.animationDelay = Math.random() * 6 + 's';
    particlesContainer.appendChild(particle);
}

// ========== MUSIC ==========
let musicPlaying = false;
const bgMusic = document.getElementById('bgMusic');
const musicBtn = document.getElementById('musicBtn');

function toggleMusic() {
    if (musicPlaying) {
        bgMusic.pause();
        musicBtn.textContent = '🎵 Nhạc (Tắt)';
        musicPlaying = false;
    } else {
        bgMusic.muted = false;
        bgMusic.play().catch(e => console.log('Play blocked'));
        musicBtn.textContent = '🎵 Nhạc (Bật)';
        musicPlaying = true;
    }
}

document.body.addEventListener('click', function() {
    if (!musicPlaying) {
        bgMusic.muted = false;
        bgMusic.play().then(() => {
            musicPlaying = true;
            musicBtn.textContent = '🎵 Nhạc (Bật)';
        }).catch(() => {});
    }
}, { once: true });

// ========== CONTENT ==========
const blessings = [
    { text: "Chúc mừng năm mới", couplet: "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa" },
    { text: "An khang thịnh vượng", couplet: "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang" },
    { text: "Vạn sự như ý", couplet: "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh" },
    { text: "Tấn tài tấn lộc", couplet: "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy" },
    { text: "Phúc lộc đầy nhà", couplet: "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa" },
    { text: "Sức khỏe dồi dào", couplet: "Trúc xanh thẳng ngắn xuân ân cả<br>Lân múa phi bay đạo đức tròn" },
    { text: "Tiền vô như nước", couplet: "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm" },
    { text: "Gia đình hạnh phúc", couplet: "Đào hồng nở thắm tươi xuân mới<br>Hạc bay lượn múa cõi trần gian" },
    { text: "Công danh phát đạt", couplet: "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình" },
    { text: "Xuân về ngàn lộc", couplet: "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa" },
    { text: "Trăm năm hạnh phúc", couplet: "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang" },
    { text: "Vạn sự cát tường", couplet: "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh" },
    { text: "Phát tài phát lộc", couplet: "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy" },
    { text: "Như ý cát tường", couplet: "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa" },
    { text: "Tài lộc tràn trề", couplet: "Trúc xanh thẳng ngắn xuân ân cả<br>Lân múa phi bay đạo đức tròn" },
    { text: "Thiên hạ thái bình", couplet: "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm" },
    { text: "Quốc thái dân an", couplet: "Đào hồng nở thắm tươi xuân mới<br>Hạc bay lượn múa cõi trần gian" },
    { text: "Lộc tới nhà đầy", couplet: "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình" },
    { text: "Học hành tiến bộ", couplet: "Xuân về bút nghiên thêm hương sắc<br>Tết đến sách vở nở muôn hoa" },
    { text: "Thi đỗ đầu bảng", couplet: "Bút sa nghiên khói vẽ xuân mới<br>Sách mở trang vàng hiện lộc thiêng" },
    { text: "Vàng bạc đầy nhà", couplet: "Vàng về nhà đầy như nước chảy<br>Bạc tới cửa rộng tựa sông trào" },
    { text: "Buôn may bán đắt", couplet: "Buôn bán hanh thông xuân ấm áp<br>Mua sắm như ý Tết thịnh vượng" },
    { text: "Tiền tài dư dả", couplet: "Tiền vào túi đầy như mưa xuống<br>Tài chất kho cao tựa núi chồng" },
    { text: "Làm ăn phát đạt", couplet: "Làm lụng siêng năng xuân phúc lộc<br>Ăn uống no đầy Tết an khang" },
    { text: "Sống lâu trăm tuổi", couplet: "Sống lâu như núi cao vững chãi<br>Trăm tuổi như biển rộng bao la" },
    { text: "Khỏe mạnh bền lâu", couplet: "Khỏe như voi chúa xuân tràn đầy<br>Mạnh như cọp thần Tết dồi dào" },
    { text: "Luôn vui tươi mới", couplet: "Luôn cười tươi như xuân về sớm<br>Vui sống khỏe như lộc xuống đầy" },
    { text: "Yêu thương sum họp", couplet: "Yêu nhau sum vầy xuân ấm áp<br>Thương gia đoàn tụ Tết an vui" },
    { text: "Mọi điều như ý muốn", couplet: "Mọi việc hanh thông xuân tươi thắm<br>Điều chi như ý Tết rộn ràng" },
    { text: "Cả nhà sum vầy", couplet: "Cả gia sum họp xuân về sớm<br>Nhà đầy tiếng cười Tết tươi vui" },
    { text: "Con cháu đầy đàn", couplet: "Con ngoan cháu thảo xuân phúc lộc<br>Đầy nhà đầy cửa Tết an khang" },
    { text: "Vợ chồng hòa thuận", couplet: "Vợ hiền chồng tốt xuân sum vầy<br>Thuận hòa êm ấm Tết an lành" },
    { text: "Tiền nhiều của nhiều", couplet: "Tiền về như lá mùa thu rụng<br>Của đến như mưa xuân tháng ba" },
    { text: "Nhà cao cửa rộng", couplet: "Nhà lầu cao vút xuân phúc lộc<br>Cửa rộng mở toang Tết tài lộc" },
    { text: "Xe hơi đầy gara", couplet: "Xe sang lăn bánh xuân rộn ràng<br>Hơi xăng đầy bình Tết thịnh vượng" },
    { text: "Kinh doanh hanh thông", couplet: "Kinh doanh thuận lợi xuân ấm áp<br>Thương mại phát đạt Tết sum vầy" },
    { text: "Thăng chức tăng lương", couplet: "Thăng quan tiến chức xuân rạng rỡ<br>Tăng lương nhận thưởng Tết đầm ấm" },
    { text: "Gặp nhiều may mắn", couplet: "Gặp lộc gặp tài xuân hanh thông<br>Nhiều phúc nhiều thọ Tết an khang" },
    { text: "Điều gì cũng tốt", couplet: "Điều chi cũng tốt xuân về sớm<br>Gì cũng hanh thông Tết an vui" },
    { text: "Luôn gặp quý nhân", couplet: "Luôn gặp quý nhân xuân phúc lộc<br>Thường có ân nhân Tết tài lộc" },
    { text: "Công việc thuận lợi", couplet: "Công thành danh toại xuân rộn ràng<br>Việc thuận lời hay Tết sum vầy" },
    { text: "Tình duyên viên mãn", couplet: "Tình như mật ngọt xuân ấm áp<br>Duyên như chỉ hồng Tết đầm ấm" },
    { text: "Tài năng xuất chúng", couplet: "Tài cao vút tận mây xanh rộng<br>Năng lực phi thường núi cao vời" },
    { text: "Học giỏi thi đỗ", couplet: "Học vấn cao siêu xuân thịnh vượng<br>Thi đậu đầu bảng Tết vinh quang" },
    { text: "Mọi người yêu quý", couplet: "Mọi người yêu mến xuân ấm áp<br>Ai cũng quý trọng Tết an vui" }
];

// ========== GAME STATE ==========
let gameActive = false;
let collectedCount = 0;
let timeLeft = 30;
let timerInterval = null;
let spawnInterval = null;
let totalEverCollected = parseInt(localStorage.getItem('totalCollected') || '0');

// ========== SCREEN MANAGEMENT ==========
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

// ========== START GAME ==========
function startGame() {
    if (navigator.vibrate) navigator.vibrate(50);
    
    // Reset
    gameActive = true;
    collectedCount = 0;
    timeLeft = 30;
    
    document.getElementById('collected').textContent = collectedCount;
    document.getElementById('timer').textContent = timeLeft;
    
    // Clear old items
    document.querySelectorAll('.falling-item').forEach(el => el.remove());
    
    showScreen('gameScreen');
    
    // Start timer
    timerInterval = setInterval(() => {
        timeLeft--;
        const timerEl = document.getElementById('timer');
        timerEl.textContent = timeLeft;
        
        if (timeLeft <= 10) {
            timerEl.parentElement.classList.add('timer-warning');
        }
        
        if (timeLeft <= 0) {
            endGame();
        }
    }, 1000);
    
    // Start spawning items
    spawnInterval = setInterval(() => {
        if (gameActive) {
            spawnItem();
        }
    }, isMobile ? 800 : 600);
    
    // Spawn initial items
    for (let i = 0; i < 3; i++) {
        setTimeout(() => spawnItem(), i * 300);
    }
}

// ========== SPAWN FALLING ITEM ==========
function spawnItem() {
    const item = document.createElement('div');
    item.className = 'falling-item';
    
    const isEnvelope = Math.random() > 0.4;
    const itemContent = document.createElement('div');
    itemContent.className = isEnvelope ? 'item-envelope' : 'item-scroll';
    itemContent.textContent = isEnvelope ? '福' : '📜';
    
    item.appendChild(itemContent);
    
    const startX = Math.random() * (window.innerWidth - 60) + 10;
    item.style.left = startX + 'px';
    item.style.top = '-80px';
    item.style.zIndex = Math.floor(Math.random() * 20) + 40; // Depth layering
    
    const duration = isMobile ? (4 + Math.random() * 3) : (3.5 + Math.random() * 2.5);
    const rotation = (Math.random() - 0.5) * 720;
    
    item.style.animationDuration = duration + 's';
    item.style.setProperty('--rotation', rotation + 'deg');
    
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    item.dataset.blessing = JSON.stringify(blessing);
    
    item.addEventListener('click', () => collectItem(item, blessing));
    
    document.getElementById('gameContainer').appendChild(item);
    
    setTimeout(() => {
        if (item.parentElement && !item.classList.contains('collected')) {
            item.remove();
        }
    }, duration * 1000 + 200);
}

// ========== COLLECT ITEM ==========
function collectItem(item, blessing) {
    if (item.classList.contains('collected')) return;
    
    if (navigator.vibrate) navigator.vibrate([20, 10, 20]);
    
    item.classList.add('collected');
    
    collectedCount++;
    totalEverCollected++;
    
    document.getElementById('collected').textContent = collectedCount;
    localStorage.setItem('totalCollected', totalEverCollected);
    
    showBlessing(blessing);
    
    setTimeout(() => item.remove(), 500);
}

// ========== SHOW BLESSING POPUP ==========
function showBlessing(blessing) {
    const popup = document.getElementById('blessingPopup');
    const text = document.getElementById('popupText');
    
    text.innerHTML = `
        ${blessing.text}
        <div class="popup-couplet">${blessing.couplet}</div>
    `;
    
    popup.classList.remove('show');
    void popup.offsetWidth;
    popup.classList.add('show');
    
    setTimeout(() => {
        popup.classList.remove('show');
    }, 3000);
}

// ========== END GAME ==========
function endGame() {
    gameActive = false;
    
    clearInterval(timerInterval);
    clearInterval(spawnInterval);
    
    document.querySelectorAll('.falling-item').forEach(el => {
        if (!el.classList.contains('collected')) {
            el.remove();
        }
    });
    
    document.getElementById('finalCollected').textContent = collectedCount;
    document.getElementById('totalEver').textContent = totalEverCollected;
    
    let endMessage = '';
    if (collectedCount >= 20) {
        endMessage = '🎊 Xuất sắc! Năm mới phát tài phát lộc!';
    } else if (collectedCount >= 15) {
        endMessage = '🌟 Tuyệt vời! An khang thịnh vượng!';
    } else if (collectedCount >= 10) {
        endMessage = '✨ Tốt lắm! Vạn sự như ý!';
    } else if (collectedCount >= 5) {
        endMessage = '🌸 Khá đấy! Chúc mừng năm mới!';
    } else {
        endMessage = '🧧 Cố gắng lên! Xuân về ngàn lộc!';
    }
    
    document.getElementById('endBlessing').textContent = endMessage;
    
    setTimeout(() => {
        showScreen('endScreen');
    }, 500);
}

// ========== RESTART GAME ==========
function restartGame() {
    if (navigator.vibrate) navigator.vibrate(50);
    
    document.getElementById('timer').parentElement.classList.remove('timer-warning');
    
    showScreen('introScreen');
}

console.log("✅ GAME READY - COLLECTING MODE");

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)