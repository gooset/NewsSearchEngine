import newspaper
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

def crawl_and_index_articles(url, source_name, from_date, to_date):
    crawler = newspaper.build(url, memoize_articles=False)

    for article in crawler.articles:
        try:
            # Download and parse the article
            article.download()
            article.parse()

            # Check if the article publish date is within the specified date range
            publish_date = article.publish_date
            if publish_date is None or publish_date < from_date or publish_date > to_date:
                continue

            # Check if the article already exists in Elasticsearch
            exists = es.exists(index='articles', id=article.url)
            if exists:
                continue

            # Extract article information
            doc = {
                'url': article.url,
                'title': article.title,
                'text': article.text,
                'publish_date': publish_date,
                'source': source_name
            }

            # Index the article in Elasticsearch
            es.index(index='articles', body=doc)

            print(f"Article indexed: {article.url}")
        except Exception as e:
            print(f"Error while processing article: {article.url}. Error: {str(e)}")


# Define the news sources and their URLs
news_sources = [
    {'name': 'The Guardian', 'url': 'https://www.theguardian.com'},
    {'name': 'Le Figaro', 'url': 'https://www.lefigaro.fr'},
    # Add more news sources as needed
]

# Specify the date range to search for new articles
from_date = datetime(2021, 6, 1)  # Start date
to_date = datetime(2021, 6, 30)  # End date

# Crawl and index articles for each news source
for source in news_sources:
    source_name = source['name']
    url = source['url']

    crawl_and_index_articles(url, source_name, from_date, to_date)

