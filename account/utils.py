# Project imports
from .models import User


def get_account_levels():
    """Returns user levels. """
    return dict(User.USER_LEVEL)


def create_account(level, **kwargs):
    """Creates account based on user level. """
    try:
        func_tag = "account:utils:create_account"
        user, created = User.objects.get_or_create(
                                                  username=username,
                                                  defaults={
                                                    "first_name": first_name,
                                                    "last_name": last_name,
                                                    "email": email,
                                                    "password": password,
                                                    "level": level}
                                                  )
        return user
    except Exception as exc:
        raise exc

def create_organization(caller, username, org_name, email, password):
    """Creates an organization. """
    try:
        func_tag = "account:utils:create_organization"
        return create_account(User.ORG, **{
            "username": username,
            "first_name": org_name,
            "email": email,
            "password": password
        })
    except Exception as exc:
        raise exc

def create_super_admin(caller, username, first_name, last_name, email, password):
    """Creates a super admin. """
    try:
        func_tag = "account:utils:create_super_admin"
        return create_account(User.SUPERADMIN, **{
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
    except Exception as exc:
        raise exc

def create_process_admin(caller, username, first_name, last_name, email, password):
    """Creates a process admin. """
    try:
        func_tag = "account:utils:create_process_admin"
        return create_account(User.PROCESSADMIN, **{
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
    except Exception as exc:
        raise exc

def create_user(caller, username, first_name, last_name, email, password):
    """Creates a user. """
    try:
        func_tag = "account:utils:create_user"
        return create_account(User.USER, **{
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
    except Exception as exc:
        raise exc