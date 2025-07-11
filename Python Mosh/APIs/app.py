from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to='+233541747842',
    from_='+14632209825',
    body='This is our first message'
)
