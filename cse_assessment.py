
#mport the modules

import requests
import json
import sqlite3
import os
from pandas import DataFrame

#Define the Api Key, Define the endpoint define the header.

API_KEY =  "API KEY GOES HERE"
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization' : 'bearer %s' % API_KEY}



def query_an_endpoint(a, b, c, d):

    root_url = "https://api.yelp.com/v3/businesses/search"

    # Definethe parameters

    PARAMETERS = {'term': a, 'limit' : b, 'radius' : c, 'location' : d}

    # Make a request to yelp API

    response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

    # convert json string to a dictionary

    business_data = response.json()

    # remove unicode from response.
    try:
        r = requests.get(ENDPOINT)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return json.dumps(business_data)



def insert_in_db(json_object):

    conn = sqlite3.connect('yelp_restaurants.db')
    c = conn.cursor()

    c.execute('CREATE TABLE RESTAURANTS (restaurant_id number, center text, total text, businesses text, display_phone number, phone number, business_id number, is_closed text, zip_code number, location text, country text, address2 text, address3 text, state text, address1 text)')
    conn.commit()

    restaurants = response
        

    df = DataFrame(Restaurants, columns= ['restaurant_id', 'center', 'total', 'businesses', 'display_phone', 'phone', 'business_id', 'is_closed', 'zip_code', 'location', 'country', 'address2', 'address3', 'state', 'address1'])
    df.to_sql('RESTAURANTS', conn, if_exists='replace', index = False)
 
    c.execute('''  
    SELECT * FROM RESTAURANTS
          ''')

    for row in c.fetchall():
        print (row)

####

response = query_an_endpoint('coffee', 1, 1000, 'Oakland')


insert_in_db(response)
