import requests
import json, os
from twilio.rest import Client
import time
import datetime
print(r"""
            _   _  _   _   ___  ___ _  ___   _____ ___ 
           /_\ | \| | /_\ | _ \/ __| || \ \ / / _ / _ \
          / _ \| .` |/ _ \|   | (__| __ |\ V /\_, \_, /
         /_/ \_|_|\_/_/ \_|_|_\\___|_||_| |_|  /_/ /_/ 
                         Twilio Get Balance And phone number
                         john.dhoe412@gmail.com
                         https://www.facebook.com/jancoxx412
                         """)
account_sid = raw_input(" [+] Input your Twilio account sid : ")
auth_token = raw_input(" [+] Input your Twilio Auth Key : ")
time.sleep(1)
print " [+] Checking ...."

def get_balance():
    r = requests.get('https://api.twilio.com/2010-04-01/Accounts/'+account_sid+'/Balance.json', auth=(account_sid, auth_token))
    Json = json.dumps(r.json())
    resp = json.loads(Json)
    balance = resp ['balance']
    currency = resp ['currency']
    return str(balance)+' '+str(currency)

def get_phone():
    client = Client(account_sid, auth_token)
    incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
    for record in incoming_phone_numbers:
        return record.phone_number
def get_type():
    client = Client(account_sid, auth_token)
    account = client.api.accounts.create()  
    return account.type

def send_sms(number_send):
    try:
        phone = get_phone()
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                                  body='HELLO IM GANS',
                                  from_= phone,
                            to=number_send
                            # +447862080501
                            # +12127319863
                            #+819066583589
                              )
        return message.status
    except:
        return 'die'

def result():
    try:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        balance = get_balance()
        number = get_phone()
        type = get_type()
        phno = ["+819074059074","+447380308872","+12127319863","+61476856482","+13363605030"]
        for phonee in phno:
            send = send_sms(phonee)
            if send == 'die':
               status = 'CANT SEND SMS'
               bisa = "CANT SEND TO ALL NUMBER"
            else:
                 status = 'LIVE'
                 bisa = phonee
            print "================================================"
            print " [+] STATUS : {}".format(str(status))
            print " [+] Account SID : {}".format(str(account_sid))
            print " [+] Auth Key :  {}".format(str(auth_token))
            print " [+] Balance :  {}".format(str(balance))
            print " [+] SENDER TO:  {}".format(str(bisa))
            print " [+] Phone Number list : {}".format(str(number))
            print " [+] Account Type : {}".format(str(type))
            print " [+] Gendeng Squad Twilio Checker"
            print "================================================"
            if status == 'CANT SEND SMS' and type == 'trial':
                      os.system("exit")
            if status == 'LIVE':
               open('twilio_result_live '+date+'.txt','a').write("[+] STATUS : {}\n[+] Account SID : {}\n[+] Auth Key : {}\n[+] Balance : {}\n[+] SENDER TO:  {}\n[+] Phone number list : {}\n[+] Account Type : {} \n\n".format(str(status),str(account_sid),str(auth_token),str(balance),str(bisa),str(number),str(type)))
            else:
                 open('twilio_result_junk'+date+'.txt','a').write("[+] STATUS : {}\n[+] Account SID : {}\n[+] Auth Key : {}\n[+] Balance : {}\n[+] SENDER TO:  {}\n[+] Phone number list : {}\n[+] Account Type : {} \n\n".format(str(status),str(account_sid),str(auth_token),str(balance),str(bisa),str(number),str(type)))
    except:
        print " [+] Api Invalid"

result()
