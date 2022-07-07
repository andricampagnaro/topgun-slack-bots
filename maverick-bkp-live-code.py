from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.environ["MAVERICK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["MAVERICK_APP_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

main_text = {
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "titulo"
			},
			"label": {
				"type": "plain_text",
				"text": "Titulo",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "descricao"
			},
			"label": {
				"type": "plain_text",
				"text": "Descrição",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Enviar"
					},
					"value": "click_me_123",
                    "action_id": "maverick_button_add_sugestion"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Menu Principal"
					},
					"value": "click_me_123",
                    "action_id": "maverick_button_manu_principal"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Template copiado"
					},
					"value": "click_me_123",
                    "action_id": "maverick_button_template_copiado"
				}
			]
		}
	]
}

text_copiado = {
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":newspaper:  Paper Company Newsletter  :newspaper:"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"text": "*November 12, 2019*  |  Sales Team Announcements",
					"type": "mrkdwn"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": " :loud_sound: *IN CASE YOU MISSED IT* :loud_sound:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Replay our screening of *Threat Level Midnight* and pick up a copy of the DVD to give to your customers at the front desk."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Watch Now",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "The *2019 Dundies* happened. \nAwards were given, heroes were recognized. \nCheck out *#dundies-2019* to see who won awards."
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":calendar: |   *UPCOMING EVENTS*  | :calendar: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "`11/20-11/22` *Beet the Competition* _ annual retreat at Schrute Farms_"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "RSVP",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "`12/01` *Toby's Going Away Party* at _Benihana_"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Learn More",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "`11/13` :pretzel: *Pretzel Day* :pretzel: at _Scranton Office_"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "RSVP",
					"emoji": True
				}
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":calendar: |   *PAST EVENTS*  | :calendar: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "`10/21` *Conference Room Meeting*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Watch Recording",
					"emoji": True
				}
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*FOR YOUR INFORMATION*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":printer: *Sabre Printers* are no longer catching on fire! The newest version of our printers are safe to use. Make sure to tell your customers today.",
				"verbatim": False
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please join me in welcoming our 3 *new hires* to the Paper Company family! \n\n *Robert California*, CEO \n\n *Ryan Howard*, Temp \n\n *Erin Hannon*, Receptionist "
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": ":pushpin: Do you have something to include in the newsletter? Here's *how to submit content*."
				}
			]
		}
	]
}

@app.event("app_mention")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def mention_handler(say, ack):
    ack()
    text = main_text
    say(text=text)

@app.action("maverick_button_add_sugestion")
def handle_some_action(ack, body, logger, say):
    ack()
    state_values = body['state']['values']
    for id in state_values:
        for field in state_values[id]:
            print(f'{field}: {state_values[id][field]["value"]}')
    say(text='Recebido')

@app.action("maverick_button_manu_principal")
def handle_some_action(say, ack):
    ack()
    text = main_text
    say(text=text)

@app.action("maverick_button_template_copiado")
def handle_some_action(say, ack):
    ack()
    text = text_copiado
    say(text=text)

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()