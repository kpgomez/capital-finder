from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        print('url:', s)

        url_components = parse.urlsplit(s)
        print('url_components:', url_components)

        query_string_list = parse.parse_qsl(url_components.query)
        print('qsl:', query_string_list)

        query = dict(query_string_list)
        print('dictionary:', query)

        country = query.get('country')
        capital = query.get('capital')

        message = ''

        if query[country]:
            message += f'The capital of {country.capitalize()} is {capital.capitalize()}'
        if query[capital]:
            message += f'{capital.capitalize()} is the capital of {country.capitalize()}'

        url = 'https://restcountries.com/v3.1/name/'
        url_2 = 'https://restcountries.com/v3.1/capital/'

        response = requests.get(url+country)
        response_2 = requests.get(url_2+capital)
        data = response.json()
        query_items = []


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())