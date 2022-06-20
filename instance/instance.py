
from flask import Flask,request
import boto3
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/')
def func():

    instancename=request.args.get('instancename')
    ec2 = boto3.client('ec2')

               
    response1 = ec2.describe_instances(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                str(instancename)
            ]
        }
            
    ]
) 

    return (response1)
    



app.run(port=2003, host="0.0.0.0",debug=True) 