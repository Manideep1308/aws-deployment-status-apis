from flask import Flask,request
import boto3
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/')
def func():

    stackname =request.args.get('stackname')
   
    ec2 = boto3.client('ec2')
    response = ec2.describe_subnets(
        Filters=[
        # {
        #     'Name': 'tag:aws-cdk:subnet-name',
        #     'Values': [
        #         str(subnetname)
        #     ]
        # },
        {"Name":"tag:aws:cloudformation:stack-name", "Values":[str(stackname)]}
        
    ]
)

    return (response)
    



app.run(port=2001, host="0.0.0.0",debug=True)    