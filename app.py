import requests
import json

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
import paytmchecksum

paytmParams = dict()

paytmParams["body"] = {
    "mid"           : "YOUR_MID_HERE",
    "orderId"       : "OREDRID98765",
    "amount"        : "1303.00",
    "businessType"  : "UPI_QR_CODE",
    "posId"         : "S12_123"
}

# Generate checksum by parameters we have in body
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
checksum = paytmchecksum.generateSignature(json.dumps(paytmParams["body"]), "YOUR_MERCHANT_KEY")

paytmParams["head"] = {
    "clientId"	        : "C11",
    "version"	        : "v1",
    "signature"         : checksum
}

post_data = json.dumps(paytmParams)

# for Staging
url = "https://securegw-stage.paytm.in/paymentservices/qr/create"

# for Production
# url = "https://securegw.paytm.in/paymentservices/qr/create"
response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
print(response)

