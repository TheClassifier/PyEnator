# Made By : Zach without love
# Date : 2022-08-18
# Version : 1.0
# Fixed Version of https://pypi.org/project/gmailnator.py/


from requests import Session

class Gmail:
    def __init__(self) -> None: # initialize the session and the endpoints
        self.sess = Session() # initialize the session

        self.init_csrf() # init csrf token if not already initialized

        self.sess.headers.update({
            'authority': 'www.emailnator.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.emailnator.com',
            'referer': 'https://www.emailnator.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': self.sess.cookies.get_dict()['XSRF-TOKEN'].replace('"', '').strip().replace('%3D', '=')
        }) # update the headers with the correct xsrf token


        self.generate_email_endpoint = "https://www.emailnator.com/generate-email" # endpoint to generate a new email address
        self.message_list_endpoint = "https://www.emailnator.com/message-list" # endpoint to get the inbox messages


    def init_csrf(self) -> None: # init csrf token if not already initialized
        self.sess.get("https://www.emailnator.com/generate-email") # sends a get request to the main page to get fetch the csrf token into the session

    def new_email(self) -> str: # generate a new email address with a "." format
        json_data = {
            'email': [
                'dotGmail',
            ],
        } # json data to send to the generate email endpoint
        
        r = self.sess.post(self.generate_email_endpoint, json=json_data) # send a post request to the generate email endpoint with the json data
        
        return r.json()["email"][0] # return the new email address

    def get_inbox(self, email:str=None) -> list: # get the inbox of the provided email address
        messages = [] # list to store the inbox messages

        if not email:
            return {"error": "No email address provided"} # Error if no email address provided

        json_data = {
            'email': email,
        } # json data to send to the message list endpoint

        response = self.sess.post(self.message_list_endpoint, json=json_data) # send a post request to the message list endpoint with the json data to get the inbox messages
        response_json = response.json() # get the json response from the post request

        for msg in response_json["messageData"]: # remove NordVPN Advertisement
            if msg["messageID"] != "ADSVPN":
                if msg not in messages:
                    messages.append(msg) # append the message to the list if it is not already in the list

        return messages # return list of messages in inbox
    
    def get_message_body(self, email:str, message_id:str) -> str: # get the body of the provided message id and email address

        json_data = {
            'email': email,
            'messageID': message_id,
        } # json data to send to the message list endpoint

        response = self.sess.post(self.message_list_endpoint, json=json_data) # send a post request to the message list endpoint to get the message body of the message with the provided message id
        response_body = response.text # get the response body from the post request
        return response_body # return body of message from message_id in email