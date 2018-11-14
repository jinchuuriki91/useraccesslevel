# Django imports
from django.contrib.auth.models import User
from django.db import models

# Project imports
from base.models import ModelBase


class UserLevelManager(models.Manager):

    def add_entry(self, user, level=None):
        """ """
        try:
            func_tag = "UserLevelManager:add_entry"
            obj, status = self.update_or_create(user=user, defaults={"level": level})
            return obj
        except Exception as exc:
            raise exc

    def get_organizations(self, user):
        """Returns all the organizations. """
        try:
            func_tag = "UserLevelManager:get_organizations"
            return self.filter(level=UserLevel.ORG, is_active=True)
        except Exception as exc:
            raise exc


class UserLevel(ModelBase):

    ORG = -1
    SUPERADMIN = 0
    PROCESSADMIN = 1
    USER = 2
    USER_LEVEL = (
        (ORG, "Organization"),
        (SUPERADMIN, "Super Admin"),
        (PROCESSADMIN, "Process Admin"),
        (USER, "User")
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    level = models.IntegerField(choices=USER_LEVEL, default=USER)

    objects = UserLevelManager()

    def __str__(self):
        return "%s (%s)" % (self.user.username, self.level)
