import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="🧧 Tết Bính Ngọ 2026", page_icon="🧧")

# ===== TẾT APP WITH MEMORY GAME - CUTE & OPTIMIZED =====
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
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
    font-family: 'Georgia', serif;
    background: linear-gradient(135deg, #FFE5B4 0%, #FFD4A3 30%, #FFC89A 50%, #FFB88C 70%, #FFA07A 100%);
    background-size: 400% 400%;
    animation: bgFlow 25s ease infinite;
    min-height: 100vh;
    position: relative;
    touch-action: none;
}

@keyframes bgFlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== SPARKLES (LIGHT) ========== */
.sparkles {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}

.sparkle {
    position: absolute;
    font-size: 16px;
    opacity: 0;
    animation: sparkleAnim linear infinite;
}

@keyframes sparkleAnim {
    0% {
        transform: translateY(-5vh) scale(0);
        opacity: 0;
    }
    20% { opacity: 0.6; }
    80% { opacity: 0.3; }
    100% {
        transform: translateY(105vh) translateX(var(--dx)) scale(1);
        opacity: 0;
    }
}

/* ========== LANTERNS (CUTE) ========== */
.lantern {
    position: fixed;
    width: 36px;
    height: 52px;
    background: linear-gradient(180deg, #FF6B6B, #EE5A5A, #FF6B6B);
    border-radius: 0 0 18px 18px;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
    pointer-events: none;
    z-index: 2;
    animation: lanternSwing 3.8s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #FFD700;
    font-size: 20px;
    font-weight: 900;
}

@keyframes lanternSwing {
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
    transition: opacity 0.5s ease;
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
}

.intro-title {
    font-size: clamp(36px, 9vw, 68px);
    font-weight: 900;
    background: linear-gradient(90deg, #FF6B6B, #FFD700, #FF6B6B);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 40px;
    animation: titleShine 3s ease infinite;
    letter-spacing: 2px;
    filter: drop-shadow(0 0 25px rgba(255, 215, 0, 0.6));
}

@keyframes titleShine {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.envelope-wrapper {
    perspective: 1500px;
    margin: 30px 0;
}

.main-envelope {
    width: min(35vw, 180px);
    height: min(46vw, 240px);
    position: relative;
    cursor: pointer;
    margin: 0 auto;
    transform-style: preserve-3d;
    transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.main-envelope:hover {
    transform: scale(1.1);
}

.main-envelope:active {
    transform: scale(0.95);
}

.main-envelope.opening {
    animation: envelopeShake 0.4s ease-out, envelopeOpen 1s 0.4s ease-out forwards;
}

@keyframes envelopeShake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-6px) rotate(-2deg); }
    75% { transform: translateX(6px) rotate(2deg); }
}

@keyframes envelopeOpen {
    0% { transform: rotateX(0deg); }
    40% { transform: rotateX(-12deg) scale(1.08); }
    100% { transform: rotateX(0deg) scale(1); }
}

.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 50%, #FF6B6B 100%);
    border-radius: 10px;
    position: relative;
    box-shadow: 
        0 20px 50px rgba(0, 0, 0, 0.35),
        0 0 50px rgba(255, 215, 0, 0.4);
    overflow: hidden;
}

.envelope-border {
    position: absolute;
    top: 10px;
    left: 10px;
    right: 10px;
    bottom: 10px;
    border: 2px solid #FFD700;
    border-radius: 8px;
}

.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: clamp(55px, 16vw, 80px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.8),
        0 0 35px rgba(255, 215, 0, 0.6),
        3px 3px 0 rgba(139, 0, 0, 0.3);
    animation: fuPulse 2.5s ease-in-out infinite;
}

@keyframes fuPulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.06); }
}

.intro-text {
    margin-top: 35px;
    font-size: clamp(18px, 4.5vw, 24px);
    color: #8B4513;
    font-weight: 700;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
}

/* ========== MEMORY GAME SCREEN ========== */
.game-container {
    width: 90%;
    max-width: 480px;
    padding: 20px;
}

.game-header {
    text-align: center;
    margin-bottom: 25px;
}

.game-title {
    font-size: clamp(24px, 6vw, 32px);
    font-weight: 900;
    color: #FF6B6B;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.6), 2px 2px 4px rgba(139, 69, 19, 0.3);
    margin-bottom: 15px;
}

.game-stats {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}

.stat-box {
    background: rgba(255, 255, 255, 0.85);
    border: 2px solid #FFD700;
    border-radius: 20px;
    padding: 8px 18px;
    font-size: clamp(14px, 3.5vw, 16px);
    font-weight: 700;
    color: #8B4513;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.stat-number {
    font-size: clamp(18px, 4.5vw, 22px);
    color: #FF6B6B;
    margin: 0 4px;
}

/* ========== CARD GRID ========== */
.card-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    max-width: 100%;
    margin: 0 auto;
}

.card {
    aspect-ratio: 0.7;
    position: relative;
    cursor: pointer;
    transform-style: preserve-3d;
    transition: transform 0.25s ease;
}

.card.flipped {
    transform: rotateY(180deg);
}

.card.matched {
    opacity: 0.6;
    pointer-events: none;
}

.card-face {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.card-back {
    background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 50%, #FF6B6B 100%);
    border: 2px solid #FFD700;
}

.card-back-icon {
    font-size: clamp(28px, 8vw, 40px);
}

.card-front {
    background: linear-gradient(135deg, #FFF8DC 0%, #FFFAF0 50%, #FFF8DC 100%);
    border: 2px solid #FFD700;
    transform: rotateY(180deg);
}

.card-content {
    font-size: clamp(24px, 7vw, 36px);
    font-weight: 900;
    text-align: center;
    padding: 8px;
    line-height: 1.3;
}

.card-content.emoji {
    font-size: clamp(32px, 9vw, 48px);
}

/* ========== WIN SCREEN ========== */
.win-container {
    text-align: center;
    width: 90%;
    max-width: 450px;
}

.win-scroll {
    background: linear-gradient(180deg, #8B0000, #B71C1C, #D32F2F, #B71C1C, #8B0000);
    border: 3px solid #FFD700;
    border-radius: 15px;
    padding: 30px 20px;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.5),
        0 0 40px rgba(255, 215, 0, 0.6);
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

.win-title {
    font-size: clamp(28px, 7vw, 40px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 0 0 25px rgba(255, 215, 0, 0.9), 3px 3px 5px rgba(0, 0, 0, 0.5);
    margin-bottom: 20px;
}

.win-blessing {
    color: #FFD700;
    font-size: clamp(18px, 4.5vw, 22px);
    font-weight: 700;
    line-height: 1.7;
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.8), 2px 2px 4px rgba(0, 0, 0, 0.6);
    margin-bottom: 18px;
}

.win-couplet {
    color: #FFD700;
    font-size: clamp(15px, 4vw, 18px);
    font-style: italic;
    line-height: 1.8;
    padding-top: 18px;
    border-top: 2px solid rgba(255, 215, 0, 0.5);
    text-shadow: 0 0 12px rgba(255, 215, 0, 0.7), 2px 2px 3px rgba(0, 0, 0, 0.5);
}

.win-stats {
    margin-top: 25px;
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}

.win-stat {
    background: rgba(255, 215, 0, 0.2);
    border: 2px solid rgba(255, 215, 0, 0.6);
    border-radius: 20px;
    padding: 8px 18px;
    font-size: clamp(14px, 3.5vw, 16px);
    font-weight: 700;
    color: #FFD700;
}

.play-again-btn {
    margin-top: 25px;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    border-radius: 30px;
    padding: 14px 35px;
    font-size: clamp(16px, 4vw, 20px);
    font-weight: 800;
    color: #8B0000;
    cursor: pointer;
    transition: transform 0.3s ease;
    box-shadow: 0 6px 20px rgba(255, 165, 0, 0.4);
}

.play-again-btn:hover {
    transform: scale(1.08);
}

.play-again-btn:active {
    transform: scale(0.95);
}

/* ========== CANVAS ========== */
#effectsCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5;
}

/* ========== COMBO DISPLAY ========== */
.combo-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    font-size: clamp(32px, 8vw, 48px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 1),
        0 0 40px rgba(255, 215, 0, 0.8),
        3px 3px 0 rgba(139, 0, 0, 0.4);
    pointer-events: none;
    z-index: 1000;
    opacity: 0;
}

.combo-popup.show {
    animation: comboAnim 1s ease-out forwards;
}

@keyframes comboAnim {
    0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 0;
    }
    20% {
        transform: translate(-50%, -50%) scale(1.2);
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -70%) scale(1);
        opacity: 0;
    }
}

/* ========== MUSIC BUTTON ========== */
.music-btn {
    position: fixed;
    bottom: 18px;
    right: 18px;
    background: rgba(255, 255, 255, 0.9);
    border: 2px solid #FFD700;
    border-radius: 30px;
    padding: 10px 20px;
    color: #8B4513;
    font-weight: 700;
    font-size: clamp(13px, 3vw, 16px);
    cursor: pointer;
    z-index: 500;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 20px rgba(255, 215, 0, 0.3);
}

.music-btn:hover {
    transform: scale(1.08);
}

.music-btn:active {
    transform: scale(0.95);
}

/* ========== MOBILE OPTIMIZATIONS ========== */
@media (max-width: 768px) {
    .main-envelope {
        width: 140px;
        height: 190px;
    }
    
    .card-grid {
        gap: 8px;
    }
    
    .game-container {
        padding: 15px;
    }
}

@media (max-width: 480px) {
    .card-grid {
        gap: 6px;
    }
    
    .game-header {
        margin-bottom: 20px;
    }
}

</style>
</head>

<body>

<!-- Canvas -->
<canvas id="effectsCanvas"></canvas>

<!-- Sparkles -->
<div class="sparkles" id="sparkles"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Combo Popup -->
<div class="combo-popup" id="comboPopup"></div>

<!-- SCREEN 1: INTRO -->
<div class="screen active" id="introScreen">
    <div class="intro-container">
        <div class="intro-title">Tết Bính Ngọ 2026</div>
        <div class="envelope-wrapper">
            <div class="main-envelope" id="mainEnvelope">
                <div class="envelope-body">
                    <div class="envelope-border"></div>
                    <div class="envelope-fu">福</div>
                </div>
            </div>
        </div>
        <div class="intro-text">🧧 Mở Lì Xì Đón Xuân 🧧</div>
    </div>
</div>

<!-- SCREEN 2: MEMORY GAME -->
<div class="screen" id="gameScreen">
    <div class="game-container">
        <div class="game-header">
            <div class="game-title">🎴 Lật Lì Xì Tết 🎴</div>
            <div class="game-stats">
                <div class="stat-box">
                    ⏱️ <span class="stat-number" id="timer">0</span>s
                </div>
                <div class="stat-box">
                    🎯 <span class="stat-number" id="moves">0</span> lượt
                </div>
                <div class="stat-box">
                    ✨ <span class="stat-number" id="matched">0</span>/8
                </div>
            </div>
        </div>
        <div class="card-grid" id="cardGrid"></div>
    </div>
</div>

<!-- SCREEN 3: WIN -->
<div class="screen" id="winScreen">
    <div class="win-container">
        <div class="win-scroll">
            <div class="win-title">🎊 Chúc Mừng! 🎊</div>
            <div class="win-blessing" id="winBlessing"></div>
            <div class="win-couplet" id="winCouplet"></div>
            <div class="win-stats">
                <div class="win-stat">
                    ⏱️ <span id="finalTime">0</span>s
                </div>
                <div class="win-stat">
                    🎯 <span id="finalMoves">0</span> lượt
                </div>
            </div>
            <button class="play-again-btn" id="playAgainBtn">
                🔄 Chơi Lại
            </button>
        </div>
    </div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn">🎵 Nhạc</div>

<!-- Audio -->
<audio id="music" loop preload="none">
    <source src="tet.mp3" type="audio/mp3">
</audio>

<script>

console.log("🧧 TẾT MEMORY GAME - CUTE & OPTIMIZED");

// ========== DEVICE DETECTION ==========
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent) || window.innerWidth < 768;
const PERF_SCALE = isMobile ? 0.3 : 1;

// ========== CANVAS SETUP ==========
const canvas = document.getElementById('effectsCanvas');
const ctx = canvas.getContext('2d', { alpha: true, desynchronized: true });

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// ========== PARTICLE SYSTEM (LIGHT) ==========
class Particle {
    constructor(x, y, type) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.life = 1;
        
        const angle = Math.random() * Math.PI * 2;
        const speed = type === 'lion' ? 2.5 + Math.random() * 1.5 : 1.5 + Math.random() * 1;
        
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed - 1.5;
        this.rotation = Math.random() * Math.PI * 2;
        this.rotSpeed = (Math.random() - 0.5) * 0.15;
        this.size = type === 'lion' ? 24 : 18;
    }
    
    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += 0.08;
        this.rotation += this.rotSpeed;
        this.life -= 0.015;
        return this.life > 0;
    }
    
    draw() {
        ctx.save();
        ctx.globalAlpha = this.life * 0.85;
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        ctx.font = `${this.size}px Arial`;
        ctx.fillText(this.type === 'lion' ? '🦁' : '🌸', -this.size/2, this.size/2);
        ctx.restore();
    }
}

let particles = [];

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles = particles.filter(p => {
        const alive = p.update();
        if (alive) p.draw();
        return alive;
    });
    requestAnimationFrame(animateParticles);
}
animateParticles();

function spawnParticles(x, y, type, count) {
    const num = Math.floor(count * PERF_SCALE);
    for (let i = 0; i < num; i++) {
        particles.push(new Particle(x, y, type));
    }
}

// ========== INIT SPARKLES ==========
const sparkles = document.getElementById('sparkles');
const sparkleIcons = ['✨', '⭐', '🌟', '💫'];
const sparkleCount = isMobile ? 10 : 18;

for (let i = 0; i < sparkleCount; i++) {
    const el = document.createElement('div');
    el.className = 'sparkle';
    el.textContent = sparkleIcons[Math.floor(Math.random() * sparkleIcons.length)];
    el.style.left = Math.random() * 100 + '%';
    el.style.setProperty('--dx', (Math.random() - 0.5) * 200 + 'px');
    el.style.animationDuration = (18 + Math.random() * 12) + 's';
    el.style.animationDelay = Math.random() * 8 + 's';
    sparkles.appendChild(el);
}

// ========== INIT LANTERNS ==========
const lanternsDiv = document.getElementById('lanterns');
const lanternCount = isMobile ? 3 : 5;
const lPos = [
    { left: '10%', top: '8%' },
    { left: '50%', top: '5%' },
    { left: '90%', top: '10%' },
    { left: '25%', top: '7%' },
    { left: '75%', top: '9%' }
];

for (let i = 0; i < lanternCount; i++) {
    const lan = document.createElement('div');
    lan.className = 'lantern';
    lan.style.left = lPos[i].left;
    lan.style.top = lPos[i].top;
    lan.style.animationDelay = (i * 0.4) + 's';
    lanternsDiv.appendChild(lan);
}

// ========== MUSIC ==========
let playing = false;
const music = document.getElementById('music');
const musicBtn = document.getElementById('musicBtn');

musicBtn.onclick = () => {
    if (playing) {
        music.pause();
        musicBtn.textContent = '🎵 Nhạc (Tắt)';
        playing = false;
    } else {
        music.load();
        music.play().then(() => {
            musicBtn.textContent = '🎵 Nhạc (Bật)';
            playing = true;
        }).catch(() => {
            musicBtn.textContent = '🎵 Không có nhạc';
            musicBtn.style.opacity = '0.6';
        });
    }
};

// ========== CONTENT ==========
const blessings = [
    "Chúc mừng năm mới", "An khang thịnh vượng", "Vạn sự như ý",
    "Tấn tài tấn lộc", "Phúc lộc đầy nhà", "Sức khỏe dồi dào",
    "Tiền vô như nước", "Gia đình hạnh phúc", "Xuân về ngàn lộc"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy"
];

// ========== CARD PAIRS ==========
const cardPairs = [
    { id: 1, content: '福', type: 'emoji' },
    { id: 2, content: '禄', type: 'emoji' },
    { id: 3, content: '🌸', type: 'emoji' },
    { id: 4, content: '🧧', type: 'emoji' },
    { id: 5, content: '🐴', type: 'emoji' },
    { id: 6, content: '🍊', type: 'emoji' },
    { id: 7, content: '🪭', type: 'emoji' },
    { id: 8, content: '🏮', type: 'emoji' }
];

// ========== GAME STATE ==========
let gameState = {
    cards: [],
    flipped: [],
    matched: [],
    moves: 0,
    timer: 0,
    timerInterval: null
};

// ========== SCREEN MANAGEMENT ==========
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

// ========== COMBO POPUP ==========
function showCombo(text) {
    const popup = document.getElementById('comboPopup');
    popup.textContent = text;
    popup.classList.remove('show');
    void popup.offsetWidth;
    popup.classList.add('show');
    setTimeout(() => popup.classList.remove('show'), 1000);
}

// ========== INTRO SCREEN ==========
const mainEnvelope = document.getElementById('mainEnvelope');

mainEnvelope.addEventListener('click', function() {
    // Haptic
    if (navigator.vibrate) navigator.vibrate(50);
    
    // Animation
    this.classList.add('opening');
    
    // Particles
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    spawnParticles(cx, cy, 'lion', 12);
    spawnParticles(cx, cy, 'flower', 15);
    
    // Start music
    if (!playing) {
        music.load();
        music.play().then(() => {
            playing = true;
            musicBtn.textContent = '🎵 Nhạc (Bật)';
        }).catch(() => {});
    }
    
    // Transition to game
    setTimeout(() => {
        showScreen('gameScreen');
        initGame();
    }, 1500);
});

// ========== GAME LOGIC ==========
function initGame() {
    gameState = {
        cards: [],
        flipped: [],
        matched: [],
        moves: 0,
        timer: 0,
        timerInterval: null
    };
    
    // Create card deck
    const deck = [...cardPairs, ...cardPairs]
        .map(card => ({ ...card, uniqueId: Math.random() }))
        .sort(() => Math.random() - 0.5);
    
    gameState.cards = deck;
    
    // Render cards
    const grid = document.getElementById('cardGrid');
    grid.innerHTML = '';
    
    deck.forEach((card, index) => {
        const cardEl = document.createElement('div');
        cardEl.className = 'card';
        cardEl.dataset.index = index;
        
        cardEl.innerHTML = `
            <div class="card-face card-back">
                <div class="card-back-icon">🧧</div>
            </div>
            <div class="card-face card-front">
                <div class="card-content ${card.type}">${card.content}</div>
            </div>
        `;
        
        cardEl.addEventListener('click', () => handleCardClick(index));
        grid.appendChild(cardEl);
    });
    
    // Start timer
    gameState.timerInterval = setInterval(() => {
        gameState.timer++;
        document.getElementById('timer').textContent = gameState.timer;
    }, 1000);
    
    updateUI();
}

function handleCardClick(index) {
    const card = gameState.cards[index];
    const cardEl = document.querySelectorAll('.card')[index];
    
    // Prevent invalid clicks
    if (gameState.flipped.length >= 2) return;
    if (gameState.flipped.includes(index)) return;
    if (gameState.matched.includes(card.id)) return;
    
    // Haptic
    if (navigator.vibrate) navigator.vibrate(20);
    
    // Flip card
    cardEl.classList.add('flipped');
    gameState.flipped.push(index);
    
    // Check for match
    if (gameState.flipped.length === 2) {
        gameState.moves++;
        updateUI();
        
        const [idx1, idx2] = gameState.flipped;
        const card1 = gameState.cards[idx1];
        const card2 = gameState.cards[idx2];
        
        if (card1.id === card2.id) {
            // Match!
            setTimeout(() => {
                handleMatch(idx1, idx2, card1.id);
            }, 400);
        } else {
            // No match
            setTimeout(() => {
                const cards = document.querySelectorAll('.card');
                cards[idx1].classList.remove('flipped');
                cards[idx2].classList.remove('flipped');
                gameState.flipped = [];
            }, 800);
        }
    }
}

function handleMatch(idx1, idx2, cardId) {
    // Mark as matched
    gameState.matched.push(cardId);
    gameState.flipped = [];
    
    const cards = document.querySelectorAll('.card');
    cards[idx1].classList.add('matched');
    cards[idx2].classList.add('matched');
    
    // Particles
    const rect1 = cards[idx1].getBoundingClientRect();
    const cx = rect1.left + rect1.width / 2;
    const cy = rect1.top + rect1.height / 2;
    spawnParticles(cx, cy, 'lion', 8);
    
    // Haptic
    if (navigator.vibrate) navigator.vibrate([30, 10, 30]);
    
    // Combo text
    const matchedCount = gameState.matched.length;
    if (matchedCount === 3) showCombo('✨ Tốt lắm!');
    if (matchedCount === 5) showCombo('🌟 Tuyệt vời!');
    if (matchedCount === 7) showCombo('🎊 Xuất sắc!');
    
    updateUI();
    
    // Check win
    if (gameState.matched.length === cardPairs.length) {
        setTimeout(() => {
            handleWin();
        }, 800);
    }
}

function updateUI() {
    document.getElementById('moves').textContent = gameState.moves;
    document.getElementById('matched').textContent = gameState.matched.length;
}

function handleWin() {
    clearInterval(gameState.timerInterval);
    
    // Set win data
    document.getElementById('finalTime').textContent = gameState.timer;
    document.getElementById('finalMoves').textContent = gameState.moves;
    document.getElementById('winBlessing').textContent = 
        blessings[Math.floor(Math.random() * blessings.length)];
    document.getElementById('winCouplet').innerHTML = 
        couplets[Math.floor(Math.random() * couplets.length)];
    
    // Show win screen
    showScreen('winScreen');
    
    // Particles
    for (let i = 0; i < 5; i++) {
        setTimeout(() => {
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            spawnParticles(x, y, 'lion', 10);
            spawnParticles(x, y, 'flower', 12);
        }, i * 300);
    }
}

// ========== PLAY AGAIN ==========
document.getElementById('playAgainBtn').addEventListener('click', () => {
    showScreen('gameScreen');
    initGame();
});

console.log("✅ GAME READY - CUTE MODE");

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)