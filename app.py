# Import the Streamlit library - this is what creates the web interface
import streamlit as st

# ==================== RESTAURANT DATABASE ====================
# This is our main data source - a list of dictionaries containing restaurant information
# Each restaurant is a dictionary with details like name, cuisine, price, etc.
RESTAURANTS = [
    {
        "name": "Restoran Nasi Kandar Simpang Empat",  # Restaurant name
        "cuisine": "malay",  # Type of cuisine (used for filtering)
        "type": ["nasi kandar", "rice"],  # Food types offered (can match multiple keywords)
        "price": "budget",  # Price range: budget, moderate, or expensive
        "location": "Bandar Seri Iskandar",  # Where the restaurant is located
        "rating": 4.2,  # Rating out of 5 stars
        "hours": "24 hours",  # Operating hours
        "description": "Popular nasi kandar spot with variety of curries and dishes."  # Brief description
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
    """
    Generate the chatbot's response based on what the user typed.
    This is the main "brain" function that decides what to say.
    
    Parameters:
        user_message (str): The message typed by the user
        
    Returns:
        str: The chatbot's response text
    """
    msg_lower = user_message.lower()  # Convert to lowercase for easier checking
    
    # Check if user is greeting the bot
    greetings = ["hi", "hello", "hey", "assalamualaikum", "hai"]
    if any(g in msg_lower for g in greetings):
        # Return welcome message with instructions
        return """Hello! 👋 Welcome to the Seri Iskandar Restaurant Recommender!

I can help you find great places to eat. Just tell me:
- What cuisine you prefer (Malay, Chinese, Indian, Western, Arab)
- Your budget (cheap, moderate, expensive)
- Type of food (rice, seafood, breakfast, coffee, etc.)
- If you need late-night options

For example: "I want cheap Malay food" or "Any good cafe nearby?"
"""

    # Check if user is asking for help
    if any(h in msg_lower for h in ["help", "how", "what can"]):
        # Return help instructions
        return """Here's how I can help you:

🍜 **Find by cuisine**: "Show me Chinese restaurants"
💵 **Find by budget**: "I want cheap food"
🍛 **Find by food type**: "Where can I get nasi kandar?"
🌙 **Late night options**: "What's open late at night?"
🔄 **Combinations**: "Cheap Malay food for breakfast"

Just ask naturally and I'll recommend the best spots!
"""

    # If not greeting or help, treat as a restaurant search query
    prefs = extract_preferences(user_message)  # Extract what user wants
    restaurants = find_restaurants(prefs)  # Find matching restaurants
    
    # If no restaurants found, apologize
    if not restaurants:
        return "Sorry, I couldn't find any restaurants matching your criteria. Try being less specific or ask for different options!"
    
    # Build response with restaurant recommendations
    response = "### 🍴 Here are my recommendations:\n\n"
    
    # Show top 3 restaurants
    for r in restaurants[:3]:
        response += format_restaurant(r)  # Add formatted restaurant card
    
    # If more than 3 matches, tell user there are more options
    if len(restaurants) > 3:
        response += f"\n\n_I found {len(restaurants)} matches. Want to see more options?_"
    
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
    
