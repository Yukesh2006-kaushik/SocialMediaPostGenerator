def generate_image_prompt(keyword, style="aesthetic"):
    base_prompt = f"An image representing {keyword}, visually rich, ideal for social media, high-quality, detailed."

    styles = {
        "aesthetic": "modern aesthetic, clean, minimal colors, Instagram-friendly",
        "futuristic": "cyberpunk, sci-fi theme, glowing lights, high contrast",
        "cartoon": "2D cartoon style, fun, playful, colorful drawing",
        "realistic": "photo-realistic, natural lighting, cinematic look",
        "3D render": "high-quality 3D rendered image, depth and lighting effects"
    }

    selected_style = styles.get(style, "")
    return f"{base_prompt} Style: {selected_style}"
