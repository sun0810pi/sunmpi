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
    background: linear-gradient(270deg, #0a0015, #1a0033, #330033, #1a0033, #0a0015);
    background-size: 600% 600%;
    animation: gradientFlow 18s ease infinite;
    position: relative;
}

@keyframes gradientFlow {
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
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
}

/* ========== FLOATING HEARTS BACKGROUND ========== */
.floating-hearts {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
}

.bg-heart {
    position: absolute;
    font-size: 20px;
    opacity: 0;
    animation: floatUp linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.6;
    }
    90% {
        opacity: 0.3;
    }
    100% {
        transform: translateY(-120vh) rotate(360deg);
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
    font-size: clamp(32px, 8vw, 72px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff6fa8, #ff3f7f, #ff94c2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 50px;
    text-shadow: 0 0 30px rgba(255, 63, 127, 0.5);
    animation: titleGlow 2s ease-in-out infinite;
}

@keyframes titleGlow {
    0%, 100% { filter: drop-shadow(0 0 20px rgba(255, 63, 127, 0.6)); }
    50% { filter: drop-shadow(0 0 40px rgba(255, 63, 127, 1)); }
}

/* ========== MAIN HEART (CSS SHAPE) ========== */
.heart-container {
    position: relative;
    display: inline-block;
    margin: 20px 0;
}

.heart {
    width: 140px;
    height: 140px;
    position: relative;
    transform: rotate(-45deg);
    cursor: pointer;
    margin: auto;
    
    background: linear-gradient(135deg, #ff2d75, #ff6fa8, #ff2d75);
    background-size: 200% 200%;
    
    box-shadow: 
        0 0 60px rgba(255, 45, 117, 0.8),
        inset 0 0 30px rgba(255, 255, 255, 0.3);
    
    animation: heartBeat 1.3s ease-in-out infinite;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.heart:hover {
    transform: rotate(-45deg) scale(1.15);
    box-shadow: 
        0 0 80px rgba(255, 45, 117, 1),
        inset 0 0 40px rgba(255, 255, 255, 0.5);
}

.heart:active {
    transform: rotate(-45deg) scale(0.95);
}

.heart:before,
.heart:after {
    content: "";
    width: 140px;
    height: 140px;
    position: absolute;
    background: inherit;
    border-radius: 50%;
}

.heart:before {
    top: -70px;
    left: 0;
}

.heart:after {
    left: 70px;
    top: 0;
}

@keyframes heartBeat {
    0% { transform: scale(1) rotate(-45deg); }
    20% { transform: scale(1.15) rotate(-45deg); }
    35% { transform: scale(1) rotate(-45deg); }
    50% { transform: scale(1.22) rotate(-45deg); }
    65% { transform: scale(1) rotate(-45deg); }
    80% { transform: scale(1.1) rotate(-45deg); }
    100% { transform: scale(1) rotate(-45deg); }
}

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: 40px;
    font-size: clamp(16px, 4vw, 22px);
    color: #ffb3d9;
    font-weight: 500;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
}

/* ========== EXPLOSION HEARTS ========== */
.explosion-heart {
    position: fixed;
    font-size: 30px;
    pointer-events: none;
    z-index: 100;
    animation: explode 1.2s ease-out forwards;
}

@keyframes explode {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--tx), var(--ty)) scale(0.3) rotate(720deg);
        opacity: 0;
    }
}

/* ========== POPUP MESSAGES ========== */
.popup-msg {
    position: fixed;
    padding: 16px 24px;
    border-radius: 20px;
    color: #fff;
    font-weight: 700;
    font-size: clamp(14px, 3vw, 18px);
    pointer-events: none;
    z-index: 200;
    
    background: rgba(255, 45, 117, 0.85);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    
    box-shadow: 
        0 8px 32px rgba(255, 45, 117, 0.4),
        inset 0 0 20px rgba(255, 255, 255, 0.2);
    
    animation: popupFade 3s ease-out forwards;
}

@keyframes popupFade {
    0% {
        transform: translateY(20px) scale(0.5);
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
    border: 3px solid rgba(255, 45, 117, 0.8);
    pointer-events: none;
    animation: rippleExpand 0.8s ease-out forwards;
}

@keyframes rippleExpand {
    0% {
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        width: 300px;
        height: 300px;
        opacity: 0;
    }
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .heart {
        width: 100px;
        height: 100px;
    }
    .heart:before,
    .heart:after {
        width: 100px;
        height: 100px;
    }
    .heart:before { top: -50px; }
    .heart:after { left: 50px; }
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

<!-- Audio Elements -->
<audio id="heartbeatSound" preload="auto">
    <source src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJysvMzc7P0NHS09TV1tfY2drb3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj5OXm5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/w==" type="audio/wav">
</audio>
<audio id="popSound" preload="auto">
    <source src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAAD/AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj5OXm5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/w==" type="audio/wav">
</audio>

<script>

// ========== CREATE STARS ==========
const starsContainer = document.getElementById('starsContainer');
for (let i = 0; i < 100; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.animationDuration = (2 + Math.random() * 3) + 's';
    star.style.animationDelay = Math.random() * 3 + 's';
    starsContainer.appendChild(star);
}

// ========== CREATE FLOATING HEARTS ==========
const floatingHearts = document.getElementById('floatingHearts');
for (let i = 0; i < 20; i++) {
    const heart = document.createElement('div');
    heart.className = 'bg-heart';
    heart.innerHTML = '❤️';
    heart.style.left = Math.random() * 100 + '%';
    heart.style.fontSize = (15 + Math.random() * 15) + 'px';
    heart.style.animationDuration = (8 + Math.random() * 8) + 's';
    heart.style.animationDelay = Math.random() * 10 + 's';
    floatingHearts.appendChild(heart);
}

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
    "Thinking of you 💭"
];

// ========== PLAY SOUND ==========
function playSound(audioId) {
    const audio = document.getElementById(audioId);
    audio.currentTime = 0;
    audio.play().catch(e => console.log('Audio play failed:', e));
}

// ========== CREATE RIPPLE EFFECT ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 150) + 'px';
    ripple.style.top = (y - 150) + 'px';
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 800);
}

// ========== CREATE EXPLOSION HEARTS ==========
function createExplosion(x, y) {
    const numHearts = 12;
    const radius = 200;
    
    for (let i = 0; i < numHearts; i++) {
        const angle = (i / numHearts) * Math.PI * 2;
        const tx = Math.cos(angle) * radius + (Math.random() - 0.5) * 100;
        const ty = Math.sin(angle) * radius + (Math.random() - 0.5) * 100;
        
        const heart = document.createElement('div');
        heart.className = 'explosion-heart';
        heart.innerHTML = '❤️';
        heart.style.left = x + 'px';
        heart.style.top = y + 'px';
        heart.style.setProperty('--tx', tx + 'px');
        heart.style.setProperty('--ty', ty + 'px');
        
        document.body.appendChild(heart);
        
        setTimeout(() => heart.remove(), 1200);
    }
}

// ========== CREATE POPUP MESSAGE ==========
function createPopup() {
    const msg = messages[Math.floor(Math.random() * messages.length)];
    const popup = document.createElement('div');
    popup.className = 'popup-msg';
    popup.innerHTML = msg;
    
    const x = Math.random() * (window.innerWidth - 200) + 100;
    const y = Math.random() * (window.innerHeight - 100) + 50;
    
    popup.style.left = x + 'px';
    popup.style.top = y + 'px';
    
    document.body.appendChild(popup);
    
    setTimeout(() => popup.remove(), 3000);
}

// ========== MAIN HEART CLICK HANDLER ==========
let clickCount = 0;
const mainHeart = document.getElementById('mainHeart');

mainHeart.addEventListener('click', function(e) {
    clickCount++;
    
    // Play sound
    playSound(clickCount === 1 ? 'heartbeatSound' : 'popSound');
    
    // Get heart center position
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Create ripple
    createRipple(centerX, centerY);
    
    // Create explosion
    createExplosion(centerX, centerY);
    
    // Spam popups
    const spamCount = clickCount === 1 ? 50 : 30;
    let count = 0;
    
    const interval = setInterval(() => {
        createPopup();
        count++;
        
        if (count >= spamCount) {
            clearInterval(interval);
        }
    }, 40);
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

components.html(html, height=900, scrolling=False)
