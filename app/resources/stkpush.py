from main import api,Resource,fields

import requests #requests library
import constants #file contantaing some of my constant details eg consumer key & consumer secret
import accessToken #file containing the generated access token
import password #file containing the generated password
import timeformat #file containing the function to generate timestamp in the following format YYYYMMDDHHmmss

generated_password = password.the_decoded_password
generated_timestamp = timeformat.the_formatted_time

# create a namespace for the stk resource
ns_stkpush = api.namespace('stkpush', description="MPESA STK PUSH")
stk_transaction = api.model('Stk',{
    "amount":fields.Integer(min=1,required=True),
    "phoneNumber": fields.String(description='Your Phone Number in the format 254XXXXXXXXX',required=True)
})
@ns_stkpush.route('')
class Stkpush(Resource):
    
    @api.expect(stk_transaction)
    def post(self):
    
        """Use this API endpoint to initiate online payment on behalf of a customer."""
        data = api.payload
        access_token = accessToken.gerated_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
            "BusinessShortCode": constants.BusinessShortCode ,
            "Password": generated_password,
            "Timestamp": generated_timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": data['amount'],
            "PartyA": constants.partya,
            "PartyB": constants.BusinessShortCode,
            "PhoneNumber": data['phoneNumber'], #pass in the phone number that will be prompted to enter the pin
            "CallBackURL": "https://webhook.site/ef7dbbbe-313f-4583-9571-267f3987ee15", #pass in an actual callback url if you have one
            "AccountReference": "SCO 306 Group 8 Mpesa STK ",
            "TransactionDesc": "Test payment"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        # print (response.text)

        return {"response":response.json()}
  
