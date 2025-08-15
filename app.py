# Import the libraries we need
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# --- Your GNews API Key ---
# ⚠ IMPORTANT: Paste the actual key you got from gnews.io here!
API_KEY = st.secrets["GNEWS_API_KEY"]

# --- Page Configuration ---
st.set_page_config(
    page_title="Live News & Events Tracker",
    page_icon="🌍",
    layout="wide",
)

# --- Function to fetch news from the API ---
def get_news(topic):
    """Fetches news articles for a given topic from the GNews API."""
    url = f"https://gnews.io/api/v4/search?q={topic}&lang=en&country=us&max=10&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "articles" in data:
            return data["articles"]
        else:
            st.error("Could not fetch news. The API might be down or your key is invalid.")
            return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# --- Main Dashboard ---
st.title("🌍 Live Global News & Events Tracker")
st.markdown("This dashboard fetches and analyzes live news headlines from around the world.")

# --- Sidebar for user input ---
st.sidebar.header("Search & Filter")
# Let the user enter a topic, with a default value
topic = st.sidebar.text_input("Enter a topic to track (e.g., 'AI', 'elections', 'spaceX'):", "technology")

# --- Auto-refresh control ---
if st.sidebar.checkbox("Enable Auto-Refresh (every 5 minutes)", True):
    refresh_interval = 300  # seconds
else:
    refresh_interval = -1

# --- Main content area ---
# Create a placeholder for the live data
data_placeholder = st.empty()

# --- Main loop to fetch and display data ---
while True:
    articles = get_news(topic)

    if articles:
        # Convert the list of articles into a pandas DataFrame
        df = pd.DataFrame(articles)

        # --- Data Cleaning and Preparation ---
        df['source_name'] = df['source'].apply(lambda x: x['name'])
        # A simple way to guess the country from the source name
        df['country'] = df['source_name'].apply(lambda x: x.split(' ')[-1]) 

        # --- Display in the placeholder ---
        with data_placeholder.container():
            st.header(f"Tracking Topic: '{topic.capitalize()}'")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("News Hotspots by Source")
                country_counts = df['country'].value_counts().reset_index()
                country_counts.columns = ['country', 'count']

                fig = px.choropleth(country_counts, 
                                    locations="country", 
                                    locationmode='country names',
                                    color="count",
                                    hover_name="country",
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title="Article Count by Source Country")
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.subheader("Top News Sources")
                source_counts = df['source_name'].value_counts().head(10)
                st.bar_chart(source_counts)

            st.subheader("Latest Headlines")
            for article in articles:
                st.write(f"[{article['title']}]({article['url']})")
                st.write(f"{article['source']['name']} - {pd.to_datetime(article['publishedAt']).strftime('%Y-%m-%d %H:%M')}")
                st.markdown("---")

    else:
        with data_placeholder.container():
            st.warning("No articles found for this topic. Try another one.")

    # --- Auto-refresh logic ---
    if refresh_interval > 0:
        time.sleep(refresh_interval)
    else:
        break # Exit the loop if auto-refresh is disabled