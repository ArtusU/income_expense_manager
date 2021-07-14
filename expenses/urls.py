from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import index, add_expense, expense_edit, delete_expense, search_expenses




urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense', add_expense, name='add-expenses'),
    path('edit-expense/<int:id>', expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', delete_expense, name="expense-delete"),
    path('search-expenses', csrf_exempt(search_expenses), name="search_expenses")
]
