import os
from openai import OpenAI

# 1. Configure the Tiiny Pocket Lab local server settings
# Replace the URL and API key with the values provided in your TiinyOS panel
TIINY_BASE_URL = "http://openai.api.tiiny/v1"  # Replace XXXX with your actual port number
TIINY_API_KEY = "f4eb81ef-6e95-9ae8-ff8c-1dca7297e648"   # Replace with your generated key
MODEL_NAME = "Qwen/Qwen3.6-35B-A3B"                          # Replace with the exact name of the model loaded on your device

# 2. Initialize the client
client = OpenAI(
    base_url=TIINY_BASE_URL,
    api_key=TIINY_API_KEY
)

print(f"Connecting to Tiiny Pocket Lab at: {TIINY_BASE_URL}...")

try:
    # 3. Send a test chat completion request
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant running locally."},
            {"role": "user", "content": "Hello! Confirm that you are running locally on the Tiiny Pocket Lab hardware."}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    # 4. Print the response text
    print("\n--- Success! Response received ---")
    print(response.choices[0].message.content.strip())
    print("----------------------------------\n")

except Exception as e:
    print("\n--- Connection Error ---")
    print(f"Could not connect to the local server. Error details:\n{e}")
    print("\nTroubleshooting tips:")
    print("1. Verify the Tiiny Pocket Lab is plugged into power and your PC via USB-C.")
    print("2. Ensure the TiinyOS desktop app is open and running.")
    print("3. Check that the port number in the URL matches the app's settings exactly.")
    print("4. Confirm the target model is downloaded and successfully loaded in TiinyOS.")