from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import index, add_expense, expense_edit, delete_expense, search_expenses, expense_category_summary, stats_view




urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense', add_expense, name='add-expenses'),
    path('edit-expense/<int:id>', expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', delete_expense, name="expense-delete"),
    path('stats-view', stats_view, name="stats_view"),
    path('search-expenses', csrf_exempt(search_expenses), name="search_expenses"),
    path('expense-category-sumary', csrf_exempt(expense_category_summary), name="expense_category_summary"),
]
