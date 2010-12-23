from django.db import models

from drumbeat.models import ModelBase
from users.models import UserProfile


class AccountPreferences(ModelBase):
    preferences = (
        'no_email_message_received',
        'no_email_new_follower',
        'no_email_new_project_follower',
        'no_email_mention',
    )
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile)
