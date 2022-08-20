# PyEnator
Python Class for emailnator.com aka Gmailnator

<img src="https://www.emailnator.com/images/logo.webp?2245a08de0624eb2d3f7cecc7337e846" width="120px" height="120px">

# Features:
- Get a temp gmail
- Check inbox
- Get email content (html/text)

# Usage:

```python
import sys
from time import sleep
from GmLib import Gmail

gmail = Gmail() # init the class

email_address = gmail.new_email() # get an email (gmail)

inbox = gmail.get_inbox(email_address) # get the inbox

while len(inbox) == 0: # watch the inbox until an email is received 
    sys.stdout.write("\rWaiting for email.")
    sys.stdout.flush()
    sys.stdout.write("\rWaiting for email..")
    sys.stdout.flush()
    sys.stdout.write("\rWaiting for email...")
    sys.stdout.flush()
    messages = gmail.get_inbox(email_address) # refresh inbox
    sleep(1) # sleep for 1 sec

for message in messages: # for each msg
  message_body = gmail.get_message_body(email_address, message["messageID"]) # get message content / body
  print(message_body) # print contents of the message received 
  
```
