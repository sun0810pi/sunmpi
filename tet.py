import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide", page_title="🧧 Tết Bính Ngọ 2026", page_icon="🧧")

# ===== ENCODE MUSIC =====
try:
    with open("tet.mp3", "rb") as f:
        audio_data = f.read()
        music_base64 = base64.b64encode(audio_data).decode()
except:
    music_base64 = ""

# ===== PREMIUM HTML =====
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
    font-family: 'Georgia', 'Palatino', serif;
    background: #1a0a00;
    min-height: 100vh;
    position: relative;
    cursor: default;
}

/* ========== GRADIENT BACKGROUND ========== */
.bg-gradient {
    position: fixed;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #ff6b00 0%, #ffa500 20%, #ffdd00 40%, #ff9900 60%, #ff4500 80%, #ff6b00 100%);
    background-size: 400% 400%;
    animation: gradientFlow 25s ease infinite;
    z-index: 1;
}

@keyframes gradientFlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== PAPER TEXTURE OVERLAY ========== */
.texture-overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: 
        repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255, 255, 255, 0.03) 2px, rgba(255, 255, 255, 0.03) 4px),
        repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0, 0, 0, 0.03) 2px, rgba(0, 0, 0, 0.03) 4px);
    opacity: 0.4;
    z-index: 2;
    pointer-events: none;
}

/* ========== SILK PATTERN ========== */
.silk-pattern {
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(255, 0, 0, 0.06) 0%, transparent 50%),
        radial-gradient(circle at 40% 80%, rgba(255, 215, 0, 0.05) 0%, transparent 40%);
    z-index: 3;
    pointer-events: none;
}

/* ========== VIGNETTE ========== */
.vignette {
    position: fixed;
    width: 100%;
    height: 100%;
    box-shadow: inset 0 0 150px rgba(0, 0, 0, 0.5);
    z-index: 4;
    pointer-events: none;
}

/* ========== FLOATING ELEMENTS (PARALLAX) ========== */
.float-layer {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
}

.float-layer-1 { z-index: 5; }
.float-layer-2 { z-index: 6; }
.float-layer-3 { z-index: 7; }

.floater {
    position: absolute;
    opacity: 0;
    animation: floatDown linear infinite;
    filter: drop-shadow(0 2px 8px rgba(255, 215, 0, 0.4));
}

@keyframes floatDown {
    0% {
        transform: translateY(-10vh) translateX(0) rotate(0deg) scale(0.8);
        opacity: 0;
    }
    10% { opacity: 0.7; }
    90% { opacity: 0.3; }
    100% {
        transform: translateY(110vh) translateX(var(--drift)) rotate(var(--rotate)) scale(1.1);
        opacity: 0;
    }
}

/* ========== LANTERNS ========== */
.lantern {
    position: fixed;
    width: 50px;
    height: 70px;
    background: linear-gradient(180deg, #ff0000 0%, #b71c1c 50%, #ff0000 100%);
    border-radius: 0 0 25px 25px;
    box-shadow: 
        0 0 30px rgba(255, 215, 0, 0.9),
        inset 0 5px 20px rgba(255, 255, 255, 0.3);
    pointer-events: none;
    animation: lanternSwing 4s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 12px rgba(255, 215, 0, 1);
}

.lantern::after {
    content: '';
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    width: 38px;
    height: 12px;
    background: #8b0000;
    border-radius: 6px;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.5);
}

@keyframes lanternSwing {
    0%, 100% { transform: translateX(-18px) rotate(-7deg); }
    50% { transform: translateX(18px) rotate(7deg); }
}

/* ========== MAIN CONTAINER ========== */
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 50;
}

/* ========== TITLE ========== */
.title {
    font-size: clamp(50px, 11vw, 95px);
    font-weight: 900;
    background: linear-gradient(90deg, #ff0000 0%, #ffd700 25%, #ff1744 50%, #ffd700 75%, #ff0000 100%);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 50px;
    animation: titleShimmer 4s ease infinite;
    filter: drop-shadow(0 0 50px rgba(255, 215, 0, 0.9));
    letter-spacing: 6px;
    position: relative;
}

@keyframes titleShimmer {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.title::before,
.title::after {
    content: '✨';
    position: absolute;
    font-size: 45px;
    top: 50%;
    transform: translateY(-50%);
    animation: sparkleFloat 3s ease-in-out infinite;
}

.title::before {
    left: -70px;
}

.title::after {
    right: -70px;
    animation-delay: 1.5s;
}

@keyframes sparkleFloat {
    0%, 100% { transform: translateY(-50%) scale(1); opacity: 0.6; }
    50% { transform: translateY(calc(-50% - 15px)) scale(1.3); opacity: 1; }
}

/* ========== 3D ENVELOPE WITH OPENING ========== */
.envelope-wrapper {
    perspective: 1800px;
    margin: 35px 0;
}

.envelope {
    width: 220px;
    height: 300px;
    position: relative;
    cursor: pointer;
    margin: 0 auto;
    transform-style: preserve-3d;
    transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    animation: envelopeFloat 4s ease-in-out infinite;
}

@keyframes envelopeFloat {
    0%, 100% { transform: translateY(0) rotateX(0deg); }
    50% { transform: translateY(-18px) rotateX(3deg); }
}

.envelope:hover {
    transform: scale(1.18) rotateY(12deg) translateZ(20px) !important;
    animation: none;
}

.envelope:active {
    transform: scale(0.92) !important;
}

.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff1744 30%, #f44336 50%, #ff1744 70%, #d32f2f 100%);
    border-radius: 14px;
    position: relative;
    box-shadow: 
        0 30px 80px rgba(0, 0, 0, 0.6),
        0 0 100px rgba(255, 215, 0, 0.7),
        inset 0 0 60px rgba(255, 215, 0, 0.35);
    overflow: hidden;
    transform-style: preserve-3d;
}

/* Shimmer light */
.envelope-body::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.3) 50%, transparent 70%);
    animation: shimmerSweep 4s ease-in-out infinite;
}

@keyframes shimmerSweep {
    0%, 100% { transform: translateX(-100%) translateY(-100%); }
    50% { transform: translateX(50%) translateY(50%); }
}

/* Golden frame */
.envelope-frame {
    position: absolute;
    top: 14px;
    left: 14px;
    right: 14px;
    bottom: 14px;
    border: 4px solid gold;
    border-radius: 11px;
    box-shadow: 
        inset 0 0 25px rgba(255, 215, 0, 0.6),
        0 0 15px rgba(255, 215, 0, 0.4);
}

/* 福 character with 3D depth */
.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) translateZ(15px);
    font-size: 110px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 40px rgba(255, 215, 0, 1),
        0 0 70px rgba(255, 215, 0, 0.8),
        5px 5px 0 rgba(139, 0, 0, 0.6),
        -2px -2px 0 rgba(255, 255, 255, 0.3);
    animation: fuBreath 2.8s ease-in-out infinite;
    filter: drop-shadow(0 8px 15px rgba(0, 0, 0, 0.4));
}

@keyframes fuBreath {
    0%, 100% { transform: translate(-50%, -50%) translateZ(15px) scale(1); }
    50% { transform: translate(-50%, -50%) translateZ(25px) scale(1.1); }
}

/* Decorative corners */
.corner-dec {
    position: absolute;
    width: 35px;
    height: 35px;
    background: radial-gradient(circle, gold 0%, #ffa500 100%);
    clip-path: polygon(0 0, 100% 0, 0 100%);
    box-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
    opacity: 0.9;
}

.corner-dec.tl { top: 8px; left: 8px; }
.corner-dec.tr { top: 8px; right: 8px; transform: rotate(90deg); }
.corner-dec.bl { bottom: 8px; left: 8px; transform: rotate(-90deg); }
.corner-dec.br { bottom: 8px; right: 8px; transform: rotate(180deg); }

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: 45px;
    font-size: clamp(24px, 5vw, 32px);
    color: white;
    font-weight: 800;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 1),
        3px 3px 6px rgba(0, 0, 0, 0.6);
    animation: subtextPulse 2.8s ease-in-out infinite;
}

@keyframes subtextPulse {
    0%, 100% { opacity: 0.9; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.06); }
}

/* ========== COUNTER ========== */
.counter {
    position: fixed;
    top: 28px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, rgba(211, 47, 47, 0.95), rgba(183, 28, 28, 0.95));
    backdrop-filter: blur(12px);
    border: 4px solid gold;
    border-radius: 45px;
    padding: 14px 35px;
    color: gold;
    font-weight: 900;
    font-size: 22px;
    z-index: 600;
    box-shadow: 
        0 10px 40px rgba(211, 47, 47, 0.7),
        0 0 40px rgba(255, 215, 0, 0.6),
        inset 0 2px 10px rgba(255, 255, 255, 0.2);
}

.counter-num {
    font-size: 34px;
    display: inline-block;
    animation: counterPop 0.4s ease;
}

@keyframes counterPop {
    0% { transform: scale(1.6); }
    50% { transform: scale(0.9); }
    100% { transform: scale(1); }
}

/* ========== LION DANCE ========== */
.lion {
    position: fixed;
    font-size: 52px;
    pointer-events: none;
    z-index: 150;
    animation: lionDance 2.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
    filter: drop-shadow(0 0 20px rgba(255, 215, 0, 1));
}

@keyframes lionDance {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(0.9);
        opacity: 1;
    }
    25% {
        transform: translate(var(--lx1), var(--ly1)) rotate(120deg) scale(1.4);
        opacity: 1;
    }
    50% {
        transform: translate(var(--lx2), var(--ly2)) rotate(240deg) scale(1.2);
        opacity: 0.95;
    }
    75% {
        transform: translate(var(--lx3), var(--ly3)) rotate(480deg) scale(0.9);
        opacity: 0.7;
    }
    100% {
        transform: translate(var(--lx4), var(--ly4)) rotate(720deg) scale(0.3);
        opacity: 0;
    }
}

/* ========== MONEY ========== */
.money {
    position: fixed;
    width: 58px;
    height: 30px;
    background: linear-gradient(135deg, #1b5e20, #43a047, #66bb6a);
    border: 2px solid gold;
    border-radius: 5px;
    pointer-events: none;
    z-index: 140;
    animation: moneyFly 2s ease-out forwards;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 4px 15px rgba(255, 215, 0, 0.5);
}

@keyframes moneyFly {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--mx), var(--my)) rotate(var(--mr)) scale(0.4);
        opacity: 0;
    }
}

/* ========== FIREWORK BLOOM ========== */
.firework {
    position: fixed;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 130;
    animation: fireworkBloom 1.6s ease-out forwards;
}

@keyframes fireworkBloom {
    0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
        box-shadow: 0 0 20px currentColor;
    }
    50% {
        box-shadow: 0 0 40px currentColor;
    }
    100% {
        transform: translate(var(--fx), var(--fy)) scale(0);
        opacity: 0;
        box-shadow: 0 0 5px currentColor;
    }
}

/* ========== CONFETTI ========== */
.confetti {
    position: fixed;
    font-size: 22px;
    pointer-events: none;
    z-index: 135;
    animation: confettiTwirl 3s ease-out forwards;
}

@keyframes confettiTwirl {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--cx), var(--cy)) rotate(var(--cr)) scale(0.5);
        opacity: 0;
    }
}

/* ========== BLESSING SCROLL WITH UNROLL ========== */
.scroll {
    position: fixed;
    width: 390px;
    pointer-events: none;
    z-index: 400;
    animation: scrollUnroll 4.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
}

@keyframes scrollUnroll {
    0% {
        transform: translateY(60px) scaleY(0) scaleX(0.3) rotate(-12deg);
        opacity: 0;
    }
    20% {
        transform: translateY(0) scaleY(0.3) scaleX(0.8) rotate(3deg);
        opacity: 1;
    }
    40% {
        transform: scaleY(1) scaleX(1) rotate(0deg);
    }
    90% {
        opacity: 1;
        transform: scaleY(1) scaleX(1) rotate(0deg);
    }
    100% {
        transform: translateY(-50px) scaleY(0.8) scaleX(0.9) rotate(-4deg);
        opacity: 0;
    }
}

.scroll-paper {
    background: linear-gradient(180deg, #7f0000 0%, #b71c1c 20%, #c62828 40%, #d32f2f 50%, #c62828 60%, #b71c1c 80%, #7f0000 100%);
    border: 5px solid gold;
    border-radius: 14px;
    padding: 32px 22px;
    position: relative;
    box-shadow: 
        0 25px 70px rgba(0, 0, 0, 0.8),
        0 0 50px rgba(255, 215, 0, 0.8),
        inset 0 0 40px rgba(255, 215, 0, 0.35);
    min-height: 200px;
}

/* Inner decorative border */
.scroll-paper::before {
    content: '';
    position: absolute;
    top: 12px;
    left: 12px;
    right: 12px;
    bottom: 12px;
    border: 2px solid rgba(255, 215, 0, 0.4);
    border-radius: 10px;
    pointer-events: none;
}

.scroll-text {
    color: gold;
    font-size: 25px;
    font-weight: 800;
    text-align: center;
    line-height: 1.75;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 0.9),
        3px 3px 6px rgba(0, 0, 0, 0.8);
    position: relative;
    z-index: 1;
}

.scroll-couplet {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 3px solid rgba(255, 215, 0, 0.6);
    font-size: 20px;
    font-style: italic;
    line-height: 2;
}

/* ========== RIPPLE WAVE ========== */
.ripple {
    position: fixed;
    border: 6px solid rgba(255, 215, 0, 1);
    border-radius: 50%;
    pointer-events: none;
    z-index: 120;
    animation: rippleWave 1.5s ease-out forwards;
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.9);
}

@keyframes rippleWave {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 600px;
        height: 600px;
        opacity: 0;
    }
}

/* ========== GOLD SPARKLE TRAIL ========== */
.sparkle-trail {
    position: fixed;
    width: 8px;
    height: 8px;
    background: gold;
    border-radius: 50%;
    pointer-events: none;
    z-index: 110;
    box-shadow: 0 0 15px gold;
    animation: sparkleTrailFade 1.2s ease-out forwards;
}

@keyframes sparkleTrailFade {
    0% {
        transform: scale(1);
        opacity: 1;
    }
    100% {
        transform: scale(0) translateY(30px);
        opacity: 0;
    }
}

/* ========== MUSIC BUTTON ========== */
.music-btn {
    position: fixed;
    bottom: 28px;
    right: 28px;
    background: linear-gradient(135deg, rgba(211, 47, 47, 0.95), rgba(183, 28, 28, 0.95));
    backdrop-filter: blur(10px);
    border: 4px solid gold;
    border-radius: 45px;
    padding: 16px 30px;
    color: gold;
    font-weight: 800;
    font-size: 19px;
    cursor: pointer;
    z-index: 600;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 
        0 8px 35px rgba(211, 47, 47, 0.7),
        0 0 40px rgba(255, 215, 0, 0.5);
}

.music-btn:hover {
    transform: scale(1.15) translateY(-4px);
    box-shadow: 
        0 12px 45px rgba(211, 47, 47, 0.9),
        0 0 60px rgba(255, 215, 0, 0.8);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .envelope {
        width: 170px;
        height: 240px;
    }
    
    .envelope-fu {
        font-size: 80px;
    }
    
    .title {
        font-size: 38px;
        letter-spacing: 3px;
    }
    
    .title::before,
    .title::after {
        font-size: 30px;
        left: -50px;
    }
    
    .title::after {
        right: -50px;
    }
    
    .subtext {
        font-size: 22px;
    }
    
    .scroll {
        width: 310px;
    }
    
    .scroll-text {
        font-size: 20px;
    }
    
    .scroll-couplet {
        font-size: 17px;
    }
    
    .counter {
        font-size: 18px;
        padding: 12px 28px;
    }
    
    .counter-num {
        font-size: 28px;
    }
}

</style>
</head>

<body>

<!-- Background Layers -->
<div class="bg-gradient"></div>
<div class="texture-overlay"></div>
<div class="silk-pattern"></div>
<div class="vignette"></div>

<!-- Parallax Float Layers -->
<div class="float-layer float-layer-1" id="floatLayer1"></div>
<div class="float-layer float-layer-2" id="floatLayer2"></div>
<div class="float-layer float-layer-3" id="floatLayer3"></div>

<!-- Lanterns -->
<div id="lanterns"></div>

<!-- Counter -->
<div class="counter">
    🎊 <span class="counter-num" id="counter">0</span> Lời Chúc 🎊
</div>

<!-- Main Content -->
<div class="container">
    <div class="title">Tết Bính Ngọ 2026</div>
    
    <div class="envelope-wrapper">
        <div class="envelope" id="envelope">
            <div class="envelope-body">
                <div class="envelope-frame"></div>
                <div class="envelope-fu">福</div>
                <div class="corner-dec tl"></div>
                <div class="corner-dec tr"></div>
                <div class="corner-dec bl"></div>
                <div class="corner-dec br"></div>
            </div>
        </div>
    </div>
    
    <div class="subtext">🦁 Nhấn Nhận Phúc Lộc 🦁</div>
</div>

<!-- Music Button -->
<div class="music-btn" id="musicBtn">🎵 Nhạc Tết</div>

<!-- Audio with fade -->
<audio id="music" loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>

// ========== INIT PARALLAX FLOATERS ==========
const floatLayer1 = document.getElementById('floatLayer1');
const floatLayer2 = document.getElementById('floatLayer2');
const floatLayer3 = document.getElementById('floatLayer3');

const floaterIcons = ['🌸', '🌺', '🏵️', '💮', '🌼', '🎋', '🌷'];

function createFloaters(container, count, speedMod) {
    for (let i = 0; i < count; i++) {
        const div = document.createElement('div');
        div.className = 'floater';
        div.textContent = floaterIcons[Math.floor(Math.random() * floaterIcons.length)];
        div.style.left = Math.random() * 100 + '%';
        div.style.fontSize = (24 + Math.random() * 18) + 'px';
        div.style.setProperty('--drift', (Math.random() - 0.5) * 400 + 'px');
        div.style.setProperty('--rotate', (Math.random() * 720) + 'deg');
        div.style.animationDuration = ((18 + Math.random() * 18) * speedMod) + 's';
        div.style.animationDelay = Math.random() * 12 + 's';
        container.appendChild(div);
    }
}

createFloaters(floatLayer1, 15, 1.2);
createFloaters(floatLayer2, 15, 1.0);
createFloaters(floatLayer3, 15, 0.8);

// ========== INIT LANTERNS ==========
const lanternsDiv = document.getElementById('lanterns');
const lanternPos = [
    { left: '8%', top: '8%', delay: 0 },
    { left: '23%', top: '4%', delay: 0.3 },
    { left: '50%', top: '2%', delay: 0.6 },
    { left: '77%', top: '6%', delay: 0.9 },
    { left: '92%', top: '10%', delay: 1.2 }
];

lanternPos.forEach(pos => {
    const lantern = document.createElement('div');
    lantern.className = 'lantern';
    lantern.style.left = pos.left;
    lantern.style.top = pos.top;
    lantern.style.zIndex = '10';
    lantern.style.animationDelay = pos.delay + 's';
    lanternsDiv.appendChild(lantern);
});

// ========== GOLD SPARKLE MOUSE TRAIL ==========
let lastSparkleTime = 0;
document.addEventListener('mousemove', (e) => {
    const now = Date.now();
    if (now - lastSparkleTime > 50) {
        createSparkleTrail(e.pageX, e.pageY);
        lastSparkleTime = now;
    }
});

function createSparkleTrail(x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle-trail';
    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    document.body.appendChild(sparkle);
    setTimeout(() => sparkle.remove(), 1200);
}

// ========== MUSIC WITH FADE ==========
let playing = false;
const music = document.getElementById('music');
const musicBtn = document.getElementById('musicBtn');

music.volume = 0;

function fadeInMusic() {
    let vol = 0;
    const interval = setInterval(() => {
        if (vol < 1) {
            vol += 0.05;
            music.volume = Math.min(vol, 1);
        } else {
            clearInterval(interval);
        }
    }, 50);
}

musicBtn.onclick = () => {
    if (playing) {
        music.pause();
        musicBtn.textContent = '🎵 Nhạc Tết (Tắt)';
        playing = false;
    } else {
        music.play().then(() => {
            fadeInMusic();
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
            playing = true;
        }).catch(e => console.log('Play error'));
    }
};

document.body.addEventListener('click', function autoPlay() {
    if (!playing) {
        music.play().then(() => {
            fadeInMusic();
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
        }).catch(e => {});
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
    "Tài lộc viên mãn", "Phúc lộc song toàn", "Cát tường như ý"
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
    "Đầu xuân cát tụng hân hoan khắp<br>Ngọ Tết khai xuân phúc lộc dồi"
];

// ========== COUNTER ==========
let count = 0;
let clickIntensity = 0;
const counter = document.getElementById('counter');

function updateCounter() {
    count++;
    counter.textContent = count;
    const numEl = counter.querySelector('.counter-num');
    numEl.style.animation = 'none';
    setTimeout(() => {
        numEl.style.animation = 'counterPop 0.4s ease';
    }, 10);
}

// ========== EFFECTS ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 300) + 'px';
    ripple.style.top = (y - 300) + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 1500);
}

function createLions(x, y, intensity) {
    const num = Math.min(10 + intensity * 2, 18);
    
    for (let i = 0; i < num; i++) {
        const lion = document.createElement('div');
        lion.className = 'lion';
        lion.textContent = '🦁';
        lion.style.left = x + 'px';
        lion.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const d1 = 160 + Math.random() * 80;
        const d2 = 290 + Math.random() * 110;
        const d3 = 460 + Math.random() * 140;
        const d4 = 620 + Math.random() * 180;
        
        lion.style.setProperty('--lx1', Math.cos(angle) * d1 + 'px');
        lion.style.setProperty('--ly1', Math.sin(angle) * d1 - 80 + 'px');
        lion.style.setProperty('--lx2', Math.cos(angle) * d2 + 'px');
        lion.style.setProperty('--ly2', Math.sin(angle) * d2 - 160 + 'px');
        lion.style.setProperty('--lx3', Math.cos(angle) * d3 + 'px');
        lion.style.setProperty('--ly3', Math.sin(angle) * d3 - 250 + 'px');
        lion.style.setProperty('--lx4', Math.cos(angle) * d4 + 'px');
        lion.style.setProperty('--ly4', Math.sin(angle) * d4 - 340 + 'px');
        
        document.body.appendChild(lion);
        setTimeout(() => lion.remove(), 2500);
    }
}

function createMoney(x, y, intensity) {
    const num = Math.min(15 + intensity, 25);
    
    for (let i = 0; i < num; i++) {
        const money = document.createElement('div');
        money.className = 'money';
        money.textContent = '💵';
        money.style.left = x + 'px';
        money.style.top = y + 'px';
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 130 + Math.random() * 240;
        
        money.style.setProperty('--mx', Math.cos(angle) * dist + 'px');
        money.style.setProperty('--my', Math.sin(angle) * dist - 90 + 'px');
        money.style.setProperty('--mr', (Math.random() - 0.5) * 900 + 'deg');
        
        document.body.appendChild(money);
        setTimeout(() => money.remove(), 2000);
    }
}

function createFireworks(x, y, intensity) {
    const num = Math.min(30 + intensity * 3, 50);
    const colors = ['#ffd700', '#ff0000', '#ffcc00', '#ff6b00', '#ff1744', '#ffa500'];
    
    for (let i = 0; i < num; i++) {
        const fw = document.createElement('div');
        fw.className = 'firework';
        fw.style.left = x + 'px';
        fw.style.top = y + 'px';
        fw.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        const angle = (i / num) * Math.PI * 2;
        const dist = 150 + Math.random() * 220;
        
        fw.style.setProperty('--fx', Math.cos(angle) * dist + 'px');
        fw.style.setProperty('--fy', Math.sin(angle) * dist + 'px');
        
        document.body.appendChild(fw);
        setTimeout(() => fw.remove(), 1600);
    }
}

function createConfetti(x, y, intensity) {
    const num = Math.min(35 + intensity * 2, 55);
    const icons = ['●', '■', '▲', '◆', '★', '✦', '❖'];
    const colors = ['#ff0000', '#ffd700', '#ff6b00', '#ffcc00', '#ff1744'];
    
    for (let i = 0; i < num; i++) {
        const conf = document.createElement('div');
        conf.className = 'confetti';
        conf.textContent = icons[Math.floor(Math.random() * icons.length)];
        conf.style.color = colors[Math.floor(Math.random() * colors.length)];
        conf.style.left = x + 'px';
        conf.style.top = y + 'px';
        
        const cx = (Math.random() - 0.5) * 600;
        const cy = Math.random() * 600 + 200;
        const cr = (Math.random() - 0.5) * 1080;
        
        conf.style.setProperty('--cx', cx + 'px');
        conf.style.setProperty('--cy', cy + 'px');
        conf.style.setProperty('--cr', cr + 'deg');
        
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), 3000);
    }
}

function createScroll() {
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    const x = Math.random() * (window.innerWidth - 420) + 210;
    const y = Math.random() * (window.innerHeight - 320) + 160;
    
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
    setTimeout(() => scroll.remove(), 4500);
}

// ========== MAIN CLICK WITH ESCALATION ==========
const envelope = document.getElementById('envelope');

envelope.addEventListener('click', function(e) {
    updateCounter();
    clickIntensity = Math.min(count, 10);
    
    if (!playing) {
        music.play().then(() => {
            fadeInMusic();
            playing = true;
            musicBtn.textContent = '🎵 Nhạc Tết (Bật)';
        }).catch(e => {});
    }
    
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    
    createRipple(cx, cy);
    createLions(cx, cy, clickIntensity);
    createMoney(cx, cy, clickIntensity);
    createFireworks(cx, cy, clickIntensity);
    createConfetti(cx, cy, clickIntensity);
    
    // Progressive scroll spawning
    const numScrolls = count === 1 ? 10 : Math.min(5 + Math.floor(clickIntensity / 2), 8);
    let scrollCount = 0;
    
    const interval = setInterval(() => {
        createScroll();
        scrollCount++;
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
        }
    }, 260);
});

// Prevent context menu
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)