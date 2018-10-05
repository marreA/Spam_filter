
import email
from bs4 import BeautifulSoup

class Email_Object:
    HTML = 'text/html'
    PLAIN = 'text/plain'
    def __init__(self, filepath, category = None):
        self.filepath = filepath
        self.category = category
        self.mail = email.message_from_file(self.filepath)
    
    def subject(self):
        return self.mail.get('Subject')
    
    def body(self):
        content_type = self.mail.get_content_type()
        body = self.mail.get_payload()
        if content_type == Email_Object.HTML:
            return BeautifulSoup(body).text
        elif content_type == Email_Object.PLAIN:
            return body
        else:
            return ''