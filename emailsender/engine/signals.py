from django.core.mail import EmailMultiAlternatives, mail_admins
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from emailsender.settings import MEDIA_URL

from .models import Sender


@receiver(post_save, sender=Sender)
def message_created(instance, created, **kwargs):  # FIXME
    if not created:
        return

    emails_to_send = list()

    # Here we take variable data from settings
    direct_to_file = MEDIA_URL[1:] + Sender.objects.all().values().last()["emails"]

    # Collecting emails from the last message in the sender model and removing the "\n" character
    with open(direct_to_file, encoding="utf-8") as emails:
        for email in emails:
            emails_to_send.append(email.replace("\n", ""))

    subject = instance.title

    html_template = 'emailsender/templates/html_template.html'
    html_content = render_to_string(html_template, {'context': instance.content, 'subject': subject})

    text_content = strip_tags(html_content)

    # Sending letters to the destination
    for _email in emails_to_send:
        msg = EmailMultiAlternatives(subject, text_content, None, [_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    mail_admins(
        subject=subject,
        message='Successful message sending',
    )
