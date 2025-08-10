'''
LOGIC FOR CITPC CONNECTOR
    written by- Meyan Adhikari
(This is not the code used for the original app, the design part is excluded
However, the funcanality and the scraping technique used is shown here)
'''

username = '080bel042' # your username 
password = '2123-2470' # your password (this is not mine)
login_url = 'https://10.100.1.1:8090/login.xml'

# the login_url is the url of the page, that asks us to input our username and password
# you may see it on the browsers address input box in the top when trying to login via broswer
# you can use functions like input() to handle the input of username and password
# in the app, the UI layout and textfields were used to take the input

# importing all the modules we need
import requests
import time

# in the original app, threading was also used and 'kivy' libraries were also used which are not used here 
# the 'time' module is optional which will be shown later


# the payload containts the parameters that are used by the server of CIT, the first is mode
# which we reversed engineered to know was 191 for logging in, 'a' refers to the time in kiloseconds (10^3 * time.time())
# you can enter any time in 'a', so time.time() may be ommited with any number so importing of time module is optional
# similarly the producttype also maybe virtually anything or empty
payload = {
            'mode': '191',
            'username': username,
            'password': password,
            'a': time.time()*1000,
            'producttype': 'none'
        }

# the headers used below are ,as an outside code for us to pretend like browsers, not using this may also work
# however, it might be risky since the moderatos in CIT will witness a program connecting to the router instead 
# of a browser, the headers simulate a web browser
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://10.100.1.1:8090/'
        }

try:
    # now, we try to 'post' request the url with our data, timeout here refers to the maximum time we allow
    # for the waiting of the request, if we get no response for more than 10 second we stop
    # we store the response we get form the server in the response variable
    response = requests.post(login_url, data=payload, headers=headers, verify=False, timeout=10)
    if response.status_code == 200:
        # 200 is the status_code for a healthy request and response
        if "You are signed in as" in response.text:
            
            # "You are signed in as" is shown to us when we are successfully connected
            # if this is not in the response then chances are the credentials were wrong
            print("Congrats! The process is successfull, You are succesfully logged in !")
        else:
            print(response.text)
            print("Hm! It seems like your credentials were wrong or in a non likely sceniaro you have reached your maximum login limit")

except requests.exceptions.RequestException as e:
    # this is the condition when the server is unreachable or the wifi is turned off 
    print(f'Unable to connect becuase of error {e}')