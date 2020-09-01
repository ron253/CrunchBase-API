import requests
import pandas as pd
import csv
from time import sleep

list_names = [ ]
facebook = [ ]
linkedin = [ ]
twitter = [ ]
person_name = [ ]
url = 'https://api.crunchbase.com/v3.1/odm-people?'

def read_csv(urls):
    with open('file path') as file:
        read_file = csv.reader(file)
        for row in read_file:
            if (row[0] != 'people-11-22-2019') and (row[0] !='Full name'):
                add_list = list_names.append(row[0])

def api_function():
    for names in list_names:
        param = {
            'name': names,
            'user_key': API_KEY
        }
        get_request = requests.get(url, params= param)
        get_data = get_request.json()

        for items in get_data['data']['items']:
            first_name = items['properties']['first_name']
            last_name = items['properties']['last_name']
            full_name = first_name + ' ' + last_name
            person_name.append(full_name)
            facebook.append(items['properties']['facebook_url'])
            twitter.append(items['properties']['twitter_url'])
            linkedin.append(items['properties']['linkedin_url'])
            sleep(1)


def convert_to_csv():
    dictionary_names = {
        'Santa Clara University Alumnus': person_name,
        'Facebook': facebook,
        'Linkedin': linkedin,
        'Twitter': twitter
    }

    convert_dictionary = pd.DataFrame(dictionary_names)
    to_csv = convert_dictionary.to_csv(r'/Applications/University Relations.csv')

read_csv(url)
api_function()
convert_to_csv()
