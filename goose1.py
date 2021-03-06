""" Basic operations using Slack_sdk """

import os
from slack_sdk import WebClient 
from slack_sdk.errors import SlackApiError 

""" We need to pass the 'Bot User OAuth Token' """
from dotenv import load_dotenv

load_dotenv()
slack_token = os.environ['GOOSE_SLACK_BOT_TOKEN']
print(slack_token)

# Creating an instance of the Webclient class
client = WebClient(token=slack_token)

try:
	# Posting a message in #random channel
	response = client.chat_postMessage(
    				channel="first-fly",
    				text="Bot's first message")
	
	# Sending a message to a particular user
	response = client.chat_postEphemeral(
                    channel="first-fly", 
                    text="Hello U03JN4TLGF3", 
                    user="U03JN4TLGF3")
	
	# Get basic information of the channel where our Bot has access 
	response = client.conversations_info(
                    channel="first-fly")
	
	# Get a list of conversations
	response = client.conversations_list()
	print(response["channels"])
	
except SlackApiError as e:
    print(e)