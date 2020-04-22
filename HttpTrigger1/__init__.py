import logging
from twilio.rest import Client

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    account_sid = "AC2016968f3f79de24cfc298fcc2ac19d8"
    # Your Auth Token from twilio.com/console
    auth_token  = "c07eafcffe01e315d9572cfb22283bc6"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+8613304843608", 
        from_="+19798594714",
        body="Hello from Python!")

    print(message.sid)
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
