from django.contrib import admin
from django.urls import re_path, path, include

from .views import (
    login,
    signup,
    test_token
)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login', login),
    re_path('signup', signup),
    re_path('test-token', test_token),
    path('api/', include("api.urls")),
]