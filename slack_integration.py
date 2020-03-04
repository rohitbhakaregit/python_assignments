import requests
import json

def post_message_to_slack(text,uname,image_url,blocks = None): 
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': "xoxp-979368346404-968354493955-980955372132-343303a034502c9c9390c147d10dae75",
        'channel': "#mesh",
        'text': text,
        'icon_url': image_url,
        'username': uname,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
"""
Slack URL : talentica-world.slack.com
username bhakarerohit@gmail.com
Password: default
"""
