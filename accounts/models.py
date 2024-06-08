from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class CustmomUser(AbstractBaseUser, UserManager)
email = models.EmailField(verbose_name="メールアドレス",unique=True, blank=False, null=False)
thumbnail = models.ImageField(upload_to="images/thumnbnail/", verbose_name="サムネイル", blank=True, null=True)
USERNAME_FIELD = 'email'
REQUUIRED_FIELDS =['username']

def _str_(self):
    return self.email