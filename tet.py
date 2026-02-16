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
    background: #1a0a00;
    position: relative;
    min-height: 100vh;
    perspective: 1000px;
}

/* ========== LAYERED BACKGROUND ========== */
.bg-layer {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}

.bg-layer-1 {
    background: linear-gradient(135deg, #ff6b00 0%, #ffa500 25%, #ffcc00 50%, #ff8c00 75%, #ff4500 100%);
    background-size: 400% 400%;
    animation: gradientShift 25s ease infinite;
    z-index: 1;
}

.bg-layer-2 {
    background-image: 
        repeating-linear-gradient(45deg, transparent, transparent 50px, rgba(255, 215, 0, 0.03) 50px, rgba(255, 215, 0, 0.03) 100px),
        repeating-linear-gradient(-45deg, transparent, transparent 50px, rgba(255, 0, 0, 0.02) 50px, rgba(255, 0, 0, 0.02) 100px);
    z-index: 2;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ========== CORNER BRANCHES ========== */
.branch {
    position: fixed;
    z-index: 5;
    pointer-events: none;
}

.branch-top-left {
    top: 0;
    left: 0;
    width: 300px;
    height: 300px;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><path d="M0,0 Q50,30 80,50 T120,90 L100,100 Q70,80 50,70 T20,50 Z" fill="%238B4513" opacity="0.8"/><circle cx="90" cy="70" r="15" fill="%23FFB6C1"/><circle cx="110" cy="85" r="12" fill="%23FFC0CB"/><circle cx="70" cy="55" r="13" fill="%23FFB6C1"/><circle cx="50" cy="45" r="10" fill="%23FFC0CB"/></svg>') no-repeat;
    background-size: contain;
    animation: branchSway 4s ease-in-out infinite;
    filter: drop-shadow(0 5px 15px rgba(139, 69, 19, 0.3));
}

.branch-top-right {
    top: 0;
    right: 0;
    width: 300px;
    height: 300px;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><path d="M300,0 Q250,30 220,50 T180,90 L200,100 Q230,80 250,70 T280,50 Z" fill="%238B4513" opacity="0.8"/><circle cx="210" cy="70" r="15" fill="%23FFD700"/><circle cx="190" cy="85" r="12" fill="%23FFA500"/><circle cx="230" cy="55" r="13" fill="%23FFD700"/><circle cx="250" cy="45" r="10" fill="%23FFA500"/></svg>') no-repeat;
    background-size: contain;
    animation: branchSway 4s ease-in-out infinite reverse;
    filter: drop-shadow(0 5px 15px rgba(139, 69, 19, 0.3));
}

@keyframes branchSway {
    0%, 100% { transform: rotate(-2deg); }
    50% { transform: rotate(2deg); }
}

/* ========== PEACH BLOSSOMS ========== */
.blossoms {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 4;
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
    10% { opacity: 0.9; }
    50% { opacity: 0.7; }
    90% { opacity: 0.4; }
    100% {
        transform: translateY(110vh) translateX(var(--drift)) rotate(720deg);
        opacity: 0;
    }
}

/* ========== LANTERNS ========== */
.lanterns {
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 6;
}

.lantern {
    position: absolute;
    width: 50px;
    height: 70px;
    background: linear-gradient(180deg, #ff0000 0%, #cc0000 50%, #ff0000 100%);
    border-radius: 0 0 25px 25px;
    box-shadow: 
        0 0 30px rgba(255, 215, 0, 0.9),
        inset 0 5px 15px rgba(255, 255, 255, 0.4);
    animation: swingLantern 4s ease-in-out infinite;
}

.lantern::before {
    content: '福';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: gold;
    font-size: 26px;
    font-weight: 900;
    text-shadow: 0 0 15px rgba(255, 215, 0, 1);
}

.lantern::after {
    content: '';
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    width: 35px;
    height: 12px;
    background: #8b0000;
    border-radius: 6px;
}

.lantern-tassel {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    width: 3px;
    height: 25px;
    background: linear-gradient(180deg, gold, #ffa500);
    animation: tassalSway 3s ease-in-out infinite;
}

.lantern-tassel::after {
    content: '🔸';
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
}

@keyframes swingLantern {
    0%, 100% { transform: translateX(-20px) rotate(-8deg); }
    50% { transform: translateX(20px) rotate(8deg); }
}

@keyframes tassalSway {
    0%, 100% { transform: translateX(-50%) rotate(-15deg); }
    50% { transform: translateX(-50%) rotate(15deg); }
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
    width: 5px;
    height: 5px;
    background: gold;
    border-radius: 50%;
    opacity: 0;
    animation: sparkle linear infinite;
    box-shadow: 0 0 15px gold;
}

@keyframes sparkle {
    0% {
        transform: translateY(100vh) scale(0) rotate(0deg);
        opacity: 0;
    }
    20% { opacity: 1; }
    80% { opacity: 0.9; }
    100% {
        transform: translateY(-10vh) scale(2) rotate(360deg);
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
    font-size: clamp(42px, 9vw, 90px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff0000, #ffd700, #ff0000, #ffd700);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 40px;
    animation: titleGlow 3s ease-in-out infinite, titleWave 5s ease-in-out infinite;
    filter: drop-shadow(0 0 40px rgba(255, 215, 0, 1));
    letter-spacing: 6px;
    position: relative;
}

.title::before,
.title::after {
    content: '✨';
    position: absolute;
    font-size: 40px;
    animation: sparkleFloat 3s ease-in-out infinite;
}

.title::before {
    left: -60px;
    animation-delay: 0s;
}

.title::after {
    right: -60px;
    animation-delay: 1.5s;
}

@keyframes sparkleFloat {
    0%, 100% { transform: translateY(0) scale(1); opacity: 0.7; }
    50% { transform: translateY(-20px) scale(1.3); opacity: 1; }
}

@keyframes titleGlow {
    0%, 100% { filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.8)); }
    50% { filter: drop-shadow(0 0 70px rgba(255, 215, 0, 1)); }
}

@keyframes titleWave {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ========== 3D RED ENVELOPE ========== */
.envelope-container {
    position: relative;
    display: inline-block;
    margin: 40px 0;
    perspective: 1500px;
}

.envelope {
    width: 220px;
    height: 300px;
    position: relative;
    cursor: pointer;
    margin: auto;
    transform-style: preserve-3d;
    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    animation: envelopeFloat 3s ease-in-out infinite;
}

@keyframes envelopeFloat {
    0%, 100% { transform: translateY(0) rotateY(0deg); }
    50% { transform: translateY(-15px) rotateY(5deg); }
}

.envelope:hover {
    transform: scale(1.2) rotateY(15deg) translateZ(30px);
    animation: none;
}

.envelope:active {
    transform: scale(0.95);
}

/* Envelope body */
.envelope-body {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 30%, #ff1744 50%, #ff0000 70%, #d32f2f 100%);
    border-radius: 15px;
    box-shadow: 
        0 30px 80px rgba(0, 0, 0, 0.6),
        0 0 100px rgba(255, 215, 0, 0.7),
        inset 0 0 60px rgba(255, 215, 0, 0.4),
        inset -10px -10px 30px rgba(0, 0, 0, 0.3);
    position: relative;
    overflow: hidden;
    transform-style: preserve-3d;
}

/* 3D Depth layers */
.envelope-body::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, transparent 0%, rgba(255, 255, 255, 0.2) 50%, transparent 100%);
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { transform: translateX(-100%); }
    50% { transform: translateX(100%); }
}

/* Golden ornate border */
.envelope-border {
    position: absolute;
    top: 15px;
    left: 15px;
    right: 15px;
    bottom: 15px;
    border: 4px solid gold;
    border-radius: 12px;
    box-shadow: 
        inset 0 0 30px rgba(255, 215, 0, 0.7),
        0 0 20px rgba(255, 215, 0, 0.5);
}

/* Corner ornaments */
.corner-ornament {
    position: absolute;
    width: 40px;
    height: 40px;
    background: radial-gradient(circle, gold, #ffa500);
    clip-path: polygon(0 0, 100% 0, 0 100%);
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
}

.corner-ornament.tl { top: 10px; left: 10px; }
.corner-ornament.tr { top: 10px; right: 10px; transform: rotate(90deg); }
.corner-ornament.bl { bottom: 10px; left: 10px; transform: rotate(-90deg); }
.corner-ornament.br { bottom: 10px; right: 10px; transform: rotate(180deg); }

/* 福 Character - 3D */
.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) translateZ(20px);
    font-size: 110px;
    font-weight: 900;
    color: gold;
    text-shadow: 
        0 0 40px rgba(255, 215, 0, 1),
        0 0 70px rgba(255, 215, 0, 0.9),
        5px 5px 0 rgba(139, 0, 0, 0.6),
        -2px -2px 0 rgba(255, 255, 255, 0.3);
    z-index: 3;
    animation: fuPulse 2.5s ease-in-out infinite;
    filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.4));
}

@keyframes fuPulse {
    0%, 100% { transform: translate(-50%, -50%) translateZ(20px) scale(1); }
    50% { transform: translate(-50%, -50%) translateZ(30px) scale(1.12); }
}

/* Decorative clouds pattern */
.cloud-pattern {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(ellipse at 30% 20%, rgba(255, 215, 0, 0.15) 0%, transparent 40%),
        radial-gradient(ellipse at 70% 80%, rgba(255, 215, 0, 0.15) 0%, transparent 40%);
    z-index: 1;
}

/* ========== CLICK COUNTER ========== */
.counter {
    position: fixed;
    top: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(204, 0, 0, 0.9));
    backdrop-filter: blur(15px);
    border: 3px solid gold;
    border-radius: 50px;
    padding: 15px 35px;
    color: gold;
    font-weight: 900;
    font-size: 22px;
    z-index: 1000;
    box-shadow: 
        0 10px 40px rgba(255, 0, 0, 0.6),
        0 0 40px rgba(255, 215, 0, 0.5),
        inset 0 0 20px rgba(255, 215, 0, 0.3);
    animation: counterGlow 2s ease-in-out infinite;
}

@keyframes counterGlow {
    0%, 100% { box-shadow: 0 10px 40px rgba(255, 0, 0, 0.6), 0 0 40px rgba(255, 215, 0, 0.5); }
    50% { box-shadow: 0 10px 50px rgba(255, 0, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.8); }
}

.counter-value {
    font-size: 32px;
    animation: counterPulse 0.5s ease-out;
}

@keyframes counterPulse {
    0% { transform: scale(1.5); }
    100% { transform: scale(1); }
}

/* ========== SUBTEXT ========== */
.subtext {
    margin-top: 45px;
    font-size: clamp(22px, 4.5vw, 30px);
    color: #fff;
    font-weight: 800;
    animation: pulse 2.5s ease-in-out infinite;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 1),
        3px 3px 6px rgba(0, 0, 0, 0.6);
    background: linear-gradient(90deg, #ff0000, #ffd700, #ff0000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

@keyframes pulse {
    0%, 100% { opacity: 0.85; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
}

/* ========== MONEY BILLS ========== */
.money {
    position: fixed;
    width: 60px;
    height: 30px;
    background: linear-gradient(135deg, #228b22, #32cd32);
    border: 2px solid #ffd700;
    border-radius: 5px;
    pointer-events: none;
    z-index: 110;
    animation: moneyFly 2s ease-out forwards;
    box-shadow: 0 5px 20px rgba(255, 215, 0, 0.6);
}

.money::before {
    content: '💵';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 20px;
}

@keyframes moneyFly {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--mx), var(--my)) rotate(var(--mr)) scale(0.3);
        opacity: 0;
    }
}

/* ========== LION & DRAGON ========== */
.creature {
    position: fixed;
    font-size: 50px;
    pointer-events: none;
    z-index: 100;
    animation: creatureJump 2.5s ease-out forwards;
    filter: drop-shadow(0 0 20px rgba(255, 215, 0, 1));
}

@keyframes creatureJump {
    0% {
        transform: translate(0, 0) scale(0.8) rotate(0deg);
        opacity: 1;
    }
    25% {
        transform: translate(var(--cx1), var(--cy1)) scale(1.4) rotate(120deg);
        opacity: 1;
    }
    50% {
        transform: translate(var(--cx2), var(--cy2)) scale(1.2) rotate(240deg);
        opacity: 0.9;
    }
    75% {
        transform: translate(var(--cx3), var(--cy3)) scale(1) rotate(480deg);
        opacity: 0.6;
    }
    100% {
        transform: translate(var(--cx4), var(--cy4)) scale(0.4) rotate(720deg);
        opacity: 0;
    }
}

/* ========== CONFETTI ========== */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    pointer-events: none;
    z-index: 120;
    animation: confettiFall 3s ease-out forwards;
}

@keyframes confettiFall {
    0% {
        transform: translate(0, 0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--cfx), var(--cfy)) rotate(720deg);
        opacity: 0;
    }
}

/* ========== BLESSING SCROLL - ENHANCED ========== */
.scroll {
    position: fixed;
    width: 380px;
    min-height: 220px;
    pointer-events: none;
    z-index: 200;
    animation: scrollAppear 4.5s ease-out forwards;
}

.scroll-rod {
    position: absolute;
    width: 35px;
    height: 100%;
    background: linear-gradient(90deg, #3d2817, #6b4423, #8b5a2b, #6b4423, #3d2817);
    top: 0;
    border-radius: 17px;
    box-shadow: 
        inset 0 0 20px rgba(0, 0, 0, 0.6),
        0 5px 15px rgba(0, 0, 0, 0.4);
}

.scroll-rod.left {
    left: -40px;
}

.scroll-rod.right {
    right: -40px;
}

.scroll-rod::before,
.scroll-rod::after {
    content: '';
    position: absolute;
    width: 45px;
    height: 15px;
    background: linear-gradient(90deg, #8b4513, #a0522d, #8b4513);
    left: 50%;
    transform: translateX(-50%);
    border-radius: 7px;
}

.scroll-rod::before { top: -5px; }
.scroll-rod::after { bottom: -5px; }

.scroll-content {
    position: relative;
    background: linear-gradient(180deg, #8b0000 0%, #b22222 25%, #cc0000 50%, #b22222 75%, #8b0000 100%);
    border-radius: 15px;
    padding: 35px 25px;
    border: 5px solid gold;
    box-shadow: 
        0 25px 70px rgba(0, 0, 0, 0.7),
        0 0 50px rgba(255, 215, 0, 0.8),
        inset 0 0 40px rgba(255, 215, 0, 0.4);
}

.scroll-content::before {
    content: '';
    position: absolute;
    top: 10px;
    left: 10px;
    right: 10px;
    bottom: 10px;
    border: 2px solid rgba(255, 215, 0, 0.4);
    border-radius: 10px;
}

.scroll-text {
    color: gold;
    font-size: 24px;
    font-weight: 800;
    text-align: center;
    line-height: 1.8;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 0.9),
        3px 3px 6px rgba(0, 0, 0, 0.8);
    font-family: 'Georgia', serif;
    position: relative;
}

.scroll-couplet {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 3px solid rgba(255, 215, 0, 0.6);
    font-size: 19px;
    font-style: italic;
    line-height: 2;
}

/* Red seal stamp */
.seal {
    position: absolute;
    bottom: 15px;
    right: 20px;
    width: 50px;
    height: 50px;
    background: #cc0000;
    border: 3px solid #8b0000;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: white;
    font-weight: 900;
    transform: rotate(-5deg);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.6);
    animation: sealStamp 0.5s ease-out 0.3s backwards;
}

@keyframes sealStamp {
    0% {
        transform: rotate(-5deg) scale(0) translateY(-50px);
        opacity: 0;
    }
    50% {
        transform: rotate(-5deg) scale(1.3);
    }
    100% {
        transform: rotate(-5deg) scale(1);
        opacity: 1;
    }
}

@keyframes scrollAppear {
    0% {
        transform: translateY(60px) scale(0) rotate(-15deg);
        opacity: 0;
    }
    15% {
        transform: translateY(0) scale(1.15) rotate(3deg);
        opacity: 1;
    }
    88% {
        opacity: 1;
    }
    100% {
        transform: translateY(-40px) scale(0.85) rotate(-3deg);
        opacity: 0;
    }
}

/* ========== FIREWORKS ========== */
.firework {
    position: fixed;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 150;
    animation: fireworkExplode 1.5s ease-out forwards;
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

/* ========== RIPPLE ========== */
.ripple {
    position: fixed;
    border-radius: 50%;
    border: 6px solid rgba(255, 215, 0, 1);
    pointer-events: none;
    animation: rippleExpand 1.5s ease-out forwards;
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.9);
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
    background: rgba(255, 0, 0, 0.9);
    backdrop-filter: blur(12px);
    border: 4px solid gold;
    border-radius: 50px;
    padding: 16px 28px;
    color: gold;
    font-weight: 800;
    font-size: 18px;
    cursor: pointer;
    z-index: 1000;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 
        0 8px 30px rgba(255, 0, 0, 0.7),
        0 0 40px rgba(255, 215, 0, 0.5);
}

.music-control:hover {
    transform: scale(1.2) translateY(-5px);
    box-shadow: 
        0 12px 40px rgba(255, 0, 0, 0.9),
        0 0 60px rgba(255, 215, 0, 0.8);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .envelope {
        width: 170px;
        height: 230px;
    }
    
    .envelope-fu {
        font-size: 80px;
    }
    
    .title {
        font-size: 36px;
        margin-bottom: 30px;
    }
    
    .title::before,
    .title::after {
        display: none;
    }
    
    .subtext {
        font-size: 20px;
        margin-top: 30px;
    }
    
    .scroll {
        width: 300px;
    }
    
    .scroll-text {
        font-size: 20px;
    }
    
    .scroll-couplet {
        font-size: 16px;
    }
    
    .counter {
        font-size: 18px;
        padding: 12px 25px;
    }
    
    .counter-value {
        font-size: 26px;
    }
    
    .branch-top-left,
    .branch-top-right {
        width: 200px;
        height: 200px;
    }
}

</style>
</head>

<body>

<!-- Background Layers -->
<div class="bg-layer bg-layer-1"></div>
<div class="bg-layer bg-layer-2"></div>

<!-- Corner Branches -->
<div class="branch branch-top-left"></div>
<div class="branch branch-top-right"></div>

<!-- Peach Blossoms -->
<div class="blossoms" id="blossomsContainer"></div>

<!-- Lanterns -->
<div class="lanterns" id="lanternsContainer"></div>

<!-- Golden Particles -->
<div class="particles" id="particlesContainer"></div>

<!-- Click Counter -->
<div class="counter" id="counter">
    🎊 <span class="counter-value" id="counterValue">0</span> Lời Chúc 🎊
</div>

<!-- Main Content -->
<div class="container">
    <div class="title">Chúc Mừng Năm Mới</div>
    
    <div class="envelope-container">
        <div class="envelope" id="mainEnvelope">
            <div class="envelope-body">
                <div class="cloud-pattern"></div>
                <div class="envelope-border"></div>
                <div class="envelope-fu">福</div>
                <div class="corner-ornament tl"></div>
                <div class="corner-ornament tr"></div>
                <div class="corner-ornament bl"></div>
                <div class="corner-ornament br"></div>
            </div>
        </div>
    </div>
    
    <div class="subtext">🧧 Nhấn Nhận Lộc 🧧</div>
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
const blossomEmojis = ['🌸', '🌺', '🏵️', '💮', '🌼'];

for (let i = 0; i < 50; i++) {
    const blossom = document.createElement('div');
    blossom.className = 'blossom';
    blossom.innerHTML = blossomEmojis[Math.floor(Math.random() * blossomEmojis.length)];
    blossom.style.left = Math.random() * 100 + '%';
    blossom.style.fontSize = (22 + Math.random() * 20) + 'px';
    blossom.style.setProperty('--drift', (Math.random() - 0.5) * 400 + 'px');
    blossom.style.animationDuration = (18 + Math.random() * 18) + 's';
    blossom.style.animationDelay = Math.random() * 12 + 's';
    blossomsContainer.appendChild(blossom);
}

// ========== CREATE LANTERNS ==========
const lanternsContainer = document.getElementById('lanternsContainer');
const lanternPositions = [
    { left: '8%', top: '8%' },
    { left: '22%', top: '4%' },
    { left: '78%', top: '6%' },
    { left: '92%', top: '10%' },
    { left: '12%', top: '82%' },
    { left: '88%', top: '86%' },
    { left: '50%', top: '5%' }
];

lanternPositions.forEach((pos, index) => {
    const lanternWrap = document.createElement('div');
    lanternWrap.style.position = 'absolute';
    lanternWrap.style.left = pos.left;
    lanternWrap.style.top = pos.top;
    
    const lantern = document.createElement('div');
    lantern.className = 'lantern';
    lantern.style.animationDelay = (index * 0.4) + 's';
    
    const tassel = document.createElement('div');
    tassel.className = 'lantern-tassel';
    tassel.style.animationDelay = (index * 0.4 + 0.2) + 's';
    
    lantern.appendChild(tassel);
    lanternWrap.appendChild(lantern);
    lanternsContainer.appendChild(lanternWrap);
});

// ========== CREATE GOLDEN PARTICLES ==========
const particlesContainer = document.getElementById('particlesContainer');
for (let i = 0; i < 120; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDuration = (10 + Math.random() * 12) + 's';
    particle.style.animationDelay = Math.random() * 10 + 's';
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

// Auto-start music
document.body.addEventListener('click', function startMusic() {
    if (!musicPlaying) {
        bgMusic.muted = false;
        bgMusic.play().then(() => {
            musicPlaying = true;
            musicControl.innerHTML = '🎵 Nhạc Tết (Bật)';
        }).catch(e => console.log('Autoplay blocked'));
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
    "Phát tài phát lộc"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Đào hồng nở thắm tươi xuân mới<br>Hạc bay lượn múa cõi trần gian",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa",
    "Cành đào khoe sắc xuân ân cả<br>Lộc biếc rực vàng nghĩa nặng tình",
    "Phúc đến nhà đầy vui sướng mãi<br>Lộc về trong phố ấm no luôn",
    "Đất trời đổi mới xuân tươi thắm<br>Nhà cửa sum vầy phúc lộc đầy"
];

// ========== CLICK COUNTER ==========
let clickCount = 0;
const counterValue = document.getElementById('counterValue');

function updateCounter() {
    clickCount++;
    counterValue.textContent = clickCount;
    counterValue.style.animation = 'none';
    setTimeout(() => {
        counterValue.style.animation = 'counterPulse 0.5s ease-out';
    }, 10);
}

// ========== CREATE EFFECTS ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 300) + 'px';
    ripple.style.top = (y - 300) + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 1500);
}

function createMoney(x, y) {
    const numBills = 20;
    
    for (let i = 0; i < numBills; i++) {
        const angle = (i / numBills) * Math.PI * 2;
        const distance = 150 + Math.random() * 250;
        
        const money = document.createElement('div');
        money.className = 'money';
        money.style.left = x + 'px';
        money.style.top = y + 'px';
        
        const mx = Math.cos(angle) * distance;
        const my = Math.sin(angle) * distance - 100;
        const mr = (Math.random() - 0.5) * 720;
        
        money.style.setProperty('--mx', mx + 'px');
        money.style.setProperty('--my', my + 'px');
        money.style.setProperty('--mr', mr + 'deg');
        
        document.body.appendChild(money);
        setTimeout(() => money.remove(), 2000);
    }
}

function createCreatures(x, y) {
    const creatures = ['🦁', '🐉'];
    const numCreatures = 16;
    
    for (let i = 0; i < numCreatures; i++) {
        const angle = (i / numCreatures) * Math.PI * 2;
        const emoji = creatures[i % creatures.length];
        
        const creature = document.createElement('div');
        creature.className = 'creature';
        creature.innerHTML = emoji;
        creature.style.left = x + 'px';
        creature.style.top = y + 'px';
        
        // Multi-stage jump trajectory
        const d1 = 180 + Math.random() * 80;
        const d2 = 320 + Math.random() * 120;
        const d3 = 480 + Math.random() * 150;
        const d4 = 650 + Math.random() * 200;
        
        creature.style.setProperty('--cx1', Math.cos(angle) * d1 + 'px');
        creature.style.setProperty('--cy1', Math.sin(angle) * d1 - 80 + 'px');
        creature.style.setProperty('--cx2', Math.cos(angle) * d2 + 'px');
        creature.style.setProperty('--cy2', Math.sin(angle) * d2 - 160 + 'px');
        creature.style.setProperty('--cx3', Math.cos(angle) * d3 + 'px');
        creature.style.setProperty('--cy3', Math.sin(angle) * d3 - 240 + 'px');
        creature.style.setProperty('--cx4', Math.cos(angle) * d4 + 'px');
        creature.style.setProperty('--cy4', Math.sin(angle) * d4 - 320 + 'px');
        
        document.body.appendChild(creature);
        setTimeout(() => creature.remove(), 2500);
    }
}

function createFireworks(x, y) {
    const numSparks = 40;
    const colors = ['gold', '#ff0000', '#ffd700', '#ff6b00', '#ffcc00', '#ff1744'];
    
    for (let i = 0; i < numSparks; i++) {
        const angle = (i / numSparks) * Math.PI * 2;
        const distance = 180 + Math.random() * 250;
        
        const firework = document.createElement('div');
        firework.className = 'firework';
        firework.style.left = x + 'px';
        firework.style.top = y + 'px';
        firework.style.background = colors[Math.floor(Math.random() * colors.length)];
        firework.style.boxShadow = `0 0 20px ${colors[Math.floor(Math.random() * colors.length)]}`;
        
        firework.style.setProperty('--fx', Math.cos(angle) * distance + 'px');
        firework.style.setProperty('--fy', Math.sin(angle) * distance + 'px');
        
        document.body.appendChild(firework);
        setTimeout(() => firework.remove(), 1500);
    }
}

function createConfetti(x, y) {
    const numConfetti = 50;
    const colors = ['#ff0000', '#ffd700', '#ff6b00', '#ffcc00', '#ff1744', '#ffa500'];
    const shapes = ['○', '■', '▲', '◆', '★'];
    
    for (let i = 0; i < numConfetti; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.innerHTML = shapes[Math.floor(Math.random() * shapes.length)];
        confetti.style.color = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.fontSize = (12 + Math.random() * 10) + 'px';
        confetti.style.left = x + 'px';
        confetti.style.top = y + 'px';
        
        const cfx = (Math.random() - 0.5) * 600;
        const cfy = Math.random() * 600 + 200;
        
        confetti.style.setProperty('--cfx', cfx + 'px');
        confetti.style.setProperty('--cfy', cfy + 'px');
        
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 3000);
    }
}

function createScrollBlessing() {
    const blessing = blessings[Math.floor(Math.random() * blessings.length)];
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    const x = Math.random() * (window.innerWidth - 450) + 225;
    const y = Math.random() * (window.innerHeight - 350) + 175;
    
    scroll.style.left = x + 'px';
    scroll.style.top = y + 'px';
    
    scroll.innerHTML = `
        <div class="scroll-rod left"></div>
        <div class="scroll-content">
            <div class="scroll-text">
                ${blessing}
                <div class="scroll-couplet">${couplet}</div>
            </div>
            <div class="seal">印</div>
        </div>
        <div class="scroll-rod right"></div>
    `;
    
    document.body.appendChild(scroll);
    setTimeout(() => scroll.remove(), 4500);
}

// ========== MAIN ENVELOPE CLICK ==========
const mainEnvelope = document.getElementById('mainEnvelope');

mainEnvelope.addEventListener('click', function(e) {
    // Update counter
    updateCounter();
    
    // Auto-start music
    if (!musicPlaying) {
        toggleMusic();
    }
    
    // Get center position
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Create all effects
    createRipple(centerX, centerY);
    createMoney(centerX, centerY);
    createCreatures(centerX, centerY);
    createFireworks(centerX, centerY);
    createConfetti(centerX, centerY);
    
    // Create scrolls
    const numScrolls = clickCount === 1 ? 10 : 6;
    let scrollCount = 0;
    
    const interval = setInterval(() => {
        createScrollBlessing();
        scrollCount++;
        
        if (scrollCount >= numScrolls) {
            clearInterval(interval);
        }
    }, 280);
});

// ========== PREVENT CONTEXT MENU ==========
document.addEventListener('contextmenu', e => e.preventDefault());

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)