"""WPI Frontiers 2026 - AI College Counselor Chatbot.

Portfolio-safe version of the course prototype created by Ajay Goverdhan
and Bruno Diaz Morales during WPI Frontiers 2026.

Public-repository changes are documented in docs/CHANGES_FROM_ORIGINAL.md.
"""

import base64
import json
import os
from io import BytesIO

import streamlit as st
from openai import OpenAI
from PIL import Image


st.set_page_config(page_title="College Counselor Bot")


def get_api_key():
    """Read the API key from an environment variable instead of source code."""
    return os.getenv("OPENAI_API_KEY")


OPENAI_API_KEY = get_api_key()

if not OPENAI_API_KEY:
    st.error(
        "OPENAI_API_KEY is not set. Set it as an environment variable before "
        "starting the application."
    )
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)


def load_student_profile(filename="student_profile.json"):
    """Load an optional local student profile."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        st.warning("student_profile.json is not valid JSON, so it was ignored.")
        return {}


student_profile = load_student_profile()

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a college counselor who answers questions about college admissions "
        "with clear, supportive, and informative guidance. First identify what the "
        "student is asking, then provide useful information aligned with the question. "
        "Do not write essays, personal statements, application responses, or other "
        "submission content for students. Instead, explain how students can approach "
        "those materials themselves. If the question is unrelated to college admissions, "
        "explain that your main purpose is college-admissions guidance and provide only "
        "a brief response. Limit college recommendations to the United States and Canada "
        "whenever possible. If there is not enough information for a reliable answer, "
        "say what additional details would help. Encourage students to verify important "
        "admissions, financial-aid, accessibility, deadline, and program information on "
        "official college websites or with the appropriate college office."
    ),
}


def build_initial_messages():
    """Build the starting conversation with optional student-profile context."""
    messages = [SYSTEM_MESSAGE]

    if student_profile:
        messages.append(
            {
                "role": "system",
                "content": (
                    "Here is the student's profile. Use it only when relevant to the "
                    "student's question, and do not mention it unless it helps answer "
                    "the request.\n\n"
                    + json.dumps(student_profile, indent=2)
                ),
            }
        )

    return messages


def generate_image(image_description):
    """Generate an image for an explicit !image request."""
    response = client.images.generate(
        model="gpt-image-2",
        prompt=image_description,
        size="1024x1024",
        quality="low",
        output_format="png",
    )
    image_bytes = base64.b64decode(response.data[0].b64_json)
    return Image.open(BytesIO(image_bytes))


def main():
    st.title("Welcome to the College Counseling Chatbot")
    st.caption(
        "Course prototype: use as a support tool, not as a replacement for a school "
        "counselor or official college information."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = build_initial_messages()

    prompt = st.chat_input("Ask any college-related question")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        if prompt.lower().startswith("!image"):
            image_description = prompt[len("!image"):].strip()
            if not image_description:
                st.warning("Add an image description after !image.")
            else:
                try:
                    generated_img = generate_image(image_description)
                    buffered = BytesIO()
                    generated_img.save(buffered, format="PNG")
                    img_str = base64.b64encode(buffered.getvalue()).decode("ascii")
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "Here is the generated image.",
                            "image": img_str,
                        }
                    )
                except Exception as exc:
                    st.error(f"Image generation failed: {exc}")
        else:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.messages,
                )
                msg = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": msg})
            except Exception as exc:
                st.error(f"Something went wrong: {exc}")

    for message in st.session_state.messages:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if "image" in message:
                buffered = BytesIO(base64.b64decode(message["image"]))
                st.image(Image.open(buffered))

    if st.button("Clear Conversation"):
        st.session_state.messages = build_initial_messages()
        st.rerun()


if __name__ == "__main__":
    main()
