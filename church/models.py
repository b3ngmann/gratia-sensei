from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models import permalink, get_model
from django.utils.translation import ugettext_lazy as _

from accounts.models import *

class Bussel(models.Model):
	
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250)


class Chapel(models.Model):
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
	

    class Meta:
        ordering = ['name']
        verbose_name = _("chapel")
        # verbose_name_plural = _("organizations")

    def __unicode__(self):
        return self.name

    # @permalink
    # def get_absolute_url(self):
    #     return ('organization_detail', (), {'organization_pk': self.pk})

    # def add_user(self, user, is_admin=False):
    #     """
    #     Adds a new user and if the first user makes the user an admin and
    #     the owner.
    #     """
    #     users_count = self.users.all().count()
    #     if users_count == 0:
    #         is_admin = True
    #     org_user = OrganizationUser.objects.create(user=user,
    #             organization=self, is_admin=is_admin)
    #     if users_count == 0:
    #         OrganizationOwner.objects.create(organization=self,
    #                 organization_user=org_user)
    #     return org_user

    # def get_or_add_user(self, user, is_admin=False):
    #     """
    #     Adds a new user to the organization, and if it's the first user makes
    #     the user an admin and the owner. Uses the `get_or_create` method to
    #     create or return the existing user.

    #     `user` should be a user instance, e.g. `auth.User`.

    #     Returns the same tuple as the `get_or_create` method, the
    #     `OrganizationUser` and a boolean value indicating whether the
    #     OrganizationUser was created or not.
    #     """
    #     users_count = self.users.all().count()
    #     if users_count == 0:
    #         is_admin = True

    #     org_user, created = OrganizationUser.objects.get_or_create(
    #             organization=self, user=user, defaults={'is_admin': is_admin})

    #     if users_count == 0:
    #         OrganizationOwner.objects.create(organization=self,
    #                 organization_user=org_user)

    #     return org_user, created

    # def is_member(self, user):
    #     return True if user in self.users.all() else False

    # def is_admin(self, user):
    #     return True if self.organization_users.filter(user=user, is_admin=True) else False
