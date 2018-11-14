# Django imports
from django.conf.urls import url

# Project imports
from . import utils
from . import rest
urlpatterns = [
    url(r'^levels/', rest.UserLevels.as_view(), name='account-levels')
]
