# SwiggyProject
The objective is to build a recommendation system based on restaurant data provided in a CSV file.

It suggests restaurants based on user preferences such as city, cuisine, rating, and price.


📌 Features

✅ Data Cleaning – Handles missing values, formats ratings & prices.

✅ One-Hot Encoding – Encodes categorical features (city, cuisine, etc.).

✅ Pickled Encoder (encoder.pkl) – Saves & reuses the trained encoder.

✅ Recommendation Engine – Uses Cosine Similarity to suggest restaurants.

✅ Streamlit UI – Interactive app for selecting user preferences.

✅ Mapping – Recommendations are displayed from the cleaned dataset (human-readable).

📂 Project Structure

📦 restaurant-recommender

├── cleaned_data.csv       # Cleaned dataset (numerical + categorical)

├── encoder.pkl            # Saved OneHotEncoder

├── app.py                 # Streamlit app (main entry point)

├── preprocessing.py       # Data cleaning + encoding script

├── requirements.txt       # Dependencies

└── README.md              # Documentation
