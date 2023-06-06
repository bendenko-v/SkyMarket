import os

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from templated_mail.mail import BaseEmailMessage

from djoser import utils
from djoser.conf import settings
from django.conf import settings as dj_settings


class PasswordResetEmail(BaseEmailMessage):
    template_name = os.path.join(dj_settings.TEMPLATES[0]['DIRS'][0], 'password_reset.html')

    def send(self, to_email, *args, **kwargs):
        context = self.get_context_data()
        user = context.get('user')
        token = default_token_generator.make_token(user)
        uid = utils.encode_uid(user.pk)
        password_reset_url = settings.PASSWORD_RESET_CONFIRM_URL.format(uid=uid, token=token)
        protocol = context.get('protocol')
        domain = context.get('domain')
        context['password_reset_url'] = protocol + '://' + domain + '/' + password_reset_url

        subject = 'SkyMarket / Password Reset'
        html_content = render_to_string(self.template_name, context)

        email = EmailMessage(subject, html_content, to=to_email)
        email.content_subtype = "html"
        email.send()
