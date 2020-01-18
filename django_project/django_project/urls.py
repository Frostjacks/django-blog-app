"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# here we are importing multiple views so provide ket as to distinct among them
from django.contrib.auth import views as auth_views  # this is to get the django's default login view
from django.urls import path,include
from users import views as user_views  # instead of creating urls file in the app you also can directly import the views in the main project's url file and give the path directly

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # by default django looks in registration/login.html template for displaying the login page. you can change it as per your liking by defining the template folder in url patterns as template_name='users/login.html'
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # this last part is for Serving files uploaded by a user during development
