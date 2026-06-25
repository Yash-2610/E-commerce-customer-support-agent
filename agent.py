from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from deep_translator import GoogleTranslator


load_dotenv()
API = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    api_key=API,
    model_name="llama-3.1-8b-instant",
    temperature=0
)
orders = {

    "1001": "Shipped",

    "1002": "Delivered",

    "1003": "Processing",

    "1004": "Cancelled"
}
RETURN_POLICY = """
Items can be returned within 30 days.

Product must be unused.

Refund processed within 5 business days.
"""
faq = {

    "laptop":
        "Laptop warranty is 1 year.",

    "mobile":
        "Mobile warranty is 6 months.",

    "shipping":
        "Standard shipping takes 3-5 days.",

    "refund":
        "Refunds take 5 business days."
}
def translate_to_english(text):
    try:
        return GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

    except Exception:
        return text
def detect_anger(text):

    text = text.lower()

    angry_words = [

        "angry",

        "worst",

        "bad",

        "fraud",

        "hate",

        "terrible",

        "useless",

        "disappointed",

        "complaint"
    ]

    for word in angry_words:

        if word in text:

            return True

    return False
def escalate_to_human():

    return """
Escalation Triggered.

A human support executive
will contact you shortly.
"""
def customer_support_bot(user_input):

    english_text = translate_to_english(
        user_input
    )

    if detect_anger(english_text):

        return escalate_to_human()

    text = english_text.lower()

    if any(
    word in text
    for word in [
        "track",
        "order",
        "status"
    ]
):

        for oid in orders:

            if oid in text:

                return f"""
Order {oid}

Status:
{orders[oid]}
"""

        return "Please provide order ID."

    if "return" in text:

        return RETURN_POLICY

    for key in faq:

        if key in text:

            return faq[key]

    prompt = f"""
You are an ecommerce support agent.

Customer:
{english_text}

Respond politely.
"""

    return llm.invoke(
        prompt
    ).content
