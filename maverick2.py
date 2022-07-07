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

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()