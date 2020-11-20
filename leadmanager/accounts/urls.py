from django.urls import path, include
<<<<<<< HEAD
from .api import RegisterAPI, LoginAPI, UserAPI
=======
from .api import RegisterAPI
>>>>>>> parent of 4ac92a6... implemented login api
from knox import views as know_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
<<<<<<< HEAD
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', know_views.LoginView.as_view(), name='knox_logout'),
=======
>>>>>>> parent of 4ac92a6... implemented login api
]
