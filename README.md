# LAB - Class 16
## Project: Serverless Functions
### Author: KP Gomez

### Description 
This application uses the restcountries API (https://restcountries.com/#rest-countries) to find either the capital of a country  and/or name of country per the 
capital specified. 

Deployed Site: https://vercel.com/kp-gomezs-projects/capital-finder-kp-gomez/Ak3Px5u4b1UZzjCYvvDjvhpn8DVk

To find the capital city of a country, change country name. Example below

https://capital-finder-kp-gomez.vercel.app/api/countries?country=laos

![name of country example]()

To find the name of country according to its capital, change capital name

https://capital-finder-kp-gomez.vercel.app/api/countries?capital=bangkok

Change both to see both the capital and the name of a country

https://capital-finder-kp-gomez.vercel.app/api/countries?country=thailand&capital=bangkok


### Links and Resources
- [Class 16 Demo](https://github.com/codefellows/seattle-code-python-401n8/tree/main/class-16/in-class-demo/api)

### Setup
#### Create and Activate Virtual Enviroment

`python3.11 -m venv .venv`

`source .venv/bin/activate`

#### Install Required Packages

`pip install -r requirements.txt`

#### How to initialize/run your application (where applicable)
*Run command* 

`python countries.py`

#### Tests
*skipped*