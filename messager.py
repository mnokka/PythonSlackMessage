#
# 5.4.2023 mika.nokka1@gmail.com
#
# from https://howchoo.com/python/python-send-slack-messages-slackclient
# pip install slackclient
# see web page for Slack app creation/configuration magic
#
# TODO: add CLI interface and token storing system

import slack

mytoken="INSERT_MY_APP_SECRET_TOKEN"


client = slack.WebClient(token=mytoken)
client.chat_postMessage(channel='test-messaging-apps', text='TESTING ONLY VIA PYTHON SCRIPT')