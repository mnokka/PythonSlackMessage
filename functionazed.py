#
#
# Using slack messaging via function  approach
# i.e having "print to slack channel" possibility
#
# mika.nokka1@gmail.com 12.4.2023
#
# ENV variable SLACKTOKEN assumed to include token for Slack app usage
# (export SLACKTOKEN=MY_SLACK_GIVEN_TOKEN_TO_MY_APP)

import slack
import os,sys

__version__ = u"0.73300"





def main():
    print ("Using slack messaging as a printing function")
    print ("--------------------------------------------")

    if 'SLACKTOKEN' in os.environ:
        print("OK , env SLACKTOKEN found")
        mytoken=(os.environ['SLACKTOKEN'])
    else:
            print("ERROR!! No SLACKTOKEN env defined! EXITING")
            sys.exit(5)

    mychannel="test-messaging-apps"
    mymessage="message using function approach"

    print ("Goint to slack-print:")
    print("Channel:"+mychannel+" Message:"+mymessage)
    
    message(mychannel,mymessage,mytoken)

    print ("Done!")

def message(SLACKCHANNEL,SLACKMESSAGE,SLACKTOKEN):
    
    try:
        client = slack.WebClient(token=SLACKTOKEN)
        client.chat_postMessage(channel=SLACKCHANNEL, text=SLACKMESSAGE)

    except Exception as e:
        print(("Slacking failed! Check your channel name?, error: %s" % e))
        sys.exit(1)

   



if __name__=="__main__":
    main()
    