# Django imports
from django.contrib.auth.models import AbstractUser
from django.db import models

# Project imports
from base.models import ModelBase


class User(AbstractUser, ModelBase):
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

    level = models.IntegerField(choices=USER_LEVEL, default=USER)

    def __str__(self):
        return "%s (%s)" % (self.username, self.level)


class OrganizationAdminManager(models.Manager):

    def add_org_admin(self, caller, org, super_admin):
        """ """
        try:
            func_tag = "OrganizationAdminManager:add_org_admin"
            return self.create(org=org, admin=super_admin) if caller.is_superuser else None
        except Exception as exc:
            raise exc


class OrganizationSuperAdmin(ModelBase):
    org = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="org_super_admin")
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    objects = OrganizationAdminManager()

    class Meta:
        unique_together = ("org", "admin")