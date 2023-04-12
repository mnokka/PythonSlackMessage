#
# 5.4.2023 mika.nokka1@gmail.com
#
# Idea from https://howchoo.com/python/python-send-slack-messages-slackclient
# 
# For Slack lib: pip install slackclient
# or  pip install -r requirements.txt
# see web page for Slack app creation/configuration magic
#
# ENV variable SLACKTOKEN assumed to include token for Slack app usage
# (export SLACKTOKEN=MY_SLACK_GIVEN_TOKEN_TO_MY_APP)
#

import slack
import os,sys,argparse

__version__ = u"0.73300"

MESSAGETEXT=u""
  

parser = argparse.ArgumentParser(description="Send message to Slack channel (as a Slack app)",
    
    
 epilog="""
    
    EXAMPLE:
    
    SLACKTOKEN env variable assumed to include Slack app token
    
    python3 messager.py  -t "TEXT FOR SLACKCHANNEL" -c SLACKCHANNEL"""  
    
)
parser.add_argument('-v', help='Send Slack message', action='version',version="Version:{0}   mika.nokka1@gmail.com ,  MIT licenced ".format(__version__) )
parser.add_argument("-t",help='<Slack Message text>',metavar="message")
parser.add_argument('-c', help='<Slack channel>',metavar="slackchannel")
   
args = parser.parse_args()       
SLACKMESSAGE = args.t or ''
SLACKCHANNEL= args.c or ''
     
# quick old-school way to check needed parameters
if (SLACKMESSAGE=='' or  SLACKCHANNEL==''):
        print("\n---> MISSING ARGUMENTS!!\n ")
        parser.print_help()
        sys.exit(2)
        

if 'SLACKTOKEN' in os.environ:
    print("OK , env SLACKTOKEN found")
    mytoken=(os.environ['SLACKTOKEN'])
else:
    print("ERROR!! No SLACKTOKEN env defined! EXITING")
    sys.exit(5)

print ("---> Channel:"+SLACKCHANNEL+"   Text:"+SLACKMESSAGE )

try:
    client = slack.WebClient(token=mytoken)
    client.chat_postMessage(channel=SLACKCHANNEL, text=SLACKMESSAGE)

except Exception as e:
        print(("Slacking failed! Check your channel name?, error: %s" % e))
        sys.exit(1)

print("Done! Bye!")
