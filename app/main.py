#on a simiple online webpage, write a simple python JSON that invokes the mpesa SIM stk for 
#payment when user clicks submit after inputs pay amount and specifies mobile number
from flask import Flask
from flask_restplus import Api,Resource,fields

app = Flask(__name__)
api = Api(app, version='1.0',title='MPESA API',
            description='mpesa api covering STK push')


from resources.stkpush import *

