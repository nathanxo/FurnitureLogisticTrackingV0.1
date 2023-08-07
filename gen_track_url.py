import requests
import random
import string
import sys
import json

#def randomString(stringLength=10):
 #   return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLength))


#def genTrackURL(customer_order_number):
    # Passed in from the AJAX call. 
    ###customer_order_number = "TOBS22272"#TODOREMOVELINE

 #   url = 'https://www.go2stream.net/API/oauth'
  #  payload = "grant_type=client_credentials&client_id=<"CHANGE">&client_secret=<"CHANGE">"
   # headers = {
    #    'content-type': 'application/x-www-form-urlencoded',
     #   'cache-control': "no-cache",
      #  'Stream-Nonce': randomString(30)
   # }
    #response = requests.post(url, data=payload, headers=headers)

    #if response.status_code != 200:
        # Order Not Found, Show warning to user
     #   return dict(status_code=response.status_code, response=str(response), tracking_url='')
        
    # Read the response
    #json_response = response.json()
 #   access_token = json_response.get("access_token", "")

#    if access_token == "":
        # Order Not Found, Show warning to user
 #       return dict(status_code=405, response='no access_token returned', tracking_url='')
  #      sys.exit()
        

   # url = 'https://www.go2stream.net/API/orders/status/'+customer_order_number
    #headers = {
     #   'Accept': "application/json",
      #  'Stream-Nonce': randomString(30),
       # 'Stream-Party': "<"CHANGE">",
        #'Authorization': "Bearer "+access_token,
        #'cache-control': "no-cache",
    #}

    #responseOrder = requests.get(url, headers=headers)

 #   if responseOrder.status_code != 200 and responseOrder.status_code != 422:
        # Order Not Found, Show warning to user
  #      print("No track 1: ")
   #     return dict(status_code=responseOrder.status_code, response=json.load(responseOrder.json()), tracking_url='')
        #sys.exit()
        
    # Read the response
    #json_response_order = responseOrder.json()
    #response_body = json_response_order.get("response", "")
#    tracking_url = response_body.get("trackingURL", "")

 #   if tracking_url == "":
        # Order Not Found, Show warning to user
  #      print("No track 2: ")
   #     return dict(status_code=404, response=response_body, tracking_url='')
        #sys.exit()
        

    # Pass this back to the AJAX then you can redirect the user via Javascript
    #print("GOT TRACKING URL: ", tracking_url)
    #return dict(status_code=200, tracking_url=tracking_url, response='all_ok')
    #sys.exit()
    

