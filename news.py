import requests

def get_news(location, category, api_key):
    url = f"https://newsapi.org/v2/top-headlines?q={location}&category={category}&apiKey={api_key}"
    response = requests.get(url)
    try:
        response.raise_for_status()
        data = response.json()
        articles = data['articles']
        if not articles:
            return None
        news = []
        for article in articles:
            news.append({
                "title": article['title'],
                "url": article['url']
            })
        return news
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"Other error occurred: {err}"
