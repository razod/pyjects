import requests
import json

class tiktok():
    def td(self, link):
        headers = {
        '0': '0'
        }
        lk = 'https://tiktok-down.sethusenthil.com/' + link
        response = requests.get(lk, headers=headers, verify=True)
        j = json.loads(response.content)
        return j['url']

t = tiktok()
print(t.td('https://vm.tiktok.com/qWjbAh'))