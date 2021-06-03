from flask import Flask, flash, redirect, render_template, request, url_for
from flask_paginate import Pagination, get_page_args
from requests import exceptions as ex_requests
from news_app import app
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'search' in request.args:
        query = request.args.get('search')

        if not query:
            flash('Please enter a search query.', 'warning')
            return redirect(url_for('home'))

        try:
            res = es.search(index="anso-search", body={"query": {"match": {"text": {"query": f"{query}"}}}})
        except ex_requests.RequestException:
            flash('An error occurred during the search. Please try again later.', 'danger')
            return redirect(url_for('home'))

        total = res['hits']['total']['value']
        docs = [hit["_source"] for hit in res['hits']['hits']]

        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

        return render_template('search.html',
                               search_results=docs,
                               page=page,
                               per_page=per_page,
                               pagination=pagination,
                               len=len)
    else:
        flash('Invalid request. Please try again.', 'danger')
        return redirect(url_for('home'))
