# Django imports
from django.db import transaction

# Project imports
from .models import UserLevel, User


def get_account_levels():
    """Returns user levels. """
    return dict(UserLevel.USER_LEVEL)

@transaction.atomic
def create_account(level, **kwargs):
    """Creates account based on user level. """
    try:
        func_tag = "account:utils:create_account"
        user = User.objects.create(**kwargs)
        obj = UserLevel.objects.add_entry(user=user, level=level)
    except Exception as exc:
        raise exc

def create_organization(caller, username, org_name, email, password):
    """Creates an organization. """
    try:
        func_tag = "account:utils:create_organization"
        data = {
            "username": username,
            "first_name": org_name,
            "email": email,
            "password": password
        }
        create_user(UserLevel.ORG, **data)
    except Exception as exc:
        raise exc

def create_super_admin(caller, username, first_name, last_name, email, password):
    """Creates a super admin. """
    try:
        func_tag = "account:utils:create_super_admin"
        data = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        create_user(UserLevel.SUPERADMIN, **data)
    except Exception as exc:
        raise exc

def create_process_admin(caller, username, first_name, last_name, email, password):
    """Creates a process admin. """
    try:
        func_tag = "account:utils:create_process_admin"
        data = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        create_user(UserLevel.PROCESSADMIN, **data)
    except Exception as exc:
        raise exc

def create_user(caller, username, first_name, last_name, email, password):
    """Creates a user. """
    try:
        func_tag = "account:utils:create_user"
        data = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        create_user(UserLevel.USER, **data)
    except Exception as exc:
        raise exc