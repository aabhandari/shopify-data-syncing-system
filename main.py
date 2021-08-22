import psycopg2
import math
import pandas as pd
import json
from pandas.io.json import json_normalize
import requests
from sqlalchemy import create_engine


# GET / admin/api/2020-10/customers/count.json
#counting customers, api has 250 records in one page, in the future if we will have more than 250 records, in order to launch loop
JSON_count = requests.get(
    ' https://username:password@store-name.myshopify.com/admin/api/{API-version}/count.json')
content = json.dumps(JSON_count.json(), indent=4, sort_keys=True)
nested = json.loads(content)
JSON_count2 = nested.get("count")
n = math.ceil(JSON_count2/250)

while True:
    df = pd.DataFrame()


    Jsondata = requests.get(
        ' https://username:password@store-name.myshopify.com/admin/api/{API-version}/customers.json')
    #gives data
    if 'json' in Jsondata.headers.get('Content-Type'):
        content = json.dumps(Jsondata.json(), indent=4, sort_keys=True)#as json is not in simplified form so, dump and load

        nested = json.loads(content)

        orders = pd.json_normalize(nested["customers"])#converting into data frame
        # df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])
        df = pd.DataFrame(orders, columns=['id', 'email', 'created_at','first_name','last_name','orders_count'])
    else:
        print('Response content is not in JSON format.')
        js = 'spam'


    print(df.head())

    engine = create_engine(
        "postgresql://postgres:username:password@hostname/database")

    # df.to_sql('products', engine, if_exists='replace')

    df.to_sql('customers', engine, if_exists='replace')#converting into sql by pandas




