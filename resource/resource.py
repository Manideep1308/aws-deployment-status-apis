from flask import Flask, request, json, Response
import boto3
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

app.config['PROPAGATE_EXCEPTIONS'] = True


@app.errorhandler(Exception)
def all_exception_handler(error):
    res = {"error": str(error)}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))



def error_401_handler(error):
    res = {"error": "Unauthorized"}
    return Response(status=401, mimetype="application/json", response=json.dumps(res))

@app.route('/')
def func():

 stackname =request.args.get('stackname')

 client = boto3.client('cloudformation')                     

 list = client.list_stack_resources(StackName = str(stackname)) 

 return list

app.run(port=2004, host='0.0.0.0', debug=True) 
