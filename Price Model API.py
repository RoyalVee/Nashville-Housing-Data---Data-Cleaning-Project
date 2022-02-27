""""
Creating the API endpoint for the sale price prediction
- the following parameters will be required from the API endpoint entry ('Property Area', 'sale Date',
        'Acreage', 'LandValue', 'BuildingValue',
       'TotalValue', 'YearBuilt', 'Bedrooms', 'FullBath', 'HalfBath')
- the Api will return serialized json with the predicted sale price for the house details provided
"""

# import the required packages
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle as pk
import pandas as pd
import numpy as np


#get price function
def get_price(Area, saledate_float, Acreage, LandValue,
       BuildingValue, TotalValue, YearBuilt, Bedrooms, FullBath,
       HalfBath):
    """"
    This function loads the machine learning model and predict the sale price
    :arg Area, sale date, Acreage, LandValue,
       BuildingValue, TotalValue, YearBuilt, Bedrooms, FullBath,
       HalfBath
    :return sale price predicted"""
    input_dict = {"Area" : Area, "saledate_float" : saledate_float, "Acreage" : Acreage, "LandValue": LandValue ,
       "BuildingValue" : BuildingValue, "TotalValue" : TotalValue, "YearBuilt" : YearBuilt, "Bedrooms" : Bedrooms, "FullBath" : FullBath,
       "HalfBath" : HalfBath}
    input_data = pd.DataFrame(data = input_dict, index = [0], columns = ['Area', 'saledate_float', 'Acreage', 'LandValue',
       'BuildingValue', 'TotalValue', 'YearBuilt', 'Bedrooms', 'FullBath',
       'HalfBath'])

    # load Machine learning model
    with open("SalePriceModel.pkl", "rb") as file:
        reg = pk.load(file)

    # predict sale price for input provided
    SalePrice = reg.predict(input_data.to_numpy())

    return SalePrice

#create a flask instance for the API
sale_app = Flask(__name__)
sale_api = Api(sale_app)

#create a request parser for collecting the required parameter for sale price prediction.
house_details_arg = reqparse.RequestParser()
house_details_arg.add_argument('Property Area', type = int, help = "Property Area is required", required = True)
house_details_arg.add_argument('Sale Date', type = int, help = "Sale Date is required", required = True)
house_details_arg.add_argument('Acreage', type = int, help = "Acreage is required", required = True)
house_details_arg.add_argument('LandValue', type = int, help = "LandValue is required", required = True)
house_details_arg.add_argument('BuildingValue', type = int, help = "BuildingValue is required", required = True)
house_details_arg.add_argument('TotalValue', type = int, help = "TotalValue is required", required = True)
house_details_arg.add_argument('YearBuilt', type = int, help = "YearBuilt is required", required = True)
house_details_arg.add_argument('Bedrooms', type = int, help = "Bedrooms is required", required = True)
house_details_arg.add_argument('FullBath', type = int, help = "FullBath is required", required = True)
house_details_arg.add_argument('HalfBath', type = int, help = "HalfBath is required", required = True)


# Create the Price model resource
class sale_price(Resource):
    """"Create the price model methods """
    def get(self):
        args = house_details_arg.parse_args()

        Property_Area = args['Property Area']
        Sale_Date = args['Sale Date']
        Acreage = args['Acreage']
        LandValue = args['LandValue']
        BuildingValue = args['BuildingValue']
        TotalValue = args['TotalValue']
        YearBuilt = args['YearBuilt']
        Bedrooms = args['Bedrooms']
        FullBath = args['FullBath']
        HalfBath = args['HalfBath']

        pred_sale_price = get_price(Area= Property_Area, saledate_float= Sale_Date, Acreage= Acreage, LandValue=LandValue,
                               BuildingValue=BuildingValue, TotalValue=TotalValue, YearBuilt=YearBuilt, Bedrooms=Bedrooms,
                               FullBath= FullBath, HalfBath=HalfBath)

        return {"Sale Price" : Property_Area}


# Register the resource in the sale api
sale_api.add_resource(sale_price, "/sale_prediction")

# initialize the endpoint
if __name__ == "__main__":
    sale_app.run(debug=True) # ensure to remove the debugger when moving to production

