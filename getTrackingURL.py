import requests
import random
import string
import sys
import json

#def randomString(stringLength=10):
#	return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLength))

#Passed in from the AJAX call.
#customerOrderNo = 'TOBS22272' #trackingNoInput

#url = 'https://www.go2stream.net/API/oauth'
#payload = "grant_type=client_credentials&client_id=<"CHANGE">&client_secret=<"CHANGE">"
#headers = {
#    'content-type': 'application/x-www-form-urlencoded',
#    'cache-control': "no-cache",
#    'Stream-Nonce': randomString(30)
#}
#response = requests.post(url, data=payload, headers=headers)

#if response.status_code != 200:
	# Order Not Found, Show warning to user
#	print("NO RESPONSE", "Got Status Code: ", response.status_code, "GotResp:", response)
#	sys.exit()
    
# Read the response
#json_response = response.json()
#access_token = json_response.get("access_token", "")

#if access_token == "":
	# Order Not Found, Show warning to user
#	print("NO ACCESS TOKEN")
#	sys.exit()

#access_token = '121212'

# if access_token == "":
# 	#Order Not Found, Show warning to user
# 	print("Order not found.")

#url = 'https://www.go2stream.net/API/orders/status/'+customerOrderNo
#headers = {'Accept': "application/json", 'Stream-Nonce': randomString(30), 'Stream-Party': "EXPRE000000000002", 'Authorization': "Bearer "+access_token, 'cache-control': "no-cache",}

#responseOrder = requests.get(url, headers=headers)

#if responseOrder.status_code != 200 and responseOrder.status_code != 422:
	#Order Not Found, Show warning to user
#	print("Order not found.", "Response: ", responseOrder)

#Read the response
#json_response_order = responseOrder.json()
#response_body = json_response_order.get("response", "")
#tracking_url = response_body.get("trackingURL", "")

#if tracking_url == "":
	#Order Not Found, Show warning to user
#	print("Order not found.")

#Pass this back to the AJAX then you can redirect the user via Javascript
#print(tracking_url)