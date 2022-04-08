# Nashville Housing price prediction
In this project, I made use of Python to build a machine learning model for the prediction of house sale price in Nashville Area in the United State of America 

## Requirements:
- IDE with python interpreter.
- Numpy package
- Panda package
- SKlearn
-Pickle

## Installation
If you don't have a working IDE kindly follow this [link](https://docs.anaconda.com/anaconda/install/windows/) to install anaconda on your machine which has all the needed requirements to run the python script.

## Usage
- Import the pickle lib to your Jupyter notebook
```
import pandas as pd
import pickle as pk
import numpy as np

```

-Load the sale price ML model

```
with open("SalePriceModel.pkl", "rb") as file: 
    model = pk.load(file)

```
- Prepare the model Function
```
 
    def get_price(Area, saledate_float, Acreage, LandValue,
       BuildingValue, TotalValue, YearBuilt, Bedrooms, FullBath,
       HalfBath):
    
    input_stuct = {"Area" : Area, "saledate_float" : saledate_float, "Acreage" : Acreage, "LandValue": LandValue ,
       "BuildingValue" : BuildingValue, "TotalValue" : TotalValue, "YearBuilt" : YearBuilt, "Bedrooms" : Bedrooms, "FullBath" : FullBath,
       "HalfBath" : HalfBath}
    
    input_data = pd.DataFrame(data = input_stuct, index = [0], columns = ['Area', 'saledate_float', 'Acreage', 'LandValue',
       'BuildingValue', 'TotalValue', 'YearBuilt', 'Bedrooms', 'FullBath',
       'HalfBath'])
    
    
    SalePrice = reg.predict(input_data.to_numpy())
    
    return "Predicted Sale Price is : {} US Dollars".format(SalePrice[0][0])

```
- Run your prediction 
```
get_price(Area, saledate_float, Acreage, LandValue,
       BuildingValue, TotalValue, YearBuilt, Bedrooms, FullBath,
       HalfBath)
```



## Authors and acknowledgment
- Victor Oguche


