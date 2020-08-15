"""sdr_reservation URL Configuration

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
from rsv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #예약하기 버튼이 있는 메인페이지
    path('', views.board, name='index'),
    #예약하기 버튼을 누르면 넘어가는 예약페이지
    path('create/', views.create, name='create'),
    #예약내용을 등록하기 위해 views.register로 넘어감
    path('create/register/', views.register, name='register'),

    path('<int:board_id>/', views.read, name="read"),
    path('delete/<int:board_id>/', views.delete, name="delete"),
    path('update/<int:board_id>/', views.update, name="update"),
    path('up/<int:board_id>/', views.update_board),
    
]