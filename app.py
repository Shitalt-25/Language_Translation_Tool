import streamlit as st
from deep_translator import GoogleTranslator
from datetime import datetime

# ----------------------------
# Function to Translate Text
# ----------------------------
def translate_text(text, source_lang, target_lang):

    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)

    return translated


# ----------------------------
# Save Translation History
# ----------------------------
def save_history(original, translated):

    with open(
        "history.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\nDate & Time : {datetime.now()}\n"
        )

        file.write(
            f"Original Text : {original}\n"
        )

        file.write(
            f"Translated Text : {translated}\n"
        )

        file.write(
            "-" * 50 + "\n"
        )


# ----------------------------
# Read History
# ----------------------------
def show_history():

    try:

        with open(
            "history.txt",
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except:

        return "No Translation History Available."


# ----------------------------
# Streamlit Settings
# ----------------------------
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# ----------------------------
# Title
# ----------------------------
st.title("🌍 Language Translation Tool")

st.write(
    "Translate text from one language to another."
)

st.write(
    "Developed by Tarde Shital"
)

st.markdown("---")

# ----------------------------
# Languages
# ----------------------------
languages = {

    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"

}

# ----------------------------
# Input Text
# ----------------------------
user_text = st.text_area(
    "Enter Text",
    height=150
)

st.write(
    f"Character Count : {len(user_text)}"
)

source_language = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# ----------------------------
# Buttons
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    translate_btn = st.button("Translate")

with col2:
    clear_btn = st.button("Clear")

# ----------------------------
# Translation
# ----------------------------
if translate_btn:

    if user_text.strip() == "":

        st.warning(
            "Please enter some text."
        )

    else:

        translated_text = translate_text(

            user_text,

            languages[source_language],

            languages[target_language]

        )

        st.success(
            "Translation Successful"
        )

        st.subheader(
            "Translated Text"
        )

        st.write(
            translated_text
        )

        save_history(
            user_text,
            translated_text
        )

# ----------------------------
# Clear
# ----------------------------
if clear_btn:
    st.rerun()

# ----------------------------
# History
# ----------------------------
st.markdown("---")

if st.checkbox(
    "Show Translation History"
):

    st.text_area(

        "History",

        show_history(),

        height=250

    )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.caption(
    "AI Internship Project - Language Translation Tool"
)