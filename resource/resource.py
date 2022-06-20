from flask import Flask, request
import boto3
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/')
def func():

 stackname =request.args.get('stackname')

 client = boto3.client('cloudformation')                     

 list = client.list_stack_resources(StackName = str(stackname)) 

 return list

app.run(port=2004, host='0.0.0.0') 
