"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

import guestbook.views
import main.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # main
    path('main/', main.views.index),


    # guestbook
    path('guestbook/', guestbook.views.index),
    path('guestbook/deleteform',guestbook.views.deleteform),
    path('guestbook/add',guestbook.views.add),
    path('guestbook/delete', guestbook.views.delete),


    # user
    path('user/joinform', user.views.joinform),
    path('user/loginform', user.views.loginform),
    path('user/updateform', user.views.updateform),
    path('user/logout', user.views.logout),
    path('user/joinsuccess', user.views.joinsuccess),
    path('user/join', user.views.join),
    path('user', user.views.login)


]
