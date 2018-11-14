from django.conf.urls import url, include
from django.contrib import admin

from account.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^account/', include("account.urls"))
]
