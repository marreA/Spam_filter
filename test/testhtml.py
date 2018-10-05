
import unittest
import io
import re
from bs4 import BeautifulSoup
from email_object import Email_Object

class TestHTMLEmail(unittest.TestCase):
    def setUp(self):
        self.html_file = io.open('./test/fixtures/html.eml', 'rb')
        self.html = self.html_file.read()
        self.html_file.seek(0)
        self.html_email = Email_Object(self.html_file)
    
    def test_parse_stores_inner_text_html(self):
        body = "\n\n".join(self.html.split("\n\n")[1:])
        expected = BeautifulSoup(body).text
        self.assertEqual(self.html_email.body(), expected)
    
    def test_stores_subject(self):
        subject = re.search("Subject: (.*)", self.html).group(1)
        self.assertEqual(self.html_email.subject(), subject)
