import torch
import json

hello_response=[]
sketch_response=[]
bye_response=[]
with open('responses.json','r') as f:
    intents=json.load(f)

for intent in intents['intents']:
    hello_response.append(intent['hello_responses'])
    sketch_response.append(intent['sketch_responses'])
    bye_response.append(intent['bye_responses'])

data={
    "hello_response":hello_response,
    "sketch_response":sketch_response,
    "bye_response":bye_response
}

FILE="Responses.pth"
torch.save(data,FILE)
