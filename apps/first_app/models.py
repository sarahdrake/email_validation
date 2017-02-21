from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def login(self, email):
        # This model should return a create function that will create a user if the email entered passes validation
        if not EMAIL_REGEX.match(email):
            print "*************************"
            return False
        else:
            print "&&&&&&&&&&&&&&&&&&&&&&&&&&"
            return super(UserManager, self).create(email=email)
class User(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
