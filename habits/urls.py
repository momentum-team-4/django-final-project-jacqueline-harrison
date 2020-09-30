"""project URL Configuration

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
from django.conf import settings
from django.urls import include, path
from django.views.generic.base import RedirectView
from users import views as users_views
from habitapp import views as habits_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='/accounts/create/')),
    path('accounts/create/', users_views.create_user, name="create_user"),
    path('accounts/login/', users_views.login_user, name="login_user"),
    path('accounts/logout/', users_views.logout_user, name="logout_user"),
    path('habits/add/', habits_views.add_habit, name="add_habit"),
    path('habits/edit/<int:pk>/', habits_views.edit_habit, name="edit_habit"),
    path('habits/delete/<int:pk>/', habits_views.delete_habit, name="delete_habit"),
    path('habits/all_habits/', habits_views.all_habits, name="all_habits"),
    path('habits/display_habit/<int:pk>/', habits_views.display_habit, name="display_habit"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
