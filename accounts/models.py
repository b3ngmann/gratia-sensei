import datetime
from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaLanguageBaseProfile
from church.models import *

class Profile(UserenaLanguageBaseProfile):  
    GENDER_CHOICES = (
    	(1, _('Male')),
        (2, _('Female')),
    	(3, _('------')),
    )

    MARITAL_STATUS = (
    	(1, _('Single')),
    	(2, _('Married')),
    )

    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')  
    role = models
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, default=3)
    marital_status = models.PositiveSmallIntegerField(_('marital status'), choices=MARITAL_STATUS, blank=True, default=1)
    address = models.CharField(_('address'), max_length=255, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True, default=datetime.date(1990,1,1))
    chapel = models.ForeignKey(Chapel, verbose_name=_('chapel'))
    bussel = models.ForeignKey(Bussel, verbose_name= ('bussel'))