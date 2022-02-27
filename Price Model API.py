""""
Creating the API endpoint for the sale price prediction
- the following parameters will be required from the API endpoint entry ('Property Area', 'sale Date',
        'Acreage', 'LandValue', 'BuildingValue',
       'TotalValue', 'YearBuilt', 'Bedrooms', 'FullBath', 'HalfBath')
- the Api will return serialized json with the predicted sale price for the house details provide
"""

# import the required packages
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle as pk
import pandas as pd
import numpy as np



#create a flask instance for the API
sale_app = Flask(__name__)
sale_api = Api(sale_app)



# initialize the endpoint
if __name__ == "__main__":
    sale_app.run(debug=True) # ensure to remove the debugger when moving to production

