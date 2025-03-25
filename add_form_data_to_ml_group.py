import json
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
import mailerlite as MailerLite

# loading variables from .env file
load_dotenv()

# Constants
MAILER_LITE_APIKEY="MAILER_LITE_APIKEY"
MAILER_LITE_GROUP_FORM_INS_PERSONA = 149878119373735539

# create connection to MailerLite
client = MailerLite.Client({
  'api_key': os.getenv(MAILER_LITE_APIKEY)
})

# data from fronted was saved as a json file
# now we read that json file
with open('sample_form_1_data.json', 'r', encoding="utf-8") as file:
    form_data = json.load(file)

# add person as subscriber in MailerLite
response = client.subscribers.create(form_data["email"], 
                                     fields=form_data, 
                                     ip_address='1.2.3.4', 
                                     optin_ip='1.2.3.4')

print(response)
subscriber_id = int(response["data"]["id"])
print(f"you just registered the subscriber_id {subscriber_id}")

# add subscriber to a group
response = client.subscribers.assign_subscriber_to_group(subscriber_id, MAILER_LITE_GROUP_FORM_INS_PERSONA)

print ("*END")