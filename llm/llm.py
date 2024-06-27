import boto3
import json
from langchain_aws import BedrockLLM


def lambda_handler(event, context):
    # Event y Context son parámetros que Lambda pasa a la función handler
    # event: contiene datos específicos del evento que invocó la función
    # context: proporciona métodos y propiedades relacionadas con la invocación
    
    the_prompt = json.loads(event['body'])['prompt']
   
    bedrock_llm = BedrockLLM(model_id="anthropic.claude-v2:1", model_kwargs={"temperature": 0.2})
    the_answer=bedrock_llm.invoke(input=the_prompt)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "answer": f"{the_answer}",
        }),
    }
