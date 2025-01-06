import argparse
import joblib
import pandas as pd

# Load the pre-trained logistic regression model
model = joblib.load('C:/salman/ML/car price dredection/model.pkl')


# Create an argument parser
parser = argparse.ArgumentParser(description="car price perdection")

# Add the --value argument to accept a data record
parser.add_argument('--Year', type=int, required=True, help='Year')
parser.add_argument('--Present_Price', type=float, required=True, help='Present_Price')
parser.add_argument('--Kms_Driven', type=float, required=True, help='Kms_Driven')
parser.add_argument('--Fuel_Type', type=str, required=True, help=	'Fuel_Type')
parser.add_argument('--Seller_Type', type=str, required=True, help='Seller_Type')
parser.add_argument('--Transmission', type=str, required=True, help='Transmission')
parser.add_argument('--Owner', type=int, required=True, help='Owner')

# Parse the command-line arguments
args = parser.parse_args()


# Parse the data record as a list of floats
data_list =[[args.Year,args.Present_Price,args.Kms_Driven,args.Fuel_Type,args.Seller_Type,args.Transmission,args.Owner]]

#convert to dataset
data_list=pd.DataFrame(data_list,columns=(['Year','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']))


# encoding "Fuel_Type" Column
data_list.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

# encoding "Seller_Type" Column
data_list.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# encoding "Transmission" Column
data_list.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)


#predict
pred=model.predict(data_list)[0]

print(f'car price is {pred}')
