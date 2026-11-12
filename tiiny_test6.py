import sys
import subprocess

try:
    from openai import OpenAI
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI

# ========================================================
# 1. CLEAN CONFIGURATION (No http:// inside these quotes)
# ========================================================
RAW_IP = "172.28.167.16"     # Pure IP only, do not add http:// here
TIINY_PORT = "80"           # Change this to 8000 or 11434 depending on your TiinyOS app
TIINY_API_KEY = "f4eb81ef-6e95-9ae8-ff8c-1dca7297e648"
MODEL_NAME = "Qwen/Qwen3.6-35B-A3B"

# Automatically clean the IP just in case there's hidden text
CLEAN_IP = RAW_IP.replace("http://", "").replace("https://", "").strip()
FINAL_URL = f"http://{CLEAN_IP}:{TIINY_PORT}/v1"

print(f"Connecting to Tiiny Pocket Lab at: {FINAL_URL}...\n")

# 2. Initialize client
client = OpenAI(
    base_url=FINAL_URL,
    api_key=TIINY_API_KEY
)

try:
    # 3. Test connection
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": "Hello! Confirm that you are running locally."}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    print("--- Success! Response received ---")
    print(response.choices.message.content.strip())
    print("----------------------------------\n")

except Exception as e:
    print("--- Connection Error ---")
    print(f"Could not connect to the local server. Error details:\n{e}")