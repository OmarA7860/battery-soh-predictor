import google.generativeai as genai
import pickle
import numpy as np
import os
from config import GEMINI_API_KEY

# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3-pro-preview")

# Load linear regression model
model_path = os.path.join("results", "soh_model.pkl")

with open(model_path, "rb") as f:
    soh_model = pickle.load(f)

def predict_soh(cells):
    arr = np.array(cells).reshape(1, -1)
    return float(soh_model.predict(arr)[0])

def classify_battery(soh):
    return "The battery has a problem." if soh < 0.6 else "The battery is healthy."

def ask_gemini(question):
    response = model.generate_content(question)
    return response.text

print("Battery SOH Chatbot (Type 'exit' to quit)")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    if "check battery soh" in user.lower():
        print("Enter 21 cell SOH values:")
        cells = []
        for i in range(1, 22):
            v = float(input(f"U{i}: "))
            cells.append(v)

        soh = predict_soh(cells)
        status = classify_battery(soh)

        print(f"\nPredicted Pack SOH: {soh:.3f}")
        print(f"Status: {status}")

    else:
        answer = ask_gemini(user)
        print("\nAI:", answer)
