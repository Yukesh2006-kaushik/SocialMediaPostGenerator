import random

HASHTAG_DB = {
    "fitness": ["#FitLife", "#NoPainNoGain", "#WorkoutMotivation"],
    "travel": ["#Wanderlust", "#TravelGoals", "#AdventureTime"],
    "coding": ["#DeveloperLife", "#CodeNewbie", "#TechTalk"],
    "motivation": ["#StayPositive", "#DailyInspo", "#MindsetMatters"]
}

EMOJI_DB = {
    "fitness": ["💪", "🏋️‍♂️", "🔥"],
    "travel": ["✈️", "🌍", "📸"],
    "coding": ["💻", "🧠", "🚀"],
    "motivation": ["🌟", "💯", "✨"]
}

def generate_caption(keyword, tone="default"):
    templates = {
        "motivational": [
            f"Push yourself — {keyword} is the key to success! 💪",
            f"Believe in the power of {keyword}. You’ve got this! 🔥",
            f"{keyword.capitalize()} turns dreams into reality. ✨"
        ],
        "funny": [
            f"I tried {keyword} once… now I’m an expert! 😎",
            f"{keyword}? Oh, you mean my part-time job 😂",
            f"Warning: Excessive {keyword} ahead 🚧"
        ],
        "professional": [
            f"Exploring the future of {keyword} in today’s world.",
            f"{keyword.capitalize()} strategy is essential in the modern workspace.",
            f"Here’s how {keyword} is reshaping industries."
        ],
        "friendly": [
            f"Hey friends! Let’s talk about {keyword} today 😊",
            f"{keyword.capitalize()} can be fun if you do it right! 💬",
            f"Just sharing a little about {keyword} — hope it helps! 🤗"
        ],
        "default": [
            f"Unlock your potential with {keyword}!",
            f"Today is a great day to talk about {keyword}.",
            f"Let’s dive into the world of {keyword}.",
            f"{keyword.capitalize()} isn't just a word — it's a lifestyle."
        ]
    }

    selected_templates = templates.get(tone, templates["default"])
    return random.choice(selected_templates)


def get_hashtags(keyword):
    return HASHTAG_DB.get(keyword.lower(), ["#trending", "#inspo", "#socialmedia"])

def get_emojis(keyword):
    return EMOJI_DB.get(keyword.lower(), ["🔥", "📢", "📱"])
