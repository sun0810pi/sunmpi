import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="❤️ Confession", page_icon="❤️")

# ===== CACHE AUDIO ENCODE (Performance boost) =====
@st.cache_data
def get_music():
    """Cache audio encoding to prevent reloading on every rerun"""
    if os.path.exists("beautiful.mp3"):
        with open("beautiful.mp3", "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

music_base64 = get_music()

# ===== HTML CODE WITH MOBILE OPTIMIZATION =====
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #1a0033 0%, #330033 25%, #4d004d 50%, #330033 75%, #1a0033 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    position: relative;
    min-height: 100vh;
    touch-action: manipulation;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ========== STARS BACKGROUND ========== */
.stars {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}

.star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    animation: twinkle linear infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 1; }
}

/* ========== FLOATING HEARTS BACKGROUND ========== */
.floating-hearts {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 2;
}

.bg-heart {
    position: absolute;
    font-size: 25px;
    opacity: 0;
    animation: floatUp linear infinite;
    filter: drop-shadow(0 0 5px rgba(255, 105, 180, 0.6));
    will-change: transform, opacity;
}

@keyframes floatUp {
    0% {
        transform: translateY(110vh) translateX(0) rotate(0deg) scale(0.8);
        opacity: 0;
    }
    10% {
        opacity: 0.7;
    }
    50% {
        opacity: 0.5;
    }
    90% {
        opacity: 0.3;
    }
    100% {
        transform: translateY(-20vh) translateX(var(--drift)) rotate(360deg) scale(1.2);
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
    width: 90%;
    max-width: 600px;
    padding: 20px;
}

/* ========== TITLE ========== */
.title {
    font-size: clamp(28px, 7vw, 68px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff6fa8, #ff3f7f, #ff94c2, #ffb3d9);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: clamp(40px, 8vh, 60px);
    animation: titleGlow 3s ease-in-out infinite, titleWave 4s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(255, 63, 127, 0.6));
    letter-spacing: 1px;
    line-height: 1.2;
}

@keyframes titleGlow {
    0%, 100% { 
        filter: drop-shadow(0 0 15px rgba(255, 63, 127, 0.5)); 
    }
    50% { 
        filter: drop-shadow(0 0 35px rgba(255, 63, 127, 0.9)); 
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

/* ========== MAIN HEART (CSS SHAPE) ========== */
.heart-container {
    position: relative;
    display: inline-block;
    margin: clamp(20px, 5vh, 30px) 0;
}

.heart {
    width: clamp(100px, 25vw, 150px);
    height: clamp(100px, 25vw, 150px);
    position: relative;
    transform: rotate(-45deg);
    cursor: pointer;
    margin: auto;
    
    background: linear-gradient(135deg, #ff1493, #ff69b4, #ff1493);
    background-size: 200% 200%;
    
    box-shadow: 
        0 0 40px rgba(255, 20, 147, 0.8),
        0 0 80px rgba(255, 105, 180, 0.5),
        inset 0 0 20px rgba(255, 255, 255, 0.3);
    
    animation: heartBeat 1.4s ease-in-out infinite, heartGlow 2s ease-in-out infinite;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    will-change: transform;
}

.heart:active {
    transform: rotate(-45deg) scale(0.85);
}

.heart:before,
.heart:after {
    content: "";
    width: clamp(100px, 25vw, 150px);
    height: clamp(100px, 25vw, 150px);
    position: absolute;
    background: inherit;
    border-radius: 50%;
}

.heart:before {
    top: calc(clamp(100px, 25vw, 150px) * -0.5);
    left: 0;
}

.heart:after {
    left: calc(clamp(100px, 25vw, 150px) * 0.5);
    top: 0;
}

@keyframes heartBeat {
    0% { transform: scale(1) rotate(-45deg); }
    15% { transform: scale(1.1) rotate(-45deg); }
    30% { transform: scale(1) rotate(-45deg); }
    45% { transform: scale(1.15) rotate(-45deg); }
    60% { transform: scale(1) rotate(-45deg); }
    75% { transform: scale(1.05) rotate(-45deg); }
    100% { transform: scale(1) rotate(-45deg); }
}

@keyframes heartGlow {
    0%, 100% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
}

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: clamp(30px, 6vh, 50px);
    font-size: clamp(16px, 4vw, 24px);
    color: #ffb3d9;
    font-weight: 600;
    animation: pulse 2.5s ease-in-out infinite;
    text-shadow: 0 0 10px rgba(255, 179, 217, 0.8);
}

@keyframes pulse {
    0%, 100% { opacity: 0.7; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.03); }
}

/* ========== EXPLOSION HEARTS ========== */
.explosion-heart {
    position: fixed;
    font-size: clamp(25px, 6vw, 35px);
    pointer-events: none;
    z-index: 100;
    animation: explode 1.5s ease-out forwards;
    filter: drop-shadow(0 0 8px rgba(255, 105, 180, 0.7));
    will-change: transform, opacity;
}

@keyframes explode {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--tx), var(--ty)) scale(0.2) rotate(720deg);
        opacity: 0;
    }
}

/* ========== POPUP MESSAGES (MOBILE OPTIMIZED) ========== */
.popup-msg {
    position: fixed;
    padding: clamp(12px, 3vw, 18px) clamp(18px, 4vw, 28px);
    border-radius: clamp(12px, 3vw, 20px);
    color: #fff;
    font-weight: 700;
    font-size: clamp(13px, 3vw, 18px);
    pointer-events: none;
    z-index: 200;
    
    /* Mobile-friendly width */
    width: auto;
    max-width: min(85vw, 320px);
    
    background: rgba(255, 20, 147, 0.95);
    backdrop-filter: blur(8px);
    border: 2px solid rgba(255, 255, 255, 0.4);
    
    box-shadow: 
        0 8px 30px rgba(255, 20, 147, 0.5),
        inset 0 0 15px rgba(255, 255, 255, 0.25);
    
    animation: popupFade 5s ease-out forwards;
    
    /* Better text wrapping */
    word-wrap: break-word;
    text-align: center;
    line-height: 1.4;
}

@keyframes popupFade {
    0% {
        transform: translateY(20px) scale(0.7);
        opacity: 0;
    }
    15% {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
    85% {
        opacity: 1;
    }
    100% {
        transform: translateY(-20px);
        opacity: 0;
    }
}

/* ========== RIPPLE EFFECT ========== */
.ripple {
    position: fixed;
    border-radius: 50%;
    border: 3px solid rgba(255, 20, 147, 0.8);
    pointer-events: none;
    animation: rippleExpand 1s ease-out forwards;
    will-change: width, height, opacity;
}

@keyframes rippleExpand {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: min(400px, 80vw);
        height: min(400px, 80vw);
        opacity: 0;
    }
}

/* ========== MUSIC CONTROL (TOUCH FRIENDLY) ========== */
.music-control {
    position: fixed;
    bottom: clamp(20px, 4vh, 30px);
    right: clamp(20px, 4vw, 30px);
    background: rgba(255, 20, 147, 0.9);
    backdrop-filter: blur(8px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    padding: clamp(10px, 2vh, 12px) clamp(16px, 3vw, 20px);
    color: white;
    font-weight: 600;
    font-size: clamp(13px, 2.5vw, 15px);
    cursor: pointer;
    z-index: 1000;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 20, 147, 0.4);
    
    /* Touch friendly */
    min-height: 44px;
    min-width: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
}

.music-control:active {
    transform: scale(0.95);
    box-shadow: 0 6px 20px rgba(255, 20, 147, 0.6);
}

/* ========== DESKTOP HOVER EFFECTS ========== */
@media (hover: hover) and (pointer: fine) {
    .heart:hover {
        transform: rotate(-45deg) scale(1.15);
        box-shadow: 
            0 0 70px rgba(255, 20, 147, 1),
            0 0 110px rgba(255, 105, 180, 0.7),
            inset 0 0 35px rgba(255, 255, 255, 0.5);
    }
    
    .music-control:hover {
        transform: scale(1.08);
        box-shadow: 0 6px 25px rgba(255, 20, 147, 0.7);
    }
}

/* ========== MOBILE OPTIMIZATIONS ========== */
@media (max-width: 768px) {
    body {
        background-size: 300% 300%;
    }
    
    .title {
        letter-spacing: 0.5px;
        filter: drop-shadow(0 0 12px rgba(255, 63, 127, 0.5));
    }
    
    /* Reduce animation complexity on mobile */
    .heart {
        box-shadow: 
            0 0 30px rgba(255, 20, 147, 0.7),
            0 0 60px rgba(255, 105, 180, 0.4),
            inset 0 0 15px rgba(255, 255, 255, 0.25);
    }
    
    /* Lighter blur on mobile */
    .popup-msg {
        backdrop-filter: blur(4px);
    }
    
    .music-control {
        backdrop-filter: blur(4px);
    }
    
    /* Prevent text selection on mobile */
    * {
        -webkit-user-select: none;
        user-select: none;
    }
}

/* ========== VERY SMALL SCREENS ========== */
@media (max-width: 480px) {
    .container {
        width: 95%;
        padding: 15px;
    }
    
    .popup-msg {
        max-width: 90vw;
        font-size: 14px;
        padding: 10px 16px;
    }
}

/* ========== LANDSCAPE MOBILE ========== */
@media (max-width: 896px) and (orientation: landscape) {
    .container {
        top: 50%;
        transform: translate(-50%, -50%) scale(0.85);
    }
    
    .title {
        margin-bottom: 30px;
    }
    
    .subtext {
        margin-top: 25px;
    }
}

</style>
</head>

<body>

<!-- Stars Background -->
<div class="stars" id="starsContainer"></div>

<!-- Floating Hearts Background -->
<div class="floating-hearts" id="floatingHearts"></div>

<!-- Main Content -->
<div class="container">
    <div class="title">Anh muốn nói với em là ...</div>
    
    <div class="heart-container">
        <div class="heart" id="mainHeart"></div>
    </div>
    
    <div class="subtext">Bấm vào trái tim 💗</div>
</div>

<!-- Music Control -->
<div class="music-control" id="musicControl" onclick="toggleMusic()">
    🎵 Music ON
</div>

<!-- Background Music -->
<audio id="bgMusic" autoplay loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>
// ========== MOBILE DETECTION ==========
const isMobile = window.innerWidth <= 768;
const isVerySmall = window.innerWidth <= 480;

// ========== CREATE STARS (Adaptive count) ==========
const starsContainer = document.getElementById('starsContainer');
const starCount = isMobile ? 80 : 150; // Fewer stars on mobile for performance

for (let i = 0; i < starCount; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.animationDuration = (2 + Math.random() * 4) + 's';
    star.style.animationDelay = Math.random() * 4 + 's';
    starsContainer.appendChild(star);
}

// ========== CREATE FLOATING HEARTS (Adaptive count) ==========
const floatingHearts = document.getElementById('floatingHearts');
const heartCount = isMobile ? 15 : 30; // Fewer hearts on mobile

for (let i = 0; i < heartCount; i++) {
    const heart = document.createElement('div');
    heart.className = 'bg-heart';
    heart.innerHTML = '❤️';
    heart.style.left = Math.random() * 100 + '%';
    heart.style.fontSize = (isMobile ? 16 : 18) + (Math.random() * (isMobile ? 12 : 20)) + 'px';
    heart.style.setProperty('--drift', (Math.random() - 0.5) * (isMobile ? 120 : 200) + 'px');
    heart.style.animationDuration = (10 + Math.random() * 10) + 's';
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
        bgMusic.muted = false;
        bgMusic.play().catch(e => console.log('Play blocked:', e));
        musicControl.innerHTML = '🎵 Music ON';
        musicPlaying = true;
    }
}

// Try to autoplay music (may be blocked by browser)
document.body.addEventListener('click', function startMusic() {
    if (!musicPlaying) {
        bgMusic.muted = false;
        bgMusic.play().then(() => {
            musicPlaying = true;
            musicControl.innerHTML = '🎵 Music ON';
        }).catch(e => console.log('Autoplay blocked'));
    }
}, { once: true });

// ========== MESSAGES ARRAY ==========
const messages = [
    "Anh nhớ em 💗",
    "Anh yêu em ❤️",
    "Quay lại đi mà 🥺",
    "Anh luôn ở đây",
    "Smile đi ✨",
    "You mean everything to me 💫",
    "Đừng buồn nữa nhé",
    "Em là điều tuyệt vời nhất 🌟",
    "Anh sẽ chờ em",
    "Forever and always 💕",
    "Em đặc biệt lắm 🌹",
    "Thinking of you 💭",
    "Anh thương em lắm 💖",
    "Be mine 💓"
];

// ========== CREATE RIPPLE EFFECT ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    
    const size = isMobile ? 200 : 400;
    ripple.style.left = (x - size/2) + 'px';
    ripple.style.top = (y - size/2) + 'px';
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 1000);
}

// ========== CREATE EXPLOSION HEARTS (Adaptive) ==========
function createExplosion(x, y) {
    const numHearts = isMobile ? 12 : 16; // Fewer hearts on mobile
    const radius = isMobile ? 150 : 250;
    
    for (let i = 0; i < numHearts; i++) {
        const angle = (i / numHearts) * Math.PI * 2;
        const tx = Math.cos(angle) * radius + (Math.random() - 0.5) * (isMobile ? 60 : 120);
        const ty = Math.sin(angle) * radius + (Math.random() - 0.5) * (isMobile ? 60 : 120);
        
        const heart = document.createElement('div');
        heart.className = 'explosion-heart';
        heart.innerHTML = '❤️';
        heart.style.left = x + 'px';
        heart.style.top = y + 'px';
        heart.style.setProperty('--tx', tx + 'px');
        heart.style.setProperty('--ty', ty + 'px');
        
        document.body.appendChild(heart);
        
        setTimeout(() => heart.remove(), 1500);
    }
}

// ========== CREATE POPUP MESSAGE (MOBILE OPTIMIZED) ==========
function createPopup() {
    const msg = messages[Math.floor(Math.random() * messages.length)];
    const popup = document.createElement('div');
    popup.className = 'popup-msg';
    popup.innerHTML = msg;
    
    // Mobile-friendly positioning
    const margin = isVerySmall ? 20 : 40;
    const maxWidth = isVerySmall ? window.innerWidth * 0.9 : 320;
    
    const x = margin + Math.random() * (window.innerWidth - maxWidth - margin * 2);
    const y = margin + Math.random() * (window.innerHeight - 80 - margin * 2);
    
    popup.style.left = x + 'px';
    popup.style.top = y + 'px';
    
    document.body.appendChild(popup);
    
    setTimeout(() => popup.remove(), 5000);
}

// ========== MAIN HEART CLICK HANDLER (OPTIMIZED) ==========
let clickCount = 0;
const mainHeart = document.getElementById('mainHeart');

// Prevent double-tap zoom on mobile
let lastTap = 0;
mainHeart.addEventListener('touchend', function(e) {
    const currentTime = new Date().getTime();
    const tapLength = currentTime - lastTap;
    if (tapLength < 500 && tapLength > 0) {
        e.preventDefault();
    }
    lastTap = currentTime;
});

mainHeart.addEventListener('click', function(e) {
    e.preventDefault();
    clickCount++;
    
    // Auto-start music on first click
    if (!musicPlaying) {
        toggleMusic();
    }
    
    // Get heart center position
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Create ripple
    createRipple(centerX, centerY);
    
    // Create explosion
    createExplosion(centerX, centerY);
    
    // Adaptive popup spam count
    const spamCount = isMobile ? 
        (clickCount === 1 ? 30 : 20) : 
        (clickCount === 1 ? 60 : 35);
    
    // Slower interval on mobile for better performance
    const interval_time = isMobile ? 50 : 35;
    
    let count = 0;
    const interval = setInterval(() => {
        createPopup();
        count++;
        
        if (count >= spamCount) {
            clearInterval(interval);
        }
    }, interval_time);
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

// ========== PREVENT SCROLLING ON MOBILE ==========
document.body.addEventListener('touchmove', function(e) {
    e.preventDefault();
}, { passive: false });

// ========== VIEWPORT HEIGHT FIX FOR MOBILE ==========
function setVH() {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
}

setVH();
window.addEventListener('resize', setVH);
window.addEventListener('orientationchange', setVH);

</script>

</body>
</html>
"""

# ===== PREVENT RERUN ANIMATION RESET =====
if "loaded" not in st.session_state:
    st.session_state.loaded = True

# ===== RENDER =====
components.html(html, height=900, scrolling=False)