import streamlit as st

def display_news(news_data):
    if news_data:
        st.header("Latest News Articles")
        for index, article in enumerate(news_data, start=1):
            st.subheader(f"{index}. {article['title']}")
            st.write(f"**Source:** {article['source']}")
            st.write(article['summary'])
            st.markdown("---")
    else:
        st.warning("No news articles available. Please try again.")