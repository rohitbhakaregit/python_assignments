
import requests
import json

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': "xoxp-979368346404-968354493955-979399085604-c416d442f729a7c9283c2d35d0c3440c",
        'channel': "#mesh",
        'text': text,
        'icon_url': "https://cdn1.iconfinder.com/data/icons/tech-multimedia-2/64/CPU-hot_proc_PC_wet_burn-512.png",
        'username': 'CPU_BURN',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()

post_message_to_slack("CPU reached maximum threashold");

"""
Slack URL : talentica-world.slack.com
username bhakarerohit@gmail.com
Password: default
"""
