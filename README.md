# informant
sends a text message for every successful login to my servers

## requirements:
* python3
* virtualenv
* twilio

## step 1: setup a twilio developer account
* go to: https://www.twilio.com/try-twilio

## step 2: clone this repo
    git clone https://github.com/brianhoppus/informant
    cd informant

## step 3: setup your development environment
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
## step 4: create a text file dev_account.py
    account_sid = "your_account_sid_here"
    auth_token = "your_auth_token_here"
    admin_phone_number = "your_admin_phone_number_here"
    twilio_phone_number = "your_twilio_phone_number_here"

phone numbers are formatted like this:

    +17075551234
    
## step 5: run it!
    python informant.py
