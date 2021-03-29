import requests

email = ''
password = ''
device_id = ''
# To get this, log in to venmo first on your browser, then in the url enter:
# "view-source:https://venmo.com/account/settings/profile" (without quotes)
# search for "fingerprint" and enter any of your device_id's found. It normally
# starts with 'fp01'.

bank_id = ''
# To get this, again in the url enter:
# "view-source:https://venmo.com/account/settings/profile"
# search for "bank_account" and copy the "id" of the appropriate bank in the html.

# Amount to Transfer in Cents (default set to 1 cent)
total_amt = 1 # 1 corresponds to $0.01; 100 corresponds to $1.00

def get_transfer_headers(email, password, device_id):
    credentials = {
        'client_id': '1',
        'phone_email_or_username': email,
        'password': password
    }
    oauth_header = {
        'device-id': device_id
    }
    authcode = requests.post('https://api.venmo.com/v1/oauth/access_token', headers = oauth_header, json = credentials).json()['access_token']
    csrftoken = requests.get('https://api.venmo.com/v1/account').cookies.values().pop()
    venmo_transfer_headers = {
        'Cookie': 'csrftoken2=' + csrftoken,
        'Authorization': 'Bearer ' + authcode
    }
    return venmo_transfer_headers

# Create Data Headers for Post
transfer_data = {
    "amount": total_amt,
    "transfer_type": "standard",
    "destination_id": bank_id,
    "final_amount": total_amt
}

transfer_header = get_transfer_headers(email, password, device_id)

transfer = requests.post('https://api.venmo.com/v1/transfers', headers = transfer_header, data = transfer_data)

transfer.status_code
transfer.text
