from openai import OpenAI
from openai import RateLimitError
from dotenv import load_dotenv
import os
import sys

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY is missing. Put it in a .env file or set it as an environment variable.")

client = OpenAI(api_key=key)

def run(text: str) -> str:
    resp = client.responses.create(
        model="gpt-5",
        input=(
            "You are an internal ops assistant. "
            "Summarize the text in 5 bullets, then extract action items as a checklist.\n\n"
            f"TEXT:\n{text}"
        ),
    )
    return resp.output_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python summarize.py "your text here"')
        sys.exit(1)

    try:
        print(run(sys.argv[1]))
    except RateLimitError as e:
        # This often happens when billing/quota isn't configured on the API account.
        print("ERROR: OpenAI API quota/billing is not available for this key/account yet.")
        print("To run this demo, configure billing/credits in the OpenAI Developer Platform and retry.")
        print(f"Details: {e}")
