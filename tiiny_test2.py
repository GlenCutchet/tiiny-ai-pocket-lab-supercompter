import requests

# Point to the static IP address of the Tiiny Pocket Lab
TIINY_IP = "172.28.167.161"
URL = f"http://{TIINY_IP}:80/v1/chat/completions" # Adjust port/endpoint based on your running model agent

payload = {
    "model": "llama3",
    "messages": [{"role": "user", "content": "Hello Tiiny Lab!"}]
}

try:
    response = requests.post(URL, json=payload, timeout=5)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("Connection error:", e)