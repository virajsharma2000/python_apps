import streamlit as st
from datetime import datetime, timedelta
import random

# Configure the page
st.set_page_config(
    page_title="Lumière Beauty | Luxury Skincare & Cosmetics",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for luxury aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    :root {
        --cream: #FAF8F5;
        --cream-dark: #F0EDE8;
        --brown: #2D2926;
        --brown-light: #5C5652;
        --rose: #C4A484;
        --rose-light: #D4C4B0;
    }
    
    .stApp {
        background-color: #FAF8F5;
    }
    
    .main-header {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3.5rem;
        font-weight: 300;
        color: #2D2926;
        text-align: center;
        letter-spacing: 0.15em;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        color: #5C5652;
        text-align: center;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 3rem;
    }
    
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 400;
        color: #2D2926;
        margin-bottom: 1.5rem;
        letter-spacing: 0.05em;
    }
    
    .product-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 1.5rem;
        border: 1px solid #E8E4DE;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .product-card:hover {
        box-shadow: 0 8px 30px rgba(45, 41, 38, 0.1);
    }
    
    .product-brand {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        color: #C4A484;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.25rem;
    }
    
    .product-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.25rem;
        font-weight: 500;
        color: #2D2926;
        margin-bottom: 0.5rem;
    }
    
    .product-price {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #2D2926;
    }
    
    .category-pill {
        display: inline-block;
        padding: 0.5rem 1.25rem;
        background: transparent;
        border: 1px solid #E8E4DE;
        border-radius: 100px;
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        color: #5C5652;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .category-pill:hover, .category-pill.active {
        background: #2D2926;
        color: #FAF8F5;
        border-color: #2D2926;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #F0EDE8 0%, #FAF8F5 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .stat-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #E8E4DE;
    }
    
    .stat-number {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem;
        font-weight: 600;
        color: #2D2926;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        color: #5C5652;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .order-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 1.5rem;
        border: 1px solid #E8E4DE;
        margin-bottom: 1rem;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 100px;
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .status-processing {
        background: #FEF3C7;
        color: #92400E;
    }
    
    .status-shipped {
        background: #DBEAFE;
        color: #1E40AF;
    }
    
    .status-delivered {
        background: #D1FAE5;
        color: #065F46;
    }
    
    .empty-state {
        text-align: center;
        padding: 4rem 2rem;
        color: #5C5652;
    }
    
    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .btn-primary {
        background: #2D2926;
        color: #FAF8F5;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        font-weight: 500;
        letter-spacing: 0.05em;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .btn-primary:hover {
        background: #1a1715;
    }
    
    .btn-secondary {
        background: transparent;
        color: #2D2926;
        border: 1px solid #2D2926;
        padding: 0.75rem 2rem;
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        font-weight: 500;
        letter-spacing: 0.05em;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .btn-secondary:hover {
        background: #2D2926;
        color: #FAF8F5;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E8E4DE;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1 {
        font-family: 'Cormorant Garamond', serif;
        color: #2D2926;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #2D2926;
        color: #FAF8F5;
        border: none;
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        letter-spacing: 0.05em;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #1a1715;
        color: #FAF8F5;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-family: 'Cormorant Garamond', serif;
        color: #2D2926;
    }
    
    [data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif;
        color: #5C5652;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        border-bottom: 1px solid #E8E4DE;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        letter-spacing: 0.05em;
        color: #5C5652;
        background: transparent;
        border: none;
        padding: 1rem 0;
    }
    
    .stTabs [aria-selected="true"] {
        color: #2D2926;
        border-bottom: 2px solid #2D2926;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Sample product data
PRODUCTS = [
    {
        "id": 1,
        "name": "Revitalizing Night Serum",
        "brand": "La Luxe",
        "price": 185.00,
        "category": "Skincare",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400&h=400&fit=crop",
        "rating": 4.9,
        "description": "A powerful overnight treatment that works while you sleep to restore and rejuvenate skin."
    },
    {
        "id": 2,
        "name": "Velvet Matte Lipstick",
        "brand": "Rouge Éternel",
        "price": 48.00,
        "category": "Makeup",
        "image": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400&h=400&fit=crop",
        "rating": 4.8,
        "description": "Rich, long-lasting color with a luxurious matte finish that feels weightless on lips."
    },
    {
        "id": 3,
        "name": "Rose Petal Eau de Parfum",
        "brand": "Maison Florale",
        "price": 220.00,
        "category": "Fragrance",
        "image": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400&h=400&fit=crop",
        "rating": 4.7,
        "description": "A romantic blend of Bulgarian rose, peony, and musk that evokes timeless elegance."
    },
    {
        "id": 4,
        "name": "Luminous Foundation",
        "brand": "Glow Atelier",
        "price": 78.00,
        "category": "Makeup",
        "image": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400&h=400&fit=crop",
        "rating": 4.9,
        "description": "Buildable coverage with a natural, radiant finish that looks like your skin, but better."
    },
    {
        "id": 5,
        "name": "Hydrating Face Cream",
        "brand": "La Luxe",
        "price": 145.00,
        "category": "Skincare",
        "image": "https://images.unsplash.com/photo-1570194065650-d99fb4b38b15?w=400&h=400&fit=crop",
        "rating": 4.8,
        "description": "Intensive moisture infused with hyaluronic acid and botanical extracts for plump, dewy skin."
    },
    {
        "id": 6,
        "name": "Silk Hair Elixir",
        "brand": "Cheveux d'Or",
        "price": 65.00,
        "category": "Hair",
        "image": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400&h=400&fit=crop",
        "rating": 4.6,
        "description": "Weightless oil that transforms dull, dry hair into lustrous, silky strands."
    },
    {
        "id": 7,
        "name": "Eye Contour Cream",
        "brand": "La Luxe",
        "price": 125.00,
        "category": "Skincare",
        "image": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400&h=400&fit=crop",
        "rating": 4.7,
        "description": "Targeted treatment for the delicate eye area, reducing fine lines and dark circles."
    },
    {
        "id": 8,
        "name": "Oud Noir Cologne",
        "brand": "Maison Florale",
        "price": 195.00,
        "category": "Fragrance",
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400&h=400&fit=crop",
        "rating": 4.9,
        "description": "A sophisticated blend of rare oud, amber, and sandalwood for the discerning individual."
    },
]

CATEGORIES = ["All", "Skincare", "Makeup", "Fragrance", "Hair"]

# Initialize session state
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []
if "cart" not in st.session_state:
    st.session_state.cart = []
if "orders" not in st.session_state:
    # Sample orders
    st.session_state.orders = [
        {
            "id": "LUM-2024-001",
            "date": datetime.now() - timedelta(days=2),
            "status": "processing",
            "items": [PRODUCTS[0], PRODUCTS[1]],
            "total": 233.00,
            "estimated_delivery": datetime.now() + timedelta(days=5)
        },
        {
            "id": "LUM-2024-002",
            "date": datetime.now() - timedelta(days=7),
            "status": "shipped",
            "items": [PRODUCTS[2]],
            "total": 220.00,
            "estimated_delivery": datetime.now() + timedelta(days=2)
        },
        {
            "id": "LUM-2024-003",
            "date": datetime.now() - timedelta(days=14),
            "status": "delivered",
            "items": [PRODUCTS[3], PRODUCTS[4], PRODUCTS[5]],
            "total": 288.00,
            "delivered_date": datetime.now() - timedelta(days=10)
        }
    ]

def add_to_wishlist(product_id):
    if product_id not in st.session_state.wishlist:
        st.session_state.wishlist.append(product_id)
        st.toast(f"Added to wishlist")

def remove_from_wishlist(product_id):
    if product_id in st.session_state.wishlist:
        st.session_state.wishlist.remove(product_id)
        st.rerun()

def add_to_cart(product_id):
    st.session_state.cart.append(product_id)
    st.toast(f"Added to bag")

def get_product_by_id(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)

# Sidebar navigation
with st.sidebar:
    st.markdown('<h1 style="font-family: \'Cormorant Garamond\', serif; font-size: 1.75rem; font-weight: 300; letter-spacing: 0.1em; margin-bottom: 2rem;">LUMIÈRE</h1>', unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["Shop", "Wishlist", "Orders", "Bag"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Cart summary
    cart_count = len(st.session_state.cart)
    wishlist_count = len(st.session_state.wishlist)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Bag", cart_count)
    with col2:
        st.metric("Wishlist", wishlist_count)
    
    st.markdown("---")
    st.markdown("""
    <div style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #5C5652; line-height: 1.8;">
        <p><strong>Customer Care</strong></p>
        <p>contact@lumiere.com</p>
        <p>+1 (800) 555-LUXE</p>
    </div>
    """, unsafe_allow_html=True)

# Main content
if page == "Shop":
    # Hero section
    st.markdown("""
    <div class="hero-section">
        <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #C4A484; margin-bottom: 1rem;">The Art of Beauty</p>
        <h1 class="main-header">LUMIÈRE BEAUTY</h1>
        <p class="sub-header">Curated Luxury for the Discerning</p>
        <p style="font-family: 'Inter', sans-serif; font-size: 1rem; color: #5C5652; max-width: 600px; margin: 0 auto; line-height: 1.8;">
            Discover our meticulously curated collection of premium skincare, 
            cosmetics, and fragrances from the world's most prestigious brands.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Category filter
    st.markdown('<h2 class="section-title">Our Collection</h2>', unsafe_allow_html=True)
    
    selected_category = st.selectbox(
        "Filter by category",
        CATEGORIES,
        label_visibility="collapsed"
    )
    
    # Filter products
    if selected_category == "All":
        filtered_products = PRODUCTS
    else:
        filtered_products = [p for p in PRODUCTS if p["category"] == selected_category]
    
    # Product grid
    cols = st.columns(4)
    for idx, product in enumerate(filtered_products):
        with cols[idx % 4]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{product['image']}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">
                <p class="product-brand">{product['brand']}</p>
                <p class="product-name">{product['name']}</p>
                <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #C4A484; margin-bottom: 0.5rem;">{'★' * int(product['rating'])} {product['rating']}</p>
                <p class="product-price">${product['price']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Add to Bag", key=f"cart_{product['id']}", use_container_width=True):
                    add_to_cart(product['id'])
            with col2:
                heart = "♥" if product['id'] in st.session_state.wishlist else "♡"
                if st.button(heart, key=f"wish_{product['id']}", use_container_width=True):
                    if product['id'] in st.session_state.wishlist:
                        remove_from_wishlist(product['id'])
                    else:
                        add_to_wishlist(product['id'])
            
            st.markdown("<br>", unsafe_allow_html=True)

elif page == "Wishlist":
    st.markdown('<h1 class="main-header" style="font-size: 2.5rem; text-align: left;">Your Wishlist</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header" style="text-align: left; margin-bottom: 2rem;">{len(st.session_state.wishlist)} saved items</p>', unsafe_allow_html=True)
    
    if not st.session_state.wishlist:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">♡</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: #2D2926; margin-bottom: 0.5rem;">Your wishlist is empty</h3>
            <p style="font-family: 'Inter', sans-serif; color: #5C5652;">Save items you love to your wishlist and they'll appear here.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(4)
        for idx, product_id in enumerate(st.session_state.wishlist):
            product = get_product_by_id(product_id)
            if product:
                with cols[idx % 4]:
                    st.markdown(f"""
                    <div class="product-card">
                        <img src="{product['image']}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">
                        <p class="product-brand">{product['brand']}</p>
                        <p class="product-name">{product['name']}</p>
                        <p class="product-price">${product['price']:.2f}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Add to Bag", key=f"wishlist_cart_{product['id']}", use_container_width=True):
                            add_to_cart(product['id'])
                    with col2:
                        if st.button("Remove", key=f"wishlist_remove_{product['id']}", use_container_width=True):
                            remove_from_wishlist(product['id'])
                    
                    st.markdown("<br>", unsafe_allow_html=True)

elif page == "Orders":
    st.markdown('<h1 class="main-header" style="font-size: 2.5rem; text-align: left;">Order History</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header" style="text-align: left; margin-bottom: 2rem;">{len(st.session_state.orders)} orders</p>', unsafe_allow_html=True)
    
    if not st.session_state.orders:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">📦</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: #2D2926; margin-bottom: 0.5rem;">No orders yet</h3>
            <p style="font-family: 'Inter', sans-serif; color: #5C5652;">When you place an order, it will appear here.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for order in st.session_state.orders:
            status_class = f"status-{order['status']}"
            status_text = order['status'].capitalize()
            
            with st.container():
                st.markdown(f"""
                <div class="order-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div>
                            <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #5C5652; text-transform: uppercase; letter-spacing: 0.1em;">Order #{order['id']}</p>
                            <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.25rem; color: #2D2926;">
                                {order['date'].strftime('%B %d, %Y')}
                            </p>
                        </div>
                        <span class="status-badge {status_class}">{status_text}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Order items
                cols = st.columns(len(order['items']) + 2)
                for idx, item in enumerate(order['items']):
                    with cols[idx]:
                        st.image(item['image'], width=80)
                        st.markdown(f"<p style='font-size: 0.75rem; color: #5C5652;'>{item['name']}</p>", unsafe_allow_html=True)
                
                with cols[-1]:
                    st.markdown(f"""
                    <div style="text-align: right;">
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #5C5652;">Total</p>
                        <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: #2D2926;">${order['total']:.2f}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Delivery info
                if order['status'] == 'delivered':
                    st.success(f"Delivered on {order['delivered_date'].strftime('%B %d, %Y')}")
                elif order['status'] == 'shipped':
                    st.info(f"Estimated delivery: {order['estimated_delivery'].strftime('%B %d, %Y')}")
                else:
                    st.warning(f"Estimated delivery: {order['estimated_delivery'].strftime('%B %d, %Y')}")
                
                st.markdown("<br>", unsafe_allow_html=True)

elif page == "Bag":
    st.markdown('<h1 class="main-header" style="font-size: 2.5rem; text-align: left;">Shopping Bag</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header" style="text-align: left; margin-bottom: 2rem;">{len(st.session_state.cart)} items</p>', unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">🛒</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: #2D2926; margin-bottom: 0.5rem;">Your bag is empty</h3>
            <p style="font-family: 'Inter', sans-serif; color: #5C5652;">Add items you love to your bag and they'll appear here.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        total = sum(get_product_by_id(pid)['price'] for pid in st.session_state.cart)
        st.markdown(f"<p style='font-family: Inter, sans-serif; font-size: 1rem; color: #2D2926;'>Total: ${total:.2f}</p>", unsafe_allow_html=True)
        
        # Razorpay Checkout modal
        razorpay_html = f"""
        <div style="margin-top: 1rem;">
            <button id="rzp-button" style="
                background-color:#2D2926;color:#FAF8F5;
                padding:0.75rem 2rem;border:none;border-radius:4px;
                font-family:'Inter',sans-serif;font-weight:500;
                cursor:pointer;
            ">Checkout</button>
        </div>
        <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
        <script>
            var options = {{
                "key": "rzp_test_yourkeyhere", // Replace with your Razorpay key
                "amount": {int(total*100)}, // amount in paise
                "currency": "INR",
                "name": "Lumière Beauty",
                "description": "Shopping Bag Payment",
                "handler": function(response){{
                    alert("Payment successful! Payment ID: " + response.razorpay_payment_id);
                }},
                "theme": {{
                    "color": "#C4A484"
                }}
            }};
            var rzp = new Razorpay(options);
            document.getElementById('rzp-button').onclick = function(e){{
                rzp.open();
                e.preventDefault();
            }}
        </script>
        """
        import streamlit.components.v1 as components
        components.html(razorpay_html, height=120)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 2rem; border-top: 1px solid #E8E4DE;">
    <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; letter-spacing: 0.1em; color: #2D2926; margin-bottom: 1rem;">LUMIÈRE</p>
    <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #5C5652;">© 2024 Lumière Beauty. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
