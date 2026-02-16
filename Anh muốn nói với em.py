import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="❤️ Confession", page_icon="❤️")

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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #1a0033 0%, #330033 25%, #4d004d 50%, #330033 75%, #1a0033 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    position: relative;
    min-height: 100vh;
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
}

/* ========== TITLE ========== */
.title {
    font-size: clamp(36px, 7vw, 68px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff6fa8, #ff3f7f, #ff94c2, #ffb3d9);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 60px;
    animation: titleGlow 3s ease-in-out infinite, titleWave 4s ease-in-out infinite;
    filter: drop-shadow(0 0 30px rgba(255, 63, 127, 0.8));
    letter-spacing: 2px;
}

@keyframes titleGlow {
    0%, 100% { 
        filter: drop-shadow(0 0 20px rgba(255, 63, 127, 0.6)); 
    }
    50% { 
        filter: drop-shadow(0 0 50px rgba(255, 63, 127, 1)); 
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
    margin: 30px 0;
}

.heart {
    width: 150px;
    height: 150px;
    position: relative;
    transform: rotate(-45deg);
    cursor: pointer;
    margin: auto;
    
    background: linear-gradient(135deg, #ff1493, #ff69b4, #ff1493);
    background-size: 200% 200%;
    
    box-shadow: 
        0 0 60px rgba(255, 20, 147, 0.9),
        0 0 100px rgba(255, 105, 180, 0.6),
        inset 0 0 30px rgba(255, 255, 255, 0.4);
    
    animation: heartBeat 1.4s ease-in-out infinite, heartGlow 2s ease-in-out infinite;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.heart:hover {
    transform: rotate(-45deg) scale(1.2);
    box-shadow: 
        0 0 80px rgba(255, 20, 147, 1),
        0 0 120px rgba(255, 105, 180, 0.8),
        inset 0 0 40px rgba(255, 255, 255, 0.6);
}

.heart:active {
    transform: rotate(-45deg) scale(0.9);
}

.heart:before,
.heart:after {
    content: "";
    width: 150px;
    height: 150px;
    position: absolute;
    background: inherit;
    border-radius: 50%;
}

.heart:before {
    top: -75px;
    left: 0;
}

.heart:after {
    left: 75px;
    top: 0;
}

@keyframes heartBeat {
    0% { transform: scale(1) rotate(-45deg); }
    15% { transform: scale(1.15) rotate(-45deg); }
    30% { transform: scale(1) rotate(-45deg); }
    45% { transform: scale(1.25) rotate(-45deg); }
    60% { transform: scale(1) rotate(-45deg); }
    75% { transform: scale(1.1) rotate(-45deg); }
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
    margin-top: 50px;
    font-size: clamp(18px, 4vw, 24px);
    color: #ffb3d9;
    font-weight: 600;
    animation: pulse 2.5s ease-in-out infinite;
    text-shadow: 0 0 10px rgba(255, 179, 217, 0.8);
}

@keyframes pulse {
    0%, 100% { opacity: 0.7; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
}

/* ========== EXPLOSION HEARTS ========== */
.explosion-heart {
    position: fixed;
    font-size: 35px;
    pointer-events: none;
    z-index: 100;
    animation: explode 1.5s ease-out forwards;
    filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.8));
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

/* ========== POPUP MESSAGES ========== */
.popup-msg {
    position: fixed;
    padding: 18px 28px;
    border-radius: 20px;
    color: #fff;
    font-weight: 700;
    font-size: clamp(15px, 3vw, 20px);
    pointer-events: none;
    z-index: 200;
    
    background: rgba(255, 20, 147, 0.9);
    backdrop-filter: blur(12px);
    border: 2px solid rgba(255, 255, 255, 0.4);
    
    box-shadow: 
        0 10px 40px rgba(255, 20, 147, 0.6),
        inset 0 0 20px rgba(255, 255, 255, 0.3);
    
    animation: popupFade 3.5s ease-out forwards;
}

@keyframes popupFade {
    0% {
        transform: translateY(30px) scale(0.5);
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
        transform: translateY(-30px);
        opacity: 0;
    }
}

/* ========== RIPPLE EFFECT ========== */
.ripple {
    position: fixed;
    border-radius: 50%;
    border: 4px solid rgba(255, 20, 147, 0.9);
    pointer-events: none;
    animation: rippleExpand 1s ease-out forwards;
}

@keyframes rippleExpand {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 400px;
        height: 400px;
        opacity: 0;
    }
}

/* ========== MUSIC CONTROL ========== */
.music-control {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: rgba(255, 20, 147, 0.8);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    padding: 12px 20px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    z-index: 1000;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(255, 20, 147, 0.5);
}

.music-control:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 30px rgba(255, 20, 147, 0.8);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .heart {
        width: 110px;
        height: 110px;
    }
    .heart:before,
    .heart:after {
        width: 110px;
        height: 110px;
    }
    .heart:before { top: -55px; }
    .heart:after { left: 55px; }
    
    .title {
        font-size: 32px;
        margin-bottom: 40px;
    }
    
    .subtext {
        font-size: 16px;
        margin-top: 35px;
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
    <div class="title">Anh muốn nói với em là...</div>
    
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
<audio id="bgMusic" loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>

<script>

// ========== CREATE STARS ==========
const starsContainer = document.getElementById('starsContainer');
for (let i = 0; i < 150; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.animationDuration = (2 + Math.random() * 4) + 's';
    star.style.animationDelay = Math.random() * 4 + 's';
    starsContainer.appendChild(star);
}

// ========== CREATE FLOATING HEARTS ==========
const floatingHearts = document.getElementById('floatingHearts');
for (let i = 0; i < 30; i++) {
    const heart = document.createElement('div');
    heart.className = 'bg-heart';
    heart.innerHTML = '❤️';
    heart.style.left = Math.random() * 100 + '%';
    heart.style.fontSize = (18 + Math.random() * 20) + 'px';
    heart.style.setProperty('--drift', (Math.random() - 0.5) * 200 + 'px');
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
        bgMusic.play().catch(e => {
            console.log('Music autoplay blocked. User interaction needed.');
        });
        musicControl.innerHTML = '🎵 Music ON';
        musicPlaying = true;
    }
}

// Try to autoplay music (may be blocked by browser)
setTimeout(() => {
    bgMusic.play().then(() => {
        musicPlaying = true;
        musicControl.innerHTML = '🎵 Music ON';
    }).catch(e => {
        console.log('Autoplay blocked');
    });
}, 1000);

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
    "Be mine 💝"
];

// ========== CREATE RIPPLE EFFECT ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 200) + 'px';
    ripple.style.top = (y - 200) + 'px';
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 1000);
}

// ========== CREATE EXPLOSION HEARTS ==========
function createExplosion(x, y) {
    const numHearts = 16;
    const radius = 250;
    
    for (let i = 0; i < numHearts; i++) {
        const angle = (i / numHearts) * Math.PI * 2;
        const tx = Math.cos(angle) * radius + (Math.random() - 0.5) * 120;
        const ty = Math.sin(angle) * radius + (Math.random() - 0.5) * 120;
        
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

// ========== CREATE POPUP MESSAGE ==========
function createPopup() {
    const msg = messages[Math.floor(Math.random() * messages.length)];
    const popup = document.createElement('div');
    popup.className = 'popup-msg';
    popup.innerHTML = msg;
    
    const x = Math.random() * (window.innerWidth - 250) + 125;
    const y = Math.random() * (window.innerHeight - 100) + 50;
    
    popup.style.left = x + 'px';
    popup.style.top = y + 'px';
    
    document.body.appendChild(popup);
    
    setTimeout(() => popup.remove(), 3500);
}

// ========== MAIN HEART CLICK HANDLER ==========
let clickCount = 0;
const mainHeart = document.getElementById('mainHeart');

mainHeart.addEventListener('click', function(e) {
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
    
    // Spam popups
    const spamCount = clickCount === 1 ? 60 : 35;
    let count = 0;
    
    const interval = setInterval(() => {
        createPopup();
        count++;
        
        if (count >= spamCount) {
            clearInterval(interval);
        }
    }, 35);
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

components.html(html, height=900, scrolling=False)
