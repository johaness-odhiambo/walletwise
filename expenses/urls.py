from django.urls import path
from .import views

app_name = 'expenses'
urlpatterns =[
    path('', views.home_page, name='homepage'),
    path('contact/', views.contact_page, name='contact'),
]