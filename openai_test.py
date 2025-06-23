import requests

response = requests.post("http://127.0.0.1:8000/speak", json={
    "text": "This is a test using OpenAI-style call."
})

if response.status_code == 200:
    with open("openai_test_output.wav", "wb") as f:
        f.write(response.content)
    print("✅ File saved as openai_test_output.wav")
else:
    print("❌ Request failed:", response.status_code)
    print(response.text)