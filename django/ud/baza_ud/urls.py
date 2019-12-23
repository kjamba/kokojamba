"""ud URL Configuration

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
from django.urls import path
from baza_ud import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('detail/<int:id>/', views.detail_page, name='detail_page'),
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page/', views.ConcertCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>/', views.ConcertUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>/', views.ConcertDeleteView.as_view(), name='delete_page'),
    path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyprojectLogout.as_view(), name='logout_page'),

]
