import streamlit as st
from caption_generator import generate_caption, get_hashtags, get_emojis
from image_prompt import generate_image_prompt

# Page Config
st.set_page_config(page_title="Social Media Post Generator", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    /* Gradient background - Blue to Purple */
    .stApp {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        padding: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.2em;
        text-shadow: 1px 1px 4px #000;
    }

    p {
        text-align: center;
        font-size: 1.2em;
        color: #fdfdfd;
        margin-bottom: 2em;
    }

    /* 3D Button Style */
    button[kind="primary"] {
        background: linear-gradient(145deg, #9f9fff, #6c63ff);
        border: none;
        border-radius: 12px;
        color: #fff;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 24px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    button[kind="primary"]:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }

    .stSuccess {
        background-color: #dff3ff;
        padding: 10px;
        border-left: 5px solid #007bff;
        border-radius: 10px;
    }

    .stCodeBlock {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("📱 Social Media Post & Caption Generator")
st.markdown("Generate catchy **captions**, relevant **hashtags**, fun **emojis**, and **image prompts** with a beautiful UI.")

# Input Section
keyword = st.text_input("🔤 Enter a keyword or theme:", placeholder="e.g. fitness, coding, travel")
platform = st.selectbox("📱 Choose platform:", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("🗣️ Choose a tone/style:", ["motivational", "funny", "professional", "friendly", "default"])
style = st.selectbox("🎨 Choose an image style:", ["aesthetic", "futuristic", "cartoon", "realistic", "3D render"])

# Generate Button
if st.button("🚀 Generate Post"):
    if not keyword.strip():
        st.warning("Please enter a keyword.")
    else:
        # Generating all elements
        caption = generate_caption(keyword, tone)
        hashtags = get_hashtags(keyword)
        emojis = get_emojis(keyword)
        image_prompt = generate_image_prompt(keyword, style)

        # Platform-Specific Post Format
        if platform == "Instagram":
            final_post = f"{caption}\n{''.join(emojis)}\n{' '.join(hashtags)}"
        elif platform == "LinkedIn":
            final_post = f"{caption}\n\nHashtags: {' '.join(hashtags)}"
        elif platform == "Twitter":
            final_post = f"{caption} {' '.join(emojis)} {' '.join(hashtags)}"
        else:
            final_post = caption

        # Display Results
        st.subheader("📝 Generated Post:")
        st.code(final_post, language="markdown")

        st.subheader("🖼 Image Prompt (for AI tools):")
        st.success(image_prompt)

        # Download Buttons
        st.download_button(
            label="📥 Download Caption as .txt",
            data=final_post,
            file_name=f"{keyword}_{platform}_caption.txt",
            mime="text/plain"
        )

        output_text = f"📸 Caption:\n{caption}\n\n🏷️ Hashtags:\n{hashtags}\n\n😄 Emojis:\n{emojis}\n\n🖼️ Image Prompt:\n{image_prompt}"

        st.download_button(
            label="📥 Download Full Post as .txt",
            data=output_text,
            file_name=f"{keyword}_post.txt",
            mime="text/plain"
        )
