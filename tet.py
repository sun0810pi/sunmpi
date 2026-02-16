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

# ===== ULTIMATE TẾT APP =====
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
    font-family: 'Georgia', 'Times New Roman', serif;
    background: linear-gradient(135deg, #ff6b00 0%, #ffa500 25%, #ffcc00 50%, #ff8c00 75%, #ff4500 100%);
    background-size: 400% 400%;
    animation: gradientShift 20s ease infinite;
    position: relative;
    min-height: 100vh;
    touch-action: none;
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
    0%, 100% { transform: translateX(-15px) rotate(-5deg); }
    50% { transform: translateX(15px) rotate(5deg); }
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
    20% { opacity: 1; }
    80% { opacity: 0.8; }
    100% {
        transform: translateY(-10vh) scale(1.5);
        opacity: 0;
    }
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
    max-width: 600px;
}

.title {
    font-size: clamp(36px, 8vw, 80px);
    font-weight: 900;
    background: linear-gradient(135deg, #ff0000, #ffd700, #ff0000, #ffd700);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 40px;
    animation: titleGlow 3s ease-in-out infinite, titleWave 5s ease-in-out infinite;
    filter: drop-shadow(0 0 30px rgba(255, 215, 0, 1));
    letter-spacing: 4px;
}

@keyframes titleGlow {
    0%, 100% { filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.8)); }
    50% { filter: drop-shadow(0 0 60px rgba(255, 215, 0, 1)); }
}

@keyframes titleWave {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.envelope-container {
    position: relative;
    display: inline-block;
    margin: 35px 0;
}

.envelope {
    width: min(40vw, 200px);
    height: min(53vw, 280px);
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

.envelope-fu {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: clamp(70px, 18vw, 100px);
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
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.08); }
}

.corner-deco {
    position: absolute;
    width: 30px;
    height: 30px;
    border: 2px solid gold;
    z-index: 1;
}

.corner-deco.top-left {
    top: 8px;
    left: 8px;
    border-width: 2px 0 0 2px;
}

.corner-deco.top-right {
    top: 8px;
    right: 8px;
    border-width: 2px 2px 0 0;
}

.corner-deco.bottom-left {
    bottom: 8px;
    left: 8px;
    border-width: 0 0 2px 2px;
}

.corner-deco.bottom-right {
    bottom: 8px;
    right: 8px;
    border-width: 0 2px 2px 0;
}

.subtext {
    margin-top: 30px;
    font-size: clamp(18px, 4.5vw, 24px);
    color: white;
    font-weight: 800;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.9), 2px 2px 5px rgba(0, 0, 0, 0.6);
}

/* ========== LEVEL SELECT SCREEN ========== */
.level-container {
    text-align: center;
    width: 90%;
    max-width: 500px;
}

.level-title {
    font-size: clamp(28px, 7vw, 48px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 25px rgba(255, 215, 0, 0.9),
        0 0 40px rgba(255, 215, 0, 0.7),
        3px 3px 5px rgba(0, 0, 0, 0.5);
    margin-bottom: 35px;
}

.level-buttons {
    display: flex;
    flex-direction: column;
    gap: 20px;
    max-width: 350px;
    margin: 0 auto;
}

.level-btn {
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 50%, #d32f2f 100%);
    border: 3px solid gold;
    border-radius: 15px;
    padding: 20px 30px;
    font-size: clamp(18px, 4.5vw, 24px);
    font-weight: 800;
    color: gold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 
        0 8px 25px rgba(0, 0, 0, 0.4),
        0 0 30px rgba(255, 215, 0, 0.5),
        inset 0 0 20px rgba(255, 215, 0, 0.2);
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.8), 2px 2px 4px rgba(0, 0, 0, 0.6);
}

.level-btn:hover {
    transform: scale(1.08);
    box-shadow: 
        0 10px 35px rgba(0, 0, 0, 0.5),
        0 0 50px rgba(255, 215, 0, 0.8),
        inset 0 0 30px rgba(255, 255, 255, 0.3);
}

.level-btn:active {
    transform: scale(0.95);
}

.level-desc {
    font-size: clamp(14px, 3.5vw, 16px);
    opacity: 0.9;
    margin-top: 8px;
}

/* ========== GAME SCREEN ========== */
.game-container {
    width: 95%;
    max-width: 600px;
    height: 95vh;
    max-height: 800px;
    display: flex;
    flex-direction: column;
    padding: 15px;
}

.game-header {
    text-align: center;
    margin-bottom: 20px;
    flex-shrink: 0;
}

.game-title {
    font-size: clamp(22px, 5.5vw, 32px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        0 0 35px rgba(255, 215, 0, 0.7),
        3px 3px 5px rgba(0, 0, 0, 0.5);
    margin-bottom: 12px;
}

.game-stats {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}

.stat-box {
    background: linear-gradient(135deg, rgba(211, 47, 47, 0.9), rgba(255, 0, 0, 0.9));
    border: 2px solid gold;
    border-radius: 20px;
    padding: 6px 16px;
    font-size: clamp(13px, 3.2vw, 15px);
    font-weight: 700;
    color: gold;
    box-shadow: 
        0 4px 15px rgba(0, 0, 0, 0.3),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.7), 1px 1px 3px rgba(0, 0, 0, 0.6);
}

.stat-number {
    font-size: clamp(16px, 4vw, 20px);
    margin: 0 4px;
}

/* ========== CARD GRID ========== */
.card-grid {
    display: grid;
    gap: 8px;
    flex: 1;
    align-content: center;
    max-width: 100%;
    margin: 0 auto;
}

.grid-easy {
    grid-template-columns: repeat(3, 1fr);
}

.grid-medium {
    grid-template-columns: repeat(4, 1fr);
}

.grid-hard {
    grid-template-columns: repeat(4, 1fr);
}

.card {
    aspect-ratio: 0.7;
    position: relative;
    cursor: pointer;
    transform-style: preserve-3d;
    transition: transform 0.3s ease;
}

.card.flipped {
    transform: rotateY(180deg);
}

.card.matched {
    opacity: 0.5;
    pointer-events: none;
}

.card-face {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.card-back {
    background: linear-gradient(135deg, #d32f2f 0%, #ff0000 50%, #d32f2f 100%);
    border: 2px solid gold;
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.4),
        inset 0 0 20px rgba(255, 215, 0, 0.3);
}

.card-back-icon {
    font-size: clamp(24px, 7vw, 40px);
}

.card-front {
    background: linear-gradient(135deg, #FFF8DC 0%, #FFFAF0 50%, #FFF8DC 100%);
    border: 2px solid gold;
    transform: rotateY(180deg);
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.4),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
}

.card-content {
    font-size: clamp(20px, 6vw, 36px);
    font-weight: 900;
    text-align: center;
    padding: 6px;
    line-height: 1.2;
}

.card-content.emoji {
    font-size: clamp(28px, 8vw, 48px);
}

/* ========== WIN SCREEN ========== */
.win-container {
    text-align: center;
    width: 90%;
    max-width: 500px;
}

.win-scroll {
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

.win-title {
    font-size: clamp(32px, 8vw, 48px);
    font-weight: 900;
    color: #FFD700;
    text-shadow: 
        0 0 30px rgba(255, 215, 0, 1),
        0 0 50px rgba(255, 215, 0, 0.8),
        4px 4px 6px rgba(0, 0, 0, 0.6);
    margin-bottom: 22px;
}

.win-blessing {
    color: #FFD700;
    font-size: clamp(20px, 5vw, 26px);
    font-weight: 800;
    line-height: 1.7;
    text-shadow: 
        0 0 18px rgba(255, 215, 0, 0.9),
        0 0 30px rgba(255, 215, 0, 0.7),
        3px 3px 5px rgba(0, 0, 0, 0.6);
    margin-bottom: 20px;
}

.win-couplet {
    color: #FFD700;
    font-size: clamp(16px, 4vw, 20px);
    font-style: italic;
    line-height: 1.9;
    padding-top: 20px;
    border-top: 2px solid rgba(255, 215, 0, 0.5);
    text-shadow: 
        0 0 15px rgba(255, 215, 0, 0.8),
        2px 2px 4px rgba(0, 0, 0, 0.6);
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
    text-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
}

.win-buttons {
    margin-top: 28px;
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
}

.win-btn {
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    border-radius: 30px;
    padding: 14px 28px;
    font-size: clamp(15px, 3.8vw, 19px);
    font-weight: 800;
    color: #8B0000;
    cursor: pointer;
    transition: transform 0.3s ease;
    box-shadow: 
        0 6px 20px rgba(255, 165, 0, 0.4),
        inset 0 0 15px rgba(255, 255, 255, 0.3);
}

.win-btn:hover {
    transform: scale(1.08);
}

.win-btn:active {
    transform: scale(0.95);
}

/* ========== EFFECTS ========== */
.lion {
    position: fixed;
    font-size: 32px;
    pointer-events: none;
    z-index: 100;
    animation: lionFly 1.5s ease-out forwards;
}

@keyframes lionFly {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translate(var(--tx), var(--ty)) scale(0.5) rotate(720deg);
        opacity: 0;
    }
}

.ripple {
    position: fixed;
    width: 500px;
    height: 500px;
    border: 3px solid rgba(255, 215, 0, 0.8);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99;
    animation: rippleAnim 1s ease-out forwards;
}

@keyframes rippleAnim {
    0% {
        transform: scale(0);
        opacity: 1;
    }
    100% {
        transform: scale(2);
        opacity: 0;
    }
}

.firework {
    position: fixed;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 98;
    box-shadow: 0 0 15px currentColor;
    animation: fireworkAnim 1s ease-out forwards;
}

@keyframes fireworkAnim {
    0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--fx), var(--fy)) scale(0);
        opacity: 0;
    }
}

.scroll {
    position: fixed;
    width: min(85vw, 380px);
    pointer-events: none;
    z-index: 999;
    animation: scrollShow 4s ease-out forwards;
}

@keyframes scrollShow {
    0% {
        transform: translateY(40px) scale(0.6) rotate(-8deg);
        opacity: 0;
    }
    12% {
        transform: translateY(0) scale(1) rotate(0deg);
        opacity: 1;
    }
    88% {
        opacity: 1;
    }
    100% {
        transform: translateY(-30px) scale(0.9) rotate(-2deg);
        opacity: 0;
    }
}

.scroll-content {
    background: linear-gradient(180deg, #8B0000, #B71C1C, #D32F2F, #B71C1C, #8B0000);
    border: 3px solid gold;
    border-radius: 15px;
    padding: 25px 20px;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.7),
        0 0 50px rgba(255, 215, 0, 0.8),
        inset 0 0 30px rgba(255, 215, 0, 0.2);
}

.scroll-text {
    color: gold;
    font-size: clamp(19px, 4.8vw, 24px);
    font-weight: 800;
    text-align: center;
    line-height: 1.7;
    text-shadow: 
        0 0 20px rgba(255, 215, 0, 0.9),
        0 0 35px rgba(255, 215, 0, 0.7),
        3px 3px 5px rgba(0, 0, 0, 0.7);
}

.scroll-couplet {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 2px solid rgba(255, 215, 0, 0.6);
    font-size: clamp(16px, 4.2vw, 20px);
    font-style: italic;
    line-height: 1.9;
}

/* ========== MUSIC CONTROL ========== */
.music-control {
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
        0 0 25px rgba(255, 215, 0, 0.4),
        inset 0 0 15px rgba(255, 215, 0, 0.2);
    text-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
}

.music-control:hover {
    transform: scale(1.08);
}

.music-control:active {
    transform: scale(0.95);
}

/* ========== MOBILE OPTIMIZATIONS ========== */
@media (max-width: 768px) {
    .envelope {
        width: 150px;
        height: 210px;
    }
    
    .card-grid {
        gap: 6px;
    }
    
    .game-container {
        padding: 10px;
    }
    
    .game-header {
        margin-bottom: 15px;
    }
}

@media (max-width: 480px) {
    .card-grid {
        gap: 5px;
    }
    
    .grid-hard {
        grid-template-columns: repeat(4, 1fr);
    }
}

@media (max-height: 700px) {
    .game-container {
        height: 98vh;
    }
    
    .game-header {
        margin-bottom: 10px;
    }
    
    .card-grid {
        gap: 4px;
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

<!-- SCREEN 1: INTRO -->
<div class="screen active" id="introScreen">
    <div class="intro-container">
        <div class="title">Chúc Mừng Năm Mới</div>
        <div class="envelope-container">
            <div class="envelope" id="mainEnvelope">
                <div class="envelope-body">
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
</div>

<!-- SCREEN 2: LEVEL SELECT -->
<div class="screen" id="levelScreen">
    <div class="level-container">
        <div class="level-title">🎴 Chọn Độ Khó 🎴</div>
        <div class="level-buttons">
            <button class="level-btn" onclick="startGame('easy')">
                🌸 Dễ Thương
                <div class="level-desc">3x4 • Chill</div>
            </button>
            <button class="level-btn" onclick="startGame('medium')">
                🎊 Vui Vẻ
                <div class="level-desc">4x4 • Bình thường</div>
            </button>
            <button class="level-btn" onclick="startGame('hard')">
                🔥 Thử Thách
                <div class="level-desc">4x6 • Khó</div>
            </button>
        </div>
    </div>
</div>

<!-- SCREEN 3: GAME -->
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
                    ✨ <span class="stat-number" id="matched">0</span>/<span id="total">0</span>
                </div>
            </div>
        </div>
        <div class="card-grid" id="cardGrid"></div>
    </div>
</div>

<!-- SCREEN 4: WIN -->
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
            <div class="win-buttons">
                <button class="win-btn" onclick="showScreen('levelScreen')">
                    🔄 Chơi Lại
                </button>
                <button class="win-btn" onclick="showScreen('introScreen')">
                    🏠 Về Trang Chủ
                </button>
            </div>
        </div>
    </div>
</div>

<!-- Music Control -->
<div class="music-control" id="musicControl" onclick="toggleMusic()">
    🎵 Nhạc Tết
</div>

<!-- Background Music -->
<audio id="bgMusic" loop>
    <source src="data:audio/mp3;base64,""" + music_base64 + """" type="audio/mp3">
</audio>

<script>

console.log("🧧 TẾT ULTIMATE - FULL FEATURED");

// ========== DEVICE DETECTION ==========
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent) || window.innerWidth < 768;

// ========== CREATE PEACH BLOSSOMS ==========
const blossomsContainer = document.getElementById('blossomsContainer');
const blossomEmojis = ['🌸', '🌺', '🏵️', '💮'];
const blossomCount = isMobile ? 25 : 40;

for (let i = 0; i < blossomCount; i++) {
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
const particleCount = isMobile ? 50 : 100;

for (let i = 0; i < particleCount; i++) {
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
const generalBlessings = [
    "Chúc mừng năm mới",
    "An khang thịnh vượng",
    "Vạn sự như ý",
    "Xuân về ngàn lộc",
    "Trăm năm hạnh phúc",
    "Vạn sự cát tường"
];

const couplets = [
    "Xuân sang cội phúc sinh nhành lộc<br>Tết về cây đức trổ thêm hoa",
    "Mai vàng nở rộ nghênh xuân đến<br>Phúc thọ đầy nhà đón Tết sang",
    "Lân múa rộn ràng xuân mới đến<br>Phúc lộc đầy nhà tấn tài vinh",
    "Thiên thời hòa thuận xuân về sớm<br>Địa lợi phì nhiêu lộc đến đầy",
    "Xuân đến trong nhà hương sắc mới<br>Tết về khắp phố ánh đèn hoa",
    "Cát tường như ý xuân hanh thông<br>Phát tài phát lộc Tết đầm ấm"
];

// ========== CARD PAIRS WITH LOGICAL BLESSINGS ==========
const cardSets = {
    easy: [
        { id: 1, content: '福', type: 'text', blessing: 'Phúc lộc đầy nhà' },
        { id: 2, content: '禄', type: 'text', blessing: 'Tấn tài tấn lộc' },
        { id: 3, content: '🌸', type: 'emoji', blessing: 'Mai vàng nở rộ' },
        { id: 4, content: '🧧', type: 'emoji', blessing: 'Tiền vô như nước' },
        { id: 5, content: '🎊', type: 'emoji', blessing: 'Xuân về ngàn lộc' },
        { id: 6, content: '🍊', type: 'emoji', blessing: 'Quả ngọt đời vàng' }
    ],
    medium: [
        { id: 1, content: '福', type: 'text', blessing: 'Phúc lộc đầy nhà' },
        { id: 2, content: '禄', type: 'text', blessing: 'Tấn tài tấn lộc' },
        { id: 3, content: '寿', type: 'text', blessing: 'Sức khỏe dồi dào' },
        { id: 4, content: '🌸', type: 'emoji', blessing: 'Mai vàng nở rộ' },
        { id: 5, content: '🧧', type: 'emoji', blessing: 'Tiền vô như nước' },
        { id: 6, content: '🎊', type: 'emoji', blessing: 'Xuân về ngàn lộc' },
        { id: 7, content: '🍊', type: 'emoji', blessing: 'Quả ngọt đời vàng' },
        { id: 8, content: '🪭', type: 'emoji', blessing: 'Mát lành an khang' }
    ],
    hard: [
        { id: 1, content: '福', type: 'text', blessing: 'Phúc lộc đầy nhà' },
        { id: 2, content: '禄', type: 'text', blessing: 'Tấn tài tấn lộc' },
        { id: 3, content: '寿', type: 'text', blessing: 'Sức khỏe dồi dào' },
        { id: 4, content: '喜', type: 'text', blessing: 'Vui vẻ hạnh phúc' },
        { id: 5, content: '🌸', type: 'emoji', blessing: 'Mai vàng nở rộ' },
        { id: 6, content: '🧧', type: 'emoji', blessing: 'Tiền vô như nước' },
        { id: 7, content: '🎊', type: 'emoji', blessing: 'Xuân về ngàn lộc' },
        { id: 8, content: '🍊', type: 'emoji', blessing: 'Quả ngọt đời vàng' },
        { id: 9, content: '🪭', type: 'emoji', blessing: 'Mát lành an khang' },
        { id: 10, content: '🏮', type: 'emoji', blessing: 'Đèn hồng chiếu sáng' },
        { id: 11, content: '🎆', type: 'emoji', blessing: 'Pháo nổ đón xuân' },
        { id: 12, content: '🐴', type: 'emoji', blessing: 'Mã đáo thành công' }
    ]
};

// ========== EFFECTS ==========
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = (x - 250) + 'px';
    ripple.style.top = (y - 250) + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 1000);
}

function createLionDance(x, y) {
    const numLions = isMobile ? 8 : 12;
    for (let i = 0; i < numLions; i++) {
        const angle = (i / numLions) * Math.PI * 2;
        const distance = 200 + Math.random() * 150;
        
        const lion = document.createElement('div');
        lion.className = 'lion';
        lion.innerHTML = '🦁';
        lion.style.left = x + 'px';
        lion.style.top = y + 'px';
        
        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance - 150;
        
        lion.style.setProperty('--tx', tx + 'px');
        lion.style.setProperty('--ty', ty + 'px');
        
        document.body.appendChild(lion);
        setTimeout(() => lion.remove(), 1500);
    }
}

function createFireworks(x, y) {
    const numSparks = isMobile ? 20 : 30;
    for (let i = 0; i < numSparks; i++) {
        const angle = (i / numSparks) * Math.PI * 2;
        const distance = 100 + Math.random() * 150;
        
        const firework = document.createElement('div');
        firework.className = 'firework';
        firework.style.left = x + 'px';
        firework.style.top = y + 'px';
        
        const fx = Math.cos(angle) * distance;
        const fy = Math.sin(angle) * distance;
        
        firework.style.setProperty('--fx', fx + 'px');
        firework.style.setProperty('--fy', fy + 'px');
        
        const colors = ['gold', '#ff0000', '#ffd700', '#ff6b00', '#ffcc00'];
        firework.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        document.body.appendChild(firework);
        setTimeout(() => firework.remove(), 1000);
    }
}

function createScrollBlessing(blessing) {
    const couplet = couplets[Math.floor(Math.random() * couplets.length)];
    
    const scroll = document.createElement('div');
    scroll.className = 'scroll';
    
    const margin = isMobile ? 40 : 80;
    const scrollWidth = isMobile ? Math.min(window.innerWidth * 0.85, 300) : 380;
    const scrollHeight = 180;
    
    const maxX = window.innerWidth - scrollWidth - margin;
    const maxY = window.innerHeight - scrollHeight - margin;
    
    const x = Math.max(margin, Math.min(maxX, Math.random() * (window.innerWidth - scrollWidth)));
    const y = Math.max(margin, Math.min(maxY, Math.random() * (window.innerHeight - scrollHeight)));
    
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

// ========== SCREEN MANAGEMENT ==========
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

// ========== INTRO SCREEN ==========
const mainEnvelope = document.getElementById('mainEnvelope');

mainEnvelope.addEventListener('click', function() {
    if (navigator.vibrate) navigator.vibrate(50);
    
    if (!musicPlaying) toggleMusic();
    
    const rect = this.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    createRipple(centerX, centerY);
    createLionDance(centerX, centerY);
    createFireworks(centerX, centerY);
    
    const numScrolls = 6;
    let scrollCount = 0;
    const interval = setInterval(() => {
        const blessing = generalBlessings[Math.floor(Math.random() * generalBlessings.length)];
        createScrollBlessing(blessing);
        scrollCount++;
        if (scrollCount >= numScrolls) clearInterval(interval);
    }, 250);
    
    setTimeout(() => {
        showScreen('levelScreen');
    }, 1500);
});

// ========== GAME STATE ==========
let gameState = {
    level: '',
    cards: [],
    flipped: [],
    matched: [],
    moves: 0,
    timer: 0,
    timerInterval: null
};

// ========== GAME LOGIC ==========
function startGame(level) {
    gameState = {
        level: level,
        cards: [],
        flipped: [],
        matched: [],
        moves: 0,
        timer: 0,
        timerInterval: null
    };
    
    const cardSet = cardSets[level];
    const deck = [...cardSet, ...cardSet]
        .map(card => ({ ...card, uniqueId: Math.random() }))
        .sort(() => Math.random() - 0.5);
    
    gameState.cards = deck;
    
    const grid = document.getElementById('cardGrid');
    grid.innerHTML = '';
    grid.className = 'card-grid grid-' + level;
    
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
    
    document.getElementById('total').textContent = cardSet.length;
    updateUI();
    
    gameState.timerInterval = setInterval(() => {
        gameState.timer++;
        document.getElementById('timer').textContent = gameState.timer;
    }, 1000);
    
    showScreen('gameScreen');
}

function handleCardClick(index) {
    const card = gameState.cards[index];
    const cardEl = document.querySelectorAll('.card')[index];
    
    if (gameState.flipped.length >= 2) return;
    if (gameState.flipped.includes(index)) return;
    if (gameState.matched.includes(card.id)) return;
    
    if (navigator.vibrate) navigator.vibrate(20);
    
    cardEl.classList.add('flipped');
    gameState.flipped.push(index);
    
    if (gameState.flipped.length === 2) {
        gameState.moves++;
        updateUI();
        
        const [idx1, idx2] = gameState.flipped;
        const card1 = gameState.cards[idx1];
        const card2 = gameState.cards[idx2];
        
        if (card1.id === card2.id) {
            setTimeout(() => {
                handleMatch(idx1, idx2, card1);
            }, 400);
        } else {
            setTimeout(() => {
                const cards = document.querySelectorAll('.card');
                cards[idx1].classList.remove('flipped');
                cards[idx2].classList.remove('flipped');
                gameState.flipped = [];
            }, 800);
        }
    }
}

function handleMatch(idx1, idx2, card) {
    gameState.matched.push(card.id);
    gameState.flipped = [];
    
    const cards = document.querySelectorAll('.card');
    cards[idx1].classList.add('matched');
    cards[idx2].classList.add('matched');
    
    const rect1 = cards[idx1].getBoundingClientRect();
    const cx = rect1.left + rect1.width / 2;
    const cy = rect1.top + rect1.height / 2;
    
    createLionDance(cx, cy);
    createFireworks(cx, cy);
    
    if (navigator.vibrate) navigator.vibrate([30, 10, 30]);
    
    // LOGICAL BLESSING based on matched card
    createScrollBlessing(card.blessing);
    
    updateUI();
    
    const totalPairs = cardSets[gameState.level].length;
    if (gameState.matched.length === totalPairs) {
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
    
    document.getElementById('finalTime').textContent = gameState.timer;
    document.getElementById('finalMoves').textContent = gameState.moves;
    document.getElementById('winBlessing').textContent = 
        generalBlessings[Math.floor(Math.random() * generalBlessings.length)];
    document.getElementById('winCouplet').innerHTML = 
        couplets[Math.floor(Math.random() * couplets.length)];
    
    showScreen('winScreen');
    
    for (let i = 0; i < 8; i++) {
        setTimeout(() => {
            const x = Math.random() * window.innerWidth;
            const y = Math.random() * window.innerHeight;
            createLionDance(x, y);
            createFireworks(x, y);
        }, i * 300);
    }
}

console.log("✅ GAME READY - FULL FEATURES");

</script>

</body>
</html>
"""

# ===== RENDER =====
components.html(html, height=900, scrolling=False)