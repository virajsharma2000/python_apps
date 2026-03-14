import streamlit as st
import requests
from pymongo import MongoClient
import json
from datetime import datetime

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
    /* Main background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Chat message styling */
    .stChatMessage {
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    /* User message */
    .stChatMessage [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Assistant message */
    .stChatMessage:has([data-testid="stChatMessageContent"]) {
        background: #f0f2f6;
        border-radius: 12px;
    }
    
    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: white;
        font-size: 1rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    /* Chat input styling */
    .stChatInputContainer {
        padding: 1rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .sidebar-header {
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    /* Info cards */
    .info-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Input field styling */
    input {
        border-radius: 8px !important;
        border: 2px solid #ddd !important;
    }
    
    input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 8px rgba(102, 126, 234, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# CONFIG
MONGO_URI = "mongodb+srv://virajsharma_db_user:pumpulili@cluster0.xclz1ks.mongodb.net/cluster0.xclz1ks.mongodb.net/?appName=Cluster0"
SARVAM_API_KEY = st.secrets['SARVAM_API_KEY']

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db = client["cluster0"]
    users_collection = db["user"]
    activity_collection = db["activity_logs"]
    products_collection = db["products"]
    mongo_connected = True
except Exception as e:
    st.error(f"MongoDB Connection Failed: {e}")
    mongo_connected = False

# HEADER
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1>🛍️ AI Shopping Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Get personalized product recommendations powered by AI</div>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# SIDEBAR - Display stats and info
with st.sidebar:
    st.markdown("<div class='sidebar-header'>📊 Dashboard</div>", unsafe_allow_html=True)
    
    if mongo_connected:
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

# Display chat history
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🧑‍💻" if msg["role"] == "user" else "🤖"):
            st.markdown(msg["content"])

# USER INPUT
user_input = st.chat_input("Ask for product suggestions...", key="user_input")

if user_input:
    if not mongo_connected:
        st.error("❌ Database connection failed. Please check MongoDB connection.")
        st.stop()
    
    if not SARVAM_API_KEY:
        st.error("❌ API key not configured. Add SARVAM_API_KEY to secrets.")
        st.stop()
    
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
            prompt = f"""Based on the following data, provide personalized product recommendations:

**User Activity Logs:**
{json.dumps(activities, indent=2, default=str)}

**Product Catalogue:**
{json.dumps(products, indent=2, default=str)}

**User Question:**
{user_input}

Please analyze the user's browsing history and suggest relevant products from the catalogue that match their interests. Be concise and helpful."""
            
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
                reply = result["choices"][0]["message"]["content"]
            except (KeyError, IndexError, TypeError):
                reply = f"⚠️ API Response Error: {json.dumps(result, indent=2)}"
            
            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": reply})
            
            # Show response
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(reply)
            
            # Log this interaction
            activity_collection.insert_one({
                "action": "chatbot_interaction",
                "user_question": user_input,
                "timestamp": datetime.now()
            })
        
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