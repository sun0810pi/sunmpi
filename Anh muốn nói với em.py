import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="❤️ Confession", page_icon="❤️")

# ===== ĐỌC VÀ ENCODE NHẠC =====
# Kiểm tra file tồn tại
if os.path.exists("beautiful.mp3"):
    with open("beautiful.mp3", "rb") as f:
        audio_data = f.read()
        music_base64 = base64.b64encode(audio_data).decode()
else:
    music_base64 = ""  # Fallback nếu không có file nhạc

# ===== HTML CODE =====
html = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💗 Confession</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            overflow: hidden;
            font-family: 'Segoe UI', 'Arial', sans-serif;
            background: #000;
            position: relative;
            min-height: 100vh;
        }

        /* ========== UNIVERSE CANVAS ========== */
        #universeCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        /* ========== PLANETS WITH BEAUTIFUL EFFECTS ========== */
        .planets {
            position: fixed;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 2;
        }

        .planet-system {
            position: absolute;
            animation: orbit ease-in-out infinite;
        }

        .planet {
            border-radius: 50%;
            position: relative;
            box-shadow: inset -25px -15px 40px rgba(0, 0, 0, 0.5);
        }

        .planet::before {
            content: '';
            position: absolute;
            top: 15%;
            left: 15%;
            width: 35%;
            height: 35%;
            background: radial-gradient(circle, rgba(255,255,255,0.4), transparent);
            border-radius: 50%;
            filter: blur(8px);
        }

        .planet::after {
            content: '';
            position: absolute;
            top: -20%;
            left: -20%;
            width: 140%;
            height: 140%;
            background: radial-gradient(circle, var(--glow-color) 0%, transparent 70%);
            border-radius: 50%;
            z-index: -1;
            opacity: 0.4;
            animation: pulse-glow 4s ease-in-out infinite;
        }

        @keyframes pulse-glow {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 0.6; transform: scale(1.1); }
        }

        .planet-ring {
            position: absolute;
            border-radius: 50%;
            border: 3px solid;
            opacity: 0.7;
            transform: rotateX(75deg);
        }

        .planet1-system {
            top: 10%;
            left: 8%;
            animation-duration: 30s;
        }

        .planet1 {
            width: 120px;
            height: 120px;
            background: radial-gradient(circle at 30% 30%, #ff8db4, #ff4d88, #d63c6f);
            --glow-color: rgba(255, 77, 136, 0.6);
            box-shadow: 
                inset -25px -15px 40px rgba(0, 0, 0, 0.5),
                0 0 80px rgba(255, 77, 136, 0.6);
        }

        .planet1-ring {
            width: 180px;
            height: 180px;
            border-color: rgba(255, 141, 180, 0.6);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotateX(75deg);
        }

        .planet2-system {
            top: 60%;
            right: 10%;
            animation-duration: 35s;
            animation-delay: -10s;
        }

        .planet2 {
            width: 90px;
            height: 90px;
            background: radial-gradient(circle at 30% 30%, #ffc4e1, #ff8ab8, #ff5a9d);
            --glow-color: rgba(255, 138, 184, 0.6);
            box-shadow: 
                inset -20px -10px 30px rgba(0, 0, 0, 0.5),
                0 0 60px rgba(255, 138, 184, 0.6);
        }

        .planet2-ring {
            width: 150px;
            height: 150px;
            border-color: rgba(255, 196, 225, 0.6);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotateX(75deg) rotate(45deg);
        }

        .planet3-system {
            bottom: 12%;
            left: 12%;
            animation-duration: 40s;
            animation-delay: -20s;
        }

        .planet3 {
            width: 80px;
            height: 80px;
            background: radial-gradient(circle at 30% 30%, #ffe0f0, #ffb8d9, #ff8db4);
            --glow-color: rgba(255, 184, 217, 0.6);
            box-shadow: 
                inset -18px -8px 25px rgba(0, 0, 0, 0.5),
                0 0 50px rgba(255, 184, 217, 0.6);
        }

        .planet3-ring {
            width: 130px;
            height: 130px;
            border-color: rgba(255, 224, 240, 0.6);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotateX(75deg) rotate(-30deg);
        }

        @keyframes orbit {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(20px, -25px) rotate(5deg); }
            50% { transform: translate(-10px, 20px) rotate(-3deg); }
            75% { transform: translate(25px, 10px) rotate(4deg); }
        }

        /* ========== FLOATING HEARTS ========== */
        .floating-hearts {
            position: fixed;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 4;
        }

        .bg-heart {
            position: absolute;
            font-size: 22px;
            opacity: 0;
            animation: floatUp linear infinite;
            filter: drop-shadow(0 0 8px rgba(255, 105, 180, 0.8));
        }

        @keyframes floatUp {
            0% {
                transform: translateY(120vh) translateX(0) rotate(0deg) scale(0.5);
                opacity: 0;
            }
            10% {
                opacity: 0.8;
            }
            50% {
                opacity: 0.6;
            }
            90% {
                opacity: 0.3;
            }
            100% {
                transform: translateY(-20vh) translateX(var(--drift)) rotate(360deg) scale(1);
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
            font-size: clamp(32px, 6vw, 58px);
            font-weight: 900;
            background: linear-gradient(135deg, #fff, #ffc0e3, #ff6fa8, #fff);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 50px;
            animation: titleShine 4s ease-in-out infinite;
            filter: drop-shadow(0 0 30px rgba(255, 111, 168, 0.7));
            letter-spacing: 3px;
        }

        @keyframes titleShine {
            0%, 100% { 
                background-position: 0% 50%;
                filter: drop-shadow(0 0 25px rgba(255, 111, 168, 0.6));
            }
            50% { 
                background-position: 100% 50%;
                filter: drop-shadow(0 0 45px rgba(255, 111, 168, 1));
            }
        }

        /* ========== PARTICLE HEART CONTAINER ========== */
        .heart-container {
            position: relative;
            width: 450px;
            height: 450px;
            margin: 0 auto;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #heartCanvas {
            width: 100%;
            height: 100%;
        }

        /* ========== SUBTEXT ========== */
        .subtext {
            margin-top: 40px;
            font-size: clamp(16px, 3.5vw, 22px);
            color: #ffc0e3;
            font-weight: 600;
            animation: pulse 2s ease-in-out infinite;
            text-shadow: 0 0 20px rgba(255, 192, 227, 0.9);
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.6; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.1); }
        }

        /* ========== POPUP MESSAGES (PERFECT DISTRIBUTION) ========== */
        .popup-msg {
            position: fixed;
            padding: 22px 38px;
            border-radius: 28px;
            color: #fff;
            font-weight: 700;
            font-size: clamp(17px, 3vw, 23px);
            pointer-events: none;
            z-index: 200;
            
            background: linear-gradient(135deg, 
                rgba(255, 20, 147, 0.96), 
                rgba(255, 105, 180, 0.96));
            backdrop-filter: blur(18px);
            border: 3px solid rgba(255, 255, 255, 0.6);
            
            box-shadow: 
                0 18px 55px rgba(255, 20, 147, 0.8),
                inset 0 0 35px rgba(255, 255, 255, 0.35),
                0 0 90px rgba(255, 105, 180, 0.5);
            
            animation: popupFloat 4.5s ease-out forwards;
            
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .popup-msg::before {
            content: '💗';
            font-size: 1.4em;
            animation: spin 2.5s linear infinite;
        }

        .popup-msg::after {
            content: '✨';
            font-size: 1.2em;
            animation: sparkle 1.8s ease-in-out infinite;
        }

        @keyframes popupFloat {
            0% {
                transform: translateY(50px) scale(0.2) rotate(-8deg);
                opacity: 0;
            }
            12% {
                transform: translateY(0) scale(1.15) rotate(3deg);
                opacity: 1;
            }
            18% {
                transform: scale(1) rotate(0deg);
            }
            82% {
                opacity: 1;
            }
            100% {
                transform: translateY(-50px) scale(0.7) rotate(5deg);
                opacity: 0;
            }
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes sparkle {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(1.4); }
        }

        /* ========== EXPLOSION HEARTS ========== */
        .explosion-heart {
            position: fixed;
            font-size: 32px;
            pointer-events: none;
            z-index: 100;
            animation: explode 2.2s ease-out forwards;
            filter: drop-shadow(0 0 18px rgba(255, 105, 180, 1));
        }

        @keyframes explode {
            0% {
                transform: translate(0, 0) scale(1.2) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) scale(0.05) rotate(var(--rotate));
                opacity: 0;
            }
        }

        /* ========== RIPPLE EFFECT ========== */
        .ripple {
            position: fixed;
            border-radius: 50%;
            border: 6px solid rgba(255, 105, 180, 0.9);
            pointer-events: none;
            animation: rippleExpand 1.8s ease-out forwards;
            box-shadow: 0 0 50px rgba(255, 105, 180, 0.8);
        }

        @keyframes rippleExpand {
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

        /* ========== MUSIC CONTROL ========== */
        .music-control {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, 
                rgba(255, 20, 147, 0.92), 
                rgba(255, 105, 180, 0.92));
            backdrop-filter: blur(12px);
            border: 3px solid rgba(255, 255, 255, 0.5);
            border-radius: 50px;
            padding: 16px 28px;
            color: white;
            font-weight: 700;
            font-size: 17px;
            cursor: pointer;
            z-index: 1000;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            box-shadow: 0 10px 35px rgba(255, 20, 147, 0.7);
        }

        .music-control:hover {
            transform: scale(1.2) rotate(8deg);
            box-shadow: 0 15px 50px rgba(255, 20, 147, 1);
        }

        .music-control:active {
            transform: scale(0.9);
        }

        /* ========== RESPONSIVE ========== */
        @media (max-width: 768px) {
            .title {
                font-size: 26px;
                margin-bottom: 30px;
            }
            
            .subtext {
                font-size: 14px;
                margin-top: 25px;
            }

            .heart-container {
                width: 320px;
                height: 320px;
            }

            .planet1 { width: 80px; height: 80px; }
            .planet1-ring { width: 130px; height: 130px; }
            .planet2 { width: 60px; height: 60px; }
            .planet2-ring { width: 100px; height: 100px; }
            .planet3 { width: 55px; height: 55px; }
            .planet3-ring { width: 90px; height: 90px; }
        }

    </style>
</head>

<body>

<!-- Universe Canvas -->
<canvas id="universeCanvas"></canvas>

<!-- Planets -->
<div class="planets">
    <div class="planet-system planet1-system">
        <div class="planet planet1"></div>
        <div class="planet-ring planet1-ring"></div>
    </div>
    <div class="planet-system planet2-system">
        <div class="planet planet2"></div>
        <div class="planet-ring planet2-ring"></div>
    </div>
    <div class="planet-system planet3-system">
        <div class="planet planet3"></div>
        <div class="planet-ring planet3-ring"></div>
    </div>
</div>

<!-- Floating Hearts Background -->
<div class="floating-hearts" id="floatingHearts"></div>

<!-- Main Content -->
<div class="container">
    <div class="title">Anh muốn nói với em là...</div>
    
    <div class="heart-container" id="heartContainer">
        <canvas id="heartCanvas"></canvas>
    </div>
    
    <div class="subtext">Bấm vào trái tim 💗</div>
</div>

<!-- Music Control -->
<div class="music-control" id="musicControl" onclick="toggleMusic()">
    🎵 Music ON
</div>

<!-- Background Music -->
<audio id="bgMusic" loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>
// ========== UNIVERSE PARTICLES FLYING IN ==========
const universeCanvas = document.getElementById('universeCanvas');
const uCtx = universeCanvas.getContext('2d');

universeCanvas.width = window.innerWidth;
universeCanvas.height = window.innerHeight;

const universeParticles = [];
const numUniverseParticles = 350;

for (let i = 0; i < numUniverseParticles; i++) {
    const angle = Math.random() * Math.PI * 2;
    const distance = Math.random() * 2500 + 1500;
    
    universeParticles.push({
        x: Math.cos(angle) * distance + universeCanvas.width / 2,
        y: Math.sin(angle) * distance + universeCanvas.height / 2,
        targetX: universeCanvas.width / 2 + (Math.random() - 0.5) * 150,
        targetY: universeCanvas.height / 2 + (Math.random() - 0.5) * 150,
        size: Math.random() * 2 + 0.5,
        speed: Math.random() * 1.8 + 0.8,
        alpha: Math.random() * 0.7 + 0.3,
        twinkleSpeed: Math.random() * 0.015 + 0.008
    });
}

function animateUniverse() {
    uCtx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    uCtx.fillRect(0, 0, universeCanvas.width, universeCanvas.height);
    
    universeParticles.forEach(p => {
        const dx = p.targetX - p.x;
        const dy = p.targetY - p.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        
        if (dist > 2) {
            p.x += (dx / dist) * p.speed;
            p.y += (dy / dist) * p.speed;
        } else {
            const angle = Math.random() * Math.PI * 2;
            const distance = Math.random() * 2000 + 1200;
            p.x = Math.cos(angle) * distance + universeCanvas.width / 2;
            p.y = Math.sin(angle) * distance + universeCanvas.height / 2;
            p.targetX = universeCanvas.width / 2 + (Math.random() - 0.5) * 150;
            p.targetY = universeCanvas.height / 2 + (Math.random() - 0.5) * 150;
        }
        
        p.alpha += Math.sin(Date.now() * p.twinkleSpeed) * 0.015;
        p.alpha = Math.max(0.3, Math.min(1, p.alpha));
        
        uCtx.beginPath();
        uCtx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        uCtx.fillStyle = `rgba(255, 255, 255, ${p.alpha})`;
        uCtx.shadowBlur = 4;
        uCtx.shadowColor = `rgba(255, 255, 255, ${p.alpha * 0.8})`;
        uCtx.fill();
    });
    
    requestAnimationFrame(animateUniverse);
}

animateUniverse();

// ========== PARTICLE HEART (EXPLOSION STYLE) ==========
const heartCanvas = document.getElementById('heartCanvas');
const hCtx = heartCanvas.getContext('2d');

heartCanvas.width = 450;
heartCanvas.height = 450;

const heartParticles = [];

function pointOnHeart(t) {
    return {
        x: 160 * Math.pow(Math.sin(t), 3),
        y: -(130 * Math.cos(t) - 50 * Math.cos(2 * t) - 20 * Math.cos(3 * t) - 10 * Math.cos(4 * t) + 25)
    };
}

class HeartParticle {
    constructor() {
        this.reset();
    }
    
    reset() {
        const t = Math.random() * Math.PI * 2;
        const pos = pointOnHeart(t);
        
        this.x = 225;
        this.y = 225;
        this.targetX = pos.x * 0.85 + 225;
        this.targetY = pos.y * 0.85 + 225;
        this.vx = (this.targetX - this.x) / 35;
        this.vy = (this.targetY - this.y) / 35;
        this.size = Math.random() * 3 + 2;
        this.alpha = 0;
        this.maxAlpha = Math.random() * 0.6 + 0.4;
        this.life = 0;
        this.maxLife = 100 + Math.random() * 50;
    }
    
    update() {
        this.life++;
        
        if (this.life > this.maxLife) {
            this.reset();
            return;
        }
        
        this.x += this.vx;
        this.y += this.vy;
        
        if (this.life < 15) {
            this.alpha = (this.life / 15) * this.maxAlpha;
        } else if (this.life > this.maxLife - 25) {
            this.alpha = ((this.maxLife - this.life) / 25) * this.maxAlpha;
        } else {
            this.alpha = this.maxAlpha;
        }
    }
    
    draw() {
        const gradient = hCtx.createRadialGradient(
            this.x, this.y, 0,
            this.x, this.y, this.size * 3
        );
        gradient.addColorStop(0, `rgba(255, 105, 180, ${this.alpha})`);
        gradient.addColorStop(0.5, `rgba(255, 20, 147, ${this.alpha * 0.7})`);
        gradient.addColorStop(1, `rgba(255, 20, 147, 0)`);
        
        hCtx.beginPath();
        hCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        hCtx.fillStyle = gradient;
        hCtx.shadowBlur = 15;
        hCtx.shadowColor = `rgba(255, 105, 180, ${this.alpha})`;
        hCtx.fill();
    }
}

for (let i = 0; i < 450; i++) {
    heartParticles.push(new HeartParticle());
}

function animateHeart() {
    hCtx.clearRect(0, 0, heartCanvas.width, heartCanvas.height);
    
    heartParticles.forEach(p => {
        p.update();
        p.draw();
    });
    
    requestAnimationFrame(animateHeart);
}

animateHeart();

// ========== COMETS (NO BUGS) ==========
const activeComets = new Set();
const MAX_COMETS = 4;

function createComet() {
    if (activeComets.size >= MAX_COMETS) return;
    
    const comet = document.createElement('div');
    comet.style.position = 'fixed';
    comet.style.width = '5px';
    comet.style.height = '5px';
    comet.style.background = '#fff';
    comet.style.borderRadius = '50%';
    comet.style.pointerEvents = 'none';
    comet.style.zIndex = '3';
    comet.style.boxShadow = '0 0 20px #fff, 0 0 40px #ffc0e3';
    
    const tail = document.createElement('div');
    tail.style.position = 'absolute';
    tail.style.width = '250px';
    tail.style.height = '4px';
    tail.style.background = 'linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(255,192,227,0.9) 20%, rgba(255,111,168,0.6) 50%, transparent 100%)';
    tail.style.right = '5px';
    tail.style.top = '0.5px';
    tail.style.borderRadius = '50%';
    tail.style.boxShadow = '0 0 15px rgba(255, 192, 227, 0.8)';
    comet.appendChild(tail);
    
    const startY = Math.random() * 40;
    const endY = startY + 70 + Math.random() * 30;
    const duration = 2.5 + Math.random() * 1.5;
    
    activeComets.add(comet);
    document.body.appendChild(comet);
    
    const startTime = Date.now();
    const startX = window.innerWidth * 1.1;
    const endX = -300;
    const startYpx = window.innerHeight * (startY / 100);
    const endYpx = window.innerHeight * (endY / 100);
    
    function animateComet() {
        const elapsed = (Date.now() - startTime) / 1000;
        const progress = elapsed / duration;
        
        if (progress >= 1) {
            comet.remove();
            activeComets.delete(comet);
            return;
        }
        
        const currentX = startX + (endX - startX) * progress;
        const currentY = startYpx + (endYpx - startYpx) * progress;
        
        comet.style.left = currentX + 'px';
        comet.style.top = currentY + 'px';
        comet.style.opacity = progress < 0.1 ? progress * 10 : 
                              progress > 0.9 ? (1 - progress) * 10 : 1;
        
        requestAnimationFrame(animateComet);
    }
    
    animateComet();
}

setInterval(() => {
    if (Math.random() > 0.4) {
        createComet();
    }
}, 1800);

// ========== CREATE FLOATING HEARTS ==========
const floatingHearts = document.getElementById('floatingHearts');
for (let i = 0; i < 35; i++) {
    const heart = document.createElement('div');
    heart.className = 'bg-heart';
    heart.innerHTML = '💗';
    heart.style.left = Math.random() * 100 + '%';
    heart.style.fontSize = (16 + Math.random() * 14) + 'px';
    heart.style.setProperty('--drift', (Math.random() - 0.5) * 140 + 'px');
    heart.style.animationDuration = (14 + Math.random() * 8) + 's';
    heart.style.animationDelay = Math.random() * 12 + 's';
    floatingHearts.appendChild(heart);
}

// ========== MUSIC CONTROL ==========
let musicPlaying = false;
const bgMusic = document.getElementById('bgMusic');
const musicControl = document.getElementById('musicControl');

function toggleMusic() {
    if (musicPlaying) {
        bgMusic.pause();
        musicControl.innerHTML = '🎵 Music OFF';
        musicPlaying = false;
    } else {
        bgMusic.play().catch(e => console.log('Play error:', e));
        musicControl.innerHTML = '🎵 Music ON';
        musicPlaying = true;
    }
}

document.body.addEventListener('click', function startMusic() {
    if (!musicPlaying) {
        toggleMusic();
    }
}, { once: true });

// ========== MESSAGES ARRAY ==========
const messages = [
    "Anh nhớ em 💗",
    "Anh yêu em ❤️",
    "Quay lại đi mà 🥺",
    "Anh luôn ở đây 🌟",
    "Smile đi ✨",
    "You mean everything to me 💫",
    "Đừng buồn nữa nhé 🌈",
    "Em là điều tuyệt vời nhất 🌸",
    "Anh sẽ chờ em 💕",
    "Forever and always 💖",
    "Em đặc biệt lắm 🌹",
    "Thinking of you 💭",
    "Anh thương em lắm 💝",
    "Be mine 🦋",
    "Em là ánh sáng của anh ⭐",
    "Miss you so much 🌙",
    "Em là cả thế giới của anh 🌍",
    "You're my everything 💫"
];

// ========== GRID-BASED POPUP DISTRIBUTION (PERFECT) ==========
const usedPositions = new Set();
const gridSize = 180;

function getGridKey(x, y) {
    const gridX = Math.floor(x / gridSize);
    const gridY = Math.floor(y / gridSize);
    return `${gridX},${gridY}`;
}

function getAvailablePosition() {
    const margin = 160;
    const maxAttempts = 60;
    
    for (let attempt = 0; attempt < maxAttempts; attempt++) {
        const x = margin + Math.random() * (window.innerWidth - margin * 2);
        const y = margin + Math.random() * (window.innerHeight - margin * 2);
        const key = getGridKey(x, y);
        
        if (!usedPositions.has(key)) {
            usedPositions.add(key);
            setTimeout(() => usedPositions.delete(key), 4500);
            return { x, y };
        }
    }
    
    const x = margin + Math.random() * (window.innerWidth - margin * 2);
    const y = margin + Math.random() * (window.innerHeight - margin * 2);
    return { x, y };
}

// ========== CREATE RIPPLE EFFECT ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 300) + 'px';
    ripple.style.top = (y - 300) + 'px';
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 1800);
}

// ========== CREATE EXPLOSION HEARTS ==========
function createExplosion(x, y) {
    const numHearts = 26;
    const radius = 400;
    
    for (let i = 0; i < numHearts; i++) {
        const angle = (i / numHearts) * Math.PI * 2;
        const variance = (Math.random() - 0.5) * 0.4;
        const actualAngle = angle + variance;
        
        const tx = Math.cos(actualAngle) * (radius + Math.random() * 80);
        const ty = Math.sin(actualAngle) * (radius + Math.random() * 80);
        const rotate = Math.random() * 1080 + 360;
        
        const heart = document.createElement('div');
        heart.className = 'explosion-heart';
        heart.innerHTML = ['💗', '💖', '💝', '💕', '❤️', '💓'][Math.floor(Math.random() * 6)];
        heart.style.left = x + 'px';
        heart.style.top = y + 'px';
        heart.style.setProperty('--tx', tx + 'px');
        heart.style.setProperty('--ty', ty + 'px');
        heart.style.setProperty('--rotate', rotate + 'deg');
        
        document.body.appendChild(heart);
        
        setTimeout(() => heart.remove(), 2200);
    }
}

// ========== CREATE POPUP MESSAGE ==========
function createPopup() {
    const msg = messages[Math.floor(Math.random() * messages.length)];
    const popup = document.createElement('div');
    popup.className = 'popup-msg';
    
    const textSpan = document.createElement('span');
    textSpan.textContent = msg;
    popup.appendChild(textSpan);
    
    const pos = getAvailablePosition();
    popup.style.left = pos.x + 'px';
    popup.style.top = pos.y + 'px';
    
    document.body.appendChild(popup);
    
    setTimeout(() => popup.remove(), 4500);
}

// ========== HEART CLICK HANDLER ==========
let clickCount = 0;
const heartContainer = document.getElementById('heartContainer');

heartContainer.addEventListener('click', function(e) {
    clickCount++;
    
    if (!musicPlaying) {
        toggleMusic();
    }
    
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    createRipple(centerX, centerY);
    createExplosion(centerX, centerY);
    
    const spamCount = clickCount === 1 ? 65 : 45;
    let count = 0;
    
    const interval = setInterval(() => {
        createPopup();
        count++;
        
        if (count >= spamCount) {
            clearInterval(interval);
        }
    }, 75);
    
    heartParticles.forEach(p => {
        if (Math.random() > 0.3) {
            p.reset();
        }
    });
});

// ========== WINDOW RESIZE ==========
window.addEventListener('resize', () => {
    universeCanvas.width = window.innerWidth;
    universeCanvas.height = window.innerHeight;
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=950, scrolling=False)