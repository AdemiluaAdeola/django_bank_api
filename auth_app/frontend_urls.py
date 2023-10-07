from django.urls import path
from auth_app.frontend_views import *

#urlpatterns here
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]