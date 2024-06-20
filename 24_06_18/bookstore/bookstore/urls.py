from django.contrib import admin
from django.urls import path, include

from .views import (
    login,
    signup,
    test_token
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path('signup', signup),
    path('test-token', test_token),
    path('api/', include("api.urls")),
]