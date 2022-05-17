import requests
import pandas
import os
import types
from functools import partial, wraps
import warnings
import json

import pyEX as p
#p.Client(api_token=None, version='v1', api_limit=5)
TOKEN = "pk_90b4d43cc11c4f059efa31db98eaf48c"

json_string = p.stats(token=TOKEN, version="stable", filter="", format="json")
with open('data.json', 'w') as outfile:
    json.dump(json_string, outfile)

with open('data.json', 'w') as outfile:
    outfile.write(json_string)


#print(k)
print(json_string.length)
def hello():
    print("hello")
