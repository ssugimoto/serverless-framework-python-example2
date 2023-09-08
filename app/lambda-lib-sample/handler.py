import json
import boto3

client = boto3.client('lambda')
ary_function_name = []

def function_list(max_items=50, next_marker=None):
    if next_marker:
        r = client.list_functions(MaxItems=max_items, Marker=next_marker)
    else:
        r = client.list_functions(MaxItems=max_items)
    
    for functions in r['Functions']:
        ary_function_name.append(functions['FunctionName'])

    if 'NextMarker' in r:
        return function_list(max_items=max_items, next_marker=r['NextMarker'])
    else:
        return
def hello_lambda_handler(event, context):
    
    r = function_list()
    print(ary_function_name)

    body = {
        "message": "lambda function list.",
        "list": ary_function_name
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
