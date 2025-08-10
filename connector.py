import requests
import time

def connect(username,password):
    login_url = 'https://10.100.1.1:8090/login.xml'

    payload = {
            'mode': '191',
            'username': username,
            'password': password,
            'a': time.time()*1000,
            'producttype': 'none'
        }
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://10.100.1.1:8090/'
        }
    
    try:
        response = requests.post(login_url, data=payload, headers=headers, verify=False, timeout=10)
        if response.status_code == 200:
            if "You are signed in as" in response.text:
                return True,"Connected"
            else:
                print(response.text)
                return False,"WRONG CREDENTIALS"
    except requests.exceptions.RequestException as e:
        # this is the condition when the server is unreachable or the wifi is turned off 
        return False,f'Unable to connect becuase of error {e}'