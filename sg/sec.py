
from flask import Flask,request
import boto3
from flask_cors import CORS


app =Flask(__name__)
CORS(app)

@app.route('/')
def func():

    securitygroupname =request.args.get('securitygroupname')
   
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups(
           Filters=[
      
          {
            'Name': 'group-name',
            'Values': [
                str(securitygroupname)
            
            ]
        }
        
    ]
)
    return (response)
    



app.run(port=2002, host="0.0.0.0",debug=True)    