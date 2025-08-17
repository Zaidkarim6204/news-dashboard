# 🌍 Live Global News & Events Tracker

A dynamic web application that fetches and visualizes live news headlines from around the world using the GNews API.

**[Live Demo Link](https://news-dashboard-gbfxoy46ttutjpevyrws7k.streamlit.app/)**



## About The Project

This dashboard allows users to track topics in real-time by fetching the latest articles from a global news API. It processes the data to display news hotspots on an interactive world map and identifies the top media sources reporting on the topic. This project demonstrates skills in API integration, data visualization, and building interactive web applications with Streamlit.

---

### Key Features

* *Real-time News:* Fetches live headlines via the GNews REST API.
* *Interactive World Map:* Visualizes the geographic distribution of news sources using Plotly.
* *Data Analysis:* Displays a bar chart of the top media sources for the tracked topic.
* *Custom Search:* Allows users to input any topic to track.
* *Secure API Key Handling:* Uses Streamlit's secrets management to protect credentials.

---

### Technologies Used

* *Language:* Python
* *Framework:* Streamlit
* *Libraries:* Pandas, Plotly Express, Requests

---

### Setup and Local Installation

To run this project locally, follow these steps:

1.  *Clone the repository:*
    bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    
2.  *Create a Conda environment:*
    bash
    conda create -n news_env python=3.9
    conda activate news_env
    
3.  *Install dependencies:*
    bash
    pip install -r requirements.txt
    
4.  *Add your API key:*
    * Create a folder named .streamlit in the project directory.
    * Inside this folder, create a file named secrets.toml.
    * Add your GNews API key to this file:
        toml
        GNEWS_API_KEY = "your_actual_api_key_goes_here"
        
5.  *Run the app:*
    bash
    streamlit run app.py
    
