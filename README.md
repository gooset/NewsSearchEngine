# News Search Application

The News Search Application is a web-based search engine that allows users to search for news articles from various sources. It utilizes Elasticsearch as the underlying search engine and Flask as the web framework.

## Features

- Crawl: The application uses the `newspaper` framework to crawl news articles from predefined sources. It retrieves the article URL, title, text, publish date, and source.

- Indexing: The crawled articles are indexed into Elasticsearch, allowing efficient searching and retrieval of articles based on user queries.

- Search: Users can search for articles using keywords. The application performs a full-text search in Elasticsearch and returns relevant articles based on the query.

- Pagination: The search results are paginated for better user experience. The application uses the `flask_paginate` library to implement pagination.


## Setup and Usage

1. Install Dependencies: Ensure that you have Python installed. Install the required dependencies by running `pip install -r requirements.txt`.

2. Configure Elasticsearch: Make sure you have Elasticsearch installed and running. Adjust the Elasticsearch connection settings in the code to match your Elasticsearch configuration.

3. Crawl Articles: Run the crawl script to collect news articles from the predefined sources. The script will crawl the articles, extract relevant information, and index them into Elasticsearch.

4. Start the Application: Run `python3 run.py` to start the Flask web server. Access the application in your browser at `http://localhost:5000`.

5. Search Articles: Use the search bar to enter keywords and retrieve relevant articles. Use the advanced search options to further refine your search.

6. Pagination: Navigate through the search results using the pagination links at the bottom of the page.

## Future Improvements

- User Authentication: Implement user authentication and authorization to allow personalized features such as saving articles or creating custom search preferences.

- Real-time Updates: Add functionality to automatically crawl and index new articles periodically to ensure the search engine is up to date with the latest news.

- User Interface Enhancements: Improve the user interface with a responsive design, additional search filters, and interactive features.

- Advanced Search: The application provides advanced search options such as filtering articles by date range or specific sources.

## Contributions

Contributions to the News Search Application are welcome! If you have any ideas for new features, bug fixes, or general improvements, feel free to submit a pull request.

## License

The News Search Application is open-source and released under the [MIT License](LICENSE).

