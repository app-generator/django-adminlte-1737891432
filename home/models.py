# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Care Providors(models.Model):

    #__Care Providors_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    telephone = models.TextField(max_length=255, null=True, blank=True)

    #__Care Providors_FIELDS__END

    class Meta:
        verbose_name        = _("Care Providors")
        verbose_name_plural = _("Care Providors")


class Care Users(models.Model):

    #__Care Users_FIELDS__
    names = models.TextField(max_length=255, null=True, blank=True)
    phone number = models.TextField(max_length=255, null=True, blank=True)

    #__Care Users_FIELDS__END

    class Meta:
        verbose_name        = _("Care Users")
        verbose_name_plural = _("Care Users")



#__MODELS__END
