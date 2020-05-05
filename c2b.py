import requests
import keys
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token


def register_url():
  my_access_token=generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
  headers = {"Authorization": "Bearer %s" % my_access_token}
  request = { "ShortCode": keys.shortcode,
      "ResponseType": "Completed",
      "ConfirmationURL": "https://fullstack.com/confirmation",
      "ValidationURL": "https://fullstack.com/validation_url"}
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
#register_url()

def simulate_transaction():
  
  my_access_token=generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % my_access_token}
  request = { "ShortCode":keys.shortcode,
    "CommandID":"CustomerPayBillOnline",#could be CustomerBuyGoodsOnline
    "Amount":"2",
    "Msisdn": keys.test_msisdn,
    "BillRefNumber":"12345" }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
simulate_transaction()