from email.mime.base import MIMEBase
from urllib3.exceptions import HTTPError

try:
    import rfc822
except ImportError:
    import email.utils as rfc822

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.base import BaseEmailBackend

from elastic_api import ApiClient

class ElasticEmailBackend(BaseEmailBackend):
    """docstring for ElasticEmailBackend"""
    def __init__(self, fail_silently=False, **kwargs):
        super(ElasticEmailBackend, self).__init__()
        if 'apiKey' in kwargs:
            self.apiKey = kwargs['apiKey']
        else:
            self.apiKey = getattr(settings, "ELASTICEMAIL_API_KEY",None)
        
        if not self.apiKey:
            raise ImproperlyConfigured('''
                ELASTICEMAIL_API_KEY must be declared in settings.py''')

        self.api_client = ApiClient(apiKey=self.apiKey)

    def send_messages(self,email_messages):
        count = 0
        if not email_messages:
            return

        for email in email_messages:
            mail = self._build_ee_mail(email)
            try:
                self.api_client.send_email(mail)
                count += 1
            except HTTPError as e:
                if not self.fail_silently:
                    raise
        return count

    def _build_ee_mail(self,email):
        mail = {}
        sender_name, sender_email = rfc822.parseaddr(email.from_email)
        if not sender_name:
            sender_name = None
        mail['senderEmail'] = sender_email
        mail['senderName'] = sender_name
        mail['subject'] = email.subject
        mail['to'] = email.to
        if email.cc:
            mail['cc'] = email.cc
        if email.bcc:
            mail['bcc'] = email.bcc
        if isinstance(email,EmailMultiAlternatives):
            if len(email.alternatives) > 0:
                for alt in email.alternatives:
                    if alt[1] == "text/html":
                        if 'bodyHtml' in bodyHtml:
                            mail['bodyHtml']+=alt[0]
                        else:
                            mail['bodyHtml'] = alt[0]
                    else:
                        if 'bodyText' in bodyHtml:
                            mail['bodyText']+=alt[0]
                        else:
                            mail['bodyText'] = alt[0]
            else:
                mail['bodyText'] = email.body
        elif email.content_subtype == "html":
            mail['bodyHtml'] = email.body
        else:
            mail['bodyText'] = email.body
        print mail
        return mail