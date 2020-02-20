import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class yolo():

    def __init__(self):
        pass

    def sendVerfCode(self, countrycode, phonenumber):
        headers = {
            'Host': 'api.onyolo.com',
            'x-parse-client-version': 'i1.17.2',
            'content-type': 'application/json; charset=utf-8',
            'accept': '*/*',
            'x-parse-application-id': 'RTE8CXsUiVWfG1XlXOyJAxfonvt',
            'x-parse-installation-id': '8b561c9c-9a69-4445-b6f8-8a227ca9af50',
            'x-parse-os-version': '13.1 (17A844)',
            'accept-language': 'en-us',
            'user-agent': 'YOLO/160 CFNetwork/1107.1 Darwin/19.0.0',
            'x-parse-app-build-version': '160',
            'x-parse-app-display-version': '2.1.1',
        }

        data = '{"timestamp":1,"as":"","phoneNumber":"+'+str(countrycode)+str(phonenumber)+'"}'

        self.phoneNumber = "+"+str(countrycode)+str(phonenumber)

        response = requests.post('https://api.onyolo.com/functions/sendVerificationCode', headers=headers, data=data, verify=False)

    def loginWithVerfCode(self, verfcode):
        import requests

        headers = {
            'Host': 'api.onyolo.com',
            'x-parse-client-version': 'i1.17.2',
            'content-type': 'application/json; charset=utf-8',
            'accept': '*/*',
            'x-parse-application-id': 'RTE8CXsUiVWfG1XlXOyJAxfonvt',
            'x-parse-installation-id': '8b561c9c-9a69-4445-b6f8-8a227ca9af50',
            'x-parse-os-version': '13.1 (17A844)',
            'accept-language': 'en-us',
            'user-agent': 'YOLO/160 CFNetwork/1107.1 Darwin/19.0.0',
            'x-parse-app-build-version': '160',
            'x-parse-app-display-version': '2.1.1',
        }

        data = '{"verificationCode":"'+str(verfcode)+'","timestamp":1,"as":"","phoneNumber":"'+str(self.phoneNumber)+'"}'

        response = requests.post('https://api.onyolo.com/functions/loginWithPhoneNumber', headers=headers, data=data, verify=False)

        j = json.loads(response.content)

        self.sesskey = j['result']

    def selfInfo(self):
        headers = {
            'Host': 'api.onyolo.com',
            'x-parse-client-version': 'i1.17.2',
            'accept': '*/*',
            'x-parse-session-token': self.sesskey,
            'x-parse-application-id': 'RTE8CXsUiVWfG1XlXOyJAxfonvt',
            'x-parse-installation-id': '8b561c9c-9a69-4445-b6f8-8a227ca9af50',
            'x-parse-os-version': '13.1 (17A844)',
            'accept-language': 'en-us',
            'user-agent': 'YOLO/160 CFNetwork/1107.1 Darwin/19.0.0',
            'x-parse-app-build-version': '160',
            'x-parse-app-display-version': '2.1.1',
        }

        response = requests.get('https://api.onyolo.com/users/me', headers=headers, verify=False)

        j = json.loads(response.content)

        return j

    def getSessionToken(self):
        return self.sesskey

    def getMessages(self, skip):
        headers = {
            'Host': 'api.onyolo.com',
            'x-parse-client-version': 'i1.17.2',
            'content-type': 'application/json; charset=utf-8',
            'accept': '*/*',
            'x-parse-session-token': self.sesskey,
            'x-parse-application-id': 'RTE8CXsUiVWfG1XlXOyJAxfonvt',
            'x-parse-installation-id': '8b561c9c-9a69-4445-b6f8-8a227ca9af50',
            'x-parse-os-version': '13.1 (17A844)',
            'accept-language': 'en-us',
            'user-agent': 'YOLO/160 CFNetwork/1107.1 Darwin/19.0.0',
            'x-parse-app-build-version': '160',
            'x-parse-app-display-version': '2.1.1',
        }

        data = '{"timestamp":1,"before":{"__type":"Date","iso":"3019-12-14T04:00:19.858Z"},"as":"","skip":'+str(skip)+'}'

        response = requests.post('https://api.onyolo.com/functions/getMessages', headers=headers, data=data, verify=False)

        j = json.loads(response.content)

        messages = []

        for i in j['result']:
            messages.append(i)

        return messages

    def getUser(self, user):
        headers = {
            'Host': 'api.onyolo.com',
            'x-parse-client-version': 'i1.17.2',
            'accept': '*/*',
            'x-parse-session-token': self.sesskey,
            'x-parse-application-id': 'RTE8CXsUiVWfG1XlXOyJAxfonvt',
            'x-parse-installation-id': '8b561c9c-9a69-4445-b6f8-8a227ca9af50',
            'x-parse-os-version': '13.1 (17A844)',
            'accept-language': 'en-us',
            'user-agent': 'YOLO/160 CFNetwork/1107.1 Darwin/19.0.0',
            'x-parse-app-build-version': '160',
            'x-parse-app-display-version': '2.1.1',
        }

        response = requests.get('https://api.onyolo.com/classes/_User/'+user, headers=headers, verify=False)

        j = json.loads(response.content)

        return j

    def sendMessage(self, user, text):
        cookies = {
            'popshow-temp-id': 'xyz',
        }

        headers = {
            'Host': 'onyolo.com',
            'accept': 'application/json, text/plain, */*',
            'origin': 'https://onyolo.com',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://onyolo.com/m/'+user,
            'accept-language': 'en-US,en;q=0.9',
        }

        data = '{"text":"'+text+'","cookie":"","wording":""}'

        response = requests.post('https://onyolo.com/'+user+'/message', headers=headers, cookies=cookies, data=data, verify=False)
