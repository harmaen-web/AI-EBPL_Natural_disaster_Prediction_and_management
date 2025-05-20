# %% [markdown]
# <a href="https://colab.research.google.com/github/harmaen-web/demo/blob/main/phase_5.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%


 #File: project.py
#Project:AI-EBPL Natural disaster Prediction and management
#Author: Harmaen Zama
#Description: provides a basic natural disaster awareness system with data visualization, user interaction, and model evaluation features.



# === PART 1: FOLIUM MAP VISUALIZATION ===
import folium

# Create map centered globally
m = folium.Map(location=[20, 0], zoom_start=2)

# Sample disaster data
disasters = [
    {"location": [34.0522, -118.2437], "type": "Earthquake", "severity": "High", "region": "A"},
    {"location": [40.7128, -74.0060], "type": "Flood", "severity": "Moderate", "region": "B"},
    {"location": [28.7041, 77.1025], "type": "Cyclone", "severity": "Low", "region": "C"},
]

# Add markers to map
for disaster in disasters:
    popup_text = f"Type: {disaster['type']}<br>Severity: {disaster['severity']}<br>Region: {disaster['region']}"
    folium.Marker(disaster["location"], popup=popup_text, icon=folium.Icon(color='red')).add_to(m)

# Save the map (you can upload this file to GitHub)
map_file = "disaster_map.html"
m.save(map_file)
print(f"✅ Disaster map saved as {map_file}")
print("📢 You can upload this file to GitHub and link to it from README.md!")

# === PART 2: CHATBOT INTERFACE ===
print("\n💬 Natural Disaster Assistant Chatbot")
print("Type your question below. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip().upper()

    if user_input == "EXIT":
        print("Bot: Goodbye! Stay safe. 👋")
        break
    elif "FLOOD" in user_input:
        print("Bot: 🌊 Flood Tip: Move to higher ground immediately.")
        print("📍 Nearest Shelter: Riverside Community Center")
        print("🧠 Moral: Help others and don’t panic.")
    elif "PREDICT" in user_input:
        print("\nBot: 🔍 Disaster Prediction:")
        print("- Earthquake Risk: Moderate (Region A)")
        print("- Flood Risk: High (Region B)")
        print("📢 Stay alert and follow official updates.\n")
    else:
        print("Bot: I'm here to help with disaster information and tips!")

# === PART 3: PREDICTION METRICS ===
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Example prediction data
y_true = [0, 1, 1]  # 0 = No Flood, 1 = Flood
y_pred = [1, 1, 1]  # Model predicted all Flood

# Classification report
print("\n📊 Model Evaluation Report:\n")
print(classification_report(y_true, y_pred, zero_division=0))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Flood", "Flood"])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix - Flood Prediction")
plt.show()
m

# %%



