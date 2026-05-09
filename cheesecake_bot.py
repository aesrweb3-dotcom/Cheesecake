import tweepy
import random
import time
import json
import os
from datetime import datetime

# ============================================================
# X (Twitter) API Credentials
# ⚠️  IMPORTANT: Regenerate these keys at console.x.com ASAP
# since they were shared publicly. Then update them here.
# ============================================================
API_KEY = "c5czcJOEeg5BED6fsl5hcReqf"
API_KEY_SECRET = "x7dnhzwQ71wuVdJfiGaauWbflMq8MctkZR68q4g9zJ94HXQy91"
ACCESS_TOKEN = "1867897633798311936-EHazsxRQ4SUGr4FYPsEO6mrfZMg0PS"
ACCESS_TOKEN_SECRET = "5SnL9BTGHLf0zyYMv4kqiQo3lSs5cNCPYL1vB4tHasFkt"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAEIP9gEAAAAA3XzdW8h6xzvtR5J0NgWwHAlnQ4M%3DQzeCb282nk66PaVFvEXRGotmBzZAq6tsmd2DTlpypIbbFSWrxe"

# ============================================================
# 365+ Cheesecake Quotes
# ============================================================
QUOTES = [
    # Philosophy & Life
    "Life is uncertain. Eat the cheesecake first. 🍰",
    "A slice of cheesecake a day keeps the sadness away.",
    "In a world full of chaos, cheesecake is my constant.",
    "Cheesecake: proof that good things take time.",
    "The secret ingredient is always cream cheese.",
    "Some days you need a friend. Other days you need cheesecake. Most days, both.",
    "Cheesecake doesn't ask silly questions. Cheesecake understands.",
    "Be the cheesecake you wish to see in the world.",
    "Stressed spelled backwards is desserts. Coincidence? I think not.",
    "There are two kinds of people: those who love cheesecake, and those who are wrong.",
    "A balanced diet is a slice of cheesecake in each hand.",
    "Not all heroes wear capes. Some bake cheesecakes.",
    "Life is short. The cheesecake is calling.",
    "Happiness is homemade, especially when it involves cream cheese.",
    "Cheesecake: the answer to a question I haven't even asked yet.",
    "When in doubt, add more cream cheese.",
    "My love language is cheesecake.",
    "The best things in life are sweet, creamy, and on a biscuit base.",
    "Cheesecake is not just a dessert. It's a philosophy.",
    "Every slice tells a story. Make yours a good one.",

    # Motivation & Inspiration
    "Rise and shine — but first, cheesecake.",
    "Dream big. Bake bigger.",
    "You can't buy happiness, but you can buy cheesecake, which is basically the same thing.",
    "Today's goal: be as smooth as a perfectly set cheesecake.",
    "Keep calm and eat cheesecake.",
    "One bite at a time. That's how you finish a cheesecake and change your life.",
    "The only bad cheesecake is no cheesecake.",
    "Start each day with a grateful heart and a fork.",
    "You were born to do great things. Like bake cheesecake.",
    "Don't count the calories. Count the smiles.",
    "Good things come to those who bake.",
    "Cheesecake is always a good idea.",
    "Push through the hard days. Cheesecake awaits.",
    "Chase your dreams with the same urgency you chase the last slice.",
    "Make every bite count.",
    "You are one cheesecake away from a good mood.",
    "Do more of what makes you happy. Cheesecake qualifies.",
    "Today is a great day for cheesecake. So is tomorrow. And the day after.",
    "If you fall, land in a cheesecake.",
    "Work hard, stay humble, eat cheesecake.",

    # Humour
    "I followed my heart and it led me to the fridge.",
    "My doctor says I need to watch my eating. So I watch it go into my mouth.",
    "I'm on a seafood diet. I see cheesecake and I eat it.",
    "You had me at cheesecake.",
    "Relationship status: in a committed relationship with cheesecake.",
    "Will work for cheesecake.",
    "I don't stress eat. I strategically consume cheesecake.",
    "Cheesecake is cheaper than therapy and you don't need an appointment.",
    "My therapist told me to embrace my problems. So I hugged a cheesecake.",
    "Technically, cheesecake contains dairy and eggs, so it's practically a health food.",
    "Sorry, I can't. I'm busy with my cheesecake.",
    "Behind every great person is a great cheesecake.",
    "Some call it an obsession. I call it passion.",
    "I have never met a cheesecake I didn't like.",
    "Cheesecake: the original comfort food.",
    "I put the 'eat' in 'great'.",
    "My superpower? Finding room for cheesecake.",
    "Just here minding my own business and eating cheesecake.",
    "Plot twist: the cheesecake was better than expected.",
    "No drama. Just cheesecake.",

    # Seasons & Occasions
    "Nothing says 'I love you' like a homemade cheesecake.",
    "Valentine's Day? More like Cheesecake Day.",
    "Summer is better with a chilled cheesecake.",
    "Autumn vibes: cosy blanket, warm drink, pumpkin cheesecake.",
    "Winter comfort food? Cheesecake. Always cheesecake.",
    "Spring cleaning? Yes. Spring cheesecake? Absolutely.",
    "Monday mood: cheesecake required.",
    "Friday night sorted. Cheesecake in hand.",
    "Sunday baking is sacred. Cheesecake is the sabbath.",
    "New year, same love for cheesecake.",
    "Birthdays are just an excuse to eat cheesecake with candles.",
    "Christmas comes once a year. Cheesecake cravings come daily.",
    "Easter egg? No thanks. Cheesecake, please.",
    "Bank holiday weekend = cheesecake baking marathon.",
    "Celebrating something? Cheesecake. Commiserating? Also cheesecake.",

    # Flavours & Varieties
    "New York style cheesecake: dense, creamy, iconic. Like a great story.",
    "Strawberry cheesecake: a love affair in every bite.",
    "Lemon cheesecake: sunshine you can eat.",
    "Chocolate cheesecake: for when regular cheesecake isn't indulgent enough.",
    "Salted caramel cheesecake: the sweet-salty balance we all need in life.",
    "Blueberry cheesecake: tiny fruits doing mighty work.",
    "Biscoff cheesecake: where caramel biscuits become immortal.",
    "Raspberry cheesecake: tart enough to keep things interesting.",
    "Vanilla bean cheesecake: simple, elegant, unforgettable.",
    "Oreo cheesecake: when two legends collide.",
    "Matcha cheesecake: for when you want your dessert to feel sophisticated.",
    "Mango cheesecake: tropical dreams on a plate.",
    "Peanut butter cheesecake: if you know, you know.",
    "No-bake cheesecake: genius in its simplicity.",
    "Baked cheesecake: patience rewarded.",
    "Mini cheesecakes: all the joy, no sharing required.",
    "Cheesecake bars: because sometimes life needs to be portable.",
    "Swirled cheesecake: a masterpiece before the fork even touches it.",
    "Frozen cheesecake: summer's greatest invention.",
    "Cheesecake ice cream: two legends, one scoop.",

    # Baking & Craft
    "The biscuit base is the foundation of all great things.",
    "Room temperature cream cheese is not optional. It's a way of life.",
    "A water bath isn't just technique. It's an act of love.",
    "Patience is the secret ingredient in every great cheesecake.",
    "Don't rush the cooling process. Good things take time.",
    "The crack in a cheesecake is just a character flaw we choose to cover with fruit.",
    "Baking is love made edible.",
    "Every cheesecake is a little different. That's what makes them special.",
    "The best kitchens smell of cream cheese and possibility.",
    "A recipe is just a suggestion. Your instincts are the real chef.",
    "Bake with intention. Eat with joy.",
    "Perfecting a cheesecake recipe is a noble pursuit.",
    "There is artistry in a perfectly smooth top.",
    "A graham cracker crust is a promise of good things to come.",
    "The fridge door opened slowly. Inside, a perfect cheesecake waited.",

    # Wisdom & Wit
    "A cheesecake shared is a memory made.",
    "The secret to a long life might just be cheesecake.",
    "Eat dessert first. Life is short and unpredictable.",
    "Not all that is golden needs to be baked. But cheesecake does.",
    "You are what you eat. I am delicious.",
    "The road to happiness is paved with cream cheese.",
    "Life's greatest luxury is a quiet moment and a perfect slice.",
    "Find what sets your soul on fire. For me, it's an oven preheated to 160°C.",
    "Some people have guardian angels. I have a guardian cheesecake.",
    "There is no problem so large that cheesecake cannot make it slightly better.",
    "In my experience, people who don't like cheesecake cannot be trusted.",
    "A good cheesecake is a miracle with a biscuit base.",
    "The only thing better than a cheesecake is leftover cheesecake for breakfast.",
    "Age is just a number. Cheesecake is timeless.",
    "Wherever life takes you, take cheesecake.",
    "The world is your cheesecake. Take a big slice.",
    "Simplicity is the ultimate sophistication — except when there's cheesecake involved.",
    "Cheesecake doesn't judge. Cheesecake accepts.",
    "All you need is love. And cheesecake. Mostly cheesecake.",
    "Tomorrow is a new day. And a new opportunity for cheesecake.",

    # Random delights
    "Currently accepting cheesecake donations.",
    "Plot twist: the calories don't count if no one saw you eat it.",
    "If cheesecake is wrong, I don't want to be right.",
    "Thinking about cheesecake 24/7. No notes.",
    "Cheesecake appreciation post. You're welcome.",
    "Let them eat cheesecake.",
    "Cheesecake o'clock somewhere.",
    "The cheesecake is a lie. But this one is real.",
    "Sending good vibes and cheesecake energy your way.",
    "Today's mood: cheesecake.",
    "Everything I know about love I learned from cheesecake.",
    "Cheesecake: morally superior to most things.",
    "Why have a slice when you can have the whole thing?",
    "The cheesecake called. I answered.",
    "There's no WiFi in the kitchen, but I promise the connection is better.",
    "Cheesecake doesn't have feelings, but I have feelings about cheesecake.",
    "Eating cheesecake alone is called self-care.",
    "Cheesecake is my spirit animal.",
    "I didn't choose the cheesecake life. The cheesecake life chose me.",
    "Warning: may spontaneously talk about cheesecake.",
    "Fun fact: cheesecake makes everything better. Not a fact. A truth.",
    "My autobiography will be titled: One More Slice.",
    "Cheesecake is the original influencer.",
    "Just a person standing in front of a cheesecake, asking it to be infinite.",
    "Cheesecake theory: there's always room for one more bite.",
    "No cheesecake was harmed in the making of this post. It was eaten.",
    "A moment on the lips, forever in the memory.",
    "Dessert menu? Skip to cheesecake. Always cheesecake.",
    "The best conversations happen over cheesecake.",
    "I like big slices and I cannot lie.",
    "Eat well. Live well. Cheesecake often.",
    "Cheesecake: the treat that never disappoints.",
    "Making the world a better place, one slice at a time.",
    "Real talk: cheesecake heals.",
    "If you're reading this, have some cheesecake.",
    "Not to be dramatic, but cheesecake might be the meaning of life.",
    "Good morning. Have you considered cheesecake?",
    "Good night. Dream of cheesecake.",
    "Mid-week reminder: cheesecake exists and it's wonderful.",
    "Cheesecake doesn't care about your problems. It only has solutions.",
    "Hot take: cheesecake is better than cake. Cold take: cheesecake is better cold.",
    "There's a thin line between cheesecake enthusiast and cheesecake expert. I've crossed it.",
    "Some acquire wisdom with age. I acquired a great cheesecake recipe.",
    "Cheesecake: the great equaliser.",
    "You don't need a reason to eat cheesecake. But here are 365.",
    "Final thought: always save room for cheesecake. Final final thought: always save more room.",

    # More philosophical
    "The universe is vast and mysterious. But cheesecake makes sense.",
    "We are all just looking for something as reliable as cheesecake.",
    "If you can make a perfect cheesecake, you can do anything.",
    "Cheesecake taught me that the best things require care, time, and a good biscuit base.",
    "Like a great cheesecake, the best people are complex, layered, and slightly sweet.",
    "I measure time in cheesecakes baked and cheesecakes eaten.",
    "Every cheesecake is a small act of courage.",
    "Trust the process. The cheesecake knows what it's doing.",
    "A cheesecake never questions its purpose. It simply is.",
    "In the end, we will only regret the cheesecakes we didn't eat.",
    "Cheesecake is the punctuation mark at the end of a good meal.",
    "To know cheesecake is to know joy.",
    "The present moment always will have been. Especially this slice.",
    "Existence is fleeting. Cheesecake is also fleeting. Eat it now.",
    "The examined life is the one spent perfecting your cheesecake recipe.",

    # Even more
    "Cheesecake: the original slow food.",
    "There is a time for everything, and the time for cheesecake is always.",
    "No bad days when there's cheesecake.",
    "Treat yourself. You deserve a whole cheesecake.",
    "What would you attempt if you knew you couldn't fail? I'd bake a cheesecake.",
    "Cheesecake is the love language of bakers.",
    "Even on your worst day, cheesecake shows up.",
    "Cheesecake: dense with flavour, light on drama.",
    "The right cheesecake can change the trajectory of your day.",
    "Not everything needs to be complicated. Sometimes it's just cheesecake.",
    "Cheesecake is the punctuation that makes life's sentences complete.",
    "Name something better than a cold cheesecake on a warm day. I'll wait.",
    "Cheesecake is an act of generosity.",
    "Make it from scratch. Make it with love. Make it cheesecake.",
    "If it doesn't involve cheesecake, think about whether it's worth it.",
    "Cheesecake: the common ground we can all agree on.",
    "The world makes more sense after cheesecake.",
    "Cheesecake is the diplomat of desserts.",
    "Every bite of cheesecake is a micro-vacation.",
    "Your future self will thank you for the cheesecake.",
    "Chilled, sliced, perfect. Goals.",
    "Cheesecake: because you earned it.",
    "Do it for the cheesecake.",
    "Plot: person discovers cheesecake. Person never goes back.",
    "Cheesecake is the chapter in the book of life you read twice.",
    "The hero of every good story deserves a cheesecake ending.",
    "Cheesecake is a full-body experience.",
    "Never underestimate the power of a well-made cheesecake.",
    "Cheesecake is not a phase. It's a lifestyle.",
    "Let the cheesecake lead.",
    "Cheesecake: the soft landing at the end of a hard day.",
    "Dessert is not the end of the meal. It's the point of the meal.",
    "Cheesecake: making Tuesdays feel like Fridays since forever.",
    "No occasion needed. Cheesecake is its own occasion.",
    "If not now, when? Eat the cheesecake.",
]

# ============================================================
# State file to track which quotes have been used
# ============================================================
STATE_FILE = "cheesecake_bot_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"used_indices": [], "total_posted": 0}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def get_next_quote(state):
    used = set(state["used_indices"])
    available = [i for i in range(len(QUOTES)) if i not in used]

    # If all quotes used, reset
    if not available:
        print("All quotes used! Resetting pool...")
        state["used_indices"] = []
        available = list(range(len(QUOTES)))

    index = random.choice(available)
    state["used_indices"].append(index)
    return QUOTES[index], state

# ============================================================
# Post a tweet
# ============================================================
def post_tweet():
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_KEY_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    state = load_state()
    quote, state = get_next_quote(state)
    state["total_posted"] += 1

    try:
        response = client.create_tweet(text=quote)
        tweet_id = response.data["id"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ✅ Posted tweet #{state['total_posted']}: {quote}")
        print(f"   Tweet ID: {tweet_id}")
        save_state(state)
        return True
    except tweepy.TweepyException as e:
        print(f"❌ Error posting tweet: {e}")
        return False

# ============================================================
# Run modes
# ============================================================
def run_once():
    """Post a single tweet. Use this with a cron job or GitHub Actions."""
    print("🍰 Cheesecake Bot — posting one tweet...")
    post_tweet()

def run_scheduled(interval_hours=24):
    """Continuously post tweets at a set interval. For always-on servers."""
    print(f"🍰 Cheesecake Bot — running every {interval_hours} hours. Press Ctrl+C to stop.")
    while True:
        post_tweet()
        print(f"   Next post in {interval_hours} hour(s)...")
        time.sleep(interval_hours * 3600)

# ============================================================
# Entry point
# ============================================================
if __name__ == "__main__":
    # Change to run_scheduled(24) if running on a server 24/7
    run_once()
