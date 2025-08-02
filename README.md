# 💸 Expense Tracker App (Python + Streamlit)

This is a simple expense tracking web app built using **Streamlit** in **Google Colab**. It allows users to manage their daily expenses through a clean, interactive interface.

---

## ✨ Features
- Add new expense entries (Date, Category, Amount, Note)
- View all expenses in a dynamic table
- Calculate total expenses
- Display a pie chart for category-wise spending
- Simple, minimal design using Streamlit

---

## 🛠 Tech Stack
- Python 3
- Streamlit
- Pandas
- Plotly (for charts)
- Ngrok (for tunneling from Colab)

---

## 🎥 Demo Video
[Click here to watch the demo video](https://colab.research.google.com/drive/1xaqj9HaFtQBm8nlzNxeLao0IAcXFq8Qs?usp=drive_link)  

---

## 🧪 Run the App in Google Colab

1. Open this Colab Notebook (if public):  
   `[Add Colab link if you make it public]`

2. Run these setup steps:
```python
!pip install streamlit pyngrok pandas plotly
!ngrok config add-authtoken YOUR_AUTHTOKEN
3.Launch the app:
from pyngrok import ngrok
public_url = ngrok.connect(8501, "http")
!streamlit run streamlit_app.py &>/dev/null &
📁 Files Included
streamlit_app.py – Main app logic

README.md – This file
📌 Note
This project is built in Python as a logic + UI prototype for an iOS-style expense app. It reflects my understanding of app structure, clean UI, and interactive UX — and can be easily translated to Swift/SwiftUI in a native iOS environment.
