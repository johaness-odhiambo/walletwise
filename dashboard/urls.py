from django.urls import path
from .import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('add_expenses/', views.add_expenses, name='add_expenses'),
    path('expenses_edit/<int:id>/', views.expense_edit, name='expense_edit'),
    path('delete_expense/<int:id>/', views.delete_expense, name='expense_delete'),
    path('expense_category_summary/', views.expense_category_summary, name='expense_category_summary'),
    path('stats/', views.stats, name='stats')



]