import requests

def get_news(location, category, api_key, shown_news_titles):
    url = f"https://newsapi.org/v2/everything?q={location}&category={category}&apiKey={api_key}&language=en"
    response = requests.get(url)
    news_data = response.json()
    
    if news_data.get('status') == 'ok' and news_data.get('articles'):
        news = [article for article in news_data['articles'] if article['title'] not in shown_news_titles]
        return news
    return []
