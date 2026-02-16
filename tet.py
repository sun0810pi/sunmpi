import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="🧧 Tết Bính Ngọ 2026", page_icon="🧧")

# ===== OPTIMIZED VERSION WITH GAME ELEMENTS =====
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
    background: linear-gradient(135deg, #ff7700 0%, #ffaa00 30%, #ffdd00 50%, #ff9900 70%, #ff6600 100%);
    background-size: 400% 400%;
    animation: bgFlow 20s ease infinite;
    min-height: 100vh;
    position: relative;
    touch-action: none;
}

@keyframes bgFlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== CANVAS LAYER ========== */
#effectsCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5;
}

/* ========== FLOATERS ========== */
.floaters {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
}

.floater {
    position: absolute;
    font-size: 24px;
    opacity: 0;
    animation: floatAnim linear infinite;
    will-change: transform, opacity;
}

@keyframes floatAnim {
    0% {
        transform: translateY(-10vh) rotate(0deg);
        opacity: 0;
    }
    10% { opacity: 0.7; }
    90% { opacity: 0.3; }
    100% {
        transform: translateY(110vh) translateX(var(--dx)) rotate(360deg);
        opacity: 0;
    }
}

/* ========== LANTERNS ========== */
.lantern {
    position: fixed;
    width: 42px;
    height: 62px;
    background: linear-gradient(180deg, #ff0000, #cc0000, #ff0000);
    border-radius: 0 0 21px 21px;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.7);
    pointer-events: none;
    z-index: 3;
    animation: lanternSwing 3.6s ease-in-out infinite;
    will-change: transform;
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

@keyframes lanternSwing {
    0%, 100% { transform: rotate(-5deg); }
    50% { transform: rotate(5deg); }
}

/* ========== MAIN CONTAINER ========== */
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 20;
    width: 90%;
    max-width: 600px;
}

.title {
    font-size: clamp(32px, 8vw, 72px);
    font-weight: 900;
    background: linear-gradient(90deg, #ff0000, #ffd700, #ff0000);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 35px;
    animation: titleShine 3.2s ease infinite;
    letter-spacing: 3px;
    filter: drop-shadow(0 0 40px rgba(255, 215, 0, 0.85));
}

@keyframes titleShine {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== ENVELOPE ========== */
.envelope-wrapper {
    perspective: 1500px;
    margin: 28px 0;
}

.envelope {
    width: min(35vw, 190px);
    height: min(46vw, 260px);
    position: relative;
    cursor: pointer;
    margin: 0 auto;
    transform-style: preserve-3d;
    transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.envelope:hover {
    transform: scale(1.12);
}

.envelope:active {
    transform: scale(0.96);
}

.envelope.opening {
    animation: envelopeShake 0.5s ease-out, envelopeOpen 1.2s 0.5s ease-out forwards;
}

@keyframes envelopeShake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-8px) rotate(-3deg); }
    75% { transform: translateX(8px) rotate(3deg); }
}

@keyframes envelopeOpen {
    0% { transform: rotateX(0deg); }
    40% { transform: rotateX(-15deg) scale(1.1); }
    100% { transform: rotateX(0deg) scale(1); }
}

.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff1744 50%, #d32f2f 100%);
    border-radius: 12px;
    position: relative;
    box-shadow: 
        0 25px 65px rgba(0, 0, 0, 0.55),
        0 0 75px rgba(255, 215, 0, 0.65);
    overflow: hidden;
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
    font-size: clamp(60px, 18vw, 90px);
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        4px 4px 0 rgba(139, 0, 0, 0.5);
    animation: fuPulse 2.5s ease-in-out infinite;
}

@keyframes fuPulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.08); }
}

.light-burst {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 200%;
    height: 200%;
    transform: translate(-50%, -50%) scale(0);
    background: radial-gradient(circle, rgba(255, 215, 0, 0.8) 0%, transparent 70%);
    pointer-events: none;
    opacity: 0;
}

.light-burst.active {
    animation: burstAnim 1s ease-out forwards;
}

@keyframes burstAnim {
    0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -50%) scale(1.5);
        opacity: 0;
    }
}

.subtext {
    margin-top: 32px;
    font-size: clamp(18px, 4.5vw, 24px);
    color: white;
    font-weight: 800;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.9), 2px 2px 5px rgba(0, 0, 0, 0.6);
}

/* ========== COMBO STREAK ========== */
.combo-display {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    font-size: 48px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        4px 4px 0 rgba(139, 0, 0, 0.5);
    pointer-events: none;
    z-index: 1000;
    opacity: 0;
}

.combo-display.active {
    animation: comboAnim 1s ease-out forwards;
}

@keyframes comboAnim {
    0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 0;
    }
    20% {
        transform: translate(-50%, -50%) scale(1.3);
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -80%) scale(1);
        opacity: 0;
    }
}

/* ========== STATS BAR ========== */
.stats-bar {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 15px;
    z-index: 500;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 90%;
}

.stat-item {
    background: rgba(211, 47, 47, 0.9);
    border: 3px solid gold;
    border-radius: 30px;
    padding: 10px 22px;
    color: gold;
    font-weight: 800;
    font-size: clamp(14px, 3.5vw, 17px);
    box-shadow: 0 6px 25px rgba(211, 47, 47, 0.6);
    white-space: nowrap;
}

.stat-num {
    font-size: clamp(20px, 5vw, 26px);
    font-weight: 900;
    margin: 0 5px;
}

/* ========== SCROLL POPUP (MOBILE OPTIMIZED) ========== */
.scroll {
    position: fixed;
    width: min(82vw, 340px);
    min-height: 160px;
    pointer-events: none;
    z-index: 999;
    animation: scrollShow 4s ease-out forwards;
}

@keyframes scrollShow {
    0% {
        transform: translateY(40px) scale(0.6) rotate(-8deg);
        opacity: 0;
    }
    16% {
        transform: translateY(0) scale(1) rotate(0deg);
        opacity: 1;
    }
    86% {
        opacity: 1;
    }
    100% {
        transform: translateY(-30px) scale(0.9) rotate(-2deg);
        opacity: 0;
    }
}

.scroll-paper {
    background: linear-gradient(180deg, #7f0000, #b71c1c, #c62828, #d32f2f, #c62828, #b71c1c, #7f0000);
    border: 3px solid gold;
    border-radius: 12px;
    padding: 20px 16px;
    position: relative;
    box-shadow: 
        0 18px 50px rgba(0, 0, 0, 0.7),
        0 0 40px rgba(255, 215, 0, 0.8);
}

.scroll-text {
    color: gold;
    font-size: clamp(18px, 4.5vw, 22px);
    font-weight: 800;
    text-align: center;
    line-height: 1.6;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.9), 2px 2px 4px rgba(0, 0, 0, 0.75);
}

.scroll-couplet {
    margin-top: 14px;
    padding-top: 14px;
    border-top: 2px solid rgba(255, 215, 0, 0.6);
    font-size: clamp(15px, 4vw, 18px);
    font-style: italic;
    line-height: 1.8;
}

/* ========== MUSIC BUTTON ========== */
.music-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: rgba(211, 47, 47, 0.9);
    border: 3px solid gold;
    border-radius: 35px;
    padding: 12px 24px;
    color: gold;
    font-weight: 800;
    font-size: clamp(14px, 3.2vw, 17px);
    cursor: pointer;
    z-index: 500;
    transition: transform 0.3s ease;
    box-shadow: 0 6px 26px rgba(211, 47, 47, 0.6);
    user-select: none;
}

.music-btn:hover {
    transform: scale(1.1);
}

.music-btn:active {
    transform: scale(0.95);
}

/* ========== MOBILE OPTIMIZATIONS ========== */
@media (max-width: 768px) {
    .envelope {
        width: 150px;
        height: 200px;
    }
    
    .title {
        font-size: 32px;
        margin-bottom: 28px;
        letter-spacing: 2px;
    }
    
    .subtext {
        font-size: 18px;
        margin-top: 28px;
    }
    
    .stats-bar {
        top: 15px;
        gap: 10px;
    }
    
    .stat-item {
        padding: 8px 18px;
    }
    
    .scroll {
        width: min(85vw, 300px);
        min-height: 140px;
    }
    
    .scroll-paper {
        padding: 18px 14px;
    }
    
    .music-btn {
        bottom: 15px;
        right: 15px;
        padding: 10px 20px;
    }
}

@media (max-width: 480px) {
    .stats-bar {
        gap: 8px;
    }
    
    .stat-item {
        padding: 6px 14px;
        font-size: 13px;
    }
    
    .stat-num {
        font-size: 18px;
    }
}

</style>
</head>

<body>

<!-- Canvas for Particles -->
<canvas id="effectsCanvas"></canvas>

<!-- Floaters -->
<div class="floaters" id="floaters"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Stats Bar -->
<div class="stats-bar">
    <div class="stat-item">
        🎊 Phúc: <span class="stat-num" id="counter">0</span>
    </div>
    <div class="stat-item">
        🔥 Combo: <span class="stat-num" id="combo">0</span>
    </div>
    <div class="stat-item">
        ⭐ Max: <span class="stat-num" id="maxCombo">0</span>
    </div>
</div>

<!-- Combo Display -->
<div class="combo-display" id="comboDisplay"></div>

<!-- Main Content -->
<div class="container">
    <div class="title">Tết Bính Ngọ 2026</div>
    
    <div class="envelope-wrapper">
        <div class="envelope" id="envelope">
            <div class="envelope-body">
                <div class="envelope-border"></div>
                <div class="envelope-fu">福</div>
                <div class="light-burst" id="lightBurst"></div>
            </div>
        </div>
    </div>
    
    <div class="subtext">🦁 Nhấn Nhận Phúc Lộc 🦁</div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn">🎵 Nhạc Tết</div>

<!-- Lazy-loaded Audio -->
<audio id="music" loop preload="none">
    <source src="tet.mp3" type="audio/mp3">
</audio>

<script>

console.log("🎊 TẾT APP - ULTRA OPTIMIZED");

// ========== DEVICE DETECTION ==========
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent) || window.innerWidth < 768;
const PERF_SCALE = isMobile ? 0.35 : 1;

console.log(`📱 Device: ${isMobile ? 'Mobile' : 'Desktop'} | Scale: ${PERF_SCALE}`);

// ========== CANVAS SETUP ==========
const canvas = document.getElementById('effectsCanvas');
const ctx = canvas.getContext('2d', { alpha: true, desynchronized: true });

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// ========== PARTICLE SYSTEM ==========
class Particle {
    constructor(x, y, type) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.life = 1;
        
        const angle = Math.random() * Math.PI * 2;
        const speed = type === 'lion' ? 3 + Math.random() * 2 : 
                      type === 'money' ? 2 + Math.random() * 1.5 :
                      1.5 + Math.random() * 1;
        
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed - (type === 'lion' ? 2 : 1);
        this.rotation = Math.random() * Math.PI * 2;
        this.rotSpeed = (Math.random() - 0.5) * 0.2;
        this.size = type === 'lion' ? 28 : type === 'money' ? 22 : 7;
        this.color = type === 'firework' ? ['#ffd700', '#ff0000', '#ffcc00', '#ff1744'][Math.floor(Math.random() * 4)] : null;
    }
    
    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += 0.08;
        this.rotation += this.rotSpeed;
        this.life -= 0.012;
        return this.life > 0;
    }
    
    draw() {
        ctx.save();
        ctx.globalAlpha = this.life * 0.9;
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        
        if (this.type === 'lion') {
            ctx.font = `${this.size}px Arial`;
            ctx.fillText('🦁', -this.size/2, this.size/2);
        } else if (this.type === 'money') {
            ctx.font = `${this.size}px Arial`;
            ctx.fillText('💵', -this.size/2, this.size/2);
        } else if (this.type === 'firework') {
            ctx.fillStyle = this.color;
            ctx.shadowBlur = 12;
            ctx.shadowColor = this.color;
            ctx.beginPath();
            ctx.arc(0, 0, this.size, 0, Math.PI * 2);
            ctx.fill();
        } else if (this.type === 'confetti') {
            const shapes = ['●', '■', '▲', '◆'];
            const colors = ['#ff0000', '#ffd700', '#ff6b00'];
            ctx.fillStyle = colors[Math.floor(Math.random() * colors.length)];
            ctx.font = `${this.size * 2}px Arial`;
            ctx.fillText(shapes[Math.floor(Math.random() * shapes.length)], -this.size, this.size);
        }
        
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

// ========== SPAWN EFFECTS ==========
function spawnLions(x, y) {
    const count = Math.floor(8 * PERF_SCALE);
    for (let i = 0; i < count; i++) {
        particles.push(new Particle(x, y, 'lion'));
    }
}

function spawnMoney(x, y) {
    const count = Math.floor(10 * PERF_SCALE);
    for (let i = 0; i < count; i++) {
        particles.push(new Particle(x, y, 'money'));
    }
}

function spawnFireworks(x, y) {
    const count = Math.floor(20 * PERF_SCALE);
    for (let i = 0; i < count; i++) {
        particles.push(new Particle(x, y, 'firework'));
    }
}

function spawnConfetti(x, y) {
    const count = Math.floor(15 * PERF_SCALE);
    for (let i = 0; i < count; i++) {
        particles.push(new Particle(x, y, 'confetti'));
    }
}

// ========== INIT FLOATERS ==========
const floaters = document.getElementById('floaters');
const icons = ['🌸', '🌺', '🏵️', '💮'];
const floaterCount = isMobile ? 12 : 22;

for (let i = 0; i < floaterCount; i++) {
    const el = document.createElement('div');
    el.className = 'floater';
    el.textContent = icons[Math.floor(Math.random() * icons.length)];
    el.style.left = Math.random() * 100 + '%';
    el.style.setProperty('--dx', (Math.random() - 0.5) * 300 + 'px');
    el.style.animationDuration = (14 + Math.random() * 14) + 's';
    el.style.animationDelay = Math.random() * 8 + 's';
    floaters.appendChild(el);
}

// ========== INIT LANTERNS ==========
const lanternsDiv = document.getElementById('lanterns');
const lanternCount = isMobile ? 3 : 5;
const lPos = [
    { left: '10%', top: '8%' },
    { left: '50%', top: '4%' },
    { left: '90%', top: '10%' },
    { left: '25%', top: '6%' },
    { left: '75%', top: '9%' }
];

for (let i = 0; i < lanternCount; i++) {
    const lan = document.createElement('div');
    lan.className = 'lantern';
    lan.style.left = lPos[i].left;
    lan.style.top = lPos[i].top;
    lan.style.animationDelay = (i * 0.3) + 's';
    lanternsDiv.appendChild(lan);
}

// ========== MUSIC ==========
let playing = false;
const music = document.getElementById('music');
const musicBtn = document.getElementById('musicBtn');

musicBtn.onclick = () => {
    if (playing) {
        music.pause();
        musicBtn.textContent = '🎵 Nhạc Tết (Tắt)';
        playing = false;
    } else {
        music.load();
        music.play().then(() => {
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
            playing = true;
        }).catch(e => {
            console.log("⚠️ Play error:", e);
            musicBtn.textContent = '🎵 Không có nhạc';
            musicBtn.style.opacity = '0.5';
        });
    }
};

// ========== CONTENT ==========
const blessings = [
    "Chúc mừng năm mới", "An khang thịnh vượng", "Vạn sự như ý",
    "Tấn tài tấn lộc", "Phúc lộc đầy nhà", "Sức khỏe dồi dào",
    "Tiền vô như nước", "Gia đình hạnh phúc", "Công danh phát đạt",
    "Xuân về ngàn lộc", "Trăm năm hạnh phúc", "Vạn sự cát tường",
    "Tài lộc tràn trề", "Phát tài phát lộc", "Như ý cát tường",
    "Thiên hạ thái bình", "Quốc thái dân an", "Lộc tới nhà đầy"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm",
    "Trúc xanh thẳng ngắn xuân ân cả<br>Lân múa phi bay đạo đức tròn"
];

// ========== GAME STATS ==========
let count = 0;
let combo = 0;
let maxCombo = 0;
let lastClickTime = 0;
const comboTimeout = 2000; // 2 seconds to maintain combo

const counter = document.getElementById('counter');
const comboEl = document.getElementById('combo');
const maxComboEl = document.getElementById('maxCombo');
const comboDisplay = document.getElementById('comboDisplay');

function updateCounter() {
    count++;
    counter.textContent = count;
    
    // Combo system
    const now = Date.now();
    if (now - lastClickTime < comboTimeout) {
        combo++;
    } else {
        combo = 1;
    }
    lastClickTime = now;
    
    comboEl.textContent = combo;
    
    if (combo > maxCombo) {
        maxCombo = combo;
        maxComboEl.textContent = maxCombo;
    }
    
    // Show combo text for milestones
    if (combo === 5) showComboText("🔥 HOT STREAK!");
    else if (combo === 10) showComboText("🌟 AMAZING!");
    else if (combo === 20) showComboText("💎 LEGENDARY!");
    else if (combo === 50) showComboText("👑 GOD MODE!");
    else if (combo > 50 && combo % 25 === 0) showComboText(`🚀 ${combo}X COMBO!`);
}

function showComboText(text) {
    comboDisplay.textContent = text;
    comboDisplay.classList.remove('active');
    void comboDisplay.offsetWidth; // Force reflow
    comboDisplay.classList.add('active');
    
    setTimeout(() => {
        comboDisplay.classList.remove('active');
    }, 1000);
}

// Reset combo after timeout
setInterval(() => {
    const now = Date.now();
    if (combo > 0 && now - lastClickTime > comboTimeout) {
        combo = 0;
        comboEl.textContent = combo;
    }
}, 100);

// ========== SCROLL POPUP (MOBILE OPTIMIZED) ==========
function createScroll() {
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    // Mobile-friendly positioning with safe margins
    const margin = isMobile ? 50 : 100;
    const scrollWidth = isMobile ? Math.min(window.innerWidth * 0.85, 300) : Math.min(window.innerWidth * 0.82, 340);
    const scrollHeight = isMobile ? 140 : 160;
    
    const maxX = window.innerWidth - scrollWidth - margin;
    const maxY = window.innerHeight - scrollHeight - margin;
    
    const x = Math.max(margin, Math.min(maxX, Math.random() * (window.innerWidth - scrollWidth)));
    const y = Math.max(margin, Math.min(maxY, Math.random() * (window.innerHeight - scrollHeight)));
    
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
    
    document.body.appendChild(scroll);
    setTimeout(() => scroll.remove(), 4000);
}

// ========== ENVELOPE INTERACTION ==========
const envelope = document.getElementById('envelope');
const lightBurst = document.getElementById('lightBurst');

envelope.addEventListener('click', function(e) {
    updateCounter();
    
    // Haptic feedback
    if (navigator.vibrate) {
        navigator.vibrate(combo > 5 ? [30, 10, 30] : 40);
    }
    
    // Cinematic opening
    this.classList.add('opening');
    lightBurst.classList.add('active');
    
    setTimeout(() => {
        this.classList.remove('opening');
        lightBurst.classList.remove('active');
    }, 1700);
    
    // Auto-play music on first click
    if (!playing && count === 1) {
        music.load();
        music.play().then(() => {
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
        }).catch(e => {});
    }
    
    // Get position
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    
    // Spawn particles (more for combos)
    const multiplier = Math.min(combo / 5 + 1, 2.5);
    spawnLions(cx, cy);
    spawnMoney(cx, cy);
    spawnFireworks(cx, cy);
    if (combo > 3) spawnConfetti(cx, cy);
    
    // Create scrolls (scale with combo but cap for performance)
    const baseScrolls = isMobile ? (count === 1 ? 3 : 2) : (count === 1 ? 5 : 3);
    const comboBonus = Math.floor(combo / 5);
    const numScrolls = Math.min(baseScrolls + comboBonus, isMobile ? 5 : 8);
    
    let scrollCount = 0;
    const interval = setInterval(() => {
        createScroll();
        scrollCount++;
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
        }
    }, isMobile ? 320 : 260);
});

console.log("✅ APP READY - GAME MODE ENABLED");

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)