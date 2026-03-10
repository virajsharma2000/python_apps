import streamlit as st
import requests
from pymongo import MongoClient
import json

# -----------------------------
# CONFIG
# -----------------------------

MONGO_URI = f"mongodb+srv://virajsharma_db_user:{st.secrets['MONGO_PASSWORD']}@cluster0.xclz1ks.mongodb.net/cluster0.xclz1ks.mongodb.net/?appName=Cluster0"
SARVAM_API_KEY = st.secrets['SARVAM_API_KEY']

client = MongoClient(MONGO_URI)
db = client["cluster0"]

users_collection = db["user"]
activity_collection = db["activity_logs"]
products_collection = db["products"]

# -----------------------------
# STREAMLIT UI
# -----------------------------

st.title("🛍️ AI Shopping Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# USER INPUT
# -----------------------------

user_input = st.chat_input("Ask for product suggestions...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # -----------------------------
    # FETCH DATA FROM MONGODB
    # -----------------------------

    users = list(users_collection.find({}, {"password": 0}))
    activities = list(activity_collection.find({}))
    products = list(products_collection.find({}))

    # convert ObjectId to string
    for a in activities:
        a["_id"] = str(a["_id"])

    for p in products:
        p["_id"] = str(p["_id"])

    # -----------------------------
    # BUILD PROMPT
    # -----------------------------

    prompt = f"""
this is the user's ecommerce site activity logs:

{json.dumps(activities, indent=2, default=str)}

this is the product catalogue data:

{json.dumps(products, indent=2, default=str)}

this is user's question:

{user_input}

give product suggestions to the user based on the catalogue and activity logs
"""

    # -----------------------------
    # SARVAM API CALL
    # -----------------------------

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
        }
    )

    result = response.json()

    try:
        reply = result["choices"][0]["message"]["content"]
    except:
        reply = f"API Error: {result}"

    # -----------------------------
    # SHOW RESPONSE
    # -----------------------------

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )