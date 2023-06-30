from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_admins
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Sender


@receiver(post_save, sender=Sender)
def message_created(instance, created, **kwargs):  # FIXME
    if not created:
        return

    emails = []

    for email in User.objects.all().values():
        emails.append(email["email"])

    # user_id = User.objects.all().values().last()["feedback_user_id"]
    #
    # email = [User.objects.filter(id=user_id).values("email").last()["email"]]
    #
    # subject = f'Comment successfully posted in {instance.feedback_post.header} post'
    #
    # text_content = (
    #     f'Feedback on : {instance.feedback_post.header} post\n'
    #     f'Link: http://127.0.0.1:8000{instance.feedback_post.get_post_url()}'
    # )
    # html_content = (
    #     f'Feedback on : {instance.feedback_post.header} post\n'
    #     f'Link: http://127.0.0.1:8000{instance.feedback_post.get_post_url()}'
    # )
    #
    # mail_admins(
    #     subject='',
    #     message=f'New comment in {instance.feedback_post.header} post',
    # )
    #
    # for _email in email:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [_email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()
