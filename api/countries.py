from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path  # http://localhost:8000/capital-finder?country=thailand&capital=bangkok
        print('url:', path)  # /capital-finder?country=thailand&capital=bangkok

        url_components = parse.urlsplit(path)
        print('url_components:', url_components)  # SplitResult(scheme='', netloc='', path='/capital-finder',
        # query='country=thailand&capital=bangkok', fragment='')

        query_string_list = parse.parse_qsl(url_components.query)
        print('qsl:', query_string_list)  # [('country', 'thailand'), ('capital', 'bangkok')]

        query = dict(query_string_list)
        print('dictionary:', query)  # {'country': 'thailand', 'capital': 'bangkok'}

        name = query.get('country')
        print('country:', name)  # country: thailand

        capital = query.get('capital')
        print('capital:', capital)  # capital: bangkok

        message = ''

        if query['country']:
            url = f'https://restcountries.com/v3.1/name/{name}'
            response = requests.get(url)
            data = response.json()
            capital = data[0]['capital'][0]
            message += f'The capital of {name.capitalize()} is {capital.capitalize()}\n'

        if query['capital']:
            url = f'https://restcountries.com/v3.1/capital/{capital}'
            response = requests.get(url)
            data = response.json()
            country = data[0]['name']['common']
            message += f'{capital.capitalize()} is the capital of {country.capitalize()}\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, handler)
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
