import google.generativeai as genai
import os

# Thay bằng API Key thật của bạn
GOOGLE_API_KEY = "AIzaSyANJ7xL4ZnG-2NPVBAoY6mbYv5I_7dkfHw" 
genai.configure(api_key=GOOGLE_API_KEY)

print("Danh sách các model khả dụng:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)