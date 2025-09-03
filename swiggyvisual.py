# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ---- Load Data ----
try:
    encoded = pd.read_csv("encoded_data.csv")
    cleaned = pd.read_csv("cleaned_data.csv")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ---- App Config ----
st.set_page_config(page_title="🍴 Restaurant Recommendation System", layout="wide")
st.title("🍴 Restaurant Recommendation System")
st.markdown("Find restaurants similar to your preferences!")

# ---- Sidebar Filters ----
st.sidebar.header("🔍 Filter Preferences")

# Dropdowns
if "city" in cleaned.columns:
    city_choice = st.sidebar.selectbox("Select City", sorted(cleaned['city'].dropna().unique()))
else:
    city_choice = None

if "cuisine" in cleaned.columns:
    cuisine_choice = st.sidebar.selectbox("Select Cuisine", sorted(cleaned['cuisine'].dropna().unique()))
else:
    cuisine_choice = None

# Sliders
rating_min = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.5, 0.1)
price_max = st.sidebar.number_input("Maximum Price (₹)", min_value=100, max_value=5000, value=1000, step=50)

# Restaurant input for similarity
restaurant_input = st.text_input("Enter a Restaurant Name (optional for similarity search):")

# ---- Recommendation Function ----
def recommend_restaurants(restaurant_name=None, top_n=5):
    if restaurant_name:
        matches = cleaned[cleaned['name'].str.lower() == restaurant_name.lower()]
        if matches.empty:
            return None
        idx = matches.index[0]

        sim_scores = cosine_similarity([encoded.iloc[idx]], encoded)[0]
        top_indices = np.argsort(sim_scores)[::-1][1:top_n+1]

        results = cleaned.iloc[top_indices].copy()
        results['similarity_score'] = sim_scores[top_indices]
        return results[['name','city','cuisine','rating','cost','similarity_score']]
    return None

# ---- Always show filtered dataset ----
st.subheader("📋 Filtered Restaurants")
if city_choice and cuisine_choice:
    filtered_data = cleaned[
        (cleaned['city'] == city_choice) &
        (cleaned['cuisine'] == cuisine_choice) &
        (cleaned['rating'] >= rating_min) &
        (cleaned['cost'] <= price_max)
    ]
else:
    filtered_data = cleaned.copy()

st.dataframe(filtered_data[['name','city','cuisine','rating','cost']].reset_index(drop=True))

# ---- Show Recommendations if user enters a restaurant ----
if restaurant_input:
    recs = recommend_restaurants(restaurant_input, top_n=5)
    if recs is not None:
        st.subheader(f"🍽 Recommendations similar to *{restaurant_input}*")
        st.dataframe(recs.reset_index(drop=True))
    else:
        st.warning(f"❌ Restaurant '{restaurant_input}' not found. Please try another name.")
