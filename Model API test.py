# import request package

import requests

Base = "http://127.0.0.1:5000/"

# sample values used are for testing

response  = requests.get(Base + "sale_prediction" , {"Property Area" : 10, "Sale Date" : 11, "Acreage" : 12, "LandValue": 13 ,
       "BuildingValue" : 14, "TotalValue" : 15, "YearBuilt" : 16, "Bedrooms" : 17, "FullBath" : 18,
       "HalfBath" : 19})
print(response.json())