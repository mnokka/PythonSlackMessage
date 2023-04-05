#
# 5.4.2023 mika.nokka1@gmail.com
#
# Idea from https://howchoo.com/python/python-send-slack-messages-slackclient
# 
# pip install slackclient
# see web page for Slack app creation/configuration magic
#
# ENV variable SLACKTOKEN assumed to include token for Slack app usage
# (export SLACKTOKEN=MY_SLACK_GIVEN_TOKEN_TO_MY_APP)
#
# TODO: add CLI interface, trap possible slacking error

import slack
import os,sys

if 'SLACKTOKEN' in os.environ:
    print("OK , env SLACKTOKEN found")
    mytoken=(os.environ['SLACKTOKEN'])
else:
    print("ERROR!! No SLACKTOKEN env defined! EXITING")
    sys.exit(5)

client = slack.WebClient(token=mytoken)
client.chat_postMessage(channel='test-messaging-apps', text='TESTING ONLY VIA PYTHON SCRIPT')