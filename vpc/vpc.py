from flask import Flask, request
import boto3
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/')
def func():

    vpcname = request.args.get('vpcname')
    ec2 = boto3.client('ec2')

               
    response = ec2.describe_vpcs(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                 str(vpcname)
            ]
        }
   
    ]
) 

    return (response)

app.run(port=2000, host="0.0.0.0")      

