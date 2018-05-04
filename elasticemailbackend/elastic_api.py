import requests
import json

class ApiClient(object):
    def __init__(self,apiKey, apiUri='https://api.elasticemail.com/v2'):
        self.apiUri = apiUri
        self.apiKey = apiKey

    def request(self,method, url, data):
        data['apikey'] = self.apiKey
        if method == 'POST':
            result = requests.post(self.apiUri + url, params = data)
        elif method == 'PUT':
            result = requests.put(self.apiUri + url, params = data)
        elif method == 'GET':
            attach = ''
            for key in data:
                attach = attach + key + '=' + data[key] + '&' 
            url = url + '?' + attach[:-1]
            result = requests.get(self.apiUri + url)
        
        if result.status_code == 200:
            json_result = result.json()
        else:
            print(result.status_code)
            print(result.text)
            raise
        if json_result['success'] is False:
            print("Failed to send email.{0}".format(json_result['error']))
            print(json_result['error'])
            raise
        print("Email sent.{0}".format(json_result['data']))
        return json_result['data']

    def send_email(self,email,isTransactional=True):
        email_data = {
            'subject': email['subject'],
            'from': email['senderEmail'],
            'fromName': email['senderName'],
            'msgTo': email['to'],
            'isTransactional': isTransactional
        }
        if 'bodyText' in email and email['bodyText']:
            email_data['bodyText'] = email['bodyText']
        if 'bodyHtml' in email and email['bodyHtml']:
            email_data['bodyHtml'] = email['bodyHtml']
        if 'cc' in email and email['cc']:
            email_data['msgCC']  = email['cc']
        if 'bcc' in email and email['bcc']:
            email_data['msgBcc'] = email['bcc']

        return self.request('POST', '/email/send', email_data)