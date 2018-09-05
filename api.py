from flask import Flask, jsonify, abort, request, make_response, url_for
import cleaners
import scrapers
from synopsis import elements

app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/api/v1.0/food/<string:search_query>', methods = ['GET'])
def get_task(search_query):
    route1 = elements[0]
    cleaned_query = route1['inputs']['clean'](search_query)
    output = [scrapers.search_scrape(route1['url'],
                                    [cleaned_query],
                                    route1['outputs'][i]['xpath'],
                                    route1['outputs'][i]['li'])
              for output in route1['outputs']]

    #for output in outputs:

    return jsonify( { 'food': outputs } )

if __name__ == '__main__':
    app.run(debug = True)
