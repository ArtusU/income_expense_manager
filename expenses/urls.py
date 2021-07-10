from django.urls import path
from .views import index, add_expense, expense_edit




urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense', add_expense, name='add-expenses'),
    path('edit-expense/<int:id>', expense_edit, name="expense-edit"),
]
