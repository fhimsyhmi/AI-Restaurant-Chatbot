%%writefile app.py
import streamlit as st

# ==================== RESTAURANT DATABASE ====================
RESTAURANTS = [
    {
        "name": "Restoran Nasi Kandar Simpang Empat",
        "cuisine": "malay",
        "type": ["nasi kandar", "rice"],
        "price": "budget",
        "location": "Bandar Seri Iskandar",
        "rating": 4.2,
        "hours": "24 hours",
        "description": "Popular nasi kandar spot with variety of curries and dishes."
    },
    {
        "name": "Kedai Makan Pak Tam",
        "cuisine": "malay",
        "type": ["nasi campur", "rice", "local"],
        "price": "budget",
        "location": "Bandar Baru Seri Iskandar",
        "rating": 4.0,
        "hours": "7am - 10pm",
        "description": "Local favorite for nasi campur with home-cooked dishes."
    },
    {
        "name": "Restoran Aroma Hijau",
        "cuisine": "malay",
        "type": ["western", "local", "cafe"],
        "price": "moderate",
        "location": "Bandar Universiti",
        "rating": 4.3,
        "hours": "10am - 11pm",
        "description": "Cafe-style restaurant serving both local and western food."
    },
    {
        "name": "Warung Kopi Tok Ayah",
        "cuisine": "malay",
        "type": ["breakfast", "coffee", "roti canai"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.1,
        "hours": "6am - 12pm",
        "description": "Best roti canai and teh tarik in town."
    },
    {
        "name": "Restoran Makanan Laut Seri Manjung",
        "cuisine": "chinese",
        "type": ["seafood", "chinese"],
        "price": "expensive",
        "location": "Near Seri Iskandar",
        "rating": 4.5,
        "hours": "11am - 10pm",
        "description": "Fresh seafood with Chinese-style cooking."
    },
    {
        "name": "Kedai Makan Selera Kampung",
        "cuisine": "malay",
        "type": ["local", "traditional", "rice"],
        "price": "budget",
        "location": "Kampung Bota",
        "rating": 4.0,
        "hours": "7am - 9pm",
        "description": "Traditional kampung-style cooking with authentic flavors."
    },
    {
        "name": "D'Chicken Rice Corner",
        "cuisine": "chinese",
        "type": ["chicken rice", "rice"],
        "price": "budget",
        "location": "Bandar Seri Iskandar",
        "rating": 4.2,
        "hours": "10am - 8pm",
        "description": "Delicious Hainanese chicken rice."
    },
    {
        "name": "Mamak Corner 24H",
        "cuisine": "indian",
        "type": ["mamak", "roti canai", "mee goreng"],
        "price": "budget",
        "location": "Bandar Universiti",
        "rating": 3.9,
        "hours": "24 hours",
        "description": "Classic mamak fare available round the clock."
    },
    {
        "name": "Cafe Latte Art",
        "cuisine": "western",
        "type": ["cafe", "coffee", "western", "dessert"],
        "price": "moderate",
        "location": "Bandar Seri Iskandar",
        "rating": 4.4,
        "hours": "9am - 11pm",
        "description": "Trendy cafe with good coffee and pasta."
    },
    {
        "name": "Restoran Nasi Arab Al-Hanin",
        "cuisine": "arab",
        "type": ["arab", "nasi arab", "middle eastern"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.3,
        "hours": "11am - 10pm",
        "description": "Authentic Arab cuisine with lamb and chicken dishes."
    }
]

# ==================== KEYWORD MAPPINGS ====================
CUISINE_KEYWORDS = {
    "malay": ["malay", "melayu", "local", "kampung", "traditional"],
    "chinese": ["chinese", "cina", "oriental"],
    "indian": ["indian", "mamak", "india"],
    "western": ["western", "cafe", "pasta", "burger"],
    "arab": ["arab", "middle eastern", "nasi arab"]
}

PRICE_KEYWORDS = {
    "budget": ["cheap", "budget", "murah", "affordable", "low price"],
    "moderate": ["moderate", "medium", "sederhana", "reasonable"],
    "expensive": ["expensive", "mahal", "fancy", "high end", "premium"]
}

FOOD_TYPE_KEYWORDS = {
    "rice": ["rice", "nasi", "nasi campur", "nasi kandar"],
    "seafood": ["seafood", "fish", "prawn", "sotong", "ikan"],
    "breakfast": ["breakfast", "sarapan", "morning", "roti canai"],
    "coffee": ["coffee", "kopi", "cafe", "latte"],
    "chicken rice": ["chicken rice", "nasi ayam"],
    "roti canai": ["roti canai", "roti", "canai"],
    "nasi kandar": ["nasi kandar", "kandar"]
}

# ==================== AI FUNCTIONS ====================
def extract_preferences(message):
    """Extract user preferences from their message."""
    msg_lower = message.lower()
    prefs = {"cuisine": None, "price": None, "food_type": None, "late_night": False}
    
    # Check for cuisine preference
    for cuisine, keywords in CUISINE_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            prefs["cuisine"] = cuisine
            break
    
    # Check for price preference
    for price, keywords in PRICE_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            prefs["price"] = price
            break
    
    # Check for food type
    for food, keywords in FOOD_TYPE_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            prefs["food_type"] = food
            break
    
    # Check for late night
    if any(word in msg_lower for word in ["late", "night", "midnight", "24", "malam", "lewat"]):
        prefs["late_night"] = True
    
    return prefs

def find_restaurants(preferences):
    """Find restaurants matching user preferences."""
    matches = []
    
    for restaurant in RESTAURANTS:
        score = 0
        
        # Check cuisine match
        if preferences["cuisine"] and restaurant["cuisine"] == preferences["cuisine"]:
            score += 3
        
        # Check price match
        if preferences["price"] and restaurant["price"] == preferences["price"]:
            score += 2
        
        # Check food type match
        if preferences["food_type"]:
            if any(preferences["food_type"] in t for t in restaurant["type"]):
                score += 2
        
        # Check late night availability
        if preferences["late_night"] and "24" in restaurant["hours"]:
            score += 2
        
        if score > 0 or not any(preferences.values()):
            matches.append((restaurant, score))
    
    # Sort by score (descending) then by rating
    matches.sort(key=lambda x: (x[1], x[0]["rating"]), reverse=True)
    return [m[0] for m in matches[:5]]

def format_restaurant(r):
    """Format restaurant info for display."""
    price_emoji = {"budget": "💰", "moderate": "💰💰", "expensive": "💰💰💰"}
    stars = "⭐" * int(r['rating'])
    return f"""
<div class="restaurant-card">
    <h4>{r['name']}</h4>
    <p>{stars} ({r['rating']})</p>
    <p>🍽️ <strong>Cuisine:</strong> {r['cuisine'].title()}</p>
    <p>{price_emoji.get(r['price'], '💰')} <strong>Price:</strong> {r['price'].title()}</p>
    <p>📍 <strong>Location:</strong> {r['location']}</p>
    <p>🕐 <strong>Hours:</strong> {r['hours']}</p>
    <p>📝 {r['description']}</p>
</div>
"""

def generate_response(user_message):
    """Generate chatbot response based on user message."""
    msg_lower = user_message.lower()
    
    # Greeting responses
    greetings = ["hi", "hello", "hey", "assalamualaikum", "hai"]
    if any(g in msg_lower for g in greetings):
        return """Hello! 👋 Welcome to the Seri Iskandar Restaurant Recommender!

I can help you find great places to eat. Just tell me:
- What cuisine you prefer (Malay, Chinese, Indian, Western, Arab)
- Your budget (cheap, moderate, expensive)
- Type of food (rice, seafood, breakfast, coffee, etc.)
- If you need late-night options

For example: "I want cheap Malay food" or "Any good cafe nearby?"
"""

    # Help responses
    if any(h in msg_lower for h in ["help", "how", "what can"]):
        return """Here's how I can help you:

🍜 **Find by cuisine**: "Show me Chinese restaurants"
💵 **Find by budget**: "I want cheap food"
🍛 **Find by food type**: "Where can I get nasi kandar?"
🌙 **Late night options**: "What's open late at night?"
🔄 **Combinations**: "Cheap Malay food for breakfast"

Just ask naturally and I'll recommend the best spots!
"""

    # Extract preferences and find matches
    prefs = extract_preferences(user_message)
    restaurants = find_restaurants(prefs)
    
    if not restaurants:
        return "Sorry, I couldn't find any restaurants matching your criteria. Try being less specific or ask for different options!"
    
    # Build response
    response = "### 🍴 Here are my recommendations:\n\n"
    for r in restaurants[:3]:
        response += format_restaurant(r)
    
    if len(restaurants) > 3:
        response += f"\n\n_I found {len(restaurants)} matches. Want to see more options?_"
    
    return response

# ==================== STREAMLIT UI ====================

# Page Configuration
st.set_page_config(
    page_title="Seri Iskandar Food Bot", 
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# PWA Support - Makes it installable as mobile app
st.markdown("""
<link rel="manifest" href="data:application/json;base64,ewogICJuYW1lIjogIlNlcmkgSXNrYW5kYXIgUmVzdGF1cmFudCBCb3QiLAogICJzaG9ydF9uYW1lIjogIkZvb2QgQm90IiwKICAiZGVzY3JpcHRpb24iOiAiQUkgUmVzdGF1cmFudCBSZWNvbW1lbmRlciBmb3IgU2VyaSBJc2thbmRhciIsCiAgInN0YXJ0X3VybCI6ICIvIiwKICAiZGlzcGxheSI6ICJzdGFuZGFsb25lIiwKICAiYmFja2dyb3VuZF9jb2xvciI6ICIjMWExYTJlIiwKICAidGhlbWVfY29sb3IiOiAiI2U5NDU2MCIsCiAgIm9yaWVudGF0aW9uIjogInBvcnRyYWl0IiwKICAiaWNvbnMiOiBbCiAgICB7CiAgICAgICJzcmMiOiAiaHR0cHM6Ly9pbWcuaWNvbnM4LmNvbS9jbG91ZHMvMTkyL3Jlc3RhdXJhbnQucG5nIiwKICAgICAgInNpemVzIjogIjE5MngxOTIiLAogICAgICAidHlwZSI6ICJpbWFnZS9wbmciCiAgICB9LAogICAgewogICAgICAic3JjIjogImh0dHBzOi8vaW1nLmljb25zOC5jb20vY2xvdWRzLzUxMi9yZXN0YXVyYW50LnBuZyIsCiAgICAgICJzaXplcyI6ICI1MTJ4NTEyIiwKICAgICAgInR5cGUiOiAiaW1hZ2UvcG5nIgogICAgfQogIF0KfQ==">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Food Bot">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#e94560">
<link rel="apple-touch-icon" href="https://img.icons8.com/clouds/192/restaurant.png">
""", unsafe_allow_html=True)

# Custom CSS Styling
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Title styling */
    h1 {
        color: #e94560 !important;
        text-align: center;
        font-size: 2.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Subtitle */
    .stCaption {
        text-align: center;
        color: #a2d2ff !important;
        font-size: 1.1rem !important;
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 10px;
        margin: 5px 0;
    }
    
    /* Restaurant card */
    .restaurant-card {
        background: linear-gradient(145deg, #0f3460, #16213e);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #e94560;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .restaurant-card h4 {
        color: #e94560;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    
    .restaurant-card p {
        color: #eaeaea;
        margin: 5px 0;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #e94560 !important;
    }
    
    /* Input box */
    .stChatInput {
        border-radius: 25px;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #e94560;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    
    .stButton > button:hover {
        background-color: #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🍽️ Seri Iskandar Restaurant Bot")
st.caption("✨ Your AI assistant for finding great food in Seri Iskandar! ✨")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome = """Hello! 👋 I'm your **Seri Iskandar Restaurant Guide**!

Tell me what you're craving and I'll recommend the best spots. You can ask things like:
- "I want cheap Malay food"
- "Where can I get good nasi kandar?"
- "Any cafe open late night?"

**What are you in the mood for today?** 🍴"""
    st.session_state.messages.append({"role": "assistant", "content": welcome})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("🔍 Ask me about restaurants..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display response
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/restaurant.png", width=150)
    st.header("🍜 About")
    st.write("This chatbot helps you find the perfect restaurant in Seri Iskandar, Perak.")
    
    st.divider()
    
    st.header("✨ Features")
    st.write("🍽️ Search by cuisine type")
    st.write("💰 Filter by budget")
    st.write("🍛 Find specific food types")
    st.write("🌙 Late-night options")
    
    st.divider()
    
    st.header("💡 Quick Tips")
    st.code("I want nasi kandar", language=None)
    st.code("Cheap breakfast spot", language=None)
    st.code("Western food cafe", language=None)
    
    st.divider()
    st.caption("Made with ❤️ for AI Assignment")
