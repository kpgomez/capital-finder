from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests # most popular python library


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path  # http://localhost:8000/capital-finder?name=thailand
        print('url:', path)  # /capital-finder?name=thailand

        url_components = parse.urlsplit(path)
        print('url_components:', url_components)  # SplitResult(scheme='', netloc='', path='/capital-finder',
        # query='name=thailand', fragment='')

        query_string_list = parse.parse_qsl(url_components.query)
        print('qsl:', query_string_list)  # [('name', 'thailand')]

        query = dict(query_string_list)
        print('dictionary:', query)  # {'name': 'thailand'}

        # name = query.get('name')
        # print('name:', name)  # name: thailand

        name = query.get('country')
        print('country:', name)  # country: None

        # name = country
        # print('name: ', name)

        capital = query.get('capital')  # None
        print('capital:', capital)
        #
        message = ''
        #
        #
        url_country = f'https://restcountries.com/v3.1/name/{name}'
        url_capital = f'https://restcountries.com/v3.1/capital/{capital}'
        #
        # country_response = requests.get(url_country)
        capital_response = requests.get(url_capital)
        # country_data = country_response.json()
        capital_data = capital_response.json()

        # query_items = []

        # country_capital = (country_data[0]['capital'])
        # print('capital:', country_capital)

        capital_country = (capital_data[0]['name']['common'])

        # if query['country']:
        #     message += f'The capital of {name.capitalize()} is {country_capital[0].capitalize()}'
        if query['capital']:
            message += f'{capital.capitalize()} is the capital of {capital_country.capitalize()}'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, handler)
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()