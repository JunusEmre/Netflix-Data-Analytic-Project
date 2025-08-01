import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv("Netflix.csv")  # Change this to your actual file name if different

# Clean missing values
df['country'] = df['country'].fillna("Unknown")
df['listed_in'] = df['listed_in'].fillna("")

# Streamlit app layout
st.title("🎬 Netflix Explorer Dashboard")

# List all genres
genre_list = sorted(set([genre for sublist in df['listed_in'].str.split(', ') for genre in sublist]))
selected_genre = st.selectbox("Choose a Genre", genre_list)

# List countries
selected_country = st.selectbox("Choose a Country", df['country'].unique())

# Filter the data
filtered = df[df['listed_in'].str.contains(selected_genre) & (df['country'] == selected_country)]

# Show results
st.write(f"Found {len(filtered)} results")
st.dataframe(filtered[['title', 'type', 'rating', 'release_year']])