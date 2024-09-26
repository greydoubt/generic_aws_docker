# lambda_function.py


# python built-ins
import sys
import os


# imports (try/catch)
#import numpy
#import torch


#try:
    
    #os.environ['TRANSFORMERS_CACHE'] = '/tmp/test_hf_transformers/'
    #import transformers

#except Exception as e:
    #print("cant load transformers: " + e)


"""
def handler(event, context):
    print("Event: ")
    print(event)

    print("\n\nContext: ")
    print(context)
    return 'running python: ' + sys.version + '!'"""

import json
import logging

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    # Log the received event

    logger.info("Received event: " + json.dumps(event, indent=2))
    
    # Generic message
    message = f"Running Python: {sys.version}"
    
    # Return the message
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f"{message} \n {json.dumps(event, indent=2)}"})
    }
