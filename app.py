# Import the Streamlit library - this is what creates the web interface
import streamlit as st

# ==================== RESTAURANT DATABASE ====================
# This is our main data source - a list of dictionaries containing restaurant information
# Each restaurant is a dictionary with details like name, cuisine, price, etc.

RESTAURANTS = [

    # ======================
    # MALAY
    # ======================
    {
        "name": "Little Ipoh Cafe",
        "cuisine": "malay",
        "type": ["local", "rice", "noodles"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.1,
        "hours": "8am - 9pm",
        "description": "Local Malaysian dishes inspired by Ipoh-style home cooking.",
        "map_link": "https://www.google.com/maps/search/Little+Ipoh+Cafe+Seri+Iskandar"
    },
    {
        "name": "Gomore Kitchen",
        "cuisine": "malay",
        "type": ["local", "rice", "fried dishes"],
        "price": "budget",
        "location": "Bandar Universiti",
        "rating": 4.0,
        "hours": "10am - 10pm",
        "description": "Comfort food with affordable Malaysian rice and noodle dishes.",
        "map_link": "https://www.google.com/maps/search/Gomore+Kitchen+Seri+Iskandar"
    },
    {
        "name": "Restoran Bunda Seri Iskandar",
        "cuisine": "malay",
        "type": ["local", "nasi campur", "home-style"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.1,
        "hours": "7am - 11pm",
        "description": "Popular local spot for nasi campur and traditional Malay dishes.",
        "map_link": "https://www.google.com/maps/search/Restoran+Bunda+Seri+Iskandar"
    },
    {
        "name": "Ayam Gepuk Pak Gembus",
        "cuisine": "malay",
        "type": ["ayam gepuk", "spicy", "rice"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.2,
        "hours": "11am - 10pm",
        "description": "Famous Indonesian-style ayam gepuk with spicy sambal.",
        "map_link": "https://www.google.com/maps/search/Ayam+Gepuk+Pak+Gembus+Seri+Iskandar"
    },
    {
        "name": "Warung Cha HQ",
        "cuisine": "malay",
        "type": ["tea", "beverages", "snacks"],
        "price": "budget",
        "location": "Bandar Universiti",
        "rating": 4.0,
        "hours": "12pm - 12am",
        "description": "Casual hangout serving flavored tea, drinks, and light snacks.",
        "map_link": "https://www.google.com/maps/search/Warung+Cha+HQ+Seri+Iskandar"
    },
    {
        "name": "Makan Pagi D' Cafetiam",
        "cuisine": "malay",
        "type": ["breakfast", "rice", "roti canai"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "6am - 12pm",
        "description": "Breakfast-focused spot offering local morning dishes.",
        "map_link": "https://www.google.com/maps/search/Makan+Pagi+D+Cafetiam+Seri+Iskandar"
    },
    {
        "name": "Ayam Gepuk Pak Gendut",
        "cuisine": "malay",
        "type": ["ayam gepuk", "rice", "spicy"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.1,
        "hours": "11am - 10pm",
        "description": "Spicy ayam gepuk with generous portion, student favourite.",
        "map_link": "https://www.google.com/maps/search/Ayam+Gepuk+Pak+Gendut+Seri+Iskandar"
    },
    {
        "name": "Ayam Gepuk Tok Pa",
        "cuisine": "malay",
        "type": ["ayam gepuk", "rice", "spicy"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "11am - 10pm",
        "description": "Local ayam gepuk with homemade sambal and crispy chicken.",
        "map_link": "https://www.google.com/maps/search/Ayam+Gepuk+Tok+Pa+Seri+Iskandar"
    },

    # ======================
    # INDIAN / MAMAK
    # ======================
    {
        "name": "Rahman Corner",
        "cuisine": "indian",
        "type": ["mamak", "nasi kandar", "roti canai"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "24 hours",
        "description": "Mamak restaurant serving nasi kandar, roti canai and tomyam.",
        "map_link": "https://www.google.com/maps/search/Rahman+Corner+Seri+Iskandar"
    },
    {
        "name": "Restoran Al Bayan",
        "cuisine": "indian",
        "type": ["mamak", "briyani", "rice"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 3.9,
        "hours": "7am - 11pm",
        "description": "Indian Muslim dishes including briyani and curry rice.",
        "map_link": "https://www.google.com/maps/search/Restoran+Al+Bayan+Seri+Iskandar"
    },
    {
        "name": "Restoran Nasi Vanggey",
        "cuisine": "indian",
        "type": ["nasi vanggey", "rice", "curry"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.1,
        "hours": "10am - 9pm",
        "description": "Ipoh-style nasi vanggey known for rich curry flavors.",
        "map_link": "https://www.google.com/maps/search/Restoran+Nasi+Vanggey+Seri+Iskandar"
    },
    {
        "name": "Bilal Bistro Nasi Kandar",
        "cuisine": "indian",
        "type": ["nasi kandar", "rice", "mamak"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "24 hours",
        "description": "Affordable nasi kandar suitable for late-night meals.",
        "map_link": "https://www.google.com/maps/search/Bilal+Bistro+Nasi+Kandar+Seri+Iskandar"
    },

    # ======================
    # ARAB
    # ======================
    {
        "name": "Restoran Nasi Arab Sana'ah",
        "cuisine": "arab",
        "type": ["arab", "mandi", "rice"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.2,
        "hours": "11am - 10pm",
        "description": "Traditional Yemeni-style nasi mandi and Arab dishes.",
        "map_link": "https://www.google.com/maps/search/Restoran+Nasi+Arab+Sanaah+Seri+Iskandar"
    },
    {
        "name": "Syriano Restaurant",
        "cuisine": "arab",
        "type": ["arab", "shawarma", "middle eastern"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.5,
        "hours": "11am - 11pm",
        "description": "Authentic Middle Eastern food with large portions.",
        "map_link": "https://www.google.com/maps/search/Syriano+Restaurant+Seri+Iskandar"
    },
    {
        "name": "Nojoum Hadramout Restaurant",
        "cuisine": "arab",
        "type": ["arab", "mandi", "grill"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.4,
        "hours": "11am - 11pm",
        "description": "Hadramaut cuisine featuring grilled meats and rice.",
        "map_link": "https://www.google.com/maps/search/Nojoum+Hadramout+Restaurant+Seri+Iskandar"
    },

    # ======================
    # WESTERN
    # ======================
    {
        "name": "The Black Caravan Seri Iskandar",
        "cuisine": "western",
        "type": ["western", "pasta", "fast food"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.2,
        "hours": "12pm - 11pm",
        "description": "Western casual dining with pastas and grilled items.",
        "map_link": "https://www.google.com/maps/search/The+Black+Caravan+Seri+Iskandar"
    },
    {
        "name": "Chegu' Cafe",
        "cuisine": "western",
        "type": ["cafe", "western", "dessert"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "10am - 10pm",
        "description": "Cafe-style meals with western and fusion menu.",
        "map_link": "https://www.google.com/maps/search/Chegu+Cafe+Seri+Iskandar"
    },
    {
        "name": "Mastergrill SIBC Restaurant & Catering",
        "cuisine": "western",
        "type": ["grill", "steak", "western"],
        "price": "moderate",
        "location": "Seri Iskandar Business Centre",
        "rating": 4.1,
        "hours": "12pm - 10pm",
        "description": "Grilled dishes and catering services for events.",
        "map_link": "https://www.google.com/maps/search/Mastergrill+SIBC+Seri+Iskandar"
    },
    {
        "name": "Kampung Burger Seri Iskandar",
        "cuisine": "western",
        "type": ["burger", "street food", "western"],
        "price": "budget",
        "location": "Seri Iskandar",
        "rating": 4.2,
        "hours": "6pm - 12am",
        "description": "Local-style burger stall popular for supper.",
        "map_link": "https://www.google.com/maps/search/Kampung+Burger+Seri+Iskandar"
    },
    {
        "name": "Kafe Cef Seri Iskandar",
        "cuisine": "western",
        "type": ["cafe", "western", "local fusion"],
        "price": "moderate",
        "location": "Seri Iskandar",
        "rating": 4.0,
        "hours": "10am - 10pm",
        "description": "Relaxed cafe serving western and Malaysian fusion dishes.",
        "map_link": "https://www.google.com/maps/search/Kafe+Cef+Seri+Iskandar"
    }
]


# ==================== KEYWORD MAPPINGS ====================
# These dictionaries map user words to our categories
# This is the "AI brain" - it understands what users mean when they type different words

# Maps various ways users might say cuisine types to our standard categories
CUISINE_KEYWORDS = {
    "malay": ["malay", "melayu", "local", "kampung", "traditional"],  # If user types any of these words, we know they want Malay food
    "chinese": ["chinese", "cina", "oriental"],  # Chinese food keywords
    "indian": ["indian", "mamak", "india"],  # Indian food keywords
    "western": ["western", "cafe", "pasta", "burger"],  # Western food keywords
    "arab": ["arab", "middle eastern", "nasi arab"]  # Arab food keywords
}

# Maps various ways users might describe their budget to our price categories
PRICE_KEYWORDS = {
    "budget": ["cheap", "budget", "murah", "affordable", "low price"],  # Budget-friendly keywords
    "moderate": ["moderate", "medium", "sederhana", "reasonable"],  # Mid-range keywords
    "expensive": ["expensive", "mahal", "fancy", "high end", "premium"]  # Expensive keywords
}

# Maps food types users might search for
FOOD_TYPE_KEYWORDS = {
    "rice": ["rice", "nasi", "nasi campur", "nasi kandar"],  # Rice-based dishes
    "seafood": ["seafood", "fish", "prawn", "sotong", "ikan"],  # Seafood keywords
    "breakfast": ["breakfast", "sarapan", "morning", "roti canai"],  # Breakfast keywords
    "coffee": ["coffee", "kopi", "cafe", "latte"],  # Coffee/cafe keywords
    "chicken rice": ["chicken rice", "nasi ayam"],  # Chicken rice specific
    "roti canai": ["roti canai", "roti", "canai"],  # Roti canai specific
    "nasi kandar": ["nasi kandar", "kandar"]  # Nasi kandar specific
}

# ==================== AI FUNCTIONS ====================
# These are the core functions that make the chatbot "intelligent"

def extract_preferences(message):
    """
    Extract user preferences from their message.
    This function analyzes what the user typed and figures out what they want.
    
    Parameters:
        message (str): The text message from the user
        
    Returns:
        dict: A dictionary containing extracted preferences (cuisine, price, food_type, late_night)
    """
    msg_lower = message.lower()  # Convert message to lowercase for easier matching
    
    # Initialize empty preferences dictionary
    prefs = {"cuisine": None, "price": None, "food_type": None, "late_night": False}
    
    # Check if user mentioned a cuisine type
    # Loop through each cuisine category and its keywords
    for cuisine, keywords in CUISINE_KEYWORDS.items():
        # Check if any keyword appears in the user's message
        if any(kw in msg_lower for kw in keywords):
            prefs["cuisine"] = cuisine  # Save the cuisine preference
            break  # Stop after finding first match
    
    # Check if user mentioned a price preference
    for price, keywords in PRICE_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            prefs["price"] = price  # Save the price preference
            break
    
    # Check if user mentioned a specific food type
    for food, keywords in FOOD_TYPE_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            prefs["food_type"] = food  # Save the food type preference
            break
    
    # Check if user wants late-night options
    # Look for words related to late night or 24-hour service
    if any(word in msg_lower for word in ["late", "night", "midnight", "24", "malam", "lewat"]):
        prefs["late_night"] = True
    
    return prefs  # Return the extracted preferences

def find_restaurants(preferences):
    """
    Find restaurants matching user preferences using a scoring system.
    Each restaurant gets points based on how well it matches user preferences.
    
    Parameters:
        preferences (dict): Dictionary of user preferences from extract_preferences()
        
    Returns:
        list: List of up to 5 matching restaurants, sorted by relevance
    """
    matches = []  # List to store (restaurant, score) tuples
    
    # Loop through each restaurant in our database
    for restaurant in RESTAURANTS:
        score = 0  # Initialize score for this restaurant
        
        # Give 3 points if cuisine matches
        if preferences["cuisine"] and restaurant["cuisine"] == preferences["cuisine"]:
            score += 3
        
        # Give 2 points if price range matches
        if preferences["price"] and restaurant["price"] == preferences["price"]:
            score += 2
        
        # Give 2 points if the restaurant serves the requested food type
        if preferences["food_type"]:
            # Check if food_type appears in any of the restaurant's type list
            if any(preferences["food_type"] in t for t in restaurant["type"]):
                score += 2
        
        # Give 2 points if restaurant is open 24 hours and user wants late-night food
        if preferences["late_night"] and "24" in restaurant["hours"]:
            score += 2
        
        # Add restaurant to matches if it has any score OR if user didn't specify preferences
        if score > 0 or not any(preferences.values()):
            matches.append((restaurant, score))  # Store restaurant with its score
    
    # Sort matches by score (highest first), then by rating (highest first)
    matches.sort(key=lambda x: (x[1], x[0]["rating"]), reverse=True)
    
    # Return only the restaurants (not scores), limited to top 5
    return [m[0] for m in matches[:5]]

def format_restaurant(r):
    """
    Format restaurant information into nice-looking HTML for display.
    This creates the restaurant "card" that users see.
    
    Parameters:
        r (dict): A restaurant dictionary
        
    Returns:
        str: HTML-formatted string for displaying the restaurant
    """
    # Dictionary mapping price categories to emoji symbols
    price_emoji = {"budget": "💰", "moderate": "💰💰", "expensive": "💰💰💰"}
    
    # Create star rating visualization (e.g., 4.2 becomes ⭐⭐⭐⭐)
    stars = "⭐" * int(r['rating'])
    
    # Return formatted HTML string with restaurant details
    # The <div class="restaurant-card"> uses CSS styling defined later
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
    
    # Handle greetings
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

    # Handle help requests
    if any(h in msg_lower for h in ["help", "how", "what can"]):
        return """Here's how I can help you:

🍜 **Find by cuisine**: "Show me Chinese restaurants"
💵 **Find by budget**: "I want cheap food"
🍛 **Find by food type**: "Where can I get nasi kandar?"
🌙 **Late night options**: "What's open late at night?"
🔄 **Combinations**: "Cheap Malay food for breakfast"

Just ask naturally and I'll recommend the best spots!
"""

    # Extract user preferences and find matching restaurants
    prefs = extract_preferences(user_message)
    restaurants = find_restaurants(prefs)
    
    # If no matches found
    if not restaurants:
        return "Sorry, I couldn't find any restaurants matching your criteria. Try being less specific or ask for different options!"
    
    # Build response header based on number of results
    if len(restaurants) == 1:
        response = "### 🍴 Here is my recommendation:\n\n"
    else:
        response = f"### 🍴 Here are my top {len(restaurants)} recommendations:\n\n"
    
    # Display ALL restaurants found (no limit!)
    for r in restaurants:
        response += format_restaurant(r)
    
    # Add footer message
    if len(restaurants) == 1:
        response += "\n\n✅ _This is the best match for your preferences!_"
    else:
        response += f"\n\n✅ _Found {len(restaurants)} restaurant(s) matching your preferences. "
        response += "They're ranked by how well they match what you're looking for!_"
    
    return response

# ==================== STREAMLIT UI ====================
# This section creates the actual website interface

# Configure the page settings
st.set_page_config(
    page_title="Seri Iskandar Food Bot",  # Browser tab title
    page_icon="🍽️",  # Browser tab icon
    layout="centered",  # Center the content (alternative: "wide")
    initial_sidebar_state="expanded"  # Show sidebar by default
)

# PWA Support - Makes the website installable as a mobile app
# This adds metadata that browsers use to enable "Add to Home Screen"
st.markdown("""
<link rel="manifest" href="data:application/json;base64,ewogICJuYW1lIjogIlNlcmkgSXNrYW5kYXIgUmVzdGF1cmFudCBCb3QiLAogICJzaG9ydF9uYW1lIjogIkZvb2QgQm90IiwKICAiZGVzY3JpcHRpb24iOiAiQUkgUmVzdGF1cmFudCBSZWNvbW1lbmRlciBmb3IgU2VyaSBJc2thbmRhciIsCiAgInN0YXJ0X3VybCI6ICIvIiwKICAiZGlzcGxheSI6ICJzdGFuZGFsb25lIiwKICAiYmFja2dyb3VuZF9jb2xvciI6ICIjMWExYTJlIiwKICAidGhlbWVfY29sb3IiOiAiI2U5NDU2MCIsCiAgIm9yaWVudGF0aW9uIjogInBvcnRyYWl0IiwKICAiaWNvbnMiOiBbCiAgICB7CiAgICAgICJzcmMiOiAiaHR0cHM6Ly9pbWcuaWNvbnM4LmNvbS9jbG91ZHMvMTkyL3Jlc3RhdXJhbnQucG5nIiwKICAgICAgInNpemVzIjogIjE5MngxOTIiLAogICAgICAidHlwZSI6ICJpbWFnZS9wbmciCiAgICB9LAogICAgewogICAgICAic3JjIjogImh0dHBzOi8vaW1nLmljb25zOC5jb20vY2xvdWRzLzUxMi9yZXN0YXVyYW50LnBuZyIsCiAgICAgICJzaXplcyI6ICI1MTJ4NTEyIiwKICAgICAgInR5cGUiOiAiaW1hZ2UvcG5nIgogICAgfQogIF0KfQ==">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Food Bot">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#e94560">
<link rel="apple-touch-icon" href="https://img.icons8.com/clouds/192/restaurant.png">
""", unsafe_allow_html=True)

# Custom CSS Styling - This controls how everything looks
# CSS (Cascading Style Sheets) defines colors, sizes, fonts, etc.
st.markdown("""
<style>
    /* Main background with image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Dark overlay for readability */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.90);
        z-index: -1;
    }
    
    /* Title styling */
    h1 {
        color: #e94560 !important;
        text-align: center;
        font-size: 2.5rem !important;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
    }
    
    /* Subtitle */
    .stCaption {
        text-align: center;
        color: #a2d2ff !important;
        font-size: 1.1rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }
    
    /* Chat messages with blur effect */
    .stChatMessage {
        background-color: rgba(255,255,255,0.1) !important;
        border-radius: 15px;
        padding: 10px;
        margin: 5px 0;
        backdrop-filter: blur(15px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    
    /* Restaurant cards with glass effect */
    .restaurant-card {
        background: rgba(15, 52, 96, 0.75);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #e94560;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        backdrop-filter: blur(15px);
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
    
    /* Sidebar with glass effect */
    section[data-testid="stSidebar"] {
        background: rgba(15, 52, 96, 0.85) !important;
        backdrop-filter: blur(15px);
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #e94560 !important;
    }
    
    /* Chat input */
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

st.title("🍽️ Seri Iskandar Restaurant Bot")
st.caption("✨ Your AI assistant for finding great food in Seri Iskandar! ✨")

if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome = """Hello! 👋 I'm your **Seri Iskandar Restaurant Guide**!

Tell me what you're craving and I'll recommend the best spots. You can ask things like:
- "I want cheap Malay food"
- "Where can I get good nasi kandar?"
- "Any cafe open late night?"

**What are you in the mood for today?** 🍴"""
    st.session_state.messages.append({"role": "assistant", "content": welcome})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input("🔍 Ask me about restaurants..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)

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
    
