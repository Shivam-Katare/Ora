from streamlit import sidebar, session_state

def render_sidebar():
    sidebar.title("News Reader Agent")
    sidebar.header("Select News Category")
    
    categories = {
        "1": "Latest",
        "2": "Politics",
        "3": "Sports",
        "4": "Business",
        "5": "Entertainment",
        "6": "India",
        "7": "World",
        "8": "Lifestyle"
    }
    
    category_choice = sidebar.selectbox("Choose a category:", list(categories.values()))
    
    if sidebar.button("Get News"):
        selected_category = [key for key, value in categories.items() if value == category_choice][0]
        session_state.selected_category = selected_category
        session_state.news_data = None  # Reset news data on new request
        session_state.audio_file = None  # Reset audio file on new request

    return session_state.selected_category if 'selected_category' in session_state else None