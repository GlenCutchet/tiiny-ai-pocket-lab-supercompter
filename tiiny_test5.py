import sys
import subprocess

# Ensure openai is available
try:
    from openai import OpenAI
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI

# ========================================================
# SET THESE THREE CONFIGURATIONS BASED ON YOUR TIINY APP
# ========================================================
TIINY_IP = "172.28.167.161"   # The IP address from your error
TIINY_PORT = "80"           # <-- CHANGE THIS to your actual port number (e.g., 8000, 11434, etc.)
TIINY_API_KEY = "f4eb81ef-6e95-9ae8-ff8c-1dca7297e648"
MODEL_NAME = "Qwen/Qwen3.6-35B-A3B"
# ========================================================

# Construct the URL programmatically to prevent string errors
FINAL_URL = f"http://{TIINY_IP}:{TIINY_PORT}/v1"

print(f"Connecting to Tiiny Pocket Lab at: {FINAL_URL}...")

client = OpenAI(
    base_url=FINAL_URL,
    api_key=TIINY_API_KEY
)

try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant running locally."},
            {"role": "user", "content": "Hello! Confirm that you are running locally."}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    print("\n--- Success! Response received ---")
    print(response.choices.message.content.strip())
    print("----------------------------------\n")

except Exception as e:
    print("\n--- Connection Error ---")
    print(f"Could not connect to the local server. Error details:\n{e}")