import sys
import subprocess

# Automatically install openai if it's missing from this specific Python path
try:
    from openai import OpenAI
except ModuleNotFoundError:
    print("OpenAI module missing. Installing it directly to this Python environment...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI
    print("Installation successful!\n")

# 1. Configure the Tiiny Pocket Lab local server settings
TIINY_BASE_URL = "http://openai.api.tiiny/v1" # Replace XXXX with your actual port number
TIINY_API_KEY = "f4eb81ef-6e95-9ae8-ff8c-1dca7297e648"   # Replace with your generated key
MODEL_NAME = "Qwen/Qwen3.6-35B-A3B"                          # Replace with the model loaded on your device

# 2. Initialize the client
client = OpenAI(
    base_url=TIINY_BASE_URL,
    api_key=TIINY_API_KEY
)

print(f"Connecting to Tiiny Pocket Lab at: {TIINY_BASE_URL}...")

try:
    # 3. Send a test chat completion request
    response = client.chat.completions.create(
    model="Qwen/Qwen3.6-35B-A3B",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about coding."}
    ],
    # Ensure this isn't set to 0 or an incredibly small value
    max_tokens=512 
    )
    
    print("\n--- Success! Response received ---")
    print(response.choices[0].message.content.strip())
    print("----------------------------------\n")

except Exception as e:
    print("\n--- Connection Error ---")
    print(f"Could not connect to the local server. Error details:\n{e}")