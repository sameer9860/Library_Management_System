from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path(
        '',
        LoginView.as_view(template_name='account/login.html', next_page='app:index'),
        name='login'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='account/login.html', next_page='app:index'),
        name='login_alt'
    ),
]
