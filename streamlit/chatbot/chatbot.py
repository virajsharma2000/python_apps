import streamlit as st
import requests
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from datetime import datetime
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main background - Background image with overlay */
    [data-testid="stAppViewContainer"] {
        background-image: url('file:///home/yash/24990776-03eb-46e3-8e9f-a13adf07eac1.png');
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        background-blend-mode: overlay;
    }
    
    /* Dark overlay for better text readability */
    [data-testid="stAppViewContainer"]::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.85);
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Chat message styling with animations */
    .stChatMessage {
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        animation: slideInMessage 0.5s ease-out;
    }
    
    @keyframes slideInMessage {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* User message - Pink/Magenta with glow */
    .stChatMessage [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #ff6b9d 0%, #ff1493 100%);
        color: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stChatMessage [data-testid="stChatMessageContent"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(255, 107, 157, 0.6);
    }
    
    /* Assistant message - Light with colorful border and animation */
    .stChatMessage:has([data-testid="stChatMessageContent"]) {
        background: linear-gradient(135deg, #f0f9ff 0%, #fff5f7 100%);
        border-radius: 12px;
        border-left: 5px solid #00d4ff;
        box-shadow: 0 2px 12px rgba(0, 212, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stChatMessage:has([data-testid="stChatMessageContent"]):hover {
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.4);
        transform: translateX(8px);
    }
    
    /* Title styling - Rainbow animated gradient */
    h1 {
        background: linear-gradient(90deg, #ff6b6b, #ffa94d, #51cf66, #37b7c3, #748ffc, #ff7fa0);
        background-size: 200% auto;
        animation: gradientText 3s linear infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    @keyframes gradientText {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    /* Subtitle with fade animation */
    .subtitle {
        text-align: center;
        background: linear-gradient(90deg, #ff6b9d, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1rem;
        margin-bottom: 2rem;
        opacity: 0.95;
        font-weight: 600;
        animation: fadeInDown 0.8s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Chat input styling with glow effect */
    .stChatInputContainer {
        padding: 1rem;
        background: linear-gradient(135deg, #fff9e6 0%, #fff0f5 100%);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(255, 107, 157, 0.15);
        border: 2px solid #ffb3d9;
        transition: all 0.3s ease;
        animation: slideInUp 0.6s ease-out;
    }
    
    .stChatInputContainer:hover {
        box-shadow: 0 8px 30px rgba(255, 107, 157, 0.3);
        border-color: #ff6b9d;
    }
    
    .stChatInputContainer:focus-within {
        box-shadow: 0 12px 40px rgba(255, 107, 157, 0.4);
        border-color: #ff1493;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar styling - Vibrant gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff5e6 0%, #ffe8f0 50%, #f0f8ff 100%);
    }
    
    .sidebar-header {
        background: linear-gradient(90deg, #ff6b6b, #ffa94d, #51cf66);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        animation: fadeInRight 0.8s ease-out;
    }
    
    @keyframes fadeInRight {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Info cards - Colorful with hover effects */
    .info-card {
        background: linear-gradient(135deg, #fff9e6 0%, #ffe8f0 50%, #e8f4ff 100%);
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        box-shadow: 0 2px 12px rgba(255, 107, 157, 0.2);
        border-left: 4px solid #ff6b9d;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .info-card:hover {
        transform: translateX(8px);
        box-shadow: 0 6px 20px rgba(255, 107, 157, 0.4);
        border-left-color: #00d4ff;
    }
    
    /* Button styling - Vibrant with ripple effect */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b9d 0%, #ffa94d 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.5);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 157, 0.5);
        background: linear-gradient(135deg, #ff7fb3 0%, #ffb84d 100%);
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Input field styling with glow */
    input {
        border-radius: 8px !important;
        border: 2px solid #ffb3d9 !important;
        background-color: white !important;
        transition: all 0.3s ease !important;
        padding: 0.75rem !important;
        font-weight: 500 !important;
    }
    
    input:focus {
        border-color: #ff6b9d !important;
        box-shadow: 0 0 12px rgba(255, 107, 157, 0.4), inset 0 0 4px rgba(255, 107, 157, 0.1) !important;
    }
    
    /* Metric styling - Ecommerce card style */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #fff0f5 0%, #fff5e6 50%, #f0f8ff 100%);
        border-radius: 12px;
        border-left: 4px solid #ff6b9d;
        padding: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 12px rgba(255, 107, 157, 0.1);
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 24px rgba(255, 107, 157, 0.2);
        border-left-color: #00d4ff;
    }
    
    /* Divider styling - Rainbow gradient */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, #ff6b6b, #ffa94d, #51cf66, #37b7c3, #748ffc);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }
    
    /* Expander styling - Enhanced */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #fff0f5 0%, #f0f8ff 100%);
        border-radius: 8px;
        border-left: 4px solid #ff6b9d;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #ffe8f0 0%, #e8f4ff 100%);
        border-left-color: #00d4ff;
        box-shadow: 0 4px 12px rgba(255, 107, 157, 0.2);
    }
    
    /* Spinner animation enhancement */
    .stSpinner {
        animation: spinnerPulse 0.8s ease-in-out infinite;
    }
    
    @keyframes spinnerPulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    /* Loading text effect */
    .stStatus {
        background: linear-gradient(90deg, #ff6b9d, #ffa94d, #51cf66, #37b7c3, #ff6b9d);
        background-size: 200% auto;
        animation: gradientShift 3s linear infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Column animations */
    .element-container {
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* Recent activities with icon animation */
    .info {
        padding: 1rem;
        background: linear-gradient(135deg, #fff9e6 0%, #ffe8f0 100%);
        border-radius: 8px;
        border-left: 4px solid #ff6b9d;
        transition: all 0.3s ease;
        animation: slideInLeft 0.5s ease-out;
    }
    
    .info:hover {
        transform: translateX(8px);
        box-shadow: 0 4px 12px rgba(255, 107, 157, 0.2);
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Product recommendation card style (if displayed) */
    .product-card {
        background: linear-gradient(135deg, #fff 0%, #f0fdf4 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #10b981;
        box-shadow: 0 2px 12px rgba(16, 185, 129, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }
    
    .product-card:hover {
        transform: translateY(-8px) rotate(1deg);
        box-shadow: 0 12px 24px rgba(16, 185, 129, 0.2);
        border-left-color: #06b6d4;
    }
    
    /* Text styling enhancements */
    h2, h3, h4, h5, h6 {
        background: linear-gradient(90deg, #1e3a8a, #ff6b9d, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Section header with bottom border animation */
    .session-header {
        border-bottom: 3px solid #ff6b9d;
        padding-bottom: 1rem;
        margin-bottom: 1rem;
        animation: slideInDown 0.6s ease-out;
    }
    
    @keyframes slideInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Delete button - Red gradient */
    [data-testid="delete_btn"] {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
    }
    
    [data-testid="delete_btn"]:hover {
        box-shadow: 0 8px 20px rgba(239, 68, 68, 0.4) !important;
    }
    
    /* Payment Section Styles */
    .payment-section {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe8d6 50%, #f0f9ff 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 6px solid #ff006e;
        margin-top: 1.5rem;
        box-shadow: 0 8px 24px rgba(255, 0, 110, 0.2);
        animation: paymentEntry 0.6s ease-out;
    }
    
    @keyframes paymentEntry {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .payment-header {
        color: #ff006e;
        font-weight: bold;
        font-size: 1.3rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Razorpay Button Container */
    .razorpay-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 3px solid #fb5607;
        box-shadow: 0 4px 16px rgba(251, 86, 7, 0.15);
        transition: all 0.3s ease;
        animation: razorpayPulse 2s ease-in-out infinite;
    }
    
    @keyframes razorpayPulse {
        0%, 100% {
            box-shadow: 0 4px 16px rgba(251, 86, 7, 0.15);
        }
        50% {
            box-shadow: 0 8px 24px rgba(251, 86, 7, 0.3);
        }
    }
    
    .razorpay-container:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(251, 86, 7, 0.3);
    }
    
    /* Product Suggestion Container */
    .products-available {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 2px solid #ffbe0b;
    }
    
    .product-list-item {
        background: linear-gradient(135deg, #fff9e6 0%, #ffe8d6 100%);
        padding: 0.75rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-left: 4px solid #fb5607;
        transition: all 0.3s ease;
    }
    
    .product-list-item:hover {
        background: linear-gradient(135deg, #ffe8d6 0%, #fff9e6 100%);
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(251, 86, 7, 0.2);
    }
    
    .product-detail {
        flex: 1;
    }
    
    .product-name-text {
        font-weight: bold;
        color: #1e3a8a;
        margin: 0;
    }
    
    .product-price-text {
        color: #ff006e;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Order Summary */
    .order-summary {
        background: linear-gradient(135deg, #fff0f5 0%, #f0f9ff 100%);
        padding: 1rem;
        border-radius: 12px;
        border: 2px solid #ff006e;
        margin-top: 1rem;
        text-align: center;
    }
    
    .summary-title {
        color: #ff006e;
        font-weight: bold;
        font-size: 1.2rem;
        margin: 0.5rem 0;
    }
    
    .total-amount {
        font-size: 1.8rem;
        font-weight: bold;
        background: linear-gradient(90deg, #ff006e 0%, #fb5607 50%, #ffbe0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.75rem 0;
    }
    
    /* Success/Info Messages */
    .success-message {
        background: linear-gradient(135deg, #06ffa5 0%, #38ada9 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        animation: successSlideIn 0.5s ease-out;
    }
    
    @keyframes successSlideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .info-message {
        background: linear-gradient(135deg, #3a86ff 0%, #748ffc 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        margin-top: 0.75rem;
    }
    
    /* Checkout Button Style */
    .checkout-btn {
        background: linear-gradient(135deg, #ff006e 0%, #fb5607 50%, #ffbe0b 100%);
        background-size: 200% 200%;
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 12px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 24px rgba(255, 0, 110, 0.3);
        animation: checkoutPulse 2s ease-in-out infinite;
    }
    
    @keyframes checkoutPulse {
        0%, 100% {
            box-shadow: 0 8px 24px rgba(255, 0, 110, 0.3);
        }
        50% {
            box-shadow: 0 12px 36px rgba(255, 0, 110, 0.5);
        }
    }
    
    .checkout-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 36px rgba(255, 0, 110, 0.5);
        background-position: 100% 100%;
    }
    
    .checkout-btn:active {
        transform: translateY(0);
    }
    
    /* ============ ADVANCED ANIMATIONS ============ */
    
    /* Floating animation for sidebar headers */
    .sidebar-header {
        animation: fadeInRight 0.8s ease-out, float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-5px);
        }
    }
    
    /* Pulse animation for metrics on hover */
    [data-testid="metric-container"] {
        animation: metricPulse 0.3s ease-out;
    }
    
    @keyframes metricPulse {
        0% {
            transform: scale(0.95);
        }
        50% {
            transform: scale(1.02);
        }
        100% {
            transform: scale(1);
        }
    }
    
    /* Glow effect animation */
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 0 5px rgba(255, 107, 157, 0.5);
        }
        50% {
            box-shadow: 0 0 20px rgba(255, 107, 157, 0.8);
        }
    }
    
    .stButton > button:hover {
        animation: glow 1.5s ease-in-out;
    }
    
    /* Rainbow border animation */
    @keyframes rainbowBorder {
        0% {
            border-left-color: #ff6b6b;
        }
        25% {
            border-left-color: #ffa94d;
        }
        50% {
            border-left-color: #51cf66;
        }
        75% {
            border-left-color: #37b7c3;
        }
        100% {
            border-left-color: #ff6b6b;
        }
    }
    
    .info-card:hover {
        animation: rainbowBorder 2s ease infinite;
    }
    
    /* Bounce animation for messages */
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    .stChatMessage:hover {
        animation: bounce 0.6s ease-in-out;
    }
    
    /* Wiggle animation for buttons */
    @keyframes wiggle {
        0%, 100% {
            transform: rotate(0deg);
        }
        25% {
            transform: rotate(-1deg);
        }
        75% {
            transform: rotate(1deg);
        }
    }
    
    .stButton > button:active {
        animation: wiggle 0.3s ease-in-out;
    }
    
    /* Neon glow effect */
    @keyframes neonGlow {
        0%, 100% {
            text-shadow: 0 0 10px #ff6b9d, 0 0 20px #ff1493;
        }
        50% {
            text-shadow: 0 0 20px #ff6b9d, 0 0 30px #ff1493, 0 0 40px #ff6b9d;
        }
    }
    
    h1:hover {
        animation: neonGlow 1.5s ease-in-out infinite;
    }
    
    /* Rotate on hover animation */
    @keyframes rotateIn {
        from {
            transform: rotateY(90deg);
            opacity: 0;
        }
        to {
            transform: rotateY(0);
            opacity: 1;
        }
    }
    
    .stChatMessage:first-child {
        animation: rotateIn 0.6s ease-out;
    }
    
    /* Typewriter effect (simulated) */
    @keyframes typing {
        from {
            width: 0;
        }
        to {
            width: 100%;
        }
    }
    
    .stChatMessage [data-testid="stChatMessageContent"] {
        animation: typing 0.8s ease-out;
    }
    
    /* Blink animation */
    @keyframes blink {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
    
    .stSpinner {
        animation: spinnerPulse 0.8s ease-in-out infinite;
    }
    
    /* Shake animation for errors */
    @keyframes shake {
        0%, 100% {
            transform: translateX(0);
        }
        10%, 30%, 50%, 70%, 90% {
            transform: translateX(-5px);
        }
        20%, 40%, 60%, 80% {
            transform: translateX(5px);
        }
    }
    
    .stAlert {
        animation: shake 0.5s ease-in-out;
    }
    
    /* Flip animation */
    @keyframes flip {
        0% {
            transform: rotateY(0deg);
        }
        50% {
            transform: rotateY(90deg);
        }
        100% {
            transform: rotateY(0deg);
        }
    }
    
    [data-testid="metric-container"]:hover {
        animation: flip 0.8s ease-in-out;
    }
    
    /* Heartbeat animation */
    @keyframes heartbeat {
        0%, 100% {
            transform: scale(1);
        }
        25% {
            transform: scale(1.1);
        }
        50% {
            transform: scale(1);
        }
    }
    
    .sidebar-header:hover {
        animation: heartbeat 0.6s ease-in-out;
    }
    
    /* Gradient animation for text */
    @keyframes gradientAnimate {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    
    h2, h3, h4, h5, h6 {
        background-size: 200% auto;
        animation: gradientAnimate 3s ease infinite;
    }
    
    /* Sliding background animation */
    @keyframes slideBackground {
        0% {
            background-position: 0% center;
        }
        100% {
            background-position: 200% center;
        }
    }
    
    [data-testid="stAppViewContainer"] {
        animation: gradientShift 15s ease infinite;
    }
    
    /* Expand animation */
    @keyframes expandWidth {
        from {
            width: 0;
            opacity: 0;
        }
        to {
            width: 100%;
            opacity: 1;
        }
    }
    
    .stChatInputContainer {
        animation: expandWidth 0.6s ease-out;
    }
    
    /* Bubble animation */
    @keyframes bubble {
        0% {
            transform: translateY(0) scale(0.9);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-20px) scale(1);
            opacity: 0;
        }
    }
    
    .info-card::before {
        content: '✨';
        animation: bubble 2s ease-in infinite;
        position: absolute;
        right: 10px;
    }
    
    /* Pulse background animation */
    @keyframes pulseBg {
        0%, 100% {
            background: linear-gradient(135deg, #fff9e6 0%, #fff0f5 100%);
        }
        50% {
            background: linear-gradient(135deg, #ffe8f0 0%, #fff9e6 100%);
        }
    }
    
    .stChatInputContainer {
        animation: slideInUp 0.6s ease-out, pulseBg 3s ease-in-out infinite;
    }
    
    /* Color shift animation */
    @keyframes colorShift {
        0%, 100% {
            border-left-color: #ff6b9d;
        }
        50% {
            border-left-color: #00d4ff;
        }
    }
    
    .item-row {
        animation: colorShift 2s ease infinite;
    }
    
    /* Scale pulse animation */
    @keyframes scalePulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    .stButton > button:focus {
        animation: scalePulse 0.8s ease-in-out;
    }
    
    /* Skew animation */
    @keyframes skew {
        0%, 100% {
            transform: skewX(0deg);
        }
        50% {
            transform: skewX(-2deg);
        }
    }
    
    .stChatMessage:hover {
        animation: bounce 0.6s ease-in-out;
    }
    
    /* Fade and scale animation */
    @keyframes fadeScale {
        from {
            opacity: 0;
            transform: scale(0.8);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    [data-testid="metric-container"] {
        animation: fadeScale 0.5s ease-out;
    }
    
    /* Infinite rotation */
    @keyframes rotate360 {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
    
    .sidebar-header::before {
        content: '';
        animation: rotate360 4s linear infinite;
    }
    
    /* Gradient text animation */
    @keyframes gradientFlow {
        0% {
            background-position: 0% center;
        }
        100% {
            background-position: 200% center;
        }
    }
    
    .subtitle {
        background-size: 200% auto;
        animation: fadeInDown 0.8s ease-out, gradientFlow 3s linear infinite;
    }
    
    /* Hover lift effect */
    @keyframes liftUp {
        from {
            transform: translateY(0);
        }
        to {
            transform: translateY(-8px);
        }
    }
    
    .info-card:hover {
        animation: liftUp 0.3s ease-out forwards;
    }
    
    /* Blur animation */
    @keyframes blurIn {
        from {
            filter: blur(10px);
            opacity: 0;
        }
        to {
            filter: blur(0);
            opacity: 1;
        }
    }
    
    .element-container {
        animation: blurIn 0.6s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

# CONFIG
MONGO_URI = "mongodb+srv://virajsharma_db_user:pumpulili@cluster0.xclz1ks.mongodb.net/cluster0.xclz1ks.mongodb.net/?appName=Cluster0"
SARVAM_API_KEY = "sk_rvrevl1p_XNtVvBkl8RqDqjcDrfdunpBu"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db = client["cluster0"]
    users_collection = db["user"]
    activity_collection = db["activity_logs"]
    products_collection = db["products"]
    chat_sessions_collection = db["chat_sessions"]
    mongo_connected = True
except Exception as e:
    st.error(f"MongoDB Connection Failed: {e}")
    mongo_connected = False

# Initialize session state
if "current_session_id" not in st.session_state:
    st.session_state.current_session_id = None
if "current_session_name" not in st.session_state:
    st.session_state.current_session_name = "New Chat"

# HEADER
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1>🛍️ AI Shopping Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Get personalized product recommendations powered by AI</div>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# SIDEBAR - Display stats and info
with st.sidebar:
    st.markdown("<div class='sidebar-header'>� Chat Sessions</div>", unsafe_allow_html=True)
    
    # New chat button
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.current_session_id = None
        st.session_state.current_session_name = "New Chat"
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Display all chat sessions
    if mongo_connected:
        all_sessions = list(chat_sessions_collection.find().sort("created_at", -1).limit(10))
        
        if all_sessions:
            st.markdown("<div class='sidebar-header'>📋 Previous Chats</div>", unsafe_allow_html=True)
            for session in all_sessions:
                session_id = str(session["_id"])
                session_name = session.get("name", "Untitled Chat")
                message_count = len(session.get("messages", []))
                
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    if st.button(f"📝 {session_name}\n({message_count} messages)", use_container_width=True, key=f"session_{session_id}"):
                        st.session_state.current_session_id = session_id
                        st.session_state.current_session_name = session_name
                        st.session_state.messages = session.get("messages", [])
                        st.rerun()
        
        st.divider()
        st.markdown("<div class='sidebar-header'>📊 Dashboard</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            user_count = users_collection.count_documents({})
            st.metric("👥 Users", user_count)
        
        with col2:
            product_count = products_collection.count_documents({})
            st.metric("📦 Products", product_count)
        
        activity_count = activity_collection.count_documents({})
        st.metric("📝 Activities Logged", activity_count)
        
        st.divider()
        
        # Recent activities
        st.markdown("<div class='sidebar-header'>📈 Recent Activities</div>", unsafe_allow_html=True)
        recent_activities = list(activity_collection.find().sort("_id", -1).limit(5))
        
        if recent_activities:
            for activity in recent_activities:
                action = activity.get('action', 'unknown')
                timestamp = activity.get('timestamp', datetime.now())
                st.info(f"**{action}** - {timestamp.strftime('%H:%M:%S')}", icon="📌")
        else:
            st.info("No activities yet", icon="ℹ️")
        
        st.divider()
        
        # Popular products
        st.markdown("<div class='sidebar-header'>⭐ Top Products</div>", unsafe_allow_html=True)
        products = list(products_collection.find().limit(3))
        
        if products:
            for product in products:
                st.write(f"**{product.get('emoji', '💄')} {product['name']}**")
                st.caption(f"${product['price']}")
    else:
        st.error("Database connection unavailable")

# MAIN CHAT AREA
st.divider()

# Display current session info
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.markdown(f"### 💬 {st.session_state.current_session_name}")
with col2:
    if st.session_state.current_session_id:
        if st.button("🗑️ Delete", key="delete_btn"):
            chat_sessions_collection.delete_one({"_id": ObjectId(st.session_state.current_session_id)})
            st.session_state.current_session_id = None
            st.session_state.messages = []
            st.rerun()
with col3:
    session_name_input = st.text_input("Rename chat", value=st.session_state.current_session_name, key="rename_input")
    if session_name_input != st.session_state.current_session_name:
        st.session_state.current_session_name = session_name_input
        if st.session_state.current_session_id:
            chat_sessions_collection.update_one(
                {"_id": ObjectId(st.session_state.current_session_id)},
                {"$set": {"name": session_name_input}}
            )

# Chat Context Window - Display statistics
if st.session_state.messages:
    with st.expander("📊 Chat Context & Statistics", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
            st.metric("👤 User Messages", user_messages)
        
        with col2:
            assistant_messages = len([msg for msg in st.session_state.messages if msg["role"] == "assistant"])
            st.metric("🤖 AI Responses", assistant_messages)
        
        with col3:
            total_chars = sum(len(msg["content"]) for msg in st.session_state.messages)
            st.metric("📝 Total Characters", f"{total_chars:,}")
        
        with col4:
            avg_response = sum(len(msg["content"]) for msg in st.session_state.messages if msg["role"] == "assistant") / max(assistant_messages, 1)
            st.metric("📏 Avg Response Length", f"{int(avg_response)}")
        
        st.divider()
        
        # Chat Summary
        st.markdown("**📋 Chat Summary:**")
        
        # Get user questions
        user_queries = [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
        
        if user_queries:
            st.markdown("**Questions Asked:**")
            for i, query in enumerate(user_queries, 1):
                query_preview = query[:60] + "..." if len(query) > 60 else query
                st.write(f"{i}. {query_preview}")
        
        st.divider()
        
        # Session metadata
        if st.session_state.current_session_id:
            session_data = chat_sessions_collection.find_one({"_id": ObjectId(st.session_state.current_session_id)})
            if session_data:
                col1, col2 = st.columns(2)
                
                with col1:
                    created_at = session_data.get("created_at", datetime.now())
                    st.write(f"**Created:** {created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                
                with col2:
                    updated_at = session_data.get("updated_at", datetime.now())
                    st.write(f"**Last Updated:** {updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

# Display chat history
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🧑‍💻" if msg["role"] == "user" else "🤖"):
            st.markdown(msg["content"])

# Initialize payment state
if "show_payment" not in st.session_state:
    st.session_state.show_payment = False
if "selected_products" not in st.session_state:
    st.session_state.selected_products = []

# Payment Section
if st.session_state.messages and len(st.session_state.messages) > 0:
    st.divider()
    
    # Show payment section
    payment_col1, payment_col2 = st.columns([2, 1])
    
    with payment_col1:
        st.markdown("### 💳 Buy Suggested Products")
        
        # Get available products from database
        if mongo_connected:
            all_products = list(products_collection.find({}).limit(10))
            
            if all_products:
                st.markdown("**📦 Available Products:**")
                st.markdown('<div class="products-available">', unsafe_allow_html=True)
                
                for idx, product in enumerate(all_products):
                    col1, col2, col3, col4 = st.columns([0.5, 2, 0.8, 0.8])
                    
                    with col1:
                        if st.checkbox(f"Select", key=f"select_{product['_id']}", help="Add to cart"):
                            if product not in st.session_state.selected_products:
                                st.session_state.selected_products.append(product)
                    
                    with col2:
                        st.write(f"**{product.get('emoji', '💄')} {product['name']}**")
                    
                    with col3:
                        st.write(f"${product['price']}")
                    
                    with col4:
                        if st.button("ℹ️", key=f"info_{product['_id']}", help="Product info"):
                            st.info(f"{product.get('description', 'No description available')}")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    with payment_col2:
        if st.session_state.selected_products:
            total = sum(float(p.get('price', 0)) for p in st.session_state.selected_products)
            st.markdown('<div class="order-summary">', unsafe_allow_html=True)
            st.markdown('<div class="summary-title">Order Summary</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-price-text">{len(st.session_state.selected_products)} items</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="total-amount">${total:.2f}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Razorpay Payment Section
if st.session_state.selected_products:
    st.divider()
    st.markdown("### 🛒 Checkout")
    
    total_amount = sum(float(p.get('price', 0)) for p in st.session_state.selected_products)
    
    # Display selected items
    st.markdown("**Items in Cart:**")
    for product in st.session_state.selected_products:
        st.markdown(f"""
        <div class="product-list-item">
            <div class="product-detail">
                <p class="product-name-text">{product.get('emoji', '💄')} {product['name']}</p>
            </div>
            <div class="product-price-text">${product['price']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Order Summary
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.metric("Items", len(st.session_state.selected_products))
    with col2:
        st.metric("Total", f"${total_amount:.2f}")
    with col3:
        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.selected_products = []
            st.rerun()
    
    st.divider()
    
    # Payment Options
    st.markdown("### 💳 Payment Options")
    
    # Option 1: Razorpay Payment Button
    st.markdown("**Option 1: Razorpay Secure Payment**")   
    
   
    # Razorpay Button HTML with your styling
    razorpay_html = """
    <div class="payment-section">
        <div class="payment-header">Pay Securely with Razorpay</div>
        <div class="razorpay-container">
            <form>
                <script src="https://checkout.razorpay.com/v1/payment-button.js"
                    data-payment_button_id="pl_SVWt1jhCrLef0w"
                    async>
                </script>
            </form>
        </div>
    </div>
    """

    # Render the HTML component
    components.html(razorpay_html, height=200)
    #st.markdown(razorpay_embed, unsafe_allow_html=True)
    
    
    st.info("✅ Click the payment button above to complete your purchase securely with Razorpay", icon="💳")
    
    # Option 2: Order Summary and Details
    st.markdown("---")
    st.markdown("**Option 2: View Order Details**")
    if st.button("📋 View Full Order Details", use_container_width=True):
        with st.expander("📦 Order Information", expanded=True):
            st.json({
                "items": [{"name": p['name'], "price": f"${p['price']}", "emoji": p.get('emoji', '💄')} for p in st.session_state.selected_products],
                "item_count": len(st.session_state.selected_products),
                "total_amount": f"${total_amount:.2f}",
                "session_id": st.session_state.current_session_id,
                "timestamp": datetime.now().isoformat()
            })
            st.success("Order details ready! Proceed to Razorpay payment above.")
    
    # Option 3: Continue Shopping
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛒 Continue Shopping", use_container_width=True):
            st.session_state.selected_products = []
            st.rerun()
    with col2:
        if st.button("🧹 Clear & Start Over", use_container_width=True):
            st.session_state.selected_products = []
            st.session_state.messages = []
            st.rerun()

# USER INPUT
user_input = st.chat_input("Ask for product suggestions...", key="user_input")

if user_input:
    if not mongo_connected:
        st.error("❌ Database connection failed. Please check MongoDB connection.")
        st.stop()
    
    if not SARVAM_API_KEY:
        st.error("❌ API key not configured. Add SARVAM_API_KEY to secrets.")
        st.stop()
    
    # Create new session if it doesn't exist
    if not st.session_state.current_session_id:
        # Generate session name using Sarvam LLM
        try:
            naming_prompt = f"Generate a short, descriptive 3-5 word chat session name for this user query. Only respond with the name, nothing else.\n\nUser query: {user_input}"
            
            naming_response = requests.post(
                "https://api.sarvam.ai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {SARVAM_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "messages": [
                        {
                            "role": "user",
                            "content": naming_prompt
                        }
                    ],
                    "model": "sarvam-m"
                },
                timeout=10
            )
            
            naming_result = naming_response.json()
            session_name = naming_result["choices"][0]["message"]["content"].strip().replace('<think>', '')
            if not session_name or len(session_name) == 0:
                session_name = "New Chat"
        except:
            session_name = "New Chat"
        
        session_doc = {
            "name": session_name,
            "messages": [],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        result = chat_sessions_collection.insert_one(session_doc)
        st.session_state.current_session_id = str(result.inserted_id)
        st.session_state.current_session_name = session_name
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    
    # Show loading spinner
    with st.spinner("🤖 AI is thinking..."):
        try:
            # FETCH DATA FROM MONGODB
            users = list(users_collection.find({}, {"password": 0}))
            activities = list(activity_collection.find({}))
            products = list(products_collection.find({}))
            
            # Convert ObjectId to string
            for a in activities:
                a["_id"] = str(a["_id"])
            for p in products:
                p["_id"] = str(p["_id"])
            
            # BUILD PROMPT
            # Include previous chat context
            chat_history = ""
            if st.session_state.messages:
                chat_history = "\n**Chat History (for context):**\n"
                for i, msg in enumerate(st.session_state.messages[-10:], 1):  # Last 10 messages for context
                    role = "User" if msg["role"] == "user" else "Assistant"
                    chat_history += f"{i}. **{role}:** {msg['content'][:200]}...\n" if len(msg['content']) > 200 else f"{i}. **{role}:** {msg['content']}\n"
            
            prompt = f"""You are an AI Shopping Assistant. Based on the following data and chat context, provide personalized product recommendations.

{chat_history}

**User Activity Logs:**
{json.dumps(activities, indent=2, default=str)}

**Product Catalogue:**
{json.dumps(products, indent=2, default=str)}

**Current User Question:**
{user_input}

Please analyze:
1. The user's browsing and activity history
2. The previous conversation context (if any)
3. The current question

Then suggest relevant products from the catalogue that match their interests and questions. Be concise, helpful, and maintain consistency with previous recommendations if applicable. If the user question is not about product, say "sorry, I am a shopping assistant" Goodbye with 1 liner 10 words message without showing analysis."""
            
            # SARVAM API CALL
            response = requests.post(
                "https://api.sarvam.ai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {SARVAM_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "model": "sarvam-m"
                },
                timeout=30
            )
            
            result = response.json()
            
            try:
                reply = result["choices"][0]["message"]["content"].replace('<think>', '')
            except (KeyError, IndexError, TypeError):
                reply = f"⚠️ API Response Error: {json.dumps(result, indent=2)}"
            
            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": reply})
            
            # Show response
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(reply)
            
            # Save session to MongoDB
            chat_sessions_collection.update_one(
                {"_id": ObjectId(st.session_state.current_session_id)},
                {
                    "$set": {
                        "messages": st.session_state.messages,
                        "updated_at": datetime.now()
                    }
                }
            )
            
            # Log this interaction
            activity_collection.insert_one({
                "action": "chatbot_interaction",
                "user_question": user_input,
                "session_id": st.session_state.current_session_id,
                "timestamp": datetime.now()
            })
            
            st.rerun()
        
        except requests.exceptions.Timeout:
            error_msg = "⏱️ Request timeout. The API took too long to respond."
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        except requests.exceptions.ConnectionError:
            error_msg = "🔌 Connection error. Please check your internet connection."
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
